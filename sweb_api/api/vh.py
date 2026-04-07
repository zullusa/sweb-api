from typing import Any, Optional
from sweb_api.api.base import BaseAPI


class SitesAPI(BaseAPI):
    def get_site_info(self, doc_root: str) -> Any:
        return self._call("getSiteInfo", {"docRoot": doc_root})

    def add(
        self,
        alias: str,
        doc_root: str,
        domain: Optional[str] = None,
        machine: Optional[str] = None,
        enable_redis_session: Optional[bool] = None,
    ) -> Any:
        params: dict = {"alias": alias, "docRoot": doc_root}
        if domain is not None:
            params["domain"] = domain
        if machine is not None:
            params["machine"] = machine
        if enable_redis_session is not None:
            params["enableRedisSession"] = enable_redis_session
        return self._call("add", params)

    def edit(
        self,
        doc_root: str,
        alias: str,
        doc_root_new: Optional[str] = None,
    ) -> Any:
        params = {"docRoot": doc_root, "alias": alias}
        if doc_root_new is not None:
            params["docRootNew"] = doc_root_new
        return self._call("edit", params)

    def delete(self, doc_root: str) -> Any:
        return self._call("del", {"docRoot": doc_root})

    def change_domain_site(
        self,
        domain: str,
        doc_root: str,
        machine: Optional[str] = None,
    ) -> Any:
        params = {"domain": domain, "docRoot": doc_root}
        if machine is not None:
            params["machine"] = machine
        return self._call("changeDomainSite", params)

    def get_backends_list(self) -> Any:
        return self._call("getBackEndsList")

    def change_backend(self, doc_root: str, back_end_id: int) -> Any:
        return self._call("changeBackEnd", {"docRoot": doc_root, "idBackEnd": back_end_id})


class HostingAPI(BaseAPI):
    def get_list(
        self,
        page: int = 1,
        sorting_type: str = "default",
        direct_order: bool = True,
        filter: Optional[str] = None,
    ) -> Any:
        params = {
            "page": page,
            "sortingType": sorting_type,
            "directOrder": direct_order,
        }
        if filter is not None:
            params["filter"] = filter
        return self._call("databaseGetList", params)

    def mysql_change_pass(self, db_name: str, db_password: str) -> Any:
        return self._call("databaseMysqlChangePass", {"dbName": db_name, "dbPassword": db_password})

    def mysql_create(
        self,
        db_name: str,
        db_password: str,
        db_comment: Optional[str] = None,
        db_version: Optional[str] = None,
    ) -> Any:
        params = {"dbName": db_name, "dbPassword": db_password}
        if db_comment is not None:
            params["dbComment"] = db_comment
        if db_version is not None:
            params["dbVersion"] = db_version
        return self._call("databaseMysqlCreate", params)

    def mysql_import(self, db_name: str, file_patch: str) -> Any:
        return self._call("databaseMysqlImport", {"dbName": db_name, "filePatch": file_patch})

    def mysql_make_copy(self, db_name: str) -> Any:
        return self._call("databaseMysqlMakeCopy", {"dbName": db_name})

    def mysql_access_list(self, db_name: str) -> Any:
        return self._call("databaseMysqlAccessList", {"dbName": db_name})

    def mysql_access_create(self, db_name: str, rule: str) -> Any:
        return self._call("databaseMysqlAccessCreate", {"dbName": db_name, "rule": rule})

    def mysql_access_delete(self, db_name: str, rule: str) -> Any:
        return self._call("databaseMysqlAccessDelete", {"dbName": db_name, "rule": rule})

    def mysql_delete(self, db_name: str) -> Any:
        return self._call("databaseMysqlDelete", {"dbName": db_name})

    def pgsql_create(
        self,
        db_name: str,
        db_password: str,
        db_charset: Optional[str] = None,
        db_comment: Optional[str] = None,
    ) -> Any:
        params = {"dbName": db_name, "dbPassword": db_password}
        if db_charset is not None:
            params["dbCharset"] = db_charset
        if db_comment is not None:
            params["dbComment"] = db_comment
        return self._call("databasePgsqlCreate", params)

    def pgsql_delete(self, db_name: str) -> Any:
        return self._call("databasePgsqlDelete", {"dbName": db_name})

    def pgsql_change_pass(self, db_name: str, db_password: str) -> Any:
        return self._call("databasePgsqlChangePass", {"dbName": db_name, "dbPassword": db_password})

    def edit_comment(self, db_type: str, db_name: str, db_comment: str) -> Any:
        return self._call(
            "databaseEditComment", {"dbType": db_type, "dbName": db_name, "dbComment": db_comment}
        )

    def get_pma_user(self, db_name: str) -> Any:
        return self._call("getPmaUser", {"dbName": db_name})


