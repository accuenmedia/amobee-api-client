import requests
import json

class Connection:

    def __init__(self, client_id=None, client_secret=None, url=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.url = url