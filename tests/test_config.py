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
        self.assertEqual('https://api.pokemontcg.io/v2', __endpoint__)