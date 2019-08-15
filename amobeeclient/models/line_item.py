import json
import requests
import datetime

from amobeeclient.models.base import Base

class LineItem(Base):

    object = "lineItems"

    def find_by_insertion_order(self, id):
        """

        :param id:
        :return: JSON array
        """
        url = "{0}/{1}/?insertionOrderId={2}".format(self.url_metadata, self.object, id)
        response = self.make_request("GET", url)

        return self.get_response_list(response)

    def find_by_package(self, id):
        """

        :param id:
        :return: JSON array
        """
        url = "{0}/{1}/?packageId={2}".format(self.url_metadata, self.object, id)
        response = self.make_request("GET", url)

        return self.get_response_list(response)
