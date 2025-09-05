import pandas as pd

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