from typing import Any, Optional
from sweb_api.api.base import BaseAPI


class VPSAPI(BaseAPI):
    def get_first_order_info(self) -> Any:
        return self._call("getFirstOrderInfo")

    def create_enable(self) -> int:
        return self._call("createEnable")

    def get_available_config(self) -> Any:
        return self._call("getAvailableConfig")

    def copy(self, billing_id: str) -> Any:
        return self._call("copy", {"billingId": billing_id})

    def create_first(
        self,
        plan_id: int,
        os_distrib_id: int,
        panel_type: Optional[str] = None,
        period: int = 1,
    ) -> Any:
        params = {"planId": plan_id, "os_distr_id": os_distrib_id, "period": period}
        if panel_type is not None:
            params["panel_type"] = panel_type
        return self._call("createFirst", params)

    def create(
        self,
        plan_id: int,
        os_distrib_id: int,
        panel_type: Optional[str] = None,
        datacenter: Optional[str] = None,
    ) -> Any:
        params = {"planId": plan_id, "os_distr_id": os_distrib_id}
        if panel_type is not None:
            params["panel_type"] = panel_type
        if datacenter is not None:
            params["datacenter"] = datacenter
        return self._call("create", params)

    def rename(self, billing_id: str, name: str) -> int:
        return self._call("rename", {"billingId": billing_id, "name": name})

    def is_running(self, billing_id: str) -> int:
        return self._call("isRunning", {"billingId": billing_id})

    def remove(self, billing_id: str) -> int:
        return self._call("remove", {"billingId": billing_id})

    def remove_first(self, billing_id: str) -> int:
        return self._call("removeFirst", {"billingId": billing_id})

    def load(self, billing_id: str) -> Any:
        return self._call("load", {"billingId": billing_id})

    def get_constructor_plan_id(self, cpu: int, ram: int, disk: int, backup: bool = False) -> Any:
        return self._call("getConstructorPlanId", {"cpu": cpu, "ram": ram, "disk": disk, "backup": backup})

    def change_plan(self, billing_id: str, plan_id: int) -> Any:
        return self._call("changePlan", {"billingId": billing_id, "planId": plan_id})

    def power_on(self, billing_id: str) -> int:
        return self._call("powerOn", {"billingId": billing_id})

    def power_off(self, billing_id: str) -> int:
        return self._call("powerOff", {"billingId": billing_id})

    def reboot(self, billing_id: str) -> int:
        return self._call("reboot", {"billingId": billing_id})

    def get_current_action(self, billing_id: str) -> str:
        return self._call("getCurrentAction", {"billingId": billing_id})

    def reinstall_os(
        self,
        billing_id: str,
        os_distrib_id: int,
        save_disk: bool = True,
    ) -> int:
        return self._call("reinstallOs", {"billingId": billing_id, "os_distr_id": os_distrib_id, "save_disk": save_disk})

    def logs(self, billing_id: str) -> Any:
        return self._call("logs", {"billingId": billing_id})


class VPSBackupAPI(BaseAPI):
    def update_index(self, billing_id: str) -> int:
        return self._call("updateIndex", {"billingId": billing_id})

    def create(self, billing_id: str) -> int:
        return self._call("create", {"billingId": billing_id})

    def restore(self, billing_id: str, backup_id: str) -> int:
        return self._call("restore", {"billingId": billing_id, "backupId": backup_id})

    def restore_int(self, billing_id: str, backup_id: str, disk: int) -> int:
        return self._call("restoreInt", {"billingId": billing_id, "backupId": backup_id, "disk": disk})

    def remove(self, billing_id: str, backup_id: str) -> int:
        return self._call("remove", {"billingId": billing_id, "backupId": backup_id})

    def get_settings(self, billing_id: str) -> Any:
        return self._call("getSettings", {"billingId": billing_id})

    def save_settings(self, billing_id: str, enabled: bool) -> int:
        return self._call("saveSettings", {"billingId": billing_id, "enabled": enabled})


class VPSSSLAPI(BaseAPI):
    def get_order_list(self) -> Any:
        return self._call("getOrderList")

    def download(self, id: int, password: str) -> Any:
        return self._call("download", {"id": id, "password": password})

    def edit_autoprolong(self, certificate_id: int, autoprolong: bool) -> int:
        return self._call("editAutoprolong", {"id": certificate_id, "autoprolong": autoprolong})

    def remove_certificate(self, certificate_id: int) -> int:
        return self._call("removeCertificate", {"id": certificate_id})

    def get_prolong_info(self, certificate_id: int) -> Any:
        return self._call("getProlongInfo", {"id": certificate_id})

    def order_submit(
        self,
        certificate_id: int,
        domain: str,
        period: int = 12,
    ) -> Any:
        return self._call("orderSubmit", {"id": certificate_id, "domain": domain, "period": period})


