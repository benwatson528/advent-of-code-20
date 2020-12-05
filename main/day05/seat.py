from dataclasses import dataclass


@dataclass
class Seat:
    row: int
    column: int
    seat_id: int
