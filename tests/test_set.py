#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of pokemontcgsdk.
# https://github.com/PokemonTCG/pokemon-tcg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

import vcr
import unittest
from pokemontcgsdk import Set

class TestSet(unittest.TestCase):
    def test_find_returns_set(self):
        with vcr.use_cassette('fixtures/xy11.yaml'):
            set = Set.find('xy11')
            
            self.assertEqual('xy11', set.code)
            self.assertEqual('Steam Siege', set.name)
            self.assertEqual('XY', set.series)
            self.assertEqual(114, set.total_cards)
            self.assertEqual(True, set.standard_legal)
            self.assertEqual('08/03/2016', set.release_date)
            
    def test_where_filters_on_name(self):
        with vcr.use_cassette('fixtures/filtered_sets.yaml'):
            sets = Set.where(name='steam').all()
            
            self.assertEqual(1, len(sets))
            self.assertEqual('xy11', sets[0].code)
            
    def test_all_returns_all_sets(self):
        with vcr.use_cassette('fixtures/all_sets.yaml'):
            sets = Set.all()

            self.assertGreater(len(sets), 70)