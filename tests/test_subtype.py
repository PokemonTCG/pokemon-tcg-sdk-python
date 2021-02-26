import vcr
import unittest
from pokemontcgsdk import Subtype

class TestSubtype(unittest.TestCase):
    def test_all_returns_subtypes(self):
        with vcr.use_cassette('fixtures/subtypes.yaml'):
            subtypes = Subtype.all()
            
            self.assertTrue(len(subtypes) > 15)
            self.assertTrue('MEGA' in subtypes)