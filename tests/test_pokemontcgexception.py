import unittest
from pokemontcgsdk import PokemonTcgException

class TestPokemonTcgException(unittest.TestCase):
    def test_constructor_sets_description(self):
        description = "An error has occurred"
        exception = PokemonTcgException(description)
        
        self.assertEqual(description, exception.__str__())