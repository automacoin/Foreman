# errors
import fastapi_jsonrpc as jsonrpc

class UnallocatedTrancheError(jsonrpc.BaseError):
    CODE = 6000
    MESSAGE = "The submitted Tranche was not allocated correctly"


class MessageError(jsonrpc.BaseError):
    CODE = 6001
    MESSAGE = "The message was improperly formed"

class SignatureError(jsonrpc.BaseError):
    CODE = 6002
    MESSAGE = "The signature did not match the message or sender address"

