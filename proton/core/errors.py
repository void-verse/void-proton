from proton.utils import err


class _BaseError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)

    def __str__(self) -> str:
        return "\n\b" + super().__str__()


class ResponseTypeError(_BaseError):
    def __init__(self, msg: str) -> None:
        super().__init__(err("RESPONSE", msg))


class DBError(_BaseError):
    def __init__(self, msg: str) -> None:
        super().__init__(err("DATABASE", msg))


class ManagerArgumentError(_BaseError):
    def __init__(self, msg: str) -> None:
        super().__init__(err("ARGUMENTS", msg))
