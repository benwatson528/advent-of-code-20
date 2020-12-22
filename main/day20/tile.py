from dataclasses import dataclass
from typing import List


@dataclass()
class Tile:
    tile_id: int
    top: str
    bottom: str
    left: str
    right: str
    rotation: int
    flip: bool
    original_tile: List[str]
