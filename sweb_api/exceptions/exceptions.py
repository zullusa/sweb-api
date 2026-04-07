class SwebAPIError(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
        super().__init__(f"Error {code}: {message}")


class AuthenticationError(SwebAPIError):
    def __init__(self, message: str = "Authentication failed"):
        super().__init__(-32601, message)


class InvalidResponseError(Exception):
    def __init__(self, message: str = "Invalid response from server"):
        super().__init__(message)


class NetworkError(Exception):
    def __init__(self, message: str = "Network error occurred"):
        super().__init__(message)