class VPSIPAPI(BaseAPI):
    def add_local(self, billing_id: str) -> int:
        return self._call("addLocal", {"billingId": billing_id})

    def remove_local(self, billing_id: str) -> int:
        return self._call("removeLocal", {"billingId": billing_id})


class VPSProtectedIPAPI(BaseAPI):
    def get_all_ip_list(self) -> Any:
        return self._call("getAllIpList")

    def get_order_info(self) -> Any:
        return self._call("getOrderInfo")

    def add_protected(self, billing_id: str, ip: str) -> int:
        return self._call("addProtected", {"billingId": billing_id, "ip": ip})

    def remove_protected(self, billing_id: str, ip: str) -> int:
        return self._call("removeProtected", {"billingId": billing_id, "ip": ip})

    def update_protected(self, billing_id: str, ip: str, enable: bool) -> int:
        return self._call("updateProtected", {"billingId": billing_id, "ip": ip, "enable": enable})

    def move_protected(self, billing_id: str, ip: str, new_billing_id: str) -> int:
        return self._call("moveProtected", {"billingId": billing_id, "ip": ip, "newBillingId": new_billing_id})

    def add(self, billing_id: str, ip: str) -> int:
        return self._call("add", {"billingId": billing_id, "ip": ip})

    def add_local(self, billing_id: str) -> int:
        return self._call("addLocal", {"billingId": billing_id})

    def remove_local(self, billing_id: str) -> int:
        return self._call("removeLocal", {"billingId": billing_id})

    def remove(self, billing_id: str, ip: str) -> int:
        return self._call("remove", {"billingId": billing_id, "ip": ip})

    def edit_ptr(self, billing_id: str, ip: str, ptr: str) -> int:
        return self._call("editPtr", {"billingId": billing_id, "ip": ip, "ptr": ptr})

    def get_ptr(self, billing_id: str, ip: str) -> str:
        return self._call("getPtr", {"billingId": billing_id, "ip": ip})


class VPSDBaaSAPI(BaseAPI):
    def set_upgrade_agree(self, agree: bool) -> int:
        return self._call("setUpgradeAgree", {"agree": agree})

    def get_available_config(self) -> Any:
        return self._call("getAvailableConfig")

    def get_constructor_plan_id(self) -> Any:
        return self._call("getConstructorPlanId")

    def get_first_order_info(self) -> Any:
        return self._call("getFirstOrderInfo")

    def remove_first(self, billing_id: str) -> int:
        return self._call("removeFirst", {"billingId": billing_id})

    def create_instance(
        self,
        name: str,
        node_count: int = 1,
        node_type: str = "db1",
    ) -> Any:
        return self._call("createInstance", {"name": name, "node_count": node_count, "node_type": node_type})

    def edit_instance(self, billing_id: str, name: str) -> int:
        return self._call("editInstance", {"billingId": billing_id, "name": name})

    def remove_instance(self, billing_id: str) -> int:
        return self._call("removeInstance", {"billingId": billing_id})

    def delete_database(self, billing_id: str, db_name: str) -> int:
        return self._call("deleteDatabase", {"billingId": billing_id, "dbName": db_name})

    def validate_users(self, billing_id: str, users: list) -> Any:
        return self._call("validateUsers", {"billingId": billing_id, "users": users})


class VPSBalancerAPI(BaseAPI):
    def is_create_enable(self) -> int:
        return self._call("isCreateEnable")

    def get_available_config(self) -> Any:
        return self._call("getAvailableConfig")

    def create(self, name: str, ip: list, port: int = 80) -> int:
        return self._call("create", {"name": name, "ip": ip, "port": port})

    def edit(self, billing_id: str, name: str, ip: list, port: int = 80) -> int:
        return self._call("edit", {"billingId": billing_id, "name": name, "ip": ip, "port": port})

    def remove(self, billing_id: str) -> int:
        return self._call("remove", {"billingId": billing_id})


class VPSRemoteBackupAPI(BaseAPI):
    def create(self, billing_id: str) -> int:
        return self._call("create", {"billingId": billing_id})

    def edit_comment(self, billing_id: str, comment: str) -> int:
        return self._call("editComment", {"billingId": billing_id, "comment": comment})

    def restore(self, billing_id: str, backup_id: str) -> int:
        return self._call("restore", {"billingId": billing_id, "backupId": backup_id})

    def restore_int(self, billing_id: str, backup_id: str, disk: int) -> int:
        return self._call("restoreInt", {"billingId": billing_id, "backupId": backup_id, "disk": disk})

    def remove(self, billing_id: str, backup_id: str) -> int:
        return self._call("remove", {"billingId": billing_id, "backupId": backup_id})


