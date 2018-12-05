import json
import requests
import datetime

from amobeeclient.models.base import Base

class LineItem(Base):

    object = "lineitems"

    def find_by_insertion_order(self, id):
        url = "{0}/{1}/{2}/{3}".format(self.url_metadata, self.object, "insertionorder", id)
        response = requests.get(
            url,
            headers=self.api_headers(),
            verify=False
        )

        return self.get_response_list(response)

    def find_by_package(self, id):
        url = "{0}/{1}/{2}/{3}".format(self.url_metadata, self.object, "package", id)
        response = requests.get(
            url,
            headers=self.api_headers(),
            verify=False
        )

        return self.get_response_list(response)
