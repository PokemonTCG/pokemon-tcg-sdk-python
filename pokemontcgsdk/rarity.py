from pokemontcgsdk.querybuilder import QueryBuilder

class Rarity():
    RESOURCE = 'rarities'

    @staticmethod
    def all():
        return QueryBuilder(Rarity).array()