#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of pokemontcgsdk.
# https://github.com/PokemonTCG/pokemon-tcg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

import unittest
from pokemontcgsdk import __pypi_packagename__, __github_username__, __github_reponame__, __endpoint__

class TestConfig(unittest.TestCase):
    def test_has_proper_packagename(self):
        self.assertEqual('pokemontcgsdk', __pypi_packagename__)
        
    def test_has_proper_github_username(self):
        self.assertEqual('PokemonTCG', __github_username__)
        
    def test_has_proper_github_reponame(self):
        self.assertEqual('pokemon-tcg-sdk-python', __github_reponame__)
        
    def test_has_proper_endpoint(self):
        self.assertEqual('https://api.pokemontcg.io/v1', __endpoint__)