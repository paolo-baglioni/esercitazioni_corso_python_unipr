# ANNO BISESTILE - EXERCISE 1.4

year=1

while(year):

    year = float(input("Inserire un anno: "))
    if(year%4):
        print("L'anno inserito non è bisestile.")
    else:
        if(year%100):
            print("L'anno inserito è bisestile")
        else:
            if(year%400):
                print("L'anno inserito non è bisestile")
            else:
                print("L'anno inserito è bisestile")
