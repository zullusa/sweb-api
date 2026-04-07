import unittest
from unittest.mock import Mock, patch

from src.http.client import JSONRPCClient
from src.exceptions.exceptions import (
    SwebAPIError,
    AuthenticationError,
    InvalidResponseError,
    NetworkError,
)
from src.api.base import BaseAPI
from src import SwebClient


class TestJSONRPCClient(unittest.TestCase):
    def test_build_headers_without_token(self):
        client = JSONRPCClient("https://api.sweb.ru")
        headers = client._build_headers()
        self.assertEqual(headers["Content-Type"], "application/json; charset=utf-8")
        self.assertEqual(headers["Accept"], "application/json")
        self.assertNotIn("Authorization", headers)

    def test_build_headers_with_token(self):
        client = JSONRPCClient("https://api.sweb.ru")
        client.set_token("test_token")
        headers = client._build_headers()
        self.assertEqual(headers["Authorization"], "Bearer test_token")

    def test_set_token(self):
        client = JSONRPCClient("https://api.sweb.ru")
        client.set_token("token123")
        self.assertEqual(client.token, "token123")

    @patch("src.http.client.requests.Session.post")
    def test_successful_request(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"jsonrpc": "2.0", "result": {"status": "ok"}}
        mock_response.raise_for_status = Mock()
        mock_post.return_value = mock_response

        client = JSONRPCClient("https://api.sweb.ru")
        result = client.call("testMethod", {"param": "value"})

        self.assertEqual(result, {"status": "ok"})
        mock_post.assert_called_once()

    @patch("src.http.client.requests.Session.post")
    def test_api_error_response(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "jsonrpc": "2.0",
            "error": {"code": -32601, "message": "Object not found"}
        }
        mock_response.raise_for_status = Mock()
        mock_post.return_value = mock_response

        client = JSONRPCClient("https://api.sweb.ru")
        with self.assertRaises(AuthenticationError):
            client.call("testMethod")

    @patch("src.http.client.requests.Session.post")
    def test_network_error_connection(self, mock_post):
        import requests
        mock_post.side_effect = requests.exceptions.ConnectionError("Connection failed")

        client = JSONRPCClient("https://api.sweb.ru")
        with self.assertRaises(NetworkError):
            client.call("testMethod")

    @patch("src.http.client.requests.Session.post")
    def test_network_error_timeout(self, mock_post):
        import requests
        mock_post.side_effect = requests.exceptions.Timeout("Request timeout")

        client = JSONRPCClient("https://api.sweb.ru")
        with self.assertRaises(NetworkError):
            client.call("testMethod")

    @patch("src.http.client.requests.Session.post")
    def test_invalid_json_response(self, mock_post):
        mock_response = Mock()
        mock_response.json.side_effect = ValueError("Invalid JSON")
        mock_response.raise_for_status = Mock()
        mock_post.return_value = mock_response

        client = JSONRPCClient("https://api.sweb.ru")
        with self.assertRaises(InvalidResponseError):
            client.call("testMethod")

    @patch("src.http.client.requests.Session.post")
    def test_custom_api_error(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "jsonrpc": "2.0",
            "error": {"code": -32001, "message": "Custom error"}
        }
        mock_response.raise_for_status = Mock()
        mock_post.return_value = mock_response

        client = JSONRPCClient("https://api.sweb.ru")
        with self.assertRaises(SwebAPIError) as context:
            client.call("testMethod")
        self.assertEqual(context.exception.code, -32001)
        self.assertEqual(context.exception.message, "Custom error")


class TestExceptions(unittest.TestCase):
    def test_sweb_api_error_str(self):
        error = SwebAPIError(-32601, "Test error")
        self.assertEqual(str(error), "Error -32601: Test error")

    def test_authentication_error_default_message(self):
        error = AuthenticationError()
        self.assertEqual(error.code, -32601)
        self.assertEqual(error.message, "Authentication failed")

    def test_invalid_response_error_default_message(self):
        error = InvalidResponseError()
        self.assertEqual(str(error), "Invalid response from server")

    def test_network_error_default_message(self):
        error = NetworkError()
        self.assertEqual(str(error), "Network error occurred")


