# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('HealthData.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:, 13].values

#handling missing data

from sklearn.impute import SimpleImputer

# Instantiate the imputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

# Fit the imputer to the data   
imputer.fit(X[:, 11:13])

# Transform the data using the fitted imputer
X[:, 11:13] = imputer.transform(X[:, 11:13])




# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.15, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#EXPLORING THE DATASET
import seaborn as sn
sn.countplot(x='num',data=dataset)
dataset.num.value_counts()


# Fitting Naive Bayes to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X_train, y_train)

import joblib
filename ='KNN_model.pkl'
joblib.dump(classifier,filename)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

#ACCURACY SCORE
from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)


#Interpretation:
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))



##PREDICTION FOR NEW DATASET

Newdataset = pd.read_csv('newdata.csv')
ynew=classifier.predict(Newdataset)




