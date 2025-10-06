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