import vcr
import unittest
from pokemontcgsdk import Supertype

class TestSupertype(unittest.TestCase):
    def test_all_returns_supertypes(self):
        with vcr.use_cassette('fixtures/supertypes.yaml'):
            supertypes = Supertype.all()
            
            self.assertEqual(["Energy","Pokémon","Trainer"], supertypes)