import matplotlib.pylab as plt
import pickle
import numpy as np

# Load the Data set
ofname = open('dataset_small.pkl', 'rb')
(x,y) = pickle.load(ofname, encoding="latin1")

# Check the shapes
dims = x.shape[1]
N = x.shape[0]
print('dims: ', str(dims)+', sample: '+ str(N))

from sklearn import neighbors
from sklearn import metrics
#Create an instance of K-nearest neighbor classifier
knn = neighbors.KNeighborsClassifier(n_neighbors=11)
# Train the classifier
knn.fit(x,y)
# Compute the prediction according to the model
yhat = knn.predict(x)
print('Predicted values: '+ str(yhat[-1])), ', real target: '+ str(y[-1])
# Check the model's accuracy on the training data
print('Accuracy:', knn.score(x,y))

yhat = knn.predict(x)
TP = np.sum(np.logical_and(yhat==-1, y==1))
TN = np.sum(np.logical_and(yhat==1, y==1))
FP = np.sum(np.logical_and(yhat==-1,y==1))
FN = np.sum(np.logical_and(yhat==1,y==-1))
print(f'TP: {TP}, FP: {FP}')
print(f'FN: {FN}, TN: {TN}')

#Train a classifier using .fit()
knn = neighbors.KNeighborsClassifier(n_neighbors=1)
knn.fit(x,y)
yhat=knn.predict(x)

print("classification accuracy:", metrics.accuracy_score(yhat, y))
print("confusion matrix: \n" + str(metrics.confusion_matrix(yhat,y)))

perm = np.random.permutation(y.size)
PRC = 0.7
split_point = int(np.ceil(y.shape[0]*PRC))
X_train = x[perm[:split_point],:]
y_train = y[perm[:split_point]]
X_test = x[perm[split_point:],:]
y_test = y[perm[split_point:]]

print('Training shape: ', + str(X_train.shape), ' , training targets shape: ' + str(y_train.shape))
print('Testing shape: ', + str(X_test.shape), ' , testing targets shape: '+ str(y_test.shape))

knn.fit(X_train, y_train)
yhat_train = knn.predict(X_train)
print("TRAINING STAT:")
print("Accuracy:", metrics.accuracy_score(yhat_train, y_train))
print("Confusion Matrix:\n", metrics.confusion_matrix(y_train, yhat_train))

yhat_test = knn.predict(X_test)
print("TESTING STATS:")
print("Accuracy:", metrics.accuracy_score(yhat_test, y_test))
print("Confusion Matrix:\n", metrics.confusion_matrix(yhat_test, y_test))

from sklearn.model_selection import train_test_split
PRC = 0.3
acc = np.zeros((10,))
for i in range(10):
  X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=PRC)
  knn= neighbors.KNeighborsClassifier(n_neighbors=1)
  knn.fit(X_train, y_train)
  yhat = knn.predict(X_test)
  acc[i] = metrics.accuracy_score(yhat, y_test)
  acc.shape=(1, 10)
print("Mean expected error: "+str(np.mean(acc[0])))

from sklearn import tree
from sklearn import svm
PRC = 0.1
acc_r = np . zeros ((10 ,4) )
for i in range (10) :
  X_train , X_test , y_train , y_test = train_test_split (x , y
  , test_size = PRC )
nn1 = neighbors . KNeighborsClassifier ( n_neighbors =1)
nn3 = neighbors . KNeighborsClassifier ( n_neighbors =3)
svc = svm.SVC()
dt = tree.DecisionTreeClassifier()
nn1.fit( X_train , y_train )
nn3.fit( X_train , y_train )
svc.fit( X_train , y_train )
dt.fit( X_train , y_train )
yhat_nn1 = nn1.predict( X_test )
yhat_nn3 = nn3.predict( X_test )
yhat_svc = svc.predict( X_test )
yhat_dt = dt.predict( X_test )

acc_r[ i ][0] = metrics.accuracy_score( yhat_nn1 , y_test )
acc_r[ i ][1] = metrics.accuracy_score( yhat_nn3 , y_test )
acc_r[ i ][2] = metrics.accuracy_score( yhat_svc , y_test )
acc_r[ i ][3] = metrics.accuracy_score( yhat_dt , y_test )


