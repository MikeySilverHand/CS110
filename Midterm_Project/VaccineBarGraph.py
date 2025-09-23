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
data = pd.read_csv("Midterm_Project/country_vaccinations.csv", encoding='latin-1')

print(data.columns)