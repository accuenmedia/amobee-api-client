import logging
import json
import requests
import datetime

class Base:

    def __init__(self, connection=None):
        self.connection = connection

    def get(self, endpoint, payload=None):
        headers = {}
        headers['Content-Type'] = 'application/json'
        headers['Authorization'] = 'Bearer {0}'.format(self.connection.access_token)

        print "headers"
        print headers

        response = requests.get(
            {0},
            headers=headers,
            data=json.dumps(payload),
            verify=False
        ).format(self.connection.url_metadata + endpoint)
        response = json.loads(response.text)
        print ""
        print ""
        print "response"
        print response
        print ""
        print ""
