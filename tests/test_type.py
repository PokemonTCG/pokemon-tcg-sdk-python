import vcr
import unittest
from pokemontcgsdk import Type

class TestType(unittest.TestCase):
    def test_all_returns_types(self):
        with vcr.use_cassette('fixtures/types.yaml'):
            types = Type.all()
            
            self.assertEqual(["Colorless","Darkness","Dragon","Fairy","Fighting","Fire","Grass","Lightning","Metal","Psychic","Water"], types)