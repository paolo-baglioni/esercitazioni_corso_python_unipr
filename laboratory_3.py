# laboraotry 2
# paolo baglioni
# paolo.baglioni@unipr.it

import pandas as pd
from scipy import stats
import seaborn as sns
from matplotlib import pylab as plt
import numpy as np
from numpy import genfromtxt
from scipy.optimize import curve_fit

print("Programma iniziato!")

data = pd.read_csv("doubleEdgesPre17.csv")
print(data)

people = data.drop_duplicates("source")

degree = []

for i in people["source"]:
    degree.append(2*len(data.loc[data["target"]==i,"target"]))

a,b = np.histogram(degree,bins=10)
x = []
for i in range(len(b)-1):
    r = (b[i+1]-b[i])/2 + b[i]
    x.append(r)

"""

plt.plot(degree,marker=".",ls="", color="#b103fc")
plt.title("Nodes Degree")
plt.xlabel("Nodes")
plt.ylabel("Degree")
plt.savefig("laboratory_3_degree_nodes.pdf")
plt.show()



plt.plot(x,a,marker=".", ls="")
plt.hist(degree,bins=200)
plt.xlabel("Value")
plt.ylabel("Count")
plt.title("Degree Distribution")
plt.savefig("laboratory_3_degree_distribution.pdf")
plt.show()

"""

def f(x, alpha):
    powers = np.power(x,-alpha)
    A = a[0] / powers[0]
    return A*powers

errors = []

t = np.linspace(0,10,100)
for i in t:
    y_model = f(x,i)
    errors.append( np.mean(np.sqrt((a-y_model)**2)))

popt, _ = curve_fit(f, x, a)  # [4, -2]
y_pred = f(x, *popt)  # arguments unpacking
mse = (np.sqrt((a - y_pred) ** 2)).mean()  # 2.8

plt.plot(t,errors, marker="",ls="-")
plt.scatter(popt,mse,marker=".",color="Red", label=f"k= {popt}, best parameter")
plt.legend()
plt.xlabel(f"$k \ (f(x)=1/x^k )$")
plt.ylabel("Errors")
plt.title("Errors as function of exponential parameter")
plt.savefig("laboratory_3_best_parameter.pdf")
plt.show()


plt.hist(degree,bins=10,label="Real Values")
plt.plot(x,f(x,popt), ls="-",label="Best power-law fit")
plt.xlabel("Value")
plt.ylabel("Count")
plt.title("Degree Distribution")
plt.legend()
plt.savefig("laboratory_3_powerlawfit.pdf")
plt.show()
