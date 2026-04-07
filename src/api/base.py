from typing import Any, Optional
from swebpy.http.client import JSONRPCClient


class BaseAPI:
    def __init__(self, client: JSONRPCClient, endpoint: str):
        self._client = client
        self._endpoint = endpoint

    def _call(self, method: str, params: Optional[dict] = None) -> Any:
        full_method = f"{self._endpoint}/{method}" if self._endpoint else method
        return self._client.call(full_method, params)

    def index(self, params: Optional[dict] = None) -> Any:
        return self._call("index", params)
