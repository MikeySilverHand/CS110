#------------------------------------------------------------ 
# Hypotheis: Countries that maneufactur more vaccinations have  
# a lower death per case ratio. 
#------------------------------------------------------------ 

import matplotlib.pylab as plt 

#from matplotlib import cm 
#import math 
import pandas as pd 
import numpy as np 
import seaborn as sns 
 
sns.set_theme() 
import random 

# ------------------------------------------------------------ 
# mv = manufacturer of vacanations 
# wdd = day wise 
# fg = full grouped 
# ------------------------------------------------------------ 

mv = pd.read_csv('Midterm_Project/country_vaccinations_by_manufacturer.csv') # manufacturer of vacanations and how much is given daily 
wdd = pd.read_csv('Midterm_Project/worldometer_data.csv') # recovered, confirmed, deaths day wise 
gdp = pd.read_csv('Midterm_Project/') # Each countries GPD from 2005-2025

Africa = wdd.loc[wdd['WHO Region']=='Africa']
North_America = wdd.loc[wdd['Country/Region']=='North America']
South_America = wdd.loc[wdd['Country/Region']=='South America']
Eastern_Mediterranean = wdd.loc[wdd['WHO Region']=='EasternMediterranean']
Europe = wdd.loc[wdd['WHO Region']=='Europe']
South_East_Asia = wdd.loc[wdd['WHO Region']=='South-EastAsia']
Western_Pacific = wdd.loc[wdd['WHO Region']=='WesternPacific']

Regions = [Africa, North_America, South_America, Eastern_Mediterranean, Europe, South_East_Asia, Western_Pacific]

for region in Regions:
  print(region)

death_count = wdd.groupby('Deaths/1M pop')['Tot Cases/1M pop'] 