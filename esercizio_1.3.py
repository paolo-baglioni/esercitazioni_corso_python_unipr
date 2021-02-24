# EQUAZIONE DI SECONDO GRADO - EXERCISE 1.2

import math 

while(True):
    print("Si consideri l'equazione ax^2 + bx + c = 0")
    a = float(input("Inserire il valore di a: "))
    b = float(input("Inserire il valore di b: "))
    c = float(input("Inserire il valore di c: "))
    print("L'equazione %dx^2 + %dx + %d = 0 ..." %(a,b,c))
    if (a == 0):
        if (b == 0):
            if (c==0):
                print("Ha una soluzione banale 0=0.")
            else :
                print("Non ha soluzioni.")
        else: 
            x = (-c)/b
            print("Ha una soluzione reale:")
            print("x = ", x)
    else:
        delta = b**2 - 4*a*c
        if (delta > 0):
            x_1 = (-b + math.sqrt(delta))/(2*a)
            x_2 = (-b - math.sqrt(delta))/(2*a)
            print("Ha due soluzioni reali:")
            print("x_1 = ", x_1)
            print("x_2 = ", x_2)
        elif (delta == 0):
            x = -b/(2*a)
            print("Ha una sola soluzione reale:")
            print("x = ",x)
        else:
            print("Non ha soluzioni reali.")
    print("Digita un numero diverso da zero se vuoi valutare un'altra equazione di secondo grado.")
    print("Digita 0 se vuoi uscire dal programma.")
    control = float(input())
    if(control):
        continue
    else:
        break
        
        