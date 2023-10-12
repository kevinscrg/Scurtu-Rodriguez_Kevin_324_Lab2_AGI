from dataclasses import dataclass

@dataclass
class Punct():
    x: float
    y: float

    def __str__(self):
        return f"( {self.x} , {self.y} )"