class BackupAPI(BaseAPI):
    def get_list(self) -> Any:
        return self._call("getList")

    def make_account_copy(self) -> Any:
        return self._call("makeAccountCopy")

    def restore_files(self, date: str, files: list) -> Any:
        return self._call("restoreFiles", {"date": date, "files": files})

    def download_file(self, date: str, files: list) -> Any:
        return self._call("downloadFile", {"date": date, "files": files})

    def get_list_files(self, date: str, dir: str) -> Any:
        return self._call("getListFiles", {"date": date, "dir": dir})

    def get_list_mysql(self, date: str, dir: str) -> Any:
        return self._call("getListMysql", {"date": date, "dir": dir})

    def receive_files(self, date: str, files: list) -> Any:
        return self._call("receiveFiles", {"date": date, "files": files})

    def receive_mysql(self, date: str, databases: list) -> Any:
        return self._call("receiveMysql", {"date": date, "databases": databases})

    def restore_mysql(self, date: str, databases: list) -> Any:
        return self._call("restoreMysql", {"date": date, "databases": databases})


class MailAPI(BaseAPI):
    def get_domains_list(
        self,
        page: int = 1,
        limit: int = 20,
        order_by: int = 0,
        order_direct: str = "asc",
    ) -> Any:
        return self._call(
            "getDomainsList",
            {
                "page": page,
                "limit": limit,
                "orderBy": order_by,
                "orderDirect": order_direct,
            },
        )

    def get_mailboxes_list(
        self,
        domain: str,
        page: int = 1,
        limit: int = 20,
        order_by: int = 0,
        order_direct: str = "asc",
        search_mbox: Optional[str] = None,
    ) -> Any:
        params = {
            "domain": domain,
            "page": page,
            "limit": limit,
            "orderBy": order_by,
            "orderDirect": order_direct,
        }
        if search_mbox is not None:
            params["searchMbox"] = search_mbox
        return self._call("getMailboxesList", params)

    def get_mail_quota(self) -> Any:
        return self._call("getMailQuota")

    def create_mbox(
        self,
        domain: str,
        mbox: str,
        password: str,
        comment: Optional[str] = None,
    ) -> Any:
        params = {"domain": domain, "mbox": mbox, "password": password}
        if comment is not None:
            params["comment"] = comment
        return self._call("createMbox", params)

    def send_requisites_to_email(self, email: str, login: str, password: str) -> Any:
        return self._call(
            "sendRequisitesToEmail", {"email": email, "login": login, "password": password}
        )

    def drop_mbox(self, domain: str, mbox: str) -> Any:
        return self._call("dropMbox", {"domain": domain, "mbox": mbox})

    def update_antispam_state(self, domain: str, mbox: str, value: int) -> Any:
        return self._call("updateAntispamState", {"domain": domain, "mbox": mbox, "value": value})

    def update_comment(self, domain: str, mbox: str, comment: str) -> Any:
        return self._call("updateComment", {"domain": domain, "mbox": mbox, "comment": comment})

    def get_autoreply(self, domain: str, mbox: str) -> Any:
        return self._call("getAutoreply", {"domain": domain, "mbox": mbox})

    def change_autoreply(self, domain: str, mbox: str, text: str) -> Any:
        return self._call("changeAutoreply", {"domain": domain, "mbox": mbox, "text": text})

    def change_mailbox_spf(self, domain: str, mbox: str, turn_on: bool) -> Any:
        return self._call("changeMailboxSpf", {"domain": domain, "mbox": mbox, "turnOn": turn_on})

    def change_domain_spf(self, domain: str, turn_on: bool) -> Any:
        return self._call("changeDomainSpf", {"domain": domain, "turnOn": turn_on})

    def get_forwarding_emails_list(self, domain: str, mbox: str) -> Any:
        return self._call("getForwardingEmailsList", {"domain": domain, "mbox": mbox})

    def add_forwarding_email(self, domain: str, mbox: str, email: str) -> Any:
        return self._call("addForwardingEmail", {"domain": domain, "mbox": mbox, "email": email})

    def remove_forwarding_email(self, domain: str, mbox: str, email: str) -> Any:
        return self._call("removeForwardingEmail", {"domain": domain, "mbox": mbox, "email": email})

    def is_enabled_deleting_after_forwarding(self, domain: str, mbox: str) -> Any:
        return self._call("isEnabledDeletingAfterForwarding", {"domain": domain, "mbox": mbox})

    def change_deleting_after_forwarding(self, domain: str, mbox: str, turn_on: bool) -> Any:
        return self._call(
            "changeDeletingAfterForwarding", {"domain": domain, "mbox": mbox, "turnOn": turn_on}
        )

    def get_delivery_addresses_list(
        self, domain: str, mbox: str, page: int = 1, limit: int = 20
    ) -> Any:
        return self._call(
            "getDeliveryAddressesList",
            {"domain": domain, "mbox": mbox, "page": page, "limit": limit},
        )

    def get_delivery_info(self, domain: str, mbox: str) -> Any:
        return self._call("getDeliveryInfo", {"domain": domain, "mbox": mbox})

    def add_delivery_address(self, domain: str, mbox: str, email: str) -> Any:
        return self._call("addDeliveryAddress", {"domain": domain, "mbox": mbox, "email": email})

    def drop_delivery_address(self, domain: str, mbox: str, email: str) -> Any:
        return self._call("dropDeliveryAddress", {"domain": domain, "mbox": mbox, "email": email})

    def get_mails_collector(self, domain: str) -> Any:
        return self._call("getMailsCollector", {"domain": domain})

    def change_mails_collector(self, domain: str, email: str) -> Any:
        return self._call("changeMailsCollector", {"domain": domain, "email": email})

    def remove_mails_collector(self, domain: str) -> Any:
        return self._call("removeMailsCollector", {"domain": domain})

    def confirm_mails_collector_email(self, domain: str, token: str) -> Any:
        return self._call("confirmMailsCollectorEmail", {"domain": domain, "token": token})

    def change_sender_verify(self, domain: str, turn_on: bool) -> Any:
        return self._call("changeSenderVerify", {"domain": domain, "turnOn": turn_on})

    def change_auto_discover(self, domain: str, turn_on: bool) -> Any:
        return self._call("changeAutoDiscover", {"domain": domain, "turnOn": turn_on})

    def delete_mails(self, domain: str, mbox: str, days: int) -> Any:
        return self._call("deleteMails", {"domain": domain, "mbox": mbox, "days": days})

    def change_mailbox_password(self, domain: str, mbox: str, password: str) -> Any:
        return self._call(
            "changeMailboxPassword", {"domain": domain, "mbox": mbox, "password": password}
        )

    def get_whitelist(self, domain: str, mbox: str, page: int = 1, limit: int = 20) -> Any:
        return self._call(
            "getWhitelist", {"domain": domain, "mbox": mbox, "page": page, "limit": limit}
        )

    def get_blacklist(self, domain: str, mbox: str, page: int = 1, limit: int = 20) -> Any:
        return self._call(
            "getBlacklist", {"domain": domain, "mbox": mbox, "page": page, "limit": limit}
        )

    def add_to_whitelist(self, domain: str, mbox: str, address: str, all: bool = False) -> Any:
        return self._call(
            "addToWhitelist", {"domain": domain, "mbox": mbox, "address": address, "all": all}
        )

    def add_to_blacklist(self, domain: str, mbox: str, email: str, all: bool = False) -> Any:
        return self._call(
            "addToBlacklist", {"domain": domain, "mbox": mbox, "email": email, "all": all}
        )

    def drop_from_whitelist(self, domain: str, mbox: str, address: str) -> Any:
        return self._call("dropFromWhitelist", {"domain": domain, "mbox": mbox, "address": address})

    def drop_from_blacklist(self, domain: str, mbox: str, email: str) -> Any:
        return self._call("dropFromBlacklist", {"domain": domain, "mbox": mbox, "email": email})

    def enable_dkim(self, domain: str) -> Any:
        return self._call("enableDkim", {"domain": domain})

    def disable_dkim(self, domain: str) -> Any:
        return self._call("disableDkim", {"domain": domain})


