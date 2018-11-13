import requests
import json

class Token:

    access_token = None

    def __init__(self, client_id=None, client_secret=None, grant_type="client_credentials"):
        self.url = "https://services.amobee.com/accounts/v1/api/token"
        self.client_id = client_id
        self.client_secret = client_secret
        self.grant_type = grant_type

    def get_access_token(self):
        if self.access_token is None:
            self.set_access_token()

    def set_access_token(self):
        headers = {
            'Content-Type': 'application/json',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': self.grant_type
        }
        response = requests.post(
            self.url,
            headers=headers,
            verify=False
        )

        print ""
        print "response"
        print response
        print ""