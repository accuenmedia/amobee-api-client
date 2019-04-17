import json
import requests
import datetime

from amobeeclient.models.base import Base

class InsertionOrder(Base):

    object = "insertionOrders"

    def find_by_advertiser(self, id):
        url = "{0}/{1}?advertiserId={2}".format(self.url_metadata, self.object, id)
        response = requests.get(
            url,
            headers=self.api_headers(),
            verify=False
        )

        return self.get_response_list(response)
