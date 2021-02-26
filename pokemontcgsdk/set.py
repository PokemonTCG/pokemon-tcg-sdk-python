from dataclasses import dataclass
from typing import Optional

from pokemontcgsdk.legality import Legality
from pokemontcgsdk.querybuilder import QueryBuilder
from pokemontcgsdk.setimage import SetImage

@dataclass
class Set():
    RESOURCE = 'sets'

    id: str
    images: SetImage
    legalities: Legality
    name: str
    printedTotal: int
    ptcgoCode: Optional[str]
    releaseDate: str
    series: str
    total: int
    updatedAt: str


    @staticmethod
    def find(id):
        return QueryBuilder(Set).find(id)

    @staticmethod
    def where(**kwargs):
        return QueryBuilder(Set).where(**kwargs)

    @staticmethod
    def all():
        return QueryBuilder(Set).all()
