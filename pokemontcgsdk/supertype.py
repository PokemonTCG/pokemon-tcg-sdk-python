from pokemontcgsdk.querybuilder import QueryBuilder

class Supertype():
    RESOURCE = 'supertypes'

    @staticmethod
    def all():
        return QueryBuilder(Supertype).array()