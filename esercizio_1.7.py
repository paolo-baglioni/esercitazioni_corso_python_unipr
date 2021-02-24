# DIVISORI - EXERCISE 1.7

n = int(input("digitare il numero n: "))
print("I divisori di ", n, " sono:")
for i in range(1,n+1):
    if ( (n%i) == 0):
        print(i," ")