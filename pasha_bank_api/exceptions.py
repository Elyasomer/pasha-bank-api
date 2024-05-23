class PashaBankAPIError(Exception):
    pass

class AuthenticationError(PashaBankAPIError):
    pass

class InvalidTransactionError(PashaBankAPIError):
    pass

