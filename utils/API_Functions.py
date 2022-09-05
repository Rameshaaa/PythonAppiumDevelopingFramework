import requests
from requests import *


class ApiFunctions:

    def GET_HTTP_METHOD(self, baseURI):

        response = requests.get(baseURI)
        response.json()
        response.status_code