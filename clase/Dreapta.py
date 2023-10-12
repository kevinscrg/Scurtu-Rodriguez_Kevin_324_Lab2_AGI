from dataclasses import dataclass
from clase.Punct import Punct
@dataclass
class drp:
    a: float
    b: float
    c: float

    def intr_ox(self):
        return Punct((-1)*self.c/self.a , 0)
    def intr_oy(self):
        return Punct(0,(-1)*self.c/self.b)
    def __str__(self):
        return f"d:  ({self.a})*x + ({self.b})*y + ({self.c}) = 0"