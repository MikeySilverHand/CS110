import pandas as pd
import numpy as np

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