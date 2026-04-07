from typing import Any, Optional
from .base import BaseAPI


class DomainsAPI(BaseAPI):
    def get_subdomains(self, domain: str) -> Any:
        return self._call("getSubdomains", {"domain": domain})

    def get_domain_info(self, domain: str) -> Any:
        return self._call("getDomainInfo", {"domain": domain})

    def reg_available(self, domain: str, pay_type: str = "balance") -> int:
        return self._call("regAvailable", {"domain": domain, "payType": pay_type})

    def get_available_packages(self, domains: str) -> Any:
        return self._call("getAvailablePackages", {"domains": domains})

    def reg_list(self, domains: str) -> int:
        return self._call("regList", {"domains": domains})

    def reg(
        self,
        domain: str,
        pay_type: str = "balance",
        dom_person: Optional[int] = None,
        prolong_type: Optional[str] = None,
        auto_reg: Optional[int] = None,
        dir: Optional[str] = None,
        id_shield: Optional[bool] = None,
    ) -> int:
        params = {"domain": domain, "payType": pay_type}
        if dom_person is not None:
            params["domPerson"] = dom_person
        if prolong_type is not None:
            params["prolongType"] = prolong_type
        if auto_reg is not None:
            params["autoReg"] = auto_reg
        if dir is not None:
            params["dir"] = dir
        if id_shield is not None:
            params["idShield"] = id_shield
        return self._call("reg", params)

    def move(
        self,
        domain: str,
        prolong_type: Optional[str] = None,
        dir: Optional[str] = None,
    ) -> Any:
        params = {"domain": domain}
        if prolong_type is not None:
            params["prolongType"] = prolong_type
        if dir is not None:
            params["dir"] = dir
        return self._call("move", params)

    def move_list(self, domains: list) -> Any:
        return self._call("moveList", {"domains": domains})

    def change_prolong(self, domain: str, prolong_type: str) -> int:
        return self._call("changeProlong", {"domain": domain, "prolongType": prolong_type})

    def change_prolong_list(self, domains: list) -> int:
        return self._call("changeProlongList", {"domains": domains})

    def remove(self, domain: str) -> int:
        return self._call("remove", {"domain": domain})

    def remove_list(self, domains: str) -> int:
        return self._call("removeList", {"domains": domains})

    def prolong(self, domain: str, pay_type: str = "balance") -> int:
        return self._call("prolong", {"domain": domain, "payType": pay_type})

    def prolong_list(self, domains: str) -> Any:
        return self._call("prolongList", {"domains": domains})

    def price_for_transfer(self, domain: str) -> int:
        return self._call("priceForTrasfer", {"domain": domain})

    def price_for_registration(self, domain: str) -> str:
        return self._call("priceForRegistration", {"domain": domain})

    def remove_subdomain(self, domain: str, machine: str) -> int:
        return self._call("removeSubdomain", {"domain": domain, "machine": machine})

    def create_subdomain(self, domain: str, machine: str, dir: str) -> int:
        return self._call("createSubdomain", {"domain": domain, "machine": machine, "dir": dir})

    def set_redirect_vh(self, domain: str, redirect: str) -> int:
        return self._call("setRedirectVh", {"domain": domain, "redirect": redirect})

    def get_redirect_vh(self, domain: str) -> Any:
        return self._call("getRedirectVh", {"domain": domain})


class DomainsBonusAPI(BaseAPI):
    def get_list(self) -> Any:
        return self._call("getList")

    def buy(self, bonus_id: int) -> int:
        return self._call("buy", {"bonusId": bonus_id})


class DomainsPersonsAPI(BaseAPI):
    def get_info(self, id: int) -> Any:
        return self._call("getinfo", {"id": id})

    def create_fiz_ip(
        self,
        name: str,
        resident: bool,
        phones: str,
        emails: str,
        post_index: str,
        post_city: str,
        post_address: str,
        birthdate: str,
        pass_series: str,
        pass_num: str,
        pass_date: str,
        pass_org: str,
        inn: Optional[str] = None,
        id: Optional[int] = None,
    ) -> int:
        params = {
            "name": name,
            "resident": resident,
            "phones": phones,
            "emails": emails,
            "postIndex": post_index,
            "postCity": post_city,
            "postAddress": post_address,
            "birthdate": birthdate,
            "passSeries": pass_series,
            "passNum": pass_num,
            "passDate": pass_date,
            "passOrg": pass_org,
        }
        if inn is not None:
            params["inn"] = inn
        if id is not None:
            params["id"] = id
        return self._call("createFizIp", params)

    def create_jur(
        self,
        name: str,
        name_trans: str,
        resident: bool,
        phones1: str,
        emails: str,
        post_index: str,
        post_city: str,
        post_address: str,
        jur_index: str,
        jur_city: str,
        jur_address: str,
        inn: str,
        pers_name: str,
        phones2: Optional[str] = None,
        faxes: Optional[str] = None,
        kpp: Optional[str] = None,
    ) -> int:
        params = {
            "name": name,
            "nameTrans": name_trans,
            "resident": resident,
            "phones1": phones1,
            "emails": emails,
            "postIndex": post_index,
            "postCity": post_city,
            "postAddress": post_address,
            "jurIndex": jur_index,
            "jurCity": jur_city,
            "jurAddress": jur_address,
            "inn": inn,
            "persName": pers_name,
        }
        if phones2 is not None:
            params["phones2"] = phones2
        if faxes is not None:
            params["faxes"] = faxes
        if kpp is not None:
            params["kpp"] = kpp
        return self._call("createJur", params)


class DomainsDNSAPI(BaseAPI):
    def info(self, domain: str) -> Any:
        return self._call("info", {"domain": domain})

    def edit_mx(
        self,
        domain: str,
        action: str,
        index: int,
        priority: int,
        value: str,
        sub_domain: Optional[str] = None,
    ) -> int:
        params = {
            "domain": domain,
            "action": action,
            "index": index,
            "priority": priority,
            "value": value,
        }
        if sub_domain is not None:
            params["subDomain"] = sub_domain
        return self._call("editMx", params)

    def edit_srv(
        self,
        domain: str,
        action: str,
        index: int,
        priority: int,
        ttl: int,
        weight: int,
        target: str,
        service: str,
        protocol: str,
        port: int,
        sub_domain: Optional[str] = None,
    ) -> bool:
        params = {
            "domain": domain,
            "action": action,
            "index": index,
            "priority": priority,
            "ttl": ttl,
            "weight": weight,
            "target": target,
            "service": service,
            "protocol": protocol,
            "port": port,
        }
        if sub_domain is not None:
            params["subDomain"] = sub_domain
        return self._call("editSrv", params)

    def edit_ns(
        self,
        domain: str,
        action: str,
        index: int,
        sub_domain: Optional[str] = None,
        value: Optional[str] = None,
    ) -> bool:
        params = {"domain": domain, "action": action, "index": index}
        if sub_domain is not None:
            params["subDomain"] = sub_domain
        if value is not None:
            params["value"] = value
        return self._call("editNS", params)

    def edit_txt(
        self,
        domain: str,
        action: str,
        index: int,
        sub_domain: Optional[str] = None,
        value: Optional[str] = None,
    ) -> bool:
        params = {"domain": domain, "action": action, "index": index}
        if sub_domain is not None:
            params["subDomain"] = sub_domain
        if value is not None:
            params["value"] = value
        return self._call("editTxt", params)

    def get_file(self, domain: str) -> Any:
        return self._call("getFile", {"domain": domain})
