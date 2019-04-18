import json
import requests
import datetime

from amobeeclient.models.base import Base

class Creative(Base):

    object = "creatives"

    def find_by_line_item(self, id):
        """
        Their "creatives" endpoint has no direct method to get assigned line items.
        Must go through the "ads" endpoint: https://services.amobee.com/campaign/v3/doc/#/Ads/getAdsUsingGET

        :param id: string
        :return: JSON object
        """
        url = "{0}/{1}?lineItemId={2}".format(self.url_metadata, 'ads', id)
        response = requests.get(
            url,
            headers=self.api_headers(),
            verify=False
        )
        return self.get_response_list(response)

    def find_by_advertiser(self, id):
        url = "{0}/{1}?advertiserId={2}".format(self.url_metadata, self.object, id)
        response = requests.get(
            url,
            headers=self.api_headers(),
            verify=False
        )

        return self.get_response_list(response)