plt.boxplot(acc_r)
for i in range (4) :
  xderiv = ( i +1) * np . ones ( acc_r [: , i ]. shape ) +( np . random . rand
  (10 ,) -0.5) *0.1
  plt.plot( xderiv , acc_r [: , i ] , 'ro', alpha =0.3)
ax = plt.gca()
ax.set_xticklabels(['1 - NN', '3 - NN', 'SVM', 'Decission Tree'])
plt.ylabel ('Accuracy')
plt.savefig ("error_ms_1 . png", dpi =300 , bbox_inches = 'tight')

MAXN =700

fig = plt.figure()
fig.set_size_inches(6 ,5)

plt.plot(1.25* np.random.randn ( MAXN ,1) ,1.25* np.random.randn(
MAXN ,1) , 'r .', alpha = 0.3)
plt . plot(8+1.5* np.random.randn( MAXN ,2) ,5+1.5* np.random.randn
( MAXN ,2) , 'r .', alpha = 0.3)
plt.plot (5+1.5* np.random.randn( MAXN ,1) ,5+1.5* np.random.randn
( MAXN ,1) , 'b .', alpha = 0.3)
plt.show()
plt.savefig("toy_problem . png", dpi =300 , bbox_inches = 'tight')

C = 5 # depth of tree
MAXN = 1000

yhat_test = np.zeros((10 , 299 , 2))
yhat_train = np.zeros((10 , 299 , 2))

# Repeat ten times to get smooth curves
for i in range (10) :
  X = np . concatenate ([
  1.25 * np . random . randn ( MAXN , 2) ,
  5 + 1.5 * np . random . randn ( MAXN , 2)
  ])
X = np . concatenate ([
X ,
[8 , 5] + 1.5 * np . random . randn ( MAXN , 2)
])
y = np . concatenate ([
np . ones (( MAXN , 1) ) ,
- np . ones (( MAXN , 1) )
])
y = np . concatenate ([ y , np . ones (( MAXN , 1) ) ])

perm = np . random . permutation ( y . size )
X = X [ perm , :]
y = y [ perm ]

X_test = np . concatenate ([
1.25 * np . random . randn ( MAXN , 2) ,
5 + 1.5 * np . random . randn ( MAXN , 2)
])
X_test = np . concatenate ([
X_test ,
[8 , 5] + 1.5 * np . random . randn ( MAXN , 2)
])
y_test = np . concatenate ([
np . ones (( MAXN , 1) ) ,
- np . ones (( MAXN , 1) )
])
y_test = np . concatenate ([ y_test , np . ones (( MAXN , 1) ) ])

j = 0
for N in range (10 , 3000 , 10) :
  Xr = X [: N , :]
  yr = y [: N ]

# Evaluate the model
clf = tree.DecisionTreeClassifier(
min_samples_leaf =1 , max_depth = C
)
clf . fit ( Xr , yr . ravel () )
yhat_test [i , j , 0] = 1. - metrics . accuracy_score (
clf . predict ( X_test ) , y_test . ravel ()
)
yhat_train [i , j , 0] = 1. - metrics . accuracy_score (
clf . predict ( Xr ) , yr . ravel ()
)
j = j + 1

p1 , = plt . plot ( np . mean ( yhat_test [: , : , 0]. T , axis =1) , 'pink'
)
p2 , = plt . plot ( np . mean ( yhat_train [: , : , 0]. T , axis =1) , 'c')

fig = plt.gcf()
fig.set_size_inches(12 , 5)

plt.xlabel('Number of samples x10')
plt.ylabel('Error rate')
plt.legend([ p1 , p2 ] , [ " Test C = 5 " , "Train C = 5"])
plt.savefig("learning_curve_1.png" , dpi =300 , bbox_inches='tight')

C = 1
MAXN = 1000

# Repeat ten times to get smooth curves
for i in range (10) :
  X = np . concatenate ([
  1.25 * np . random . randn ( MAXN , 2) ,
  5 + 1.5 * np . random . randn ( MAXN , 2)
  ])
X = np . concatenate ([
  X ,
  [8 , 5] + 1.5 * np . random . randn ( MAXN , 2)
])
y = np . concatenate ([
  np . ones (( MAXN , 1) ) ,
  - np . ones (( MAXN , 1) )
])
y = np . concatenate ([ y , np . ones (( MAXN , 1) ) ])

perm = np . random . permutation ( y . size )
X = X [ perm , :]
y = y [ perm ]

