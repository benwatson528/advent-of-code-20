from dataclasses import dataclass


@dataclass()
class Instruction:
    action: str
    value: int
