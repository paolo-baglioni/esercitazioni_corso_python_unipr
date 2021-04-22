# laboratory 1
# paolo baglioni
# paolo.baglioni@unipr.it

print("Programma iniziato!")

import pandas as pd
from scipy import stats
import seaborn as sns
from matplotlib import pylab as plt

tips = sns.load_dataset("tips")
dinner = tips.loc[tips["time"] == "Dinner"]
lunch = tips.loc[tips["time"] == "Lunch"]

sns.distplot(dinner["tip"], rug=False,hist=False, kde=True , label="Dinner")
sns.distplot(lunch["tip"], rug=False, hist=False, kde=True, label="Lunch")
plt.legend()
plt.savefig("dinner_and_lunch_tips_distribution.pdf")
plt.show()
