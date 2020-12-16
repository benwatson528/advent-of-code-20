from dataclasses import dataclass
from typing import List, Tuple


@dataclass()
class Notes:
    field_rules: List[Tuple[range, range]]
    your_ticket: List[int]
    nearby_tickets: List[List[int]]