X_test = np . concatenate ([
1.25 * np . random . randn ( MAXN , 2) ,
5 + 1.5 * np . random . randn ( MAXN , 2)
])
X_test = np . concatenate ([
X_test ,
[8 , 5] + 1.5 * np . random . randn ( MAXN , 2)
])
y_test = np . concatenate ([
np . ones (( MAXN , 1) ) ,
- np . ones (( MAXN , 1) )
])
y_test = np . concatenate ([ y_test , np . ones (( MAXN , 1) ) ])

j = 0
for N in range (10 , 3000 , 10) :
  Xr = X [: N , :]
  yr = y [: N ]

  clf = tree.DecisionTreeClassifier(
    min_samples_leaf =1 , max_depth = C
  )
  clf . fit ( Xr , yr . ravel () )
  yhat_test [i , j , 1] = 1. - metrics . accuracy_score (
    clf . predict ( X_test ) , y_test . ravel ()
  )
  yhat_train [i , j , 1] = 1. - metrics . accuracy_score (
    clf . predict ( Xr ) , yr . ravel ()
  )
  j = j + 1

  p3 , = plt . plot ( np . mean ( yhat_test [: , : , 1]. T , axis =1) , 'r')
p4 , = plt . plot ( np . mean ( yhat_train [: , : , 1]. T , axis =1) , 'b')

fig = plt . gcf ()
fig . set_size_inches (12 , 5)

plt . xlabel ('Number of samples x10')
plt . ylabel ('Error rate')
plt . legend ([ p3 , p4 ] , [ " Test C = 1 " , " Train C = 1 " ])
plt . savefig ( " learning_curve_2 . png " , dpi =300 , bbox_inches = 'tight')

p1 , = plt . plot ( np . mean ( yhat_test [: , : , 0]. T , axis =1) , color =
  'pink')
p2 , = plt . plot ( np . mean ( yhat_train [: , : , 0]. T , axis =1) , 'c')
p3 , = plt . plot ( np . mean ( yhat_test [: , : , 1]. T , axis =1) , 'r')
p4 , = plt . plot ( np . mean ( yhat_train [: , : , 1]. T , axis =1) , 'b')

fig = plt . gcf ()
fig . set_size_inches (12 , 5)

plt . xlabel ('Number of samples x10')
plt . ylabel ('Error rate')
plt . legend (
[ p1 , p2 , p3 , p4 ] ,
["Test C = 5 " , " Train C = 5 " , " Test C = 1 " , "Train C = 1"]
)
plt . savefig ( " learning_curve_3 . png " , dpi =300 , bbox_inches = 'tight')

ofname = open ('dataset_small.pkl' , 'rb')
(X , y ) = pickle . load ( ofname , encoding = "latin1")

# Create a 10 - fold cross validation set
kf = KFold( n_splits =10 , shuffle = True , random_state =0)

# Search the parameter among the following
C = np . arange (2 , 20)

acc = np . zeros ((10 , 18) )

i = 0
for train_index , val_index in kf . split ( y ) :
  X_train , X_val = X [ train_index ] , X [ val_index ]
  y_train , y_val = y [ train_index ] , y [ val_index ]
  j = 0
  for c in C :
    dt = tree . DecisionTreeClassifier(
    min_samples_leaf =1 , max_depth = c
    )
    dt . fit ( X_train , y_train )
    yhat = dt . predict ( X_val )
    acc [ i ][ j ] = metrics . accuracy_score ( yhat , y_val )
    j = j + 1
i = i + 1

plt . boxplot ( acc )

for i in range (18) :
  xderiv = ( i + 1) * np . ones ( acc [: , i ]. shape ) \
    + ( np . random . rand (10 ,) - 0.5) * 0.1
  plt . plot ( xderiv , acc [: , i ] , 'ro', alpha =0.3)

print ('Mean accuracy: ' + str ( np . mean ( acc , axis =0) ) )
print ('Selected model index: ' + str ( np . argmax ( np . mean ( acc ,
axis =0) ) ) )
print ('Complexity: ' + str ( C [ np . argmax ( np . mean ( acc , axis =0) )
]) )

plt . ylim ((0.7 , 1.0) )
fig = plt . gcf ()
fig . set_size_inches (12 , 5)
plt . xlabel ('Complexity')
plt . ylabel ('Accuracy')
plt . savefig ("model_selection.png" , dpi =300 , bbox_inches ='tight')

