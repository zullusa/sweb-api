from typing import Any, Optional
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from sweb_api.exceptions.exceptions import (
    SwebAPIError,
    AuthenticationError,
    InvalidResponseError,
    NetworkError,
)


class JSONRPCClient:
    def __init__(self, base_url: str, timeout: int = 30):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.token: Optional[str] = None

        self.session = requests.Session()
        retry_strategy = Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def set_token(self, token: str) -> None:
        self.token = token

    def _build_headers(self) -> dict:
        headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def _make_request(
        self,
        endpoint: str,
        method: str,
        params: Optional[dict] = None,
        request_id: Optional[str] = None,
    ) -> dict:
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params or {},
        }
        if request_id:
            payload["id"] = request_id

        try:
            response = self.session.post(
                f"{self.base_url}/{endpoint}",
                json=payload,
                headers=self._build_headers(),
                timeout=self.timeout,
            )
            response.raise_for_status()
        except requests.exceptions.ConnectionError as e:
            raise NetworkError(f"Connection failed: {e}")
        except requests.exceptions.Timeout as e:
            raise NetworkError(f"Request timeout: {e}")
        except requests.exceptions.HTTPError as e:
            raise NetworkError(f"HTTP error: {e}")

        try:
            data = response.json()
        except ValueError as e:
            raise InvalidResponseError(f"Failed to parse JSON response: {e}")

        if "error" in data:
            error = data["error"]
            code = error.get("code", -32603)
            message = error.get("message", "Unknown error")
            if code == -32601:
                raise AuthenticationError(message)
            raise SwebAPIError(code, message)

        return data.get("result")

    def call(self, endpoint: str, method: str, params: Optional[dict] = None) -> Any:
        return self._make_request(endpoint, method, params)