class SSLAPI(BaseAPI):
    def get_order_list(self) -> Any:
        return self._call("getOrderList")

    def download(self, id: int, password: str) -> Any:
        return self._call("download", {"id": id, "password": password})

    def edit_autoprolong(self, certificate_id: int, autoprolong: bool) -> Any:
        return self._call("editAutoprolong", {"id": certificate_id, "autoprolong": autoprolong})

    def remove_certificate(self, certificate_id: int) -> Any:
        return self._call("removeCertificate", {"id": certificate_id})

    def get_prolong_info(self, certificate_id: int) -> Any:
        return self._call("getProlongInfo", {"id": certificate_id})

    def prolong_certificate(self, current_certificate_id: int, certificate_prolong_id: int) -> Any:
        return self._call(
            "prolongCertificate",
            {"id": current_certificate_id, "certificateProlongId": certificate_prolong_id},
        )

    def install_lets_encrypt(
        self,
        domain: str,
        virtdom: Optional[str] = None,
        ip: str = "sni",
        wildcard: int = 0,
        challenge: str = "dns",
    ) -> Any:
        params = {"domain": domain, "ip": ip, "wildcard": wildcard, "challenge": challenge}
        if virtdom is not None:
            params["virtdom"] = virtdom
        return self._call("installLetsEncrypt", params)


class TariffAPI(BaseAPI):
    def server_info(self) -> Any:
        return self._call("serverInfo")


class LoadAPI(BaseAPI):
    def get_load_table(self, year: int, month: int, type: str = "null") -> Any:
        return self._call("getLoadTable", {"year": year, "month": month, "type": type})


class UtilsAPI(BaseAPI):
    def ssh_on(self, period: int) -> Any:
        return self._call("sshOn", {"period": period})

    def ssh_off(self) -> Any:
        return self._call("sshOff")


class CronAPI(BaseAPI):
    def add_task(
        self,
        minute: int,
        hour: int,
        day: int,
        month: int,
        weekday: int,
        command: str,
    ) -> Any:
        return self._call(
            "addTask",
            {
                "minute": minute,
                "hour": hour,
                "day": day,
                "month": month,
                "weekday": weekday,
                "command": command,
            },
        )

    def edit_task(
        self,
        old_task: str,
        minute: int,
        hour: int,
        day: int,
        month: int,
        weekday: int,
        command: str,
    ) -> Any:
        return self._call(
            "editTask",
            {
                "oldTask": old_task,
                "minute": minute,
                "hour": hour,
                "day": day,
                "month": month,
                "weekday": weekday,
                "command": command,
            },
        )

    def remove_task(self, task: str) -> Any:
        return self._call("removeTask", {"task": task})

    def get_tasks(self) -> Any:
        return self._call("getTasks")


class DiskUsageAPI(BaseAPI):
    def get_tasks_info(self) -> Any:
        return self._call("getTasksInfo")

    def start_task(self) -> Any:
        return self._call("startTask")

    def get_email(self) -> Any:
        return self._call("getEmail")

    def change_email(self, email: str) -> Any:
        return self._call("changeEmail", {"email": email})


class DDGAPI(BaseAPI):
    def count_all_domains(self) -> Any:
        return self._call("countAllDomains")

    def enable(self, domain: str) -> Any:
        return self._call("enable", {"domain": domain})

    def disable(self, domain: str) -> Any:
        return self._call("disable", {"domain": domain})

    def enable_info(self) -> Any:
        return self._call("enableInfo")

    def price_widget(self) -> Any:
        return self._call("priceWidget")

    def get_price(self) -> Any:
        return self._call("getPrice")
