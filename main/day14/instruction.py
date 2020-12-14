from dataclasses import dataclass


@dataclass()
class Instruction:
    mask: str
    address: int
    value: int
