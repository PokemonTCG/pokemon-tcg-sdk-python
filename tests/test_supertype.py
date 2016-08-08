#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of pokemontcgsdk.
# https://github.com/PokemonTCG/pokemon-tcg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

import vcr
import unittest
from pokemontcgsdk import Supertype

class TestSupertype(unittest.TestCase):
    def test_all_returns_supertypes(self):
        with vcr.use_cassette('fixtures/supertypes.yaml'):
            supertypes = Supertype.all()
            
            self.assertEqual(["Energy","Pokémon","Trainer"], supertypes)