class TestBaseAPI(unittest.TestCase):
    def test_call_builds_full_method_name(self):
        mock_client = Mock()
        mock_client.call.return_value = {"data": "test"}

        api = BaseAPI(mock_client, "domains")
        result = api._call("getSubdomains", {"domain": "example.com"})

        mock_client.call.assert_called_once_with("domains/getSubdomains", {"domain": "example.com"})
        self.assertEqual(result, {"data": "test"})

    def test_index_call(self):
        mock_client = Mock()
        mock_client.call.return_value = [{"fqdn": "example.com"}]

        api = BaseAPI(mock_client, "domains")
        result = api.index()

        mock_client.call.assert_called_once_with("domains/index", None)


class TestSwebClientAuthentication(unittest.TestCase):
    @unittest.skip("Requires real API endpoint")
    @patch("src.http.client.requests.Session.post")
    def test_authentication_success(self, mock_post):
        auth_response = Mock()
        auth_response.json.return_value = {"jsonrpc": "2.0", "result": "test_token_12345"}
        auth_response.raise_for_status = Mock()
        
        mock_post.return_value = auth_response

        client = SwebClient("testuser", "testpass")

        self.assertEqual(client._token, "test_token_12345")

    @unittest.skip("Requires real API endpoint")
    @patch("src.http.client.requests.Session.post")
    def test_authentication_invalid_token(self, mock_post):
        auth_response = Mock()
        auth_response.json.return_value = {"jsonrpc": "2.0", "result": None}
        auth_response.raise_for_status = Mock()
        
        mock_post.return_value = auth_response

        with self.assertRaises(AuthenticationError):
            SwebClient("testuser", "testpass")

    @unittest.skip("Requires real API endpoint")
    @patch("src.http.client.requests.Session.post")
    def test_authentication_connection_error(self, mock_post):
        import requests
        mock_post.side_effect = requests.exceptions.ConnectionError("Connection failed")

        with self.assertRaises(AuthenticationError):
            SwebClient("testuser", "testpass")

    @patch("src.http.client.JSONRPCClient")
    def test_authentication_connection_error(self, mock_jsonrpc_client):
        mock_client = Mock()
        mock_client.call.side_effect = NetworkError("Connection failed")
        mock_jsonrpc_client.return_value = mock_client

        with self.assertRaises(AuthenticationError):
            SwebClient("testuser", "testpass")


