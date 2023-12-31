from dataclasses import dataclass
from clase.Punct import Punct
import math
@dataclass
class drp:
    a: float
    b: float
    c: float

    def intr_ox(self):
        return Punct((-1)*self.c/self.a , 0)
    def intr_oy(self):
        return Punct(0,(-1)*self.c/self.b)

    def M_trans(self):
        if self.a!=0 and self.b !=0:
            mt = [[1,0,(-1)*self.c/(2*self.a)], [0,1,(-1)*self.c/(2*self.b)], [0,0,1]]
        elif self.a!=0:
            mt = [[1, 0, (-1) * self.c / (self.a)], [0, 1, 0], [0, 0, 1]]
        elif self.b !=0:
            mt = [[1, 0, 0], [0, 1, (-1) * self.c / (self.b)], [0, 0, 1]]
        return mt

    def M_trans_i(self):
        if self.a != 0 and self.b != 0:
            mt = [[1, 0, self.c / (2 * self.a)], [0, 1, self.c / (2 * self.b)], [0, 0, 1]]
        elif self.a != 0:
            mt = [[1, 0,  self.c / (self.a)], [0, 1, 0], [0, 0, 1]]
        elif self.b != 0:
            mt = [[1, 0, 0], [0, 1, self.c / (self.b)], [0, 0, 1]]
        return mt
    def M_rot(self):
        t = (-1)*self.a/self.b
        u = math.atan(t)
        mt = [[math.cos(u), (-1)*math.sin(u), 0], [math.sin(u), math.cos(u), 0], [0,0,1]]
        return mt

    def M_rot_i(self):
        t = (-1) * self.a / self.b
        u = math.atan(t)
        mt = [[math.cos(math.radians(360)-u), (-1) * math.sin(math.radians(360)-u), 0], [math.sin(math.radians(360)-u), math.cos(math.radians(360)-u), 0], [0, 0, 1]]
        return mt

    def M_ref(self):
        return [[1,0,0],[0,-1,0],[0,0,1]]

    def afis(self):
        if self.c == 0:
            print("\ndreapta trece prin origine.")
        else:
            print("\nmatricea de translatie (prin origine): \n")
            for i in range(3):
                print(self.M_trans()[i])
        if self.a == 0:
            print("\ndreapta este orizontala")
        elif self.b == 0:
            print("\ndreapta este verticala")
        else:
            print("\nmatricea de rotatie (se suprapune cu OX): \n")
            for i in range(3):
                print(self.M_rot()[i])
        print("\nmatricea de reflexie:\n ")
        for i in range(3):
            print(self.M_ref()[i])
        if self.a !=0 and self.b !=0:
            print("\nmatricea de rotatie (directia initiala): \n")
            for i in range(3):
                print(self.M_rot_i()[i])
        if self.c !=0:
            print("\nmatricea de translatie (pozitia initiala): \n")
            for i in range(3):
                print(self.M_trans_i()[i])





    def __str__(self):
        return f"d:  ({self.a})*x + ({self.b})*y + ({self.c}) = 0"