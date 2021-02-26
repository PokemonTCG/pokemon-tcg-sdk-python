from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Attack():
    name: str
    cost: List[str]
    convertedEnergyCost: int
    damage: Optional[str]
    text: Optional[str]