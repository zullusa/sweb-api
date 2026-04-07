from src.http.client import JSONRPCClient
from src.api.domains import DomainsAPI, DomainsBonusAPI, DomainsPersonsAPI, DomainsDNSAPI
from src.api.vh import (
    SitesAPI, HostingAPI, BackupAPI, MailAPI, SSLAPI, TariffAPI,
    LoadAPI, UtilsAPI, CronAPI, DDGAPI, DiskUsageAPI,
)
from src.api.vps import (
    VPSAPI, VPSBackupAPI, VPSSSLAPI, VPSIPAPI, VPSProtectedIPAPI,
    VPSDBaaSAPI, VPSBalancerAPI, VPSRemoteBackupAPI, VPSMonitoringAPI,
    VPSMonitoringChecksAPI, VPSMonitoringContactsAPI,
)
from src.api.pay import PayAPI
from src.exceptions.exceptions import AuthenticationError


class SwebClient:
    BASE_URL = "https://api.sweb.ru"

    def __init__(self, login: str, password: str, timeout: int = 30):
        self._login = login
        self._password = password
        self._client = JSONRPCClient(self.BASE_URL, timeout)
        self._token = self._authenticate()
        self._client.set_token(self._token)

    def _authenticate(self) -> str:
        client = JSONRPCClient(f"{self.BASE_URL}/notAuthorized")
        try:
            result = client.call("getToken", {"login": self._login, "password": self._password})
            if not result or not isinstance(result, str):
                raise AuthenticationError("Invalid token received")
            return result
        except Exception as e:
            if isinstance(e, AuthenticationError):
                raise
            raise AuthenticationError(f"Failed to authenticate: {e}")

    @property
    def domains(self) -> DomainsAPI:
        return DomainsAPI(self._client, "domains")

    @property
    def domains_bonus(self) -> DomainsBonusAPI:
        return DomainsBonusAPI(self._client, "domains/bonus")

    @property
    def domains_persons(self) -> DomainsPersonsAPI:
        return DomainsPersonsAPI(self._client, "domains/persons")

    @property
    def domains_dns(self) -> DomainsDNSAPI:
        return DomainsDNSAPI(self._client, "domains/dns")

    @property
    def sites(self) -> SitesAPI:
        return SitesAPI(self._client, "sites")

    @property
    def hosting(self) -> HostingAPI:
        return HostingAPI(self._client, "vh/hosting")

    @property
    def backup(self) -> BackupAPI:
        return BackupAPI(self._client, "vh/backup")

    @property
    def mail(self) -> MailAPI:
        return MailAPI(self._client, "vh/mail")

    @property
    def ssl(self) -> SSLAPI:
        return SSLAPI(self._client, "vh/ssl")

    @property
    def tariff(self) -> TariffAPI:
        return TariffAPI(self._client, "tariff")

    @property
    def load(self) -> LoadAPI:
        return LoadAPI(self._client, "vh/load")

    @property
    def utils(self) -> UtilsAPI:
        return UtilsAPI(self._client, "vh/utils")

    @property
    def cron(self) -> CronAPI:
        return CronAPI(self._client, "vh/cron")

    @property
    def disk_usage(self) -> DiskUsageAPI:
        return DiskUsageAPI(self._client, "vh/utils/diskUsage")

    @property
    def ddg(self) -> DDGAPI:
        return DDGAPI(self._client, "vh/ddg")

    @property
    def vps(self) -> VPSAPI:
        return VPSAPI(self._client, "vps")

    @property
    def vps_backup(self) -> VPSBackupAPI:
        return VPSBackupAPI(self._client, "vps/backup")

    @property
    def vps_ssl(self) -> VPSSSLAPI:
        return VPSSSLAPI(self._client, "vps/ssl")

    @property
    def vps_ip(self) -> VPSIPAPI:
        return VPSIPAPI(self._client, "vps/ip")

    @property
    def vps_protected_ip(self) -> VPSProtectedIPAPI:
        return VPSProtectedIPAPI(self._client, "vps/protected-ip")

    @property
    def vps_dbaas(self) -> VPSDBaaSAPI:
        return VPSDBaaSAPI(self._client, "vps/dbaas")

    @property
    def vps_balancer(self) -> VPSBalancerAPI:
        return VPSBalancerAPI(self._client, "vps/balancer")

    @property
    def vps_remote_backup(self) -> VPSRemoteBackupAPI:
        return VPSRemoteBackupAPI(self._client, "vps/remote-backup")

    @property
    def vps_monitoring(self) -> VPSMonitoringAPI:
        return VPSMonitoringAPI(self._client, "vps/monitoring")

    @property
    def vps_monitoring_checks(self) -> VPSMonitoringChecksAPI:
        return VPSMonitoringChecksAPI(self._client, "vps/monitoring/checks")

    @property
    def vps_monitoring_contacts(self) -> VPSMonitoringContactsAPI:
        return VPSMonitoringContactsAPI(self._client, "vps/monitoring/contacts")

    @property
    def pay(self) -> PayAPI:
        return PayAPI(self._client, "pay")
