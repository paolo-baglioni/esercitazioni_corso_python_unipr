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

print(old_dataframe)
aggregation_functions = {'question': 'first', 'students': 'mean' , 'mark': 'mean'}
sorted_old_dataframe = old_dataframe.groupby(old_dataframe['cod']).aggregate(aggregation_functions)

slope, intercept, r_value, p_value, std_err = stats.linregress(sorted_old_dataframe["students"], sorted_old_dataframe["mark"])

def f(x): return x*slope + intercept

x = np.linspace(-1,170,10)




plt.plot(sorted_old_dataframe["students"], sorted_old_dataframe["mark"],ls="", marker=".", label="Real Data")
plt.plot(x,f(x),marker="", ls="-", label=f"Linear fit:\n slope={round(slope,2)}\n interc={round(intercept,2)}")
plt.xlabel("Students")
plt.ylabel("Avg mark")
plt.title("Correlation between Students and Avg Mark")
plt.xlim(-1,170)
plt.ylim(10,30)
plt.legend()
plt.show()
