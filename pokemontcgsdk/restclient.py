import json
import os
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from urllib.parse import urlencode

class RestClient():
    api_key = None

    @classmethod
    def configure(cls, api_key):
        cls.api_key = api_key

    @classmethod
    def get(cls, url, params={}):
        """Invoke an HTTP GET request on a url
        
        Args:
            url (string): URL endpoint to request
            params (dict): Dictionary of url parameters 
        Returns:
            dict: JSON response as a dictionary
        """
        request_url = url
        
        if (len(params) > 0):
            request_url = "{}?{}".format(url, urlencode(params))

        try:
            headers = { 'User-Agent': 'Mozilla/5.0' }
            api_key = cls.api_key if cls.api_key is not None else os.getenv('POKEMONTCG_IO_API_KEY')
            if api_key:
                headers['X-Api-Key'] = api_key

            req = Request(request_url, headers=headers)
            response = json.loads(urlopen(req).read().decode("utf-8"))

            return response
        except HTTPError as err:
            raise PokemonTcgException(err.read())
            
class PokemonTcgException(Exception):
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description