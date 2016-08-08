#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of pokemontcgsdk.
# https://github.com/PokemonTCG/pokemon-tcg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

import vcr
import unittest
from pokemontcgsdk import Type

class TestType(unittest.TestCase):
    def test_all_returns_types(self):
        with vcr.use_cassette('fixtures/types.yaml'):
            types = Type.all()
            
            self.assertEqual(["Colorless","Dark","Darkness","Dragon","Fairy","Fighting","Fire","Grass","Lightning","Metal","Psychic","Water"], types)