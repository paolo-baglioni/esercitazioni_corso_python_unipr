# TRE CARTE - EXERCISE 1.9

import random

monete = 10
print("Benvenuto nel gioco delle tre carte.")
print("************************************")
print("La tua partita inizia con 10 monete ...")

while(monete):

    indicator = int(input("Digita 1 per giocare \nDigita 2 per sapere quante monete rimangono \nDigita 3 per ritirarti dal gioco \n"))
    
    if(indicator == 1):
        puntata = int(input("Quante monete vuoi puntare? "))
        if(puntata>monete): 
            print("Non hai tutte queste monete") 
            continue
        elif(puntata <= monete):
            azzardo = int(input("Digita un numero da 1 a 3 su cui scommettere .. "))
            carta = random.randint(1,3)
            print("ho estratto il numero %i" % carta )
            if(azzardo == carta):
                monete = monete + puntata
                print("Hai vinto, ora hai %i monete" % monete)
            else:
                monete = monete - puntata
                print("Hai perso, ora hai %i monete" % monete)
        
    elif(indicator == 2):
        print("Ti rimangono %i monete" % monete)
        
    elif(indicator == 3):
        print("Ti stai ritirando dal gioco con %i monete!" % monete)
        break
        
    else:
        print("Non hai digitato nessuno dei 3 numeri.")
        continue

if(monete == 0 ):
    print("Ho chiuso il gioco perchè hai finito le monete.")