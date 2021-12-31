from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np


apple= pd.read_json('./apple.json')
# print(apple)
data = apple['Adj Close']
days = 50
print(data)
data['Shifted'] = data['Adj Close'].shift(-days) #ricky has bugs here
data.dropna(inplace = True)

# prepare data for our model to learn

X = np.array(data.drop(['Shifted'],1))
Y = np.array(data['Shifted'])
X = preprocessing.scale(X)
# training and testing 
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)
# We are using a test size of 20%, which means that we use 80% of the data for
# training and 20% for calculating the accuracy
clf = LinearRegression()
clf.fit(X_train, Y_train)
accuracy = clf.score(X_test, Y_test)
print('accuracy is {}%'.format(accuracy*100))
# predicting data
X = X[:-days]
X_new = X[-days]

# Here we cut out the last 50 days and then create a new array X_new which
# takes the last 50 days of the remaining days. We will use these for predicting
# future values.
prediction = clf.predict(X_new)
print(prediction)

# ricky has bugs