import logging
import json
import requests
import datetime

class Base:
    url_metadata = "https://services.amobee.com/metadata/v2/api"
    object = None

    def __init__(self, connection=None):
        self.connection = connection

    def api_headers(self):
        headers = {}
        headers['Content-Type'] = 'application/json'
        headers['Authorization'] = 'Bearer {0}'.format(self.connection.access_token)

        return headers

    def get_by_id(self, id):
        url = "{0}/{1}/{2}".format(self.url_metadata, self.object, id)
        response = requests.get(
            url,
            headers=self.api_headers(),
            verify=False
        )

        return self.get_response_object(response)

    def list_objects(self, url_params=''):
        url = "{0}/{1}?{2}".format(self.url_metadata, self.object, url_params)
        response = requests.get(
            url,
            headers=self.api_headers(),
            verify=False
        )

        return self.get_response_list(response)

    def create(self, payload):
        url = "{0}/{1}/".format(self.url_metadata, self.object)
        response = requests.post(
            url,
            headers=self.api_headers(),
            data=payload,
            verify=False
        )

        return self.get_response_object(response)

    def get_response_list(self, response):
        data = json.loads(response.text)

        rval = {}
        rval["response_code"] = response.status_code
        if response.status_code == 200:
            rval["msg_type"] = "success"
            rval["msg"] = ""
            rval["data"] = data.get('items')
            rval["request_body"] = ""
        else:
            rval["msg_type"] = "error"
            rval["msg"] = data.get('error')
            rval["data"] = data
            rval["request_body"] = ""

        return json.dumps(rval)

    def get_response_object(self, response):
        data = json.loads(response.text)

        rval = {}
        rval["response_code"] = response.status_code
        if response.status_code == 200:
            rval["msg_type"] = "success"
            rval["msg"] = ""
            rval["data"] = data
            rval["request_body"] = ""
        else:
            rval["msg_type"] = "error"
            rval["msg"] = data.get('error')
            rval["data"] = data
            rval["request_body"] = ""

        return json.dumps(rval)
