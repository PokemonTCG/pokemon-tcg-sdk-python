from pokemontcgsdk.querybuilder import QueryBuilder

class Type():
    RESOURCE = 'types'

    @staticmethod
    def all():
        return QueryBuilder(Type).array()