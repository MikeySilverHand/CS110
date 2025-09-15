file = open('adult.data', 'r')

def chr_int(a):
  if a.isdigit():
    return int(a)
  else: return 0

data = []
for line in file:
  data1 = line.split(', ')
  if len(data1) == 15:
    data.append([
      chr_int(data1[0]), data1[1], chr_int(data1[2]),
      data1[3], chr_int(data1[4]), data1[5], data1[6],
      data1[7], data1[8], data1[9], chr_int(data1[10]),
      chr_int(data1[11]), chr_int(data1[12]), data1[13],
      data1[14]
    ])

print(data[1:2])
#Output:
#[[50, 'Self-emp-not-inc', 83311, 'Bachelors', 13,
#  'Married-civ-spoise', 'Exec-managerial', 'Husband', 'White,'
#  'Male', 0, 0, 13, 'United-States', '<=50K/n']]

import pandas as pd
import matplotlib as plt

df = pd.DataFrame(data)
df.columns = ['age', 'type_employer', 'fnlwgt', 'education',
              'education-num', 'marital', 'occupation', 'relationship',
              'race', 'sex', 'capital_gain', 'capital_loss', 
              'hr_per_week', 'country', 'income']

df.head()

counts = df. groupby ('country').size()
print (counts)
# Filter for males
ml = df [(df.sex == 'Male')]
# Filter for males with high income
ml1 = df [(df.sex == 'Male') & (df.income=='>50K\n')]
# Filter for females
fm = df [(df.sex == 'Female')]
# Filter for females with high income
fm1 = df [(df.sex == 'Female') & (df.income=='>50K\n')]


df1 = df [(df.income =='>50K\n')]

print ('The rate of people with high income is: ',
  int(len (df1) /float (len (df))*100), '%.')

# Output: The rate of people with high income is: 24 %.
print ('The rate of men with high income is: ',
  int(len (ml1) / float (len (ml))*100), '%.')

# Output: The rate of men with high income is: 30 %.
print ('The rate of women with high income is: ',
  int(len (fm1) /float (len (fm))*100), '%.')

#Output: The rate of women with high income is: 11 ٪٠

ml_mu = ml['age'].mean()
fm_mu = fm['age'].mean()
ml_var = ml['age'].var()
fm_var = fm['age'].var()
ml_std = ml['age'].std()
fm_std = fm['age'].std()
print('Statistics of age for men: mu:', ml_mu, 'var:', ml_var, 'std:', ml_std)
print('Statistics of age for women: mu:', fm_mu, 'var:', fm_var, 'std:', fm_std)

ml_mu_hr = ml['hr_per_week'].mean()
fm_mu_hr = fm['hr_per_week'].mean()
ml_var_hr = ml['hr_per_week'].var()
fm_var_hr = fm['hr_per_week'].var()
ml_std_hr = ml['hr_per_week'].std()
fm_std_hr = fm['hr_per_week'].std()
print('Statistics of hours per week for men: mu:', ml_mu_hr, 'var:', ml_var_hr, 'std:', ml_std_hr)
print('Statistics of hours per week for women: mu:', fm_mu_hr, 'var:', fm_var_hr, 'std:', fm_std_hr)

ml_median = ml ['age']. median ()
fm_median = fm ['age']. median ()
print ("Median age per men and women :", ml_median , fm_median )
ml_median_age = ml1 ['age']. median ()
fm_median_age = fm1 ['age']. median ()
print ("Median age per men and women with high - income :", ml_median_age , fm_median_age )
ml_median_hr = ml ['hr_per_week']. median ()
fm_median_hr = fm ['hr_per_week']. median ()
print ("Median hours per week per men and women :", ml_median_hr , fm_median_hr )


import matplotlib.pyplot as plt
ml_age = ml['age']
ml_age . hist(density = False , histtype = 'stepfilled', bins =20)
plt.xlabel('Age', fontsize =15)
plt.ylabel('Male samples', fontsize =15)
plt.show()
fm_age = fm['age']
fm_age.hist( density = False , histtype = 'stepfilled', bins =10)
plt.xlabel('Age', fontsize =15)
plt.ylabel('Female samples', fontsize =15)
plt.show()

