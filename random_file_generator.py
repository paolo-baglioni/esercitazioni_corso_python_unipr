# Generator of file with random float numbers for the "marge two sorted files" exercise

from random import random
from random import randint

rows_1 = randint(1,10)
cols_1 = randint(1,10)

print(rows_1,cols_1)

with open("random_file_1.txt","w") as file_1:
    for j in range(rows_1):
        array_1 = [random() for i in range(cols_1)]
        array_1.sort()
        file_1.write(str(array_1[0]))
        for i in range(1,cols_1):
            file_1.write(",")
            file_1.write(str(array_1[i]))
        file_1.write("\n")


rows_2 = randint(1,10)
cols_2 = randint(1,10)

print(rows_2,cols_2)

with open("random_file_2.txt","w") as file_2:
    for j in range(rows_2):
        array_2 = [random() for i in range(cols_2)]
        array_2.sort()
        file_2.write(str(array_2[0]))
        for i in range(1,cols_2):
            file_2.write(",")
            file_2.write(str(array_2[i]))
        file_2.write("\n")
