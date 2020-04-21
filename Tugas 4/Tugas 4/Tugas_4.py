import os,sys
import math

def head():
    print("\n\t------- Penghitung Proyektil Peluru -------")
    print("\t Dalam Satuan International || Senjata Perang Dunia 2")
    print("\t Kelompok 27")
    print("\t Ega Oktabrianto (21120119130066) || M. Ilzam Muhtaromi (21120119120027) \n")
def list():
    mu = ["Invalid",
         "Kar98K", 
         "StG 44", 
         "FG42",
         "M1 Garand",
         "Arisaka 99",
         "(Mortar Berat) 21Cm Granatenwerfer 69"]
    for i in range(1,7):
        print("\t ",i,"=",mu[i])

    a = int(input("\n  Pilih senjata (angkanya saja) : "))
    if a!=1 and a!=2 and a!=3 and a!=4 and a!=5 and a!=6 :
        print(" ---------------------------------------------\n  INVALID INPUT\n")
        print("  Try Again\n")
        head()
        list()

    b = input("  Pilih Ketinggian Maksimum / Jarak terjauh (k/j)  : ")
    print("\n Senjata : "+mu[a])

    if b == "k":
        print("  Menghitung Ketinggian Maksimum {}".format(mu[a]))
        p = float(input("  Input sudut : "))
        if a == 1:
            q = 700*math.sin(math.radians(p))
            eq = q*q/ (2*9.81)
            print("Ketinggian Maksimum",str(eq) + " M")
        elif a == 2:
            q = 685*math.sin(math.radians(p))
            eq = q*q/ (2*9.81)
            print("Ketinggian Maksimum",str(eq) + " M")
        elif a == 3:
            q = 740*math.sin(math.radians(p))
            eq = q*q/ (2*9.81)
            print("Ketinggian Maksimum",str(eq) + " M")
        elif a == 4:
            q = 853*math.sin(math.radians(p))
            eq = q*q/ (2*9.81)
            print("Ketinggian Maksimum",str(eq) + " M")
        elif a == 5:
            q = 755*math.sin(math.radians(p))
            eq = q*q/ (2*9.81)
            print("Ketinggian Maksimum",str(eq) + " M")
        elif a == 6:
            q = 247*math.sin(math.radians(p))
            eq = q*q/ (2*9.81)
            print("Ketinggian Maksimum",str(eq) + " M")
        else:
            print(" ---------------------------------------------\n  INVALID INPUT Input hanya k / j\n")
            print("  Try Again\n")
            head()
            list()

    elif b == "j":
        print(" Menghitung Jarak Maksimum {}".format(mu[a]))
        p = float(input("  Input sudut : "))
        if a == 1:
           q = 700*math.sin(math.radians(p))
           qq = 700*math.cos(math.radians(p))
           eq = q*qq/ (9.81)
           print("Jarak Maksimum",str(eq) + " M")
        elif a == 2:
           q = 685*math.sin(math.radians(p))
           qq = 685*math.cos(math.radians(p))
           eq = q*qq/ (9.81)
           print("Jarak Maksimum",str(eq) + " M")
        elif a == 3:
           q = 740*math.sin(math.radians(p))
           qq = 740*math.cos(math.radians(p))
           eq = q*qq/ (9.81)
           print("Jarak Maksimum",str(eq) + " M")
        elif a == 4:
           q = 853*math.sin(math.radians(p))
           qq = 853*math.cos(math.radians(p))
           eq = q*qq/ (9.81)
           print("Jarak Maksimum",str(eq) + " M")
        elif a == 5:
           q = 755*math.sin(math.radians(p))
           qq = 755*math.cos(math.radians(p))
           eq = q*qq/ (9.81)
           print("Jarak Maksimum",str(eq) + " M")
        elif a == 6:
           q = 247*math.sin(math.radians(p))
           qq = 247*math.cos(math.radians(p))
           eq = q*qq/ (9.81)
           print("Jarak Maksimum",str(eq) + " M")
    else:
        print(" ---------------------------------------------\n  INVALID INPUT Input hanya k / j\n")
        print("  Try Again\n")
        head()
        list()

def lagi():
    p = input("\n  Lagi (y/n) : ")
    if p == "y":
        print(" ---------------------------------------------")
        head()
        list()
    elif p == "n":
        exit(0)
    else:
        print(" ---------------------------------------------\n  INVALID INPUT\n")
        print("  Try Again\n")
        lagi()    

if __name__=='__main__':
    head()
    list()
    lagi()
