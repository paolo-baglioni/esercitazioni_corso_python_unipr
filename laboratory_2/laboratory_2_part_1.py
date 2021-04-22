# laboraotry 2
# paolo baglioni
# paolo.baglioni@unipr.it

print("Programma iniziato!")

import pandas as pd
from scipy import stats
import seaborn as sns
from matplotlib import pylab as plt
import numpy as np
from numpy import genfromtxt

new_data = np.genfromtxt('marks-2017-2018.csv', delimiter=",")
new_dataframe = pd.DataFrame(new_data,columns=["cod", "question", "students", "mark"])

old_data = np.genfromtxt('marks-2016-2017.csv', delimiter=",")
old_dataframe = pd.DataFrame(old_data,columns=["cod", "question", "students", "mark"])

N=len(new_data[:,0])
students_second_year = []
mark_second_year = []
for i in range(0,N,11):
     mark_second_year.append(np.mean(new_data[i:i+11,3]))
     students_second_year.append(np.mean(new_data[i:i+11,2]))

N=len(old_data[:,0])
students_first_year = []
mark_first_year = []
for i in range(0,N,11):
     mark_first_year.append(np.mean(old_data[i:i+11,3]))
     students_first_year.append(np.mean(old_data[i:i+11,2]))

# first (mean) scatter plot
plt.scatter(students_second_year,mark_second_year)
plt.xlabel("Students")
plt.ylabel("Mark")
plt.show()



# kde plot - second year
std_second_year = np.round(np.std(mark_second_year),2)
mean_second_year = np.round(np.mean(mark_second_year),2)
sns.distplot(mark_second_year, rug=False, kde=True ,hist=False ,label=f"2017-2018:\nstd = {std_second_year},\nmean= {mean_second_year}")

# kde plot - first year
std_first_year = np.round(np.std(mark_first_year),2)
mean_first_year = np.round(np.mean(mark_first_year),2)
sns.distplot(mark_first_year, rug=False, kde=True , hist=False ,label=f"2016-2017:\nstd= {std_first_year},\nmean= {mean_first_year}")

plt.xlabel("Mark")
plt.legend()
plt.show()

# second (colored) scatter plot

fig, ax = plt.subplots()
scatter = ax.scatter(new_data[:,2],new_data[:,3], c=new_data[:,1])
legend1 = ax.legend(*scatter.legend_elements(),loc="lower right", title="Question")
plt.xlabel("Students")
plt.ylabel("Mark")
ax.add_artist(legend1)
plt.show()

plt.subplot(121)
for i in range(1,12):
    old_mean = np.round(np.mean(old_dataframe.loc[old_dataframe["question"]==i,"mark"]),2)
    old_std = np.round(np.std(old_dataframe.loc[old_dataframe["question"]==i,"mark"]),2)
    old_info = "Q" + str(i) + ":" +" avg: "+ str(old_mean) + ", std:" + str(old_std)
    sns.distplot(old_dataframe.loc[old_dataframe["question"]==i,"mark"],hist=False,label=old_info)
plt.legend()

plt.subplot(122)
for j in range(1,12):
    new_mean = np.round(np.mean(new_dataframe.loc[new_dataframe["question"]==j,"mark"]),2)
    new_std = np.round(np.std(new_dataframe.loc[new_dataframe["question"]==j,"mark"]),2)
    new_info = "Q" + str(j) + ":" +" avg: "+ str(new_mean) + ", std:" + str(new_std)
    sns.distplot(new_dataframe.loc[new_dataframe["question"]==j,"mark"],hist=False,label=new_info)
plt.legend()
plt.show()