import seaborn as sns
fm_age.hist(density = False , histtype = 'stepfilled', alpha =.5 , bins =20) # default number of bins = 10
ml_age.hist(density = False , histtype = 'stepfilled', alpha =.5 , color = sns.desaturate ("indianred", .75) , bins =10)
plt.xlabel('Age', fontsize =15)
plt.ylabel('Samples', fontsize =15)
plt.show()

import scipy.stats as stats
ml_age.hist(density = True , histtype = 'stepfilled', bins =20)
plt.xlabel('Age', fontsize =15)
plt.ylabel('Probability', fontsize =15)
plt.show()

fm_age.hist( density = True , histtype = 'stepfilled', bins =20)
plt.xlabel('Age', fontsize =15)
plt.ylabel('Probability', fontsize =15)
plt.show()

# Plot CDFs on the same axes
ml ['age'].hist (density = True , histtype = 'step', cumulative = True ,
linewidth =3.5 , bins =20 , label = 'Male')
fm ['age']. hist ( density = True , histtype = 'step', cumulative = True ,
linewidth =3.5 , bins =20 , label = 'Female', color = sns.desaturate ("indianred", .75))
plt.xlabel('Age', fontsize =15)
plt.ylabel('CDF', fontsize =15)
plt.legend()
plt.show()

df['age'].median() #37
 # Lets see how many outliers we can detect in our example :
len( df[( df.income == ' >50 K \ n ') & ( df['age'] < df ['age'].median () - 15) ]) #5
len( df[( df.income == ' >50 K \ n ') & ( df['age'] > df ['age'].median () + 35) ]) #69
 # If we think that outliers correspond to errors , an option is to trim the data by discarting the highest and lowest values .
df2 = df.drop (df.index[( df.income == ' >50 K \ n ') &
((df ['age'] > df['age'].median () + 35) | ( df['age'] < df['age'].median () - 15) ) ])

ml1_age = ml1['age']
fm1_age = fm1['age']
ml2_age = ml1_age.drop(ml1_age.index[(ml1_age > df['age'].median() + 35) & (ml1_age > df['age'].median () - 15) ])
fm2_age = fm1_age.drop(fm1_age.index[(fm1_age > df ['age'].median() + 35) & (fm1_age > df['age'].median () - 15) ])

mu2ml = ml2_age.mean()
std2ml = ml2_age.std()
md2ml = ml2_age.median()
# Computing the mean , std , median , min and max for the high - income male population
print ("Men statistics: Mean :" , mu2ml , "Std:" , std2ml , "Median:" , md2ml , "Min:" , ml2_age .
min () , " Max : " , ml2_age . max () )
# Men statistics : Mean : 4 4 .3 17 9 82 1 23 92 0 61 5 Std : 1 0. 0 19 74 9 85 71 7 14 1 2 Median : 44.0 Min : 19
Max: 72
mu3ml = fm2_age.mean()
std3ml = fm2_age.std()
md3ml = fm2_age.median()
# Computing the mean , std , median , min and max for the high - income female population
print ("Women statistics: Mean:", mu3ml , "Std:" , std3ml , "Median:" , md3ml , "Min:" , fm2_age.min () , "Max:" , fm2_age.max() )
# Women statistics : Mean : 44 . 31 79 8 21 2 39 20 6 15 Std : 1 0 .0 1 97 49 8 57 1 71 41 2 Median : 44.0 Min : 19
Max : 72
print('The mean difference with outliers is : %4.2f.' % (ml_age.mean() - fm_age.mean()))
print ("The mean difference without outliers is : %4.2f." % (ml2_age.mean() - fm2_age.mean()))
# The mean difference with outliers is : 2.58.
# The mean difference without outliers is : 2.44.

plt.figure(figsize=(13.4, 5))
df.age[(df.income == '>50K\n')].plot(alpha =.25, color='blue')
df2.age[(df2.income == '>50K\n')].plot(alpha =.45, color='red')
plt.ylabel('Age')
plt.xlabel('Samples')
plt.show()

import numpy as np
countx, divisionx = np.histogram(ml2_age, density = True)
county, divisiony = np.histogram(fm2_age, density = True)