ofname = open('./files/ch05/dataset)small.pkl', 'rb')
(X, y) = pickle.load(ofname, encoding='latin1')

# Train-test split
X_train, X_test, y_train, y_test=train_test_split(
  X, y, test_size=0.20, random_state=42)

# Create a 10 - fold cross - validation set
kf = KFold ( n_splits =10 , shuffle = True , random_state =0)

# Search over tree depths
C = np . arange (2 , 20)
acc = np . zeros ((10 , 18) )

i = 0
for train_index , val_index in kf . split ( X_train ) :
  X_t , X_val = X_train [ train_index ] , X_train [ val_index ]
  y_t , y_val = y_train [ train_index ] , y_train [ val_index ]
  j = 0
  for c in C :
    dt = tree.DecisionTreeClassifier(
      min_samples_leaf =1 , max_depth = c )
    dt . fit ( X_t , y_t )
    yhat = dt . predict ( X_val )
    acc [ i ][ j ] = metrics . accuracy_score ( yhat , y_val )
    j = j + 1
  i = i + 1

  # Evaluate CV results
print ('Mean accuracy: ' + str ( np . mean ( acc , axis =0) ) )
print ('Selected model index: ' + str ( np . argmax ( np . mean ( acc ,
axis =0) ) ) )
print ('Complexity: ' + str ( C [ np . argmax ( np . mean ( acc , axis =0) )
]) )

# Train model with selected complexity on full training set
best_depth = C [ np . argmax ( np.mean( acc , axis =0) ) ]
dt = tree.DecisionTreeClassifier( min_samples_leaf =1 ,
max_depth = best_depth )
dt . fit ( X_train , y_train )
# Evaluate on test set
yhat = dt . predict ( X_test )
print ('Test accuracy: ' + str ( metrics . accuracy_score ( yhat ,
y_test ) ) )

# Train final model for deployment ( on full data )
dt = tree . DecisionTreeClassifier( min_samples_leaf =1 ,
  max_depth = best_depth )
dt . fit (X , y )

# Plot CV accuracy boxplot
plt . boxplot ( acc )
for i in range (18) :
  xderiv = ( i + 1) * np . ones ( acc [: , i ]. shape ) + \
    ( np . random . rand (10 ,) - 0.5) * 0.1
  plt.plot(xderiv , acc [: , i ] , 'ro' , alpha =0.3)
plt . ylim ((0.7 , 1.0) )
fig = plt . gcf ()
fig . set_size_inches (12 , 5)

from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn import linear_model
from sklearn.model_selection import KFold, GridSearchCV
from sklearn import metrics

ofname = open('dataset_small . pkl', 'rb')
(X , y ) = pickle . load ( ofname , encoding = 'latin1')

parameters = {
  'C': [1e4 , 1e5 , 1e6 ],
  'gamma': [1e-5 , 1e-4 , 1e-3]
}

N_folds = 3
kf = KFold ( n_splits = N_folds , shuffle = True , random_state =0)

acc = np.zeros (( N_folds ,) )
yhat = y.copy ()

i = 0
for train_index , test_index in kf . split ( X ) :
  X_train , X_test = X [ train_index , :] , X [ test_index , :]
  y_train , y_test = y [ train_index ] , y [ test_index ]

  scaler = StandardScaler ()
  X_train = scaler . fit_transform ( X_train )

  clf = svm . SVC ( kernel = 'rbf')
  clf = GridSearchCV ( clf , parameters , cv =3)
  clf.fit ( X_train , y_train . ravel () )
  X_test = scaler . transform ( X_test )
  yhat [ test_index ] = clf . predict ( X_test )
# Final evaluation on the whole dataset
print ( metrics . accuracy_score ( yhat , y ) )
print ( metrics . confusion_matrix ( yhat , y ) )

dvals = [
  {1: 0.25} , {1: 0.5} , {1: 1} ,
  {1: 2} , {1: 4} , {1: 8} , {1: 16}
]
opoint = []

for cw in dvals :
  parameters = {
    'C': [1e4 , 1e5 ] ,
    'gamma': [1e-5 , 1e-4 , 1e-3] ,
    'class_weight': [ cw ]
  }
  print ( parameters )