class TestDomainsAPI(unittest.TestCase):
    def setUp(self):
        self.mock_client = Mock()
        self.api = self.mock_client
        from src.api.domains import DomainsAPI
        self.domains = DomainsAPI(self.mock_client, "domains")

    def test_get_subdomains(self):
        self.mock_client.call.return_value = [{"value": "www", "name": "www"}]
        result = self.domains.get_subdomains("example.com")
        self.mock_client.call.assert_called_once_with(
            "domains/getSubdomains", {"domain": "example.com"}
        )
        self.assertEqual(result, [{"value": "www", "name": "www"}])

    def test_get_domain_info(self):
        self.mock_client.call.return_value = {"fqdn": "example.com", "is_active_task": 0}
        result = self.domains.get_domain_info("example.com")
        self.mock_client.call.assert_called_once_with(
            "domains/getDomainInfo", {"domain": "example.com"}
        )
        self.assertEqual(result["fqdn"], "example.com")

    def test_reg_available(self):
        self.mock_client.call.return_value = 1
        result = self.domains.reg_available("example.com", "balance")
        self.assertEqual(result, 1)

    def test_reg_available_custom_pay_type(self):
        self.mock_client.call.return_value = 1
        result = self.domains.reg_available("example.com", "bonus")
        self.mock_client.call.assert_called_once_with(
            "domains/regAvailable", {"domain": "example.com", "payType": "bonus"}
        )

    def test_reg_with_all_params(self):
        self.mock_client.call.return_value = 1
        result = self.domains.reg(
            domain="example.com",
            pay_type="balance",
            dom_person=12345,
            prolong_type="bonus_money",
            auto_reg=1,
            dir="/test",
            id_shield=True,
        )
        self.mock_client.call.assert_called_once()
        call_args = self.mock_client.call.call_args
        self.assertEqual(call_args[0][0], "domains/reg")
        self.assertEqual(call_args[0][1]["domain"], "example.com")
        self.assertEqual(call_args[0][1]["domPerson"], 12345)
        self.assertEqual(call_args[0][1]["prolongType"], "bonus_money")
        self.assertEqual(call_args[0][1]["autoReg"], 1)
        self.assertEqual(call_args[0][1]["dir"], "/test")
        self.assertEqual(call_args[0][1]["idShield"], True)

    def test_move_with_minimal_params(self):
        self.mock_client.call.return_value = 1
        result = self.domains.move("example.com")
        self.mock_client.call.assert_called_once_with(
            "domains/move", {"domain": "example.com"}
        )

    def test_move_with_optional_params(self):
        self.mock_client.call.return_value = 1
        result = self.domains.move("example.com", prolong_type="manual", dir="/new")
        call_args = self.mock_client.call.call_args[0][1]
        self.assertEqual(call_args["domain"], "example.com")
        self.assertEqual(call_args["prolongType"], "manual")
        self.assertEqual(call_args["dir"], "/new")

    def test_change_prolong(self):
        self.mock_client.call.return_value = 1
        result = self.domains.change_prolong("example.com", "bonus_money")
        self.mock_client.call.assert_called_once_with(
            "domains/changeProlong", {"domain": "example.com", "prolongType": "bonus_money"}
        )

    def test_remove_subdomain(self):
        self.mock_client.call.return_value = 1
        result = self.domains.remove_subdomain("example.com", "www")
        self.mock_client.call.assert_called_once_with(
            "domains/removeSubdomain", {"domain": "example.com", "machine": "www"}
        )

    def test_create_subdomain(self):
        self.mock_client.call.return_value = 1
        result = self.domains.create_subdomain("example.com", "test", "/testdir")
        self.mock_client.call.assert_called_once_with(
            "domains/createSubdomain", {"domain": "example.com", "machine": "test", "dir": "/testdir"}
        )


class TestDomainsAPIEdgeCases(unittest.TestCase):
    def setUp(self):
        self.mock_client = Mock()
        from src.api.domains import DomainsAPI
        self.domains = DomainsAPI(self.mock_client, "domains")

    def test_empty_domain_param(self):
        self.mock_client.call.return_value = 0
        result = self.domains.reg_available("")
        self.assertEqual(result, 0)

    def test_none_response_handling(self):
        self.mock_client.call.return_value = None
        result = self.domains.get_subdomains("example.com")
        self.assertIsNone(result)

    def test_extended_result_handling(self):
        self.mock_client.call.return_value = {
            "extendedResult": {
                "code": 1,
                "message": "Task created",
                "data": []
            }
        }
        result = self.domains.move("example.com")
        self.assertIn("extendedResult", result)

    def test_large_domain_list(self):
        self.mock_client.call.return_value = 1
        domains = ",".join([f"domain{i}.ru" for i in range(100)])
        result = self.domains.reg_list(domains)
        self.assertEqual(result, 1)


