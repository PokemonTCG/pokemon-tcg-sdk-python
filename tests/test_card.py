import unittest
import vcr
from pokemontcgsdk import Card

# Python 3.6 Workaround until https://github.com/kevin1024/vcrpy/issues/293 is fixed.
vcr_connection_request = vcr.stubs.VCRConnection.request 
vcr.stubs.VCRConnection.request = lambda *args, **kwargs: vcr_connection_request(*args)

class TestCard(unittest.TestCase):
    def test_find_returns_card(self):
        with vcr.use_cassette('fixtures/gardevoir.yaml'):
            card = Card.find('xy7-54')
            self.assertEqual('xy7-54', card.id)
            self.assertEqual('Gardevoir', card.name)
            self.assertEqual('Pokémon', card.supertype)
            self.assertEqual(['Stage 2'], card.subtypes)
            self.assertEqual('130', card.hp)
            self.assertEqual(['Fairy'], card.types)
            self.assertEqual('Kirlia', card.evolvesFrom)
            self.assertTrue(len(card.abilities) == 1)
            self.assertTrue(len(card.attacks) == 1)
            self.assertTrue(len(card.weaknesses) == 1)
            self.assertTrue(len(card.resistances) == 1)
            self.assertEqual(['Colorless', 'Colorless'], card.retreatCost)
            self.assertEqual(2, card.convertedRetreatCost)
            self.assertEqual('xy7', card.set.id)
            self.assertEqual('54', card.number)
            self.assertEqual('TOKIYA', card.artist)
            self.assertEqual('Rare Holo', card.rarity)
            self.assertEqual('It has the power to predict the future. Its power peaks when it is protecting its Trainer.', card.flavorText)
            self.assertEqual([282], card.nationalPokedexNumbers)
            self.assertEqual('https://prices.pokemontcg.io/tcgplayer/xy7-54', card.tcgplayer.url)

    def test_all_with_params_return_cards(self):
        with vcr.use_cassette('fixtures/mega_pokemon.yaml'):
            cards = Card.where(q='supertype:pokemon subtypes:mega')
            self.assertTrue(len(cards) >= 70)

    def test_all_with_page_returns_cards(self):
        with vcr.use_cassette('fixtures/all_first_page.yaml'):
            cards = Card.where(page=1)
            self.assertEqual(250, len(cards))

    def test_all_with_page_and_page_size_returns_card(self):
        with vcr.use_cassette('fixtures/all_first_page_one_card.yaml'):
            cards = Card.where(page=1, pageSize=1)
            self.assertEqual(1, len(cards))

