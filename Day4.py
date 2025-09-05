import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {'year': [2010, 2011, 2012, 2010, 2011, 2012, 2010, 2011, 2012], 
        'team': ['FCBarcelona', 'FCBarcelona', 'FCBarcelona', 'RMadrid', 'RMadrid', 'RMadrid', 'ValenciaCF', 'ValenciaCF', 'ValenciaCF'],
        'wins': [30, 28, 32, 29, 32, 26, 21, 17, 19],
        'draws': [6, 7, 4, 5, 4, 7, 8, 10, 8],
        'losses': [2, 3, 2, 4, 2, 5, 9, 11, 11]
        }

football = pd.DataFrame(
  data, columns = ['year', 'team', 'wins', 'draws', 'losses'])

print(football)

edu = pd.read_csv('educ_figdp_1_Data.csv',
                  na_values=':', usecols=['TIME', 'GEO', 'Value'])

print(edu)
#edu.head(), edu.columns, edu.index, edu.tail(), edu.values(), edu.describe()
#edu['Value'], edu[10:14], edu.loc[90:94,['TIME','GEO']]
#edu[edu['Value'] <6.5].tail, edu[edi['Value'].isnull()].head()
#count(), sum(), mean(), median(), min(), max(), prod(), std(), var()

#The pandas max function excludes NaN values, thus they are interpreted
#as missing values, while the standard Python max function will take the
#mathematical interpretation of NaN and return it as the maximum
print('Pandas max function:', edu['Value'].max())
print('Python max function:', max(edu['Value']))

#Apply operations over all the values in rows, columns or a selection of both                         
s = edu['Value']/100
print(s.head())

#Apply any function to a DataFrame or Series just putting its name as
#argument of the apply method. For example, in the following code, we
#apply the sqrt function from the numpy library to perform the square root
#of each value in the ’Value’ column
s = edu['Value'].apply(np.sqrt)
print(s.head())

#If we need to design a specific function to apply it, we can write an in-line
#function, commonly known as a -function
s = edu['Value'].apply(lambda d: d**2)
print(s.head())

#Another basic manipulation operation is to set new values in our
#DataFrame. This can be done directly using the assign operator = over a
#DataFrame
edu['ValueNorm'] = edu['Value']/edu['Value'].max()
print(edu.tail())

#his removes the indicated rows if axis=0, or the indicated columns if axis=1
edu.drop('ValueNorm', axis=1, inplace=True)
print(edu.head())

#This function receives as an argument two data frames, and returns a new data frame
#with the contents of both
edu = pd.concat([edu,pd.DataFrame({'TIME': 2000, 'Value': 5.00, 'GEO': 'a'}, index=[max(edu.index)+1])])
print(edu.tail())

#Now we have to set the axis to 0, and specify the index of the row we want to remove
edu.drop(max(edu.index), axis=0, inplace=True)
print(edu.tail())

#f we want to erase any row that contains an NaN value, we have to set the how keyword to an
eduDrop = edu.dropna(how='any', subset=['Value'], axis=0)
print(eduDrop.head())

eduFilled = edu.fillna(value={'Value': 0})
print(eduFilled.head())

#Sort a dataframe using nay column descending
edu.sort_values(by='Value', ascending=False, inplace=True)
print(edu.head())

edu.sort_index(axis=0, ascending=True, inplace=True)
print(edu.head())

group = edu[['GEO', 'Value']].groupby('GEO').mean()
print(group.head())

filtered_data = edu[edu['TIME'] > 2005]
pivedu = pd.pivot_table(filtered_data, values='Value', index=['GEO'], columns=['TIME'])
print(pivedu.head())

#Now we can use the new index to select specific rows by label, using the loc operator
print(pivedu.loc [['Spain' , 'Portugal'] , [2006 , 2011]])

pivedu = pivedu.drop(['Euro area (13 countries)',
                      'Euro area (15 countries)',
                      'Euro area (17 countries)',
                      'Euro area (18 countries)',
                      'European Union (25 countries)',
                      'European Union (27 countries)',
                      'European Union (28 countries)'
                      ], axis=0)
pivedu = pivedu.rename(
  index={'Germany (untill 1990 former territory of the FRG)': 'Germany'})
pivedu = pivedu.dropna()
print(pivedu.rank(ascending=False, method='first').head())

#sum up all of the columns and rank the result
totalSum = pivedu.sum(axis=1)
print(totalSum.rank(ascending=False, method='dense').sort_values().head())

fig = plt.figure(figsize=(12, 5))
totalSum = pivedu.sum(axis=1).sort_values(ascending=False)
totalSum.plot(kind='bar', style='b', alpha=0.4, title='Total Values for Country')
plt.savefig('Totalvalue_Country.png', dpi=300, bbox_inches='tight')
plt.show()

my_colors = ['b', 'r', 'g', 'y', 'm', 'c']
ax = pivedu.plot(kind='barh', stacked=True, color=my_colors, figsize=(12, 6))
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig('Value_Time_Country.png', dpi=300, bbox_inches='tight')
plt.show()