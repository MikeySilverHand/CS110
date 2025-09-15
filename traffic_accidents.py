import matplotlib.pylab as plt
from matplotlib import cm
import math
import pandas as pd
import numpy as np
import random

plt.rc('font', family='times')
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)
plt.rc('font', size=12)
#%matplotlib inline #Depends on coding IDE!
data = pd.read_csv("ACCIDENTS_GU_BCN_2013.csv", encoding='latin-1')

print(data.columns)

# Create a new column which is the date
data['Date'] = '2013-'+data['Mes de any'].astype(str) + '-' + data['Dia de mes'].astype(str)
data['Date'] = pd.to_datetime(data['Date'])
accidents = data.groupby(['Date']).size()
print("Population Mean:", accidents.mean())

fig, ax = plt.subplots(1, 1, figsize=(12, 4))
plt.ylabel('Number of accidents')
plt.xlabel('Day')
plt.plot(range(0, 365), np.array(accidents), 'b-+', lw=0.7)
plt.plot(range(0,365), [accidents.mean()]*365, 'r-', lw=0.7)
plt.show()

fig, ax = plt.subplots(1, 1, figsize=(12, 3))
plt.ylabel('Frequency')
plt.xlabel('Number of accidents')
plt.hist(np.array(accidents), bins=20)
ax.axvline(x=accidents.mean(), color='r')
plt.savefig("bootmean.png",dpi=300)
plt.show()

print("Mean:", accidents.mean(), "; STD:", accidents.std())

df = accidents.to_frame()
m = []
for i in range(10):
  # get a 25% sample
  sampled_ids = np.random.choice(df.index,
  size=np.int64(np.ceil(df.index.size * 0.25)),
  replace=False)
  accidents_sample = df.loc[sampled_ids]
  m.append(accidents_sample[0].mean())
  print('Sample '+str(i)+': Mean', '%.2f' % accidents_sample[0].mean())

fig, ax = plt.subplots(1, 1, figsize=(12, 2))
x = range(10)
ax.step(x,m, where='mid')
ax.set_ylabel('Mean')
ax.set_xlabel('Sample')
plt.show()

# population
df = accidents.to_frame()
N_test = 10000
elements = 200
# mean array of samples
means = [0] * N_test

# sample generation
for i in range(N_test):
  rows = np.random.choice(df.index.values, elements)
  sampled_df = df.loc[rows]
  means[i] = sampled_df.mean()

fig, ax = plt.subplots(1, 1, figsize=(12,3))

plt.hist(np.array(means),bins=50)
plt.ylabel('Frequency')
plt.xlabel('Sample mean value')
ax.axvline(x = np.array(means).mean(),
ymin = 0,
ymax = 700,
color = [1, 0, 0])
plt.savefig("empiricalmean.png",dpi=300, bbox_inches='tight')
plt.show()
plt.set_cmap(cmap=cm.Pastel2)
print("Sample mean:", np.array(means).mean())

rows = np.random.choice(df.index.values, 200)
sampled_df = df.loc[rows]
est_sigma_mean = sampled_df.std()/math.sqrt(200)

print(f'Direct estimation of SE from one sample of 200 elements: {est_sigma_mean[0]}')
print(f'Estimation of the SE by simulating 10000 samples of 200 elements: {np.array(means).std()}')

def meanBootstrap(X, numberb):
  x = [0]*numberb
  for i in range(numberb):
    # Sample with replacement from original data
    sample = np.random.choice(X, size=len(X), replace=True)
    x[i] = np.mean(sample)
    return x

m = meanBootstrap(accidents, 10000)
print("Mean estimate:", np.mean(m))
print("Standard Error (from bootstrap):", np.std(m))

fig, ax = plt.subplots(1, 1, figsize=(12, 3))
plt.ylabel('Frequency')
plt.xlabel('Sample mean value')
plt.hist(m, bins = 50, density = True)
ax.axvline(x = np.mean(m), ymin = 0.0, ymax = 1.0, color = [1, 0, 0])

def medBootstrap(X,numberb):
  import numpy as np
  x = [0]*numberb
  for i in range(numberb):
    sample = [X[_] for _ in np.random.randint(len(X), size=len(X))]
    x[i] = np.median(sample)
  return x

med = medBootstrap(accidents, 10000)
print("Median estimate:", np.mean(med) )
fig, ax = plt.subplots(1, 1, figsize=(12, 3))
plt.hist(med, bins=5, density=True)
plt.ylabel('Frequency')
plt.xlabel('Sample median value')
ax.axvline(x = np.array(med).mean(), ymin = 0, ymax = 1.0, color = [1, 0, 0])