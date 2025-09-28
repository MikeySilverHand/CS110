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
data = pd.read_csv("Traffic/ACCIDENTS_GU_BCN_2013.csv", encoding='latin-1')

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
ax.axvline(x = np.array(means).mean(), ymin = 0, ymax = 700, color = [1, 0, 0])
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
plt.show()

def medBootstrap(X, numberb):
  medians = np.zeros(numberb)
  for i in range(numberb):
    sample = np.random.choice(X, size=len(X), replace=True)
    medians[i] = np.median(sample)
  return medians

med = medBootstrap(accidents, 10000)
print("Median estimate:", np.mean(med) )
fig, ax = plt.subplots(1, 1, figsize=(12, 3))
plt.hist(med, bins=5, density=True)
plt.ylabel('Frequency')
plt.xlabel('Sample median value')
ax.axvline(x = np.array(med).mean(), ymin = 0, ymax = 1.0, color = [1, 0, 0])
plt.show()

m= medBootstrap(accidents, 10000)
sample_mean = np.mean(m)
sample_se = np.std(m)

print("Mean estimate:", sample_mean)
print("SE of the estimate:", sample_se)

ci = [np.percentile(m, 2.5), np.percentile(m, 97.5)]
print("Confidence interval:, ci")

m = meanBootstrap(accidents, 10000)

#The CI is the range between the 2.5th and 97.5th percentile
ci = [np.percentile(m, 2.5), np.percentile(m, 97.5)]

print("Mean estimate:", np.mean(m))
print("Bootstrap 95% Convidence interval:", ci)

df = accidents 
n = 100 #number of observations
N_test = 100 #number of samples with n observations
means = np.array([0.0] * N_test) #samples' mean
s = np.array([0.0] * N_test) #samples' std
ci = np.array([[0.0,0.0]] * N_test)
tm = df.mean() #"true" mean

for i in range(N_test): #sample generation and CI computation
  rows = np.random.choice(df.index.values, n)
  sampled_df = df.loc[rows]
  means[i] = sampled_df.mean()
  s[i] = sampled_df.std()
  ci[i] = means[i] + np.array([-s[i] * 1.96/np.sqrt(n), s[i]*1.96/np.sqrt(n)])

out1 = ci[:,0] > tm #Ci that do not contain the "true" mean
out2 = ci[:,1] < tm

fig, ax = plt.subplots(1, 1, figsize=(12, 5))
ind = np.arange(1, N_test+1)
ax.axhline(y = tm, xmin = 0, xmax = N_test+1, color = [0, 0, 0])
ci = np.transpose(ci)

ax.plot([ind,ind], ci, color = '0.75', marker = '_', ms = 0, linewidth = 3)
ax.plot([ind[out1], ind[out1]], ci[:, out1], color = [1, 0, 0, 0.8], marker = '_', ms = 0, linewidth = 3)
ax.plot([ind[out2],ind[out2]],
ci[:, out2], color = [1, 0, 0, 0.8], marker = '_', ms = 0, linewidth = 3)

ax.plot(ind, means, color = [0, .8, .2, .8], marker = '.', ms = 10, linestyle = '')
ax.set_ylabel("Confidence interval for the samples' mean estimate", fontsize =12)
ax.set_xlabel('Samples (with %d observations). ' %n, fontsize = 12)
plt.savefig("confidence.png", dpi = 300, bbox_inches = 'tight')
plt.show()

data = pd.read_csv("ACCIDENTS_GU_BCN_2010.csv", encoding='latin -1')
#Create a new column which is the date
data['Date'] = data['Dia de mes'].apply(lambda x : str(x)) + '-' + \
data['Mes de any'].apply(lambda x : str(x))
data2 = data['Date']
counts2010 =data['Date'].value_counts()
print('2010: Mean', counts2010.mean())

data = pd.read_csv("ACCIDENTS_GU_BCN_2013.csv", encoding='latin -1')
#Create a new column which is the date
data['Date'] = data['Dia de mes'].apply(lambda x : str(x)) + '-' + \
data['Mes de any'].apply(lambda x : str(x))
data2 = data['Date']
counts2013 = data['Date'].value_counts()
print('2013: Mean', counts2013.mean())

n = len(counts2013)
mean = counts2013.mean()
s = counts2013.std()
ci = [mean - s*1.96/np.sqrt(n), mean + s*1.96/np.sqrt(n)]
print('2010 accident rate estimate:', counts2010.mean())
print('2013 accident rate estimate:', counts2013.mean())
print('CI for 2013:', ci)

# Observed difference in our real data
m = len(counts2010)
n = len(counts2013)
p = (counts2013.mean() - counts2010.mean())
print('m:',m, 'n:', n)
print('mean difference: ', p)

x = counts2010 
y= counts2013
pool = np.concatenate([x,y])
np.random.shuffle(pool)

fig, ax = plt.subplots(1, 1, figsize =(12, 3))
plt.hist(pool, bins = 25, density = True)
plt.ylabel('Frequency')
plt.xlabel('Number of accidents')
plt.title("Pooled distribution")

N = 10000 #number of samples
diff = np.arange(N)
for i in np.arange(N):
  p1 = [random.choice(pool) for _ in np.arange(n)]
  p2 = [random.choice(pool) for _ in np.arange(n)]
  diff[i] = (np.mean(p1)-np.mean(p2))

fig, ax = plt.subplots(1, 1, figsize=(12, 3))
plt.hist(diff, bins = 50, density = True)
plt.ylabel('Frequency')
plt.xlabel('Difference in the mean')

#counting how many differences are larger than the observed one
diff2 = np.array(diff)
w1 = np.where(diff2 > p)[0]

len(w1)
print('p-value (Simulation)=', len(w1)/float(N), '(', len(w1)/float(N)*100 ,'%)', 'Difference =', p)
if len(w1)/float(N)<0.05:
  print('The effect is likely')
else:
  print('The effect is not likely')