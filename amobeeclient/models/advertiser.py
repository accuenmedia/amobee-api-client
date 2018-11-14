import json
import requests
import datetime

from amobeeclient.models.base import Base

class Advertiser(Base):

    def list_all(self):
        response = self.get("advertisers")
