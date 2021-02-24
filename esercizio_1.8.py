n = 1
max_value = 0

while( n>0 ):
    n = int(input("Digirate un numero naturale: "))
    if ((n > max_value) & ((n%2)!=0)):
        max_value = n
if(max_value):       
    print("Numero massimo e dispari tra quelli inseriti: ",max_value)
else:
    print("Non hai inserito alcun numero dispari.")
        
