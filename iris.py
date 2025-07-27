# this code is  only to make the predictions
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
data = pd.read_excel('iris-train.xlsx')
data.head()
x = data.iloc[:,:-1]
x
y = data.iloc[:,-1]
y
model = RandomForestClassifier()
model.fit(x.values,y.values)
prediction = model.predict([[5.2,2.7,3.9,1.4]])
prediction
datatest = pd.read_excel('iris-test.xlsx')
x_test = datatest.iloc[:,:-1]
predictions = model.predict(x_test.values)
predictions


# For the accuracy of the model try different models to check the accuracy
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
data = pd.read_excel('iris-train.xlsx')
data.head()
x = data.iloc[:,:-1]
x
y = data.iloc[:,-1]
y
model = RandomForestClassifier()
model.fit(x.values,y.values)
prediction = model.predict([[5.2,2.7,3.9,1.4]])
prediction
datatest = pd.read_excel('iris-test.xlsx')
x_test = datatest.iloc[:,:-1]
predictions = model.predict(x_test.values)
predictions
y_test = datatest.iloc[:,-1]
actual = y_test.values
count = 0
for i in range(0 , len(actual)):
    if actual[i] == predictions[i]:
        count = count + 1
print((count * 100)/len(actual))
