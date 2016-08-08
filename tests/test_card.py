#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of pokemontcgsdk.
# https://github.com/PokemonTCG/pokemon-tcg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

import vcr
import unittest
from pokemontcgsdk import Card

class TestCard(unittest.TestCase):
    def test_find_returns_card(self):
        with vcr.use_cassette('fixtures/gardevoir.yaml'):
            card = Card.find('xy7-54')

            self.assertEqual('Gardevoir', card.name)
            self.assertEqual('xy7-54', card.id)
            self.assertEqual(282, card.national_pokedex_number)
            self.assertEqual('https://s3.amazonaws.com/pokemontcg/xy7/54.png', card.image_url)
            self.assertEqual('Stage 2', card.subtype)
            self.assertEqual('Pokémon', card.supertype)
            self.assertEqual('Bright Heal', card.ability['name'])
            self.assertEqual('Once during your turn (before your attack), you may heal 20 damage from each of your Pokémon.', card.ability['text'])
            self.assertEqual('130', card.hp)
            self.assertEqual(['Colorless', 'Colorless'], card.retreat_cost)
            self.assertEqual('54', card.number)
            self.assertEqual('TOKIYA', card.artist)
            self.assertEqual('Rare Holo', card.rarity)
            self.assertEqual('XY', card.series)
            self.assertEqual('Ancient Origins', card.set)
            self.assertEqual('xy7', card.set_code)
            self.assertEqual(['Fairy'], card.types)
            self.assertTrue(len(card.attacks) == 1)
            self.assertTrue(len(card.weaknesses) == 1)
            self.assertTrue(len(card.resistances) == 1)
            
    def test_all_with_params_return_cards(self):
        with vcr.use_cassette('fixtures/mega_pokemon.yaml'):
            cards = Card.where(supertype='pokemon') \
                        .where(subtype='mega') \
                        .all()

            self.assertTrue(len(cards) >= 70)
            
    def test_all_with_page_returns_cards(self):
        with vcr.use_cassette('fixtures/all_first_page.yaml'):
            cards = Card.where(page=1).all()
            
            self.assertEqual(100, len(cards))
            
    def test_all_with_page_and_page_size_returns_card(self):
        with vcr.use_cassette('fixtures/all_first_page_one_card.yaml'):
            cards = Card.where(page=1).where(pageSize=1).all()
            
            self.assertEqual(1, len(cards))