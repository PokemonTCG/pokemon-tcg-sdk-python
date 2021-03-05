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
        self.id = response_dict.get('id')
        self.images = response_dict.get('images')
        self.legalities = response_dict.get('legalities')
        self.name = response_dict.get('name')
        self.printedTotal = response_dict.get('printedTotal')
        self.ptcgoCode = response_dict.get('ptcgoCode')
        self.releaseDate = response_dict.get('releaseDate')
        self.series = response_dict.get('series')
        self.total = response_dict.get('total')
        self.updatedAt = response_dict.get('updatedAt')

    @staticmethod
    def find(id):
        return QueryBuilder(Set).find(id)

    @staticmethod
    def where(**kwargs):
        return QueryBuilder(Set).where(**kwargs)

    @staticmethod
    def all():
        return QueryBuilder(Set).all()
