from dataclasses import dataclass


@dataclass
class Policy:
    lower_bound: int
    upper_bound: int
    letter: str
