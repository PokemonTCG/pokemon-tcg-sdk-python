#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of pokemontcgsdk.
# https://github.com/PokemonTCG/pokemon-tcg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

import json
import os
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from urllib.parse import urlencode

class RestClient(object):
    @staticmethod
    def get(url, params={}):
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
            api_key = os.getenv('POKEMONTCG_IO_API_KEY')
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