import seaborn as sns
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1, rc={"lines.linewidth": 2, 'font.family': [u'times']})
import matplotlib.pylab as plt
import numpy as np

x = [5, 2, 12, 9, 15, 6, 25, 16, 23] #Driving experience (years).
y = [65, 89, 50, 73, 45, 55, 38, 61, 35] #Monthly Auto Insurance

plt.scatter(x, y, color = 'red')
plt.show()

X1 = np.random.randn(300, 2) # Random points sampled from a university normal (Gaussian) distribution
A = np.array([[0.6, .4], [.4, 0.6]])
X2 = np.dot(X1, A)
plt.plot(X2[:, 0], X2[:, 1], "o", alpha = 0.3) #alpha, blendingf value, between 0 (transparent) and 1 (opaque).
plt.show()

model = [0+1*x for x in np.arange(-2,3)]
plt.plot(X2[:, 0], X2[:, 1], "o", alpha = 0.3)
plt.plot(np.arange(-2,3), model, 'r')
plt.show()

plt.plot(X2[:, 0], X2[:, 1], "o", alpha = 0.3)
#We can use several parameters and we do not know which is the best model
model1 = [0+1*x for x in np.arange(-2,3)]
model2 = [0.3+0.9*x for x in np.arange(-2,3)]
model3 = [0-0.1*x for x in np.arange(-2,3)]
plt.plot(np.arange(-2,3), model1, 'r')
plt.plot(np.arange(-2,3), model2, 'g')
plt.plot(np.arange(-2,3), model3, 'y')
plt.savefig("ExSimpleRegModels.png", dpi = 300, bbox_inches = 'tight')
plt.show()

from scipy.optimize import fmin

x = np.array([2.2, 4.3, 5.1, 5.8, 6.4, 8.0])
y = np.array([0.4, 10.1, 14.0, 10.9, 15.4, 18.5])

# SUm of squared errors function
sse = lambda a, x, y: np.sum((a[0] +a[1]*x - y)**2)

# Minimize SSE
a0, a1 = fmin(sse, [0, 1], args=(x, y))

plt.plot(x, y, 'ro')
plt.plot([0, 10], [a0, a0 + a1*10], alpha=0.8)
for xi, yi in zip(x, y):
    plt.plot([xi]*2, [yi, a0 + a1*xi], "k:")
plt.xlim(2,9); plt.ylim(0, 20) # Restrict the doman
plt.savefig("ExYErrors.png", dpi=300, bbox_inches='tight')

x = np.array([2.2, 4.3, 5.1, 5.8, 6.4, 8.0])
y = np.array([0.4, 10.1, 14.0, 10.9, 15.4, 18.5])

# Minimize the sum of squares using a lambda function

# Store the sum of absolute differences functions
sae = lambda b, x, y: np.sum(abs(b[0] + b[1]*x - y))
#Lambda function is a small anonymous function
#it can take any number of arguements, but can only have one expression
#Syntax "Lambda arguements: expression"

b0, b1 = fmin(sae, [0,1], args=(x,y)) # Minimize the sum of absolute errors
#[0,1] is the initial guess for b[0] and b[1] in function sse.

plt.plot(x, y, 'ro')
plt.plot([0,10], [a0, a0+a1*10], alpha = 0.8) # Add the regression line (sse), colored in blue
plt.plot([0,10], [b0, b0+b1*10], alpha = 0.8) # Add the regression line (sae), colred in orange

for xi, yi in zip(x,y):
    plt.plot([xi]*2, [yi, a0+a1*xi], "k:") # Add pointed black line to illustrate the errors

plt.xlim(2, 9); plt.ylim(0, 20) # Restrict the domain
plt.savefig("ErYErrors_SSE_SAE.png", dpi=300, bbox_inches='tight')

import pandas as pd
ice = pd.read_csv('SeaIce.txt', sep='\s+')

# Remove rows with missing data
ice2 = ice[ice.data_type != '-9999']

#Plot with cleaned data
x = ice2.year
y = ice2.extent
plt.scatter(x, y, color='red')
plt.xlabel('Year')
plt.ylabel('Extent')
plt.savefig("IceOne.png", dpi=300, bbox_inches = 'tight')

from sklearn.linear_model import LinearRegression
from sklearn import metrics
est = LinearRegression(fit_intercept=True)
x = ice2[['year']]
y = ice2[['extent']]
est.fit(x, y)
# Make predictions
y_hat = est.predict(x)

print("MSE:", metrics.mean_squared_error(y_hat, y))
print("R^2", metrics.r2_score(y, y_hat))

plt.plot(x, y, 'o', alpha = 0.5)
plt.plot(x, y_hat, 'r', alpha=0.5)
plt.xlabel('year')
plt.ylabel('extent (All Months)')
plt.savefig ("IceTwo.png" , dpi = 300 , bbox_inches = 'tight')
plt.show()

# Analysis for a particular month .
jan = ice2 [ ice2 . mo == 1]
x = jan [['year']]
y = jan [['extent']]

model = LinearRegression ()
model . fit (x , y )

y_hat = model . predict ( x )
plt . figure ()
plt . plot (x , y , '-o' , alpha = 0.5)
plt . plot (x , y_hat , 'r', alpha = 0.5)
plt . xlabel ('year')
plt . ylabel ('extent (January)')
plt . savefig ("IceThree.png" , dpi = 300 , bbox_inches ='tight')
plt . show ()

print ( " MSE : " , metrics . mean_squared_error ( y_hat , y ) )
print ( " R ^2: " , metrics . r2_score ( y_hat , y ) )

# Compute the mean for each month .
grouped = ice2.groupby('mo')
month_means = grouped.extent.mean()
month_variances = grouped.extent.var ()
print ('Means: ', month_means )
print ('Variances: ', month_variances )

X = np.array([2025]).reshape( -1 ,1)
y_hat = model.predict( X )
j = 1 # January
# Original value ( before normalization )
y_hat = ( y_hat * month_means . mean () /100) + month_means [ j ]
print ("Prediction of extent for January 2025 (in millions ofsquare km): " , y_hat )