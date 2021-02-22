#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of pokemontcgsdk.
# https://github.com/PokemonTCG/pokemon-tcg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

import json
from pokemontcgsdk.querybuilder import QueryBuilder
from pokemontcgsdk.set import Set

class Card(object):
    RESOURCE = 'cards'

    def __init__(self, response_dict={}):
        self.abilities = response_dict.get('abilities')
        self.artist = response_dict.get('artist')
        self.ancientTrait = response_dict.get('ancientTrait')
        self.attacks = response_dict.get('attacks')
        self.convertedRetreatCost = response_dict.get('convertedRetreatCost')
        self.evolvesFrom = response_dict.get('evolvesFrom')
        self.flavorText = response_dict.get('flavorText')
        self.hp = response_dict.get('hp')
        self.id = response_dict.get('id')
        self.images = response_dict.get('images')
        self.legalities = response_dict.get('legalities')
        self.name = response_dict.get('name')
        self.nationalPokedexNumbers = response_dict.get('nationalPokedexNumbers')
        self.number = response_dict.get('number')
        self.rarity = response_dict.get('rarity')
        self.resistances = response_dict.get('resistances')
        self.retreatCost = response_dict.get('retreatCost')
        self.rules = response_dict.get('rules')
        self.set = Set(response_dict.get('set'))
        self.subtypes = response_dict.get('subtypes')
        self.supertype = response_dict.get('supertype')
        self.tcgplayer = response_dict.get('tcgplayer')
        self.types = response_dict.get('types')
        self.weaknesses = response_dict.get('weaknesses')

    @staticmethod
    def find(id):
        return QueryBuilder(Card).find(id)

    @staticmethod
    def where(**kwargs):
        return QueryBuilder(Card).where(**kwargs)

    @staticmethod
    def all():
        return QueryBuilder(Card).all()
