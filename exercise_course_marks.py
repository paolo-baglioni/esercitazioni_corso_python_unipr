# EXERCISE -> courses' marks

import csv

with open("report-2017-2018.csv") as file:
    with open("new_file.txt", "w") as new_file:
        reader = csv.reader(file,delimiter=",")
        writer = csv.writer(new_file,delimiter=",")
        init= [" ","Unit","Question","Students", "Mark"]
        writer.writerow(init)
        row_number = 0
        line = [0] * 5
        line[0] = 0
        for row in reader:
            if(((row_number-9)%19)==0):
                line[1] = int(row[1][0:6])
            if(((row_number-9-5)%19)==0):
                line[2] = 1
                line[3] = int(row[2])
                line[4] = (int(row[3]) * 0 + int(row[4]) * 10 + int(row[6]) * 20 + int(row[8]) * 30)/line[3]
                writer.writerow(line)
                line[0] += 1
            if(((row_number-9-6)%19)==0):
                line[2] = 2
                line[3] = int(row[2])
                line[4] = (int(row[3]) * 0 + int(row[4]) * 10 + int(row[6]) * 20 + int(row[8]) * 30)/line[3]
                writer.writerow(line)
                line[0] += 1
            if(((row_number-9-7)%19)==0):
                line[2] = 3
                line[3] = int(row[2])
                line[4] = (int(row[3]) * 0 + int(row[4]) * 10 + int(row[6]) * 20 + int(row[8]) * 30)/line[3]
                writer.writerow(line)
                line[0] += 1
            if(((row_number-9-8)%19)==0):
                line[2] = 4
                line[3] = int(row[2])
                line[4] = (int(row[3]) * 0 + int(row[4]) * 10 + int(row[6]) * 20 + int(row[8]) * 30)/line[3]
                writer.writerow(line)
                line[0] += 1
            if(((row_number-9-9)%19)==0):
                line[2] = 5
                line[3] = int(row[2])
                line[4] = (int(row[3]) * 0 + int(row[4]) * 10 + int(row[6]) * 20 + int(row[8]) * 30)/line[3]
                writer.writerow(line)
                line[0] += 1
            if(((((row_number-9-10)%19)==0) & (row_number>0))):
                line[2] = 6
                line[3] = int(row[2])
                line[4] = (int(row[3]) * 0 + int(row[4]) * 10 + int(row[6]) * 20 + int(row[8]) * 30)/line[3]
                writer.writerow(line)
                line[0] += 1
            if(((((row_number-9-11)%19)==0) & (row_number>1))):
                line[2] = 7
                line[3] = int(row[2])
                line[4] = (int(row[3]) * 0 + int(row[4]) * 10 + int(row[6]) * 20 + int(row[8]) * 30)/line[3]
                writer.writerow(line)
                line[0] += 1
            if(((((row_number-9-12)%19)==0) & (row_number>2))):
                line[2] = 8
                line[3] = int(row[2])
                line[4] = (int(row[3]) * 0 + int(row[4]) * 10 + int(row[6]) * 20 + int(row[8]) * 30)/line[3]
                writer.writerow(line)
                line[0] += 1
            if(((((row_number-9-13)%19)==0)& (row_number>3))):
                line[2] = 9
                line[3] = int(row[2])
                line[4] = (int(row[3]) * 0 + int(row[4]) * 10 + int(row[6]) * 20 + int(row[8]) * 30)/line[3]
                writer.writerow(line)
                line[0] += 1
            if(((((row_number-9-14)%19)==0)& (row_number>4))):
                line[2] = 10
                line[3] = int(row[2])
                line[4] = (int(row[3]) * 0 + int(row[4]) * 10 + int(row[6]) * 20 + int(row[8]) * 30)/line[3]
                writer.writerow(line)
                line[0] += 1
            if(((((row_number-9-15)%19)==0)& (row_number>5))):
                line[2] = 11
                line[3] = int(row[2])
                line[4] = (int(row[3]) * 0 + int(row[4]) * 10 + int(row[6]) * 20 + int(row[8]) * 30)/line[3]
                writer.writerow(line)
                line[0] += 1






            row_number = row_number +1
