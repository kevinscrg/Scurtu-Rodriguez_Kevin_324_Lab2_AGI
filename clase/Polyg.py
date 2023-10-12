from dataclasses import dataclass

from clase.Punct import Punct
@dataclass
class poligon:
    l: []

    def adaug(self, p: Punct):
        self.l.append(p)

    def __str__(self):
        s = ""
        for i in range(0,len(self.l)):
            s += f"{i}:{self.l[i]}\n"
        return s