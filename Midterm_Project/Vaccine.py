#------------------------------------------------------------ 
# Hypotheis: Countries that maneufactur more vaccinations have  
# a lower death per case ratio. 
#------------------------------------------------------------ 

import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
import seaborn as sns 
import random 

sns.set_theme() 

# ------------------------------------------------------------ 
# mv = manufacturer of vacanations 
# wom = worldometer 
# gdp = gross domestic product
# ------------------------------------------------------------ 

mv = pd.read_csv('country_vaccinations_by_manufacturer.csv') # manufacturer of vacanations and how much is given daily 
wom = pd.read_csv('worldometer_data.csv') # recovered, confirmed, deaths day wise 
gdp = pd.read_csv('GDP.csv') # Each countries GPD from 2005-2025

#All of the countries that have information
countries = wom['Country/Region'].unique()

#Limit the data to only use 2020-2022 and make sure all the countries match up
gdp_filtered = gdp.loc[gdp['Year'].isin([2020, 2021, 2022]) & (gdp['Country Name'].isin(countries))]

#see how many times each country is referred to each year
counts = gdp_filtered.groupby('Country Name')['Year'].nunique()

#find the valid countries that are referred to 3 times for each year
valid_countries = counts[counts == 3].index

#filter it so that only countries that are considered "valid" will be kept
years = gdp_filtered[gdp_filtered['Country Name'].isin(valid_countries)]

countries_names = years['Country Name'].unique()

sums = years.groupby('Country Name')['Value'].sum()

#store the GDP's of each country for each year
gdp_2020 = np.sort(years[(years['Year'] == 2020)]['Value'])
gdp_2021 = np.sort(years[(years['Year'] == 2021)]['Value'])
gdp_2022 = np.sort(years[(years['Year'] == 2022)]['Value'])

gdp_sums = years.groupby(years['Country Name'].unique())[years.groupby('Country Name')['Value'].sum()]
