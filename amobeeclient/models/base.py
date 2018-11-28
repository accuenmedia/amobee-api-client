import logging
import json
import requests
import datetime

class Base:
    url_metadata = "https://services.amobee.com/metadata/v2/api/"

    def __init__(self, connection=None):
        self.connection = connection

    def get(self, endpoint):
        headers = {}
        headers['Content-Type'] = 'application/json'
        headers['Authorization'] = 'Bearer {0}'.format(self.connection.access_token)

        response = requests.get(
            self.url_metadata + endpoint,
            headers=headers,
            verify=False
        )
        self.__get_response_list(response)

    def __get_response_list(self, raw):
        rval = {}
        rval["response_code"] = raw.status_code
        rval["msg_type"] = "success"
        rval["msg"] = ""
        rval["data"] = json.loads(raw.text).get('list')
        rval["request_body"] = ""

        return json.dumps(rval)