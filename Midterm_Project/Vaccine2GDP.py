#------------------------------------------------------------ 
# Hypotheis: Countries that produce more vaccines will have a higher gas consumption and higher GDP
#------------------------------------------------------------ 

import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
import seaborn as sns 
import math
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
max_countries_one = wom['Country/Region'].unique()
max_countries_two = mv['location'].unique()

#Group By GDP

#Limit the data to only use 2020-2022 and make sure all the countries match up
gdp_unfiltered_countries = gdp.loc[gdp['Year'].isin([2020, 2021, 2022]) & (gdp['Country Name'].isin(max_countries_one)) & (gdp['Country Name'].isin(max_countries_two))]

#see how many times each country is referred to each year
counts = gdp_unfiltered_countries.groupby('Country Name')['Year'].nunique()

#find the valid countries that are referred to 3 times for each year
valid_countries = counts[counts == 3].index

#filter it so that only countries that are considered "valid" will be kept
gdp_filtered_countries = gdp_unfiltered_countries[gdp_unfiltered_countries['Country Name'].isin(valid_countries)]

#Store everything in a data set with one of each country and their GDP
countries = gdp_filtered_countries.groupby('Country Name')['Value'].sum().reset_index()

#Group By Total Vaccinations

#Filter vaccinations
vaccinations_filtered_countries = mv[mv['location'].isin(valid_countries)]

#Store everything in a data set
sum_vaccinations = vaccinations_filtered_countries.groupby('location')['total_vaccinations'].sum().reset_index().sort_values(by='location').reset_index(drop=True)
countries['Vaccinations'] = sum_vaccinations['total_vaccinations']

#Group By Total cases and deaths by 1 million pop

#Filter total cases
total_cases_n_deaths_filtered_countries = wom[wom['Country/Region'].isin(valid_countries)]

#Store everything in a data set
total_cases = total_cases_n_deaths_filtered_countries.groupby('Country/Region')['Tot Cases/1M pop'].sum().reset_index().sort_values(by='Country/Region').reset_index(drop=True)
countries['Cases'] = total_cases['Tot Cases/1M pop']
total_deaths = total_cases_n_deaths_filtered_countries.groupby('Country/Region')['Deaths/1M pop'].sum().reset_index().sort_values(by='Country/Region').reset_index(drop=True)
countries['Deaths'] = total_deaths['Deaths/1M pop']

#order the countries by GDP
countries = countries.reset_index().sort_values(by='Value').reset_index(drop=True)

subset = countries.iloc[0:len(countries), 1]

#group it into 16 different groups
n = len(countries)
r = math.ceil((n-1)/10)
c = math.ceil((n-1)/4)

groups = [[0 for i in range(c)] for j in range(r)]

num = 0
for i in range(c):
    for j in range(r):
        if(num == n):
            break
        else:
            groups[j][i] = subset.iloc[num]
        num+=1

for i in range(c):
    print(f"\n---Group {i+1}---")
    for j in range(r):
        if(groups[j][i] != 0):
         print(groups[j][i])

print(countries)