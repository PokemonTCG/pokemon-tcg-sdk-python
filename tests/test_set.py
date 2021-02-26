import vcr
import unittest
from pokemontcgsdk import Set

class TestSet(unittest.TestCase):
    def test_find_returns_set(self):
        with vcr.use_cassette('fixtures/xy11.yaml'):
            set = Set.find('xy11')
            self.assertEqual('xy11', set.id)
            self.assertEqual('Steam Siege', set.name)
            self.assertEqual('XY', set.series)
            self.assertEqual(114, set.printedTotal)
            self.assertEqual(116, set.total)
            self.assertEqual('STS', set.ptcgoCode)
            self.assertEqual("2016/08/03", set.releaseDate)
            
    def test_where_filters_on_name(self):
        with vcr.use_cassette('fixtures/filtered_sets.yaml'):
            sets = Set.where(q='name:steam')
            
            self.assertEqual(1, len(sets))
            self.assertEqual('xy11', sets[0].id)
            
    def test_all_returns_all_sets(self):
        with vcr.use_cassette('fixtures/all_sets.yaml'):
            sets = Set.all()

            self.assertGreater(len(sets), 70)
