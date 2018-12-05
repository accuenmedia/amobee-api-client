import json
import requests
import datetime

from amobeeclient.models.base import Base

class Package(Base):

    object = "packages"

    def find_by_advertiser(self, id):
        url = "{0}/{1}/{2}/{3}".format(self.url_metadata, self.object, "advertiser", id)
        response = requests.get(
            url,
            headers=self.api_headers(),
            verify=False
        )

        return self.get_response_list(response)
