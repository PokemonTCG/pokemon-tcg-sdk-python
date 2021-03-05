from dataclasses import dataclass
from typing import Optional

@dataclass
class Ability():
    name: str
    text: str
    type: str