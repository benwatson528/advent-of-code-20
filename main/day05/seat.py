from dataclasses import dataclass, field


@dataclass
class Seat:
    row: int
    column: int
    seat_id: int = field(compare=False)
