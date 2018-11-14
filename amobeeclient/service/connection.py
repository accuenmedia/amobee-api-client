import requests
import json

class Connection:

    access_token = None
    url_token = "https://services.amobee.com/accounts/v1/api/token"
    url_metadata = "https://services.amobee.com/metadata/v2/api/"
    url_reporting = "https://services.amobee.com/reporting/v2/api/"

    def __init__(self, client_id=None, client_secret=None, grant_type="client_credentials"):
        self.client_id = client_id
        self.client_secret = client_secret
        self.grant_type = grant_type

        if self.access_token is None:
            self.get_access_token()

    def get_access_token(self):
        headers = {
            'Content-Type': 'application/json'
        }

        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': self.grant_type
        }

        response = requests.post(
            self.url_token,
            headers=headers,
            data=json.dumps(data),
            verify=False
        )
        response = json.loads(response.text)
        self.access_token = response.get('access_token')