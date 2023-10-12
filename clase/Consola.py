from clase.Dreapta import drp
from clase.Punct import Punct

class cons():

    def drp(self, p: Punct, v: Punct):
        a = (-1)*v.y
        b = v.x
        c = v.y*p.x - v.x*p.y
        return  drp(a,b,c)

    def ec_g(self):
        try:
            print("scrieti coeficentii ecuatiei")
            a = float(input("a= "))
            b = float(input("b= "))
            c = float(input("c= "))
            d = drp(a,b,c)


        except KeyError:
            print("nu ati introdus date coerente. ")
        except ValueError:
            print("nu ati introdus date coerente. ")
    def vect(self):
        try:
            print("scrieti coordonatele punctului:")
            a = float(input("x= "))
            b = float(input("y= "))
            print("scrieti valorile vectorului:")
            v1 = float(input("v1= "))
            v2 = float(input("v2= "))

            p = Punct(a,b)
            v = Punct(v1,v2)
            d = self.drp(p,v)

        except KeyError:
            print("nu ati introdus date coerente. ")
        except ValueError:
            print("nu ati introdus date coerente. ")



    def printm(self):
        print("Cum doriti sa dati dreapta?")
        print("1. ecuatie generala.")
        print("2. punct si vector director.")
        print("x. iesire din program. ")


    def Meniu(self):
        print()
        while True:
            self.printm()
            a = input("")
            if a == "1":
                self.ec_g()
            elif a == "2":
               self.vect()
            elif a == "x":
                break
            else:
                print("optiune gresita. ")
