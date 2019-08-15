import json
import requests
import datetime

from amobeeclient.models.base import Base

class InsertionOrder(Base):

    object = "insertionOrders"

    def find_by_advertiser(self, id):
        """

        :param id:
        :return: JSON array
        """
        url = "{0}/{1}?advertiserId={2}".format(self.url_metadata, self.object, id)
        response = self.make_request("GET", url)

        return self.get_response_list(response)
