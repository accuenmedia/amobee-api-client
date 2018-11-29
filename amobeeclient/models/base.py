import logging
import json
import requests
import datetime

class Base:
    url_metadata = "https://services.amobee.com/metadata/v2/api"
    object = None

    def __init__(self, connection=None):
        self.connection = connection

    def get_one(self, id):
        headers = {}
        headers['Content-Type'] = 'application/json'
        headers['Authorization'] = 'Bearer {0}'.format(self.connection.access_token)

        url = "{0}/{1}/{2}".format(self.url_metadata, self.object, id)
        print "URL"
        print url
        response = requests.get(
            url,
            headers=headers,
            verify=False
        )
        return self.__get_response_object(response)

    def list_objects(self, url_params=''):
        headers = {}
        headers['Content-Type'] = 'application/json'
        headers['Authorization'] = 'Bearer {0}'.format(self.connection.access_token)

        url = "{0}/{1}?{2}".format(self.url_metadata, self.object, url_params)
        print "URL"
        print url
        response = requests.get(
            url,
            headers=headers,
            verify=False
        )
        return self.__get_response_list(response)

    def __get_response_list(self, response):
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
            rval["msg"] = data.get('message')
            rval["data"] = data.get('errors')
            rval["request_body"] = ""

        return json.dumps(rval)

    def __get_response_object(self, response):
        data = json.loads(response.text)
        print ""
        print ""
        print "__get_response_object :: data"
        print data
        print ""
        print ""

        return None

        rval = {}
        rval["response_code"] = response.status_code
        rval["msg_type"] = "success"
        rval["msg"] = ""
        rval["data"] = data.get('items')
        rval["request_body"] = ""

        return json.dumps(rval)