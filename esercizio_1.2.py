# EQUAZIONE DI SECONDO GRADO - EXERCISE 1.2

print("Si consideri l'equazione ax^2 + bx + c = 0")
a = float(input("Inserire il valore di a: "))
b = float(input("Inserire il valore di b: "))
c = float(input("Inserire il valore di c: "))
print("L'equazione %dx^2 + %dx + %d = 0 ..." %(a,b,c))

if (a == 0):
    if (b == 0):
        if (c==0):
            print("Ha una soluzione banale.")
        else :
            print("Non ha soluzioni.")
    else: print("Ha una soluzione reale.")
else:
    delta = b**2 - 4*a*c
    if (delta > 0):
        print("Ha due soluzioni reali.")
    elif (delta == 0):
        print("Ha una sola soluzione reale.")
    else:
        print("Non ha soluzioni reali.")