import logging
import json
import requests
import datetime

class Base:
    url_metadata = "https://services.amobee.com/campaign/v3/api"
    object = None

    def __init__(self, connection=None):
        self.connection = connection

    def api_headers(self):
        """

        :return:
        """
        headers = {}
        headers['Content-Type'] = 'application/json'
        headers['Authorization'] = 'Bearer {0}'.format(self.connection.access_token)

        return headers

    def get_by_id(self, id):
        """

        :param id:
        :return: JSON object
        """
        url = "{0}/{1}/{2}".format(self.url_metadata, self.object, id)
        response = self.make_request("GET", url)

        return self.get_response_object(response)

    def list_objects(self, url_params=''):
        """

        :param url_params:
        :return: JSON array
        """
        url = "{0}/{1}?{2}".format(self.url_metadata, self.object, url_params)
        response = self.make_request("GET", url)

        return self.get_response_list(response)

    def create(self, payload):
        """

        :param payload:
        :return: JSON object
        """
        url = "{0}/{1}/".format(self.url_metadata, self.object)
        response = self.make_request("POST", url, payload)

        return self.get_response_object(response)

    def make_request(self, method, url, payload=None):
        """

        :param method: String
        :param url:
        :param payload:
        :return: Response object
        """
        headers = self.api_headers()

        if method == "GET":
            self.curl = "curl -H 'Content-Type: application/json' -H 'Authorization:Bearer {0}' '{1}'".format(
                headers,
                url
            )
            response = requests.get(
                url,
                headers=headers,
                verify=False
            )

        elif method == "POST":
            self.curl = "curl -XPOST -H 'Content-Type: application/json' -H 'Authorization:Bearer {0}' -d '{1}' '{2}'".format(
                headers,
                payload,
                url
            )
            response = requests.post(
                url,
                headers=headers,
                data=payload,
                verify=False
            )

        elif method == "PUT":
            self.curl = "curl -XPUT -H 'Content-Type: application/json' -H 'Authorization:Bearer {0}' -d '{1}' '{2}'".format(
                headers,
                payload,
                url
            )
            response = requests.post(
                url,
                headers=headers,
                data=payload,
                verify=False
            )

        return response

    def get_response_list(self, response):
        """

        :param response:
        :return: JSON object
        """
        data = json.loads(response.text)

        rval = {}
        rval["response_code"] = response.status_code
        rval["request_body"] = self.curl
        if response.status_code == 200:
            rval["msg_type"] = "success"
            rval["msg"] = "Success"
            rval["data"] = data.get('data')
        else:
            rval["msg_type"] = "error"
            rval["msg"] = data.get('errors')
            rval["data"] = data

        return json.dumps(rval)

    def get_response_object(self, response):
        """

        :param response:
        :return: JSON object
        """
        data = json.loads(response.text)

        rval = {}
        rval["response_code"] = response.status_code
        rval["request_body"] = self.curl
        if response.status_code == 200:
            rval["msg_type"] = "success"
            rval["msg"] = "Success"
            rval["data"] = data.get('data')[0]
        else:
            rval["msg_type"] = "error"
            rval["msg"] = data.get('errors')
            rval["data"] = data

        return json.dumps(rval)
