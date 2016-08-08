#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of pokemontcgsdk.
# https://github.com/PokemonTCG/pokemon-tcg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

import json
from pokemontcgsdk.restclient import RestClient
from pokemontcgsdk.config import __endpoint__

class QueryBuilder(object):
    def __init__(self, type):
        self.params = {}
        self.type = type

    def find(self, id):
        """Get a resource by its id
        
        Args:
            id (string): Resource id    
        Returns:
            object: Instance of the resource type
        """
        url = "{}/{}/{}".format(__endpoint__, self.type.RESOURCE, id)
        response = RestClient.get(url)[self.type.RESOURCE[:-1]]
        return self.type(response)

    def where(self, **kwargs):
        """Adds a parameter to the dictionary of query parameters
        
        Args:
            **kwargs: Arbitrary keyword arguments.
        Returns:
            QueryBuilder: Instance of the QueryBuilder
        """
        for key, value in kwargs.items():
            self.params[key] = value

        return self

    def all(self):
        """Get all resources, automatically paging through data

        Returns:
            list of object: List of resource objects
        """
        list = []
        page = 1
        fetch_all = True
        url = "{}/{}".format(__endpoint__, self.type.RESOURCE)

        if 'page' in self.params:
            page = self.params['page']
            fetch_all = False

        while True:
            response = RestClient.get(url, self.params)[self.type.RESOURCE]
            if len(response) > 0:
                for item in response:
                    list.append(self.type(item))

                if not fetch_all:
                    break
                else:
                    page += 1
                    self.where(page=page)
            else:
                break

        return list
        
    def array(self):
        """Get all resources and return the result as an array

        Returns:
            array of str: Array of resources
        """
        url = "{}/{}".format(__endpoint__, self.type.RESOURCE)
        return RestClient.get(url, self.params)[self.type.RESOURCE]