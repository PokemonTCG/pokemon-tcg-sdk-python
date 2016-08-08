#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of pokemontcgsdk.
# https://github.com/PokemonTCG/pokemon-tcg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

import json
from pokemontcgsdk.querybuilder import QueryBuilder

class Set(object):
    RESOURCE = 'sets'

    def __init__(self, response_dict={}):
        self.name = response_dict.get('name')
        self.code = response_dict.get('code')
        self.series = response_dict.get('series')
        self.total_cards = response_dict.get('totalCards')
        self.standard_legal = response_dict.get('standardLegal')
        self.release_date = response_dict.get('releaseDate')

    @staticmethod
    def find(id):
        return QueryBuilder(Set).find(id)

    @staticmethod
    def where(**kwargs):
        return QueryBuilder(Set).where(**kwargs)

    @staticmethod
    def all():
        return QueryBuilder(Set).all()