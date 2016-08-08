#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of pokemontcgsdk.
# https://github.com/PokemonTCG/pokemon-tcg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

import json
from pokemontcgsdk.querybuilder import QueryBuilder

class Card(object):
    RESOURCE = 'cards'

    def __init__(self, response_dict={}):
        self.name = response_dict.get('name')
        self.id = response_dict.get('id')
        self.national_pokedex_number = response_dict.get('nationalPokedexNumber')
        self.image_url = response_dict.get('imageUrl')
        self.types = response_dict.get('types')
        self.subtype = response_dict.get('subtype')
        self.supertype = response_dict.get('supertype')
        self.hp = response_dict.get('hp')
        self.number = response_dict.get('number')
        self.artist = response_dict.get('artist')
        self.rarity = response_dict.get('rarity')
        self.series = response_dict.get('series')
        self.set = response_dict.get('set')
        self.set_code = response_dict.get('setCode')
        self.retreat_cost = response_dict.get('retreatCost')
        self.text = response_dict.get('text')
        self.attacks = response_dict.get('attacks')
        self.weaknesses = response_dict.get('weaknesses')
        self.resistances = response_dict.get('resistances')
        self.ability = response_dict.get('ability')

    @staticmethod
    def find(id):
        return QueryBuilder(Card).find(id)

    @staticmethod
    def where(**kwargs):
        return QueryBuilder(Card).where(**kwargs)

    @staticmethod
    def all():
        return QueryBuilder(Card).all()