#--------------------------------------------------------------------- 
# Hypotheis: 
# The more vaccinations a country Manufactured coorelates to less time 
# of cases dropping lower than 2000 cases per 1 million population
#---------------------------------------------------------------------

# ------------------------------------------------------------
# Imports
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
# ------------------------------------------------------------

# ------------------------------------------------------------ 
# mv = manufacturer of vacanations 
# wom = worldometer 
# cases = cases per country every day
# ------------------------------------------------------------ 
mv = pd.read_csv('country_vaccinations_by_manufacturer.csv')
wom = pd.read_csv('worldometer_data.csv') 
cases = pd.read_csv('Cases.csv') 
# ------------------------------------------------------------


# ------------------------------------------------------------
# All of the countries that have information
max_countries_one = wom['Country/Region'].unique()
max_countries_two = mv['location'].unique()
max_countries_three = cases['Country'].unique()
# ------------------------------------------------------------


# ------------------------------------------------------------
# All of the countries who dont have any data in active cases
check = cases[cases['Country'].isin(max_countries_one) & cases['Country'].isin(max_countries_two)]
temp = check.groupby('Country')['Active_cases'].sum()
max_countries_four = check[(check['Active_cases'] != '') & (check['Active_cases'].notna())]
# ------------------------------------------------------------

# ------------------------------------------------------------
# Group By Total Vaccinations

# Filter countries
vaccination_unfiltered = mv[mv['location'].isin(max_countries_one) & mv['location'].isin(max_countries_three)]

valid_country = vaccination_unfiltered['location'].unique()

# Store everything in a data set
countries = vaccination_unfiltered.groupby('location')['total_vaccinations'].sum().reset_index().sort_values(by='location').reset_index(drop=True)
# ------------------------------------------------------------


# ------------------------------------------------------------
# Group By Total population

# Filter population
population_unfiltered = wom[wom['Country/Region'].isin(valid_country)]

# Store everything in a data set
population_filtered = population_unfiltered.groupby('Country/Region')['Population'].sum().reset_index().sort_values(by='Country/Region').reset_index(drop=True)
countries['Population'] = population_filtered['Population']
# ------------------------------------------------------------


# ------------------------------------------------------------
# Group by 2021-2022

# filter cases
max_countries_four = max_countries_four.copy()
max_countries_four['Date'] = pd.to_datetime(max_countries_four['Date'])
cases_filtered = max_countries_four[(max_countries_four['Date'] >= '2021-01-01') ]
# ------------------------------------------------------------

# ------------------------------------------------------------
# Population with cases/1M in a new dataframe

merged = cases_filtered.merge(countries, left_on='Country', right_on='location', how='left')
merged['Cases/1M'] = (merged['Active_cases'] / merged['Population']) * 1000000
# ------------------------------------------------------------

# ------------------------------------------------------------
# Outputs

countries_to_plot = np.random.choice(merged['Country'].unique(), 10, replace=False)

#  Graph 1
plt.figure(figsize=(10,8))
for country in countries_to_plot:
    country_data = merged[merged['Country'] == country]
    country_to_output = country_data.groupby('Country')['total_vaccinations'].sum()
    for i in country_to_output:
        print(f"{country_data['Country'].unique()}: {i}")
    plt.plot(country_data['Date'], country_data['Cases/1M'], label=country)

plt.xlabel('Date')
plt.ylabel('Cases per 1M people')
plt.title('Cases per 1M people in 2021-2022')
plt.legend()
plt.savefig('Cases_per_1M_2021_2022.png')
plt.show()

# Graph 2
plt.figure(figsize=(10,8))
temp = merged[merged['Country'].isin(countries_to_plot)]
total_vaccinations_by_country = temp.groupby('Country')['total_vaccinations'].sum().reset_index().sort_values(by='total_vaccinations', ascending=False).reset_index(drop=True)

plt.bar(total_vaccinations_by_country['Country'], total_vaccinations_by_country['total_vaccinations'])
plt.xlabel('Country')
plt.ylabel('Total Vaccinations')
plt.title('Total Vaccinations by Country')
plt.savefig('Total_Vaccinations_by_Country.png')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# ------------------------------------------------------------