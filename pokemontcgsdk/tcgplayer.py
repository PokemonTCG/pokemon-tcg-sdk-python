from dataclasses import dataclass
from typing import Optional

@dataclass
class TCGPrice():
  low: Optional[float]
  mid: Optional[float]
  high: Optional[float]
  market: Optional[float]
  directLow: Optional[float]

@dataclass
class TCGPrices():
    normal: Optional[TCGPrice]
    holofoil: Optional[TCGPrice]
    reverseHolofoil: Optional[TCGPrice]
    firstEditionHolofoil: Optional[TCGPrice]
    firstEditionNormal: Optional[TCGPrice]


@dataclass
class TCGPlayer():
    url: str
    updatedAt: str
    prices: Optional[TCGPrices]