import matplotlib . pyplot as plt
val = [(divisionx[i]+ divisionx [i+1]) /2 for i in range(len(divisionx) -1)]
plt.plot( val , countx - county , 'o-')
plt.title('Differences in promoting men vs. women')
plt.xlabel('Age', fontsize =15)
plt.ylabel('Differences', fontsize =15)
plt.show()

# The difference between the mean values of male and female populations .
print("Remember: We have the following mean values for men , women and the difference: Originally: ", ml_age.mean(), fm_age.mean(), ml_age.mean() - fm_age.mean())
# The difference between the mean values of male and female populations .
print("For high - income: ", ml1_age.mean() , fm1_age.mean() , ml1_age.mean() - fm1_age.mean())
# The difference between the mean values of male and female populations .
print("After cleaning: ", ml2_age.mean() , fm2_age.mean() , ml2_age.mean() - fm2_age.mean())
print("\nThe same for the median: ")
# The difference between the mean values of male and female populations .
print(ml_age.median(), fm_age.median(), ml_age.median() - fm_age.median() )
# The difference between the mean values of male and female populations .
print(ml1_age.median(), fm1_age.median(), ml1_age.median() - fm1_age.median() )
# The difference between the mean values of male and female populations .
print(ml2_age.median() , fm2_age.median() , ml2_age.median() - fm2_age.median())

# ml1 = df [( df . sex == ’ Male ’) &( df . income == ’ >50 K \ n ’) ]
ml2 = ml1.drop(ml1.index[(ml1['age'] > df['age'].median() + 35) & (ml1['age'] > df['age']. median () - 15)])
fm2 = fm1.drop(fm1.index[(fm1['age'] > df['age'].median() + 35) & (fm1['age'] > df['age']. median () - 15)])
print(ml2.shape, fm2.shape)

print("Men grouped in 3 categories : " )
print("Young: " , int(round(100*len(ml2_age[ml2_age <41])/float(len(ml2_age.index)))), "%." )
print("Elder: " , int(round(100*len(ml2_age[ml2_age >44])/float(len(ml2_age.index)))), "%." )
print("Average age: ", int(round(100* len(ml2_age[(ml2_age >40) & (ml2_age < 45) ])/float(len(ml2_age.index)))), "%.")

print("Men grouped in 3 categories : " )
print("Young: " , int(round(100*len(fm2_age[fm2_age <41])/float(len(fm2_age.index)))), "%." )
print("Elder: " , int(round(100*len(fm2_age[fm2_age >44])/float(len(fm2_age.index)))), "%." )
print("Average age: ", int(round(100* len(fm2_age[(fm2_age >40) & (fm2_age < 45) ])/float(len(fm2_age.index)))), "%.")

print("The male mean:", ml2_age.mean())
print("The female mean:", fm2_age.mean())

# Assuming ml2_age and fm2_age are cleaned datasets of high - income earners
ml2_young = len(ml2_age[ml2_age <41]) / float (len(ml2_age))
fm2_young = len(fm2_age[fm2_age <41]) / float (len(fm2_age))
# This is the risk reduction for men , or risk increase for women
print("Relative risk increase for women getting early promotion: ",
100 * (1 - ml2_young / fm2_young), "%." )
# Output : Relative risk increase for women getting early promotion : 21.0 %.
ml2_elder = len(ml2_age[ml2_age >44]) / float(len(ml2_age))
fm2_elder = len(fm2_age[fm2_age >44]) / float(len(fm2_age))
print("Relative risk for men getting late promotion:" ,
100 * ml2_elder / fm2_elder , "%.")
# Output : Relative risk for men getting late promotion : 129.0 %.
# ( Men are 29% more likely )

import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 4, sharey = True, squeeze = True, figsize =(14, 5))
x = np.linspace(0, 1, 100)
for i in range (4) : 
  f = np.mean(np.random.random((10000, i +1)), 1)
  m, s = np.mean(f), np.std(f, ddof =1)
  fn = (1/(s * np.sqrt(2* np.pi))) * np.exp(-(x-m)**2/(2*s**2)) # normal pdf
  ax[i].hist(f, 40, density = True, color =[0, 0.2, .8, .6])
  ax[i].set_title('n =% d' %(i+1))
  ax[i].plot(x, fn, color =[1, 0, 0, .6], linewidth =5)
plt.suptitle('Demonstration of the central limit theorem for a uniform distribution', y=1.05)
plt.show ()