from typing import Any, Optional
from sweb_api.http.client import JSONRPCClient


class BaseAPI:
    def __init__(self, client: JSONRPCClient, endpoint: str):
        self._client = client
        self._endpoint = endpoint

    def _call(self, method: str, params: Optional[dict] = None) -> Any:
        return self._client.call(self._endpoint, method, params)

    def index(self, params: Optional[dict] = None) -> Any:
        return self._call("index", params)
