# exercise -> merge two sorted files

import csv

numbers_file_1 = []
with open("random_file_1.txt", "r") as file_1:
        reader_1 = csv.reader(file_1, delimiter=",")
        for row_1 in reader_1:
            count = 0
            for j in row_1:
                numbers_file_1.append(float(row_1[count]))
                count +=1
numbers_file_1.sort()

numbers_file_2 = []
with open("random_file_2.txt", "r") as file_2:
        reader_2 = csv.reader(file_2, delimiter=",")
        for row_2 in reader_2:
            count = 0
            for j in row_2:
                numbers_file_2.append(float(row_2[count]))
                count +=1
numbers_file_2.sort()

sorted_array = []

for i in range(len(numbers_file_1)+len(numbers_file_2)):

    print(numbers_file_1)
    print(numbers_file_2)

    if(((len(numbers_file_1)>1) & (len(numbers_file_2)>1))):

        if (numbers_file_1[0]<numbers_file_2[0]):
            sorted_array.append(numbers_file_1[0])
            numbers_file_1.pop(0)

        else:
            sorted_array.append(numbers_file_2[0])
            numbers_file_2.pop(0)

    elif( ((len(numbers_file_1)>1) & (len(numbers_file_2)==1))):

        if (numbers_file_1[0]<numbers_file_2[0]):
            sorted_array.append(numbers_file_1[0])
            numbers_file_1.pop(0)

        else:
            sorted_array.append(numbers_file_2[0])
            sorted_array.extend(numbers_file_1)
            break

    elif( ((len(numbers_file_1)==1) & (len(numbers_file_2)>1))):

        if (numbers_file_1[0]<numbers_file_2[0]):
            sorted_array.append(numbers_file_1[0])
            sorted_array.extend(numbers_file_2)
            break
        else:
            sorted_array.append(numbers_file_2[0])
            numbers_file_2.pop(0)



with open("sorted_file.txt", "w") as sorted_file:
    writer = csv.writer(sorted_file,delimiter=",")
    writer.writerow(sorted_array)
