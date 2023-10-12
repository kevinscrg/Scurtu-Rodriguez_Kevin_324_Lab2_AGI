from clase.Dreapta import drp
from clase.Punct import Punct
from clase.Polyg import poligon

class cons():


    def inm(self,a,b):
        c=[]
        for i in range(len(a)):
            c.append([])
            for j in range(len(b[0])):
                c[i].append(None)
        for i in range(len(b[0])):
            for j in range(len(a)):
                x=0
                for k in range(len(a[0])):
                    x+=a[j][k]*b[k][i]
                c[j][i] =x
        return c

    def mat_fin(self,d: drp):
        if d.c !=0:
            mt1 = d.M_trans()
        if d.a !=0 and d.b !=0:
            mr1 = d.M_rot()
        mrf = d.M_ref()
        if d.a != 0 and d.b != 0:
            mr2 = d.M_rot_i()
        if d.c != 0:
            mt2 = d.M_trans_i()

        if d.c != 0 and d.a !=0 and d.b !=0:
            aux1 = self.inm(mt1,mr1)
            aux2 = self.inm(aux1,mrf)
            aux3 = self.inm(aux2,mr2)
            return self.inm(aux3, mt2)
        elif d.c !=0 :
            aux1 = self.inm(mt1, mrf)
            return self.inm(aux1,mt2)

        elif d.a !=0 and d.b !=0:
            aux1 = self.inm(mr1, mrf)
            return self.inm(aux1, mr2)
        else:
            return mrf

    def pol(self):
        try:
            p = poligon([])
            n = int(input("dati numarul de varfuri ale poligonului: "))
            while n<1:
                print("nu ati introdus un numar corect de varfuri. ")
                n = int(input("dati numarul de varfuri ale poligonului: "))
            for i in range(0,n):
                a = float(input("x= "))
                b = float(input("y= "))
                x = Punct(a,b)
                p.adaug(x)
            print(p)


        except KeyError:
            print("nu ati introdus date coerente. ")
        except ValueError:
            print("nu ati introdus date coerente. ")

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
            return drp(a,b,c)

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
            return self.drp(p,v)

        except KeyError:
            print("nu ati introdus date coerente. ")
        except ValueError:
            print("nu ati introdus date coerente. ")

    def main(self, d :drp):
        d.afis()
        print("matrice transformarii: ")
        for i in range(3):
            print(self.mat_fin(d)[i])




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
                d = self.ec_g()
                self.main(d)
            elif a == "2":
                d = self.vect()
                self.main(d)

            elif a == "x":
                break
            else:
                print("optiune gresita. ")
