from dataclasses import dataclass

from main.day08.operation import Operation


@dataclass()
class Instruction:
    operation: Operation
    argument: int
