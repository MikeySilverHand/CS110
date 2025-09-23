#------------------------------------------------------------
# Hypotheis: 
#
#------------------------------------------------------------

import matplotlib.pylab as plt
#from matplotlib import cm
#import math
import pandas as pd
import numpy as np
import seaborn as sns

sns.set_theme()
#import random

# ------------------------------------------------------------
# mv = manufacturer of vacanations
# wdd = day wise
# fg = full grouped
# ------------------------------------------------------------
mv = pd.read_csv('Midterm_Project/country_vaccinations_by_manufacturer.csv') # manufacturer of vacanations and how much is given daily
wdd = pd.read_csv('Midterm_Project/worldometer_data.csv') # recovered, confirmed, deaths day wise
# fg = pd.read_csv('Midterm_Project/full_grouped.csv') # cases by country (recovered, confirmed, deaths)


wdd['Coutry/Region'] = 'Country/Region'
death_count = wdd.groupby('TotalDeaths')['TotalCases']

g = sns.lmplot(data=wdd, x="TotalCases", y="TotalDeaths", hue="Country/Region", height=5)
g.set_axis_labels("Total Cases Recoreded millions", "Total Deaths recorded thousands")
plt.show()
