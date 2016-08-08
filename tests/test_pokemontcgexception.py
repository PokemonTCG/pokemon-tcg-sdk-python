#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of pokemontcgsdk.
# https://github.com/PokemonTCG/pokemon-tcg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

import unittest
from pokemontcgsdk import PokemonTcgException

class TestPokemonTcgException(unittest.TestCase):
    def test_constructor_sets_description(self):
        description = "An error has occurred"
        exception = PokemonTcgException(description)
        
        self.assertEqual(description, exception.__str__())