class VPSMonitoringAPI(BaseAPI):
    def enable(self, billing_id: str) -> int:
        return self._call("enable", {"billingId": billing_id})

    def disable(self, billing_id: str) -> int:
        return self._call("disable", {"billingId": billing_id})

    def change_plans(self, billing_id: str, plan_id: int) -> int:
        return self._call("changePlans", {"billingId": billing_id, "planId": plan_id})


class VPSMonitoringChecksAPI(BaseAPI):
    def get_types(self) -> Any:
        return self._call("getTypes")

    def get_intervals(self) -> Any:
        return self._call("getIntervals")

    def get_ports(self) -> Any:
        return self._call("getPorts")

    def get_keyword_modes(self) -> Any:
        return self._call("getKeywordModes")

    def get_info(self, billing_id: str) -> Any:
        return self._call("getInfo", {"billingId": billing_id})

    def get_full_check_info(self, billing_id: str, check_id: int) -> Any:
        return self._call("getFullCheckInfo", {"billingId": billing_id, "checkId": check_id})

    def create(
        self,
        billing_id: str,
        check_type: str,
        host: str,
        port: int,
        interval: int = 60,
    ) -> int:
        return self._call("create", {
            "billingId": billing_id,
            "check_type": check_type,
            "host": host,
            "port": port,
            "interval": interval,
        })

    def edit(
        self,
        billing_id: str,
        check_id: int,
        host: str,
        port: int,
        interval: int = 60,
    ) -> int:
        return self._call("edit", {
            "billingId": billing_id,
            "checkId": check_id,
            "host": host,
            "port": port,
            "interval": interval,
        })

    def activate(self, billing_id: str, check_id: int) -> int:
        return self._call("activate", {"billingId": billing_id, "checkId": check_id})

    def activate_list(self, billing_id: str, check_ids: list) -> int:
        return self._call("activateList", {"billingId": billing_id, "checkIds": check_ids})

    def deactivate(self, billing_id: str, check_id: int) -> int:
        return self._call("deactivate", {"billingId": billing_id, "checkId": check_id})

    def deactivate_list(self, billing_id: str, check_ids: list) -> int:
        return self._call("deactivateList", {"billingId": billing_id, "checkIds": check_ids})

    def remove(self, billing_id: str, check_id: int) -> int:
        return self._call("remove", {"billingId": billing_id, "checkId": check_id})

    def remove_list(self, billing_id: str, check_ids: list) -> int:
        return self._call("removeList", {"billingId": billing_id, "checkIds": check_ids})

    def history(self, billing_id: str, check_id: int) -> Any:
        return self._call("history", {"billingId": billing_id, "checkId": check_id})


class VPSMonitoringContactsAPI(BaseAPI):
    def get_all_contacts(self) -> Any:
        return self._call("getAllContacts")

    def add_contact(self, name: str, email: str) -> int:
        return self._call("addContact", {"name": name, "email": email})

    def edit_contact(self, contact_id: int, name: str, email: str) -> int:
        return self._call("editContact", {"contactId": contact_id, "name": name, "email": email})

    def add_email(self, contact_id: int, email: str) -> int:
        return self._call("addEmail", {"contactId": contact_id, "email": email})

    def edit_email(self, contact_id: int, email_id: int, email: str) -> int:
        return self._call("editEmail", {"contactId": contact_id, "emailId": email_id, "email": email})

    def add_phone(self, contact_id: int, phone: str) -> int:
        return self._call("addPhone", {"contactId": contact_id, "phone": phone})

    def edit_phone(self, contact_id: int, phone_id: int, phone: str) -> int:
        return self._call("editPhone", {"contactId": contact_id, "phoneId": phone_id, "phone": phone})

    def delete_contact(self, contact_id: int) -> int:
        return self._call("deleteContact", {"contactId": contact_id})

    def delete_contacts(self, contact_ids: list) -> int:
        return self._call("deleteContacts", {"contactIds": contact_ids})

    def add_telegram(self, contact_id: int, username: str) -> int:
        return self._call("addTelegram", {"contactId": contact_id, "username": username})

    def request_telegram_verify_code(self, contact_id: int, phone: str) -> int:
        return self._call("requestTelegramVerifyCode", {"contactId": contact_id, "phone": phone})

    def is_verified(self, contact_id: int) -> int:
        return self._call("isVerified", {"contactId": contact_id})

    def edit_telegram(self, contact_id: int, username: str) -> int:
        return self._call("editTelegram", {"contactId": contact_id, "username": username})

    def verify_contact(self, contact_id: int, code: str) -> int:
        return self._call("verifyContact", {"contactId": contact_id, "code": code})
