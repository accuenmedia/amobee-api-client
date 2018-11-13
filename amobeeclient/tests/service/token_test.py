import unittest

from amobeeclient.service.token import Token

class TokenTest():

    def testSetToken(self):
        token = Token(
            "07ea458a-0ab0-1038-813c-dbf3ea0ca4fc@1181.api",
            "XZ37O8o1OtynJQPL"
        )
        assert token is not None
