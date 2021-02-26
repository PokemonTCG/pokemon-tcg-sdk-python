from pokemontcgsdk.querybuilder import QueryBuilder

class Subtype():
    RESOURCE = 'subtypes'

    @staticmethod
    def all():
        return QueryBuilder(Subtype).array()