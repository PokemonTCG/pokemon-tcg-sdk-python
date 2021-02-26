from dataclasses import dataclass
from typing import Optional

@dataclass
class Legality():
    unlimited: Optional[str]
    expanded: Optional[str]
    standard: Optional[str]