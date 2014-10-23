"""
Exceptions that can be raised by the backend.
"""

class PyntercomException(Exception):
    """
    Root Pyntercom Exception
    """

    def __init__(self, message, resp=None):
        super(PyntercomException, self).__init__(message)
        self.resp = resp

class AuthenticationError(PyntercomException):
    """
    Raised when app_id and/or app_key is rejected by the server (aka 401).
    """

class ResourceNotFound(PyntercomException):
    """
    Raised when resource (user, company, etc) could not be found (aka 404).
    """

class ServerError(PyntercomException):
    """
    Raised when the server unexpected failed to process request (aka 50X).
    """
