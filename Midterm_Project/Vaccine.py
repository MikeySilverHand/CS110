#------------------------------------------------------------ 
# Hypotheis: The more vaccinations a country Manufactured coorelates to less time of cases dropping lower than 10 cases per 1 million population
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
# fg = full grouped
# gdp = gross domestic product
# ------------------------------------------------------------ 

mv = pd.read_csv('country_vaccinations_by_manufacturer.csv') # manufacturer of vacanations and how much is given daily 
wom = pd.read_csv('worldometer_data.csv') #population
cases = pd.read_csv('Cases.csv') #Cases

#All of the countries that have information
max_countries_one = wom['Country/Region'].unique()
max_countries_two = mv['location'].unique()
max_countries_three = cases['Country'].unique()


check = cases[cases['Country'].isin(max_countries_one) & cases['Country'].isin(max_countries_two)]
temp = check.groupby('Country')['Active_cases'].sum()
max_countries_four = check[(check['Active_cases'] != '') & (check['Active_cases'].notna())]

#Group By Total Vaccinations

#Filter countries
vaccination_unfiltered = mv[mv['location'].isin(max_countries_one) & mv['location'].isin(max_countries_three)]

valid_country = vaccination_unfiltered['location'].unique()

#Store everything in a data set
countries = vaccination_unfiltered.groupby('location')['total_vaccinations'].sum().reset_index().sort_values(by='location').reset_index(drop=True)


#Group By Total population

#Filter population
population_unfiltered = wom[wom['Country/Region'].isin(valid_country)]

#Store everything in a data set
population_filtered = population_unfiltered.groupby('Country/Region')['Population'].sum().reset_index().sort_values(by='Country/Region').reset_index(drop=True)
countries['Population'] = population_filtered['Population']


#Group by 2021-2022

#filter cases
max_countries_four = max_countries_four.copy()
max_countries_four['Date'] = pd.to_datetime(max_countries_four['Date'])
cases_filtered = max_countries_four[(max_countries_four['Date'] >= '2021-01-01') ]#& (cases['Country'].isin(max_countries_four))

# population 

merged = cases_filtered.merge(countries, left_on='Country', right_on='location', how='left')
merged['Cases/1M'] = (merged['Active_cases'] / merged['Population']) * 1000000
print(merged)






#order the countries by Population
countries = countries.reset_index().sort_values(by='Population').reset_index(drop=True)


countries_to_plot = ['US', 'India', 'Brazil', 'Russia', 'UK', 'France', 'Turkey', 'Italy', 'Spain', 'Germany']

plt.figure(figsize=(10,8))
for country in countries_to_plot:
    country_data = merged[merged['Country'] == country]
    plt.plot(country_data['Date'], country_data['Cases/1M'], label=country)

# plt.plot(merged['Date'], merged['Cases/1M'])
plt.xlabel('Date')
plt.ylabel('Cases per 1M people')
plt.title('Cases per 1M people in 2021-2022')
plt.legend()
plt.savefig('Cases_per_1M_2021_2022.png')
plt.show()












# subset = countries.iloc[0:len(countries), 1]

# #group it into 10 different groups
# n = len(countries)
# r = math.ceil((n-1)/10)
# c = math.ceil((n-1)/4)

# groups = [[0 for i in range(c)] for j in range(r)]

# num = 0
# for i in range(c):
#     for j in range(r):
#         if(num == n):
#             break
#         else:
#             groups[j][i] = subset.iloc[num]
#         num+=1

# for i in range(c):
#     print(f"\n---Group {i+1}---")
#     for j in range(r):
#         if(groups[j][i] != 0):
#          print(groups[j][i])