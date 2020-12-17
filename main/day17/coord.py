from dataclasses import dataclass


@dataclass(frozen=True)
class Coord:
    x: int
    y: int
    z: int
