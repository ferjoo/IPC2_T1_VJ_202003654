from dataclasses import dataclass

@dataclass
class Flight:
    code: str
    origin: str
    destination: str
    duration: int
    airline: str 