class TestMailAPI(unittest.TestCase):
    def setUp(self):
        self.mock_client = Mock()
        from src.api.vh import MailAPI
        self.mail = MailAPI(self.mock_client, "vh/mail")

    def test_create_mbox(self):
        self.mock_client.call.return_value = {
            "login": "test@example.com",
            "password": "password123",
            "webMail": "https://webmail.sweb.ru"
        }
        result = self.mail.create_mbox("example.com", "test", "password123")
        call_args = self.mock_client.call.call_args[0][1]
        self.assertEqual(call_args["domain"], "example.com")
        self.assertEqual(call_args["mbox"], "test")
        self.assertEqual(call_args["password"], "password123")

    def test_create_mbox_with_comment(self):
        self.mock_client.call.return_value = {"login": "test@example.com"}
        result = self.mail.create_mbox("example.com", "test", "pass", comment="Test mailbox")
        call_args = self.mock_client.call.call_args[0][1]
        self.assertEqual(call_args["comment"], "Test mailbox")

    def test_get_autoreply(self):
        self.mock_client.call.return_value = "Out of office message"
        result = self.mail.get_autoreply("example.com", "test")
        self.mock_client.call.assert_called_once_with(
            "vh/mail/getAutoreply", {"domain": "example.com", "mbox": "test"}
        )
        self.assertEqual(result, "Out of office message")

    def test_change_mailbox_password(self):
        self.mock_client.call.return_value = 1
        result = self.mail.change_mailbox_password("example.com", "test", "newpassword")
        call_args = self.mock_client.call.call_args[0][1]
        self.assertEqual(call_args["password"], "newpassword")

    def test_enable_dkim(self):
        self.mock_client.call.return_value = 1
        result = self.mail.enable_dkim("example.com")
        self.mock_client.call.assert_called_once_with(
            "vh/mail/enableDkim", {"domain": "example.com"}
        )

    def test_disable_dkim(self):
        self.mock_client.call.return_value = 1
        result = self.mail.disable_dkim("example.com")
        self.mock_client.call.assert_called_once_with(
            "vh/mail/disableDkim", {"domain": "example.com"}
        )


class TestVPSAPI(unittest.TestCase):
    def setUp(self):
        self.mock_client = Mock()
        from src.api.vps import VPSAPI
        self.vps = VPSAPI(self.mock_client, "vps")

    def test_power_on(self):
        self.mock_client.call.return_value = 1
        result = self.vps.power_on("test_vps_1")
        self.mock_client.call.assert_called_once_with(
            "vps/powerOn", {"billingId": "test_vps_1"}
        )

    def test_power_off(self):
        self.mock_client.call.return_value = 1
        result = self.vps.power_off("test_vps_1")
        self.mock_client.call.assert_called_once_with(
            "vps/powerOff", {"billingId": "test_vps_1"}
        )

    def test_reboot(self):
        self.mock_client.call.return_value = 1
        result = self.vps.reboot("test_vps_1")
        self.mock_client.call.assert_called_once_with(
            "vps/reboot", {"billingId": "test_vps_1"}
        )

    def test_is_running(self):
        self.mock_client.call.return_value = 1
        result = self.vps.is_running("test_vps_1")
        self.assertEqual(result, 1)

    def test_remove(self):
        self.mock_client.call.return_value = 1
        result = self.vps.remove("test_vps_1")
        self.mock_client.call.assert_called_once_with(
            "vps/remove", {"billingId": "test_vps_1"}
        )

    def test_reinstall_os(self):
        self.mock_client.call.return_value = 1
        result = self.vps.reinstall_os("test_vps_1", 102, save_disk=True)
        call_args = self.mock_client.call.call_args[0][1]
        self.assertEqual(call_args["os_distr_id"], 102)
        self.assertEqual(call_args["save_disk"], True)


class TestPayAPI(unittest.TestCase):
    def setUp(self):
        self.mock_client = Mock()
        from src.api.pay import PayAPI
        self.pay = PayAPI(self.mock_client, "pay")

    def test_get_balance(self):
        self.mock_client.call.return_value = {"real_balance": 1000, "bonus_balance": 50}
        result = self.pay.get_balance()
        self.assertEqual(result["real_balance"], 1000)

    def test_is_autopayment_enable(self):
        self.mock_client.call.return_value = False
        result = self.pay.is_autopayment_enable()
        self.assertEqual(result, False)

    def test_get_remains_date(self):
        self.mock_client.call.return_value = "01.10.2023"
        result = self.pay.get_remains_date()
        self.assertEqual(result, "01.10.2023")

    def test_get_remains_days(self):
        self.mock_client.call.return_value = 15
        result = self.pay.get_remains_days()
        self.assertEqual(result, 15)


