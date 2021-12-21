from dataclasses import dataclass
from typing import Optional

@dataclass
class CardmarketPrices():
    averageSellPrice: Optional[float]
    lowPrice: Optional[float]
    trendPrice: Optional[float]
    germanProLow: Optional[float]
    suggestedPrice: Optional[float]
    reverseHoloSell: Optional[float]
    reverseHoloLow: Optional[float]
    reverseHoloTrend: Optional[float]
    lowPriceExPlus: Optional[float]
    avg1: Optional[float]
    avg7: Optional[float]
    avg30: Optional[float]
    reverseHoloAvg1: Optional[float]
    reverseHoloAvg7: Optional[float]
    reverseHoloAvg30: Optional[float]


@dataclass
class Cardmarket():
    url: str
    updatedAt: str
    prices: Optional[CardmarketPrices]