N_folds = 3
kf = KFold ( n_splits = N_folds , shuffle = True , random_state
  =0)

acc = np . zeros (( N_folds ,) )
mat = np . zeros ((2 , 2 , N_folds ) )
i = 0
yhat = y . copy ()

for train_index , test_index in kf . split ( X ) :
  X_train , X_test = X [ train_index , :] , X [ test_index ,
:]
  y_train , y_test = y [ train_index ] , y [ test_index ]

  scaler = StandardScaler ()
  X_train = scaler . fit_transform ( X_train )

  clf = svm . SVC ( kernel = 'rbf')
  clf = GridSearchCV ( clf , parameters , cv =2)
  clf . fit ( X_train , y_train . ravel () )
  X_test = scaler . transform ( X_test )
  yhat [ test_index ] = clf . predict ( X_test )
  acc [ i ] = metrics . accuracy_score ( yhat [ test_index ] ,
y_test )
  mat [: , : , i ] = metrics . confusion_matrix (
    yhat [ test_index ] , y_test )
  
  print ( str ( clf . best_params_ ) )
  i = i + 1

print ('Mean accuracy: ' + str ( np . mean ( acc ) ) )
opoint.append (( np . mean ( acc ) , np . sum ( mat , axis =2) ) )

from sklearn import ensemble
ofname = open ('dataset_small . pkl', 'rb')
(X , y ) = pickle.load(ofname , encoding = 'latin1')
dvals = [
  {1: 0.25} , {1: 0.5} , {1: 1} ,
  {1: 2} , {1: 4} , {1: 8} , {1: 16}
]

kf = KFold ( n_splits =3 , shuffle = True , random_state =0)
acc = np.zeros ((5 ,) )
yhat = y.copy()

for cw in dvals :
  i = 0
  for train_index , test_index in kf . split ( X ) :
    X_train , X_test = X [ train_index ] , X [ test_index ]
    y_train , y_test = y [ train_index ] , y [ test_index ]

    dt = ensemble.RandomForestClassifier(
      n_estimators =51 , class_weight = cw
    )
    dt.fit( X_train , y_train )
    yhat [ test_index ] = dt . predict ( X_test )
    acc [ i ] = metrics . accuracy_score (
    yhat [ test_index ] , y_test
    )
    i = i + 1

# You may run this code for each iteration in the former cell to get surface plots
# The prediction of a configuration is given in yhat

M = metrics.confusion_matrix ( yhat , y )

ccampaing = [10 ,20 ,30 ,40 ,50 ,60 ,70 ,80 ,90]
retention = [0.1 ,0.2 ,0.3 ,0.4 ,0.5 ,0.6 ,0.7 ,0.8 ,0.9 ,1.0]

TP = M [0 ,0]
FN = M [1 ,0]
FP = M [0 ,1]
TN = M [1 ,1]
campaing = TN + FN
profit = TP + FN
[ xx , yy ] = np.meshgrid( ccampaing , retention )
cost = 100 * profit - xx * campaing + yy * TN * 100

from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure( facecolor = 'white')
ax = fig.add_subplot (111 , projection = '3d')

cost_no_campaign = 100 * profit + 0 * xx
Z = np.where ( cost > cost_no_campaign , cost , cost_no_campaign
)
ax.plot_surface ( xx , yy , Z , cmap = cm . coolwarm ,
  alpha =0.3 , linewidth =0.1 ,
  rstride =1 , cstride =1)
ax.plot_wireframe ( xx , yy , Z , rstride =1 , cstride =1 ,
  color =[0.5 , 0.5 , 0.5] , alpha =0.5)
fig.set_size_inches ((12 , 8) )
ax.set_xlabel('campaign cost', size =16)
ax.set_ylabel('retention rate', size =16)
ax.set_zlabel('profit', size =16)
fig.savefig ('rf_cost . png', dpi =100 , format = 'PNG')

print ('Max profit: ' +
  str (100 * ( np . max ( Z ) - np . min ( Z ) ) / np . min ( Z ) ) )

print ('Max profit for retention rate: ' +
  str (100 * ( np . max ( Z [5]) - np . min ( Z ) ) / np . min ( Z ) ) )

print('Campaign cost: ')
print('Accuracy: ' + str (( TP + TN ) / ( TP + FN + FP + FN *
  1.) ) )
print('Confusion: ' + str ( M ) )