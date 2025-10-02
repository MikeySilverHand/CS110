#--------------------------------------------------------------------- 
# Hypotheis: 
# The more vaccinations a country Manufactured coorelates to less time 
# of cases dropping lower than 2000 cases per 1 million population
#---------------------------------------------------------------------

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


#Group By Total Vaccinations

#filter total vaccinations
vaccination_unfiltered = mv[mv['location'].isin(max_countries_one) & mv['location'].isin(max_countries_three)]

valid_country = vaccination_unfiltered['location'].unique()

#Store everything in a data set
countries = vaccination_unfiltered.groupby('location')['total_vaccinations'].sum().reset_index().sort_values(by='location').reset_index(drop=True)

check_two = mv[mv['location'].isin(max_countries_one) & mv['location'].isin(max_countries_three)]
check_three = (check_two.groupby('location')['total_vaccinations'].sum())
check_four = check_three.astype('float')
max_countries_four = check_four[(check_four > 0.0)]

countries['total_vaccinations'] = max_countries_four

print(countries)

#Group by 2021-2022

#filter cases
check = cases[cases['Country'].isin(max_countries_one) & cases['Country'].isin(max_countries_two)]
max_countries_five = check[(check['Active_cases'] != '') & (check['Active_cases'].notna())]
max_countries_five = max_countries_five.copy()
max_countries_five['Date'] = pd.to_datetime(max_countries_five['Date'])
cases_filtered = max_countries_five[(max_countries_five['Date'] >= '2021-01-01') ]

print(cases_filtered)

#Group By Total population

#Filter population
population_unfiltered = wom[wom['Country/Region'].isin(max_countries_four) & wom['Country/Region'].isin(max_countries_five)]
population_filtered = population_unfiltered.groupby('Country/Region')['Population'].sum().reset_index().sort_values(by='Country/Region').reset_index(drop=True)
countries['Population'] = population_filtered['Population']

print(countries)

#Population with cases/1M in a new dataframe

merged = cases_filtered.merge(countries, left_on='Country', right_on='location', how='left')
merged['Cases/1M'] = (merged['Active_cases'] / merged['Population']) * 1000000


#Outputs

countries_to_plot = [np.random.choice(merged['Country'], 10)]

plt.figure(figsize=(10,8))
for country in countries_to_plot:
    country_data = merged[merged['Country'] == country]
    plt.plot(country_data['Date'], country_data['Cases/1M'], label=country)

plt.xlabel('Date')
plt.ylabel('Cases per 1M people')
plt.title('Cases per 1M people in 2021-2022')
plt.legend()
plt.savefig('Cases_per_1M_2021_2022.png')
plt.show()


plt.figure(figsize=(10,8))
total_vaccinations_by_country = merged.groupby('Country')['total_vaccinations'].max()
total_vaccinations_by_country = total_vaccinations_by_country.reindex(countries_to_plot)

plt.bar(total_vaccinations_by_country.index, total_vaccinations_by_country.values)
plt.xlabel('Country')
plt.ylabel('Total Vaccinations')
plt.title('Total Vaccinations by Country')
plt.savefig('Total_Vaccinations_by_Country.png')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()