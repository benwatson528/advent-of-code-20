from dataclasses import dataclass
from typing import List, Tuple, Dict


@dataclass()
class Notes:
    field_rules: Dict[str, Tuple[range, range]]
    your_ticket: List[int]
    nearby_tickets: List[List[int]]