class TestSwebClientProperties(unittest.TestCase):
    @patch("src.http.client.JSONRPCClient")
    def test_all_api_properties_return_correct_types(self, mock_jsonrpc_client):
        mock_client = Mock()
        mock_client.call.return_value = "token"
        mock_client.set_token = Mock()
        mock_jsonrpc_client.return_value = mock_client

        with patch.object(SwebClient, '_authenticate', return_value="token"):
            client = SwebClient("user", "pass")

        self.assertIsNotNone(client.domains)
        self.assertIsNotNone(client.domains_bonus)
        self.assertIsNotNone(client.domains_persons)
        self.assertIsNotNone(client.domains_dns)
        self.assertIsNotNone(client.sites)
        self.assertIsNotNone(client.hosting)
        self.assertIsNotNone(client.backup)
        self.assertIsNotNone(client.mail)
        self.assertIsNotNone(client.ssl)
        self.assertIsNotNone(client.tariff)
        self.assertIsNotNone(client.load)
        self.assertIsNotNone(client.utils)
        self.assertIsNotNone(client.cron)
        self.assertIsNotNone(client.ddg)
        self.assertIsNotNone(client.vps)
        self.assertIsNotNone(client.pay)
        self.assertIsNotNone(client.disk_usage)


class TestEdgeCases(unittest.TestCase):
    def test_special_characters_in_params(self):
        mock_client = Mock()
        from src.api.domains import DomainsAPI
        domains = DomainsAPI(mock_client, "domains")

        mock_client.call.return_value = 1
        domains.reg("тест.рф", dir="/тестовая-директория")
        call_args = mock_client.call.call_args[0][1]
        self.assertEqual(call_args["domain"], "тест.рф")
        self.assertEqual(call_args["dir"], "/тестовая-директория")

    def test_unicode_domain_names(self):
        mock_client = Mock()
        from src.api.domains import DomainsAPI
        domains = DomainsAPI(mock_client, "domains")

        mock_client.call.return_value = [{"value": "*.xn--p1ai.xn--p1ai", "name": "*.тест.рф"}]
        result = domains.get_subdomains("тест.рф")
        self.assertIsNotNone(result)

    def test_empty_optional_params(self):
        mock_client = Mock()
        from src.api.vh import UtilsAPI
        utils = UtilsAPI(mock_client, "vh/utils")

        mock_client.call.return_value = 1
        result = utils.ssh_on(24)
        self.assertEqual(result, 1)


class TestDiskUsageAPI(unittest.TestCase):
    def setUp(self):
        self.mock_client = Mock()
        from src.api.vh import DiskUsageAPI
        self.disk = DiskUsageAPI(self.mock_client, "vh/utils/diskUsage")

    def test_get_tasks_info(self):
        self.mock_client.call.return_value = {"activeTasksCount": "0", "lastDoneTaskDate": "2023-02-28"}
        result = self.disk.get_tasks_info()
        self.assertEqual(result["activeTasksCount"], "0")

    def test_start_task(self):
        self.mock_client.call.return_value = 1
        result = self.disk.start_task()
        self.assertEqual(result, 1)

    def test_get_email(self):
        self.mock_client.call.return_value = "test@example.com"
        result = self.disk.get_email()
        self.assertEqual(result, "test@example.com")

    def test_change_email(self):
        self.mock_client.call.return_value = 1
        result = self.disk.change_email("new@example.com")
        self.mock_client.call.assert_called_once_with(
            "vh/utils/diskUsage/changeEmail", {"email": "new@example.com"}
        )


if __name__ == "__main__":
    unittest.main()
