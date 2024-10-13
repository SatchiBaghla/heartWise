# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Importing the dataset
#DIR='C:/Users/Mansi/Desktop/Heart_disease_prediction_project/predict_risk/machine_learning_models'

dataset = pd.read_csv('HealthData.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 13].values


#handling missing data

from sklearn.impute import SimpleImputer

# Instantiate the imputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

# Fit the imputer to the data
imputer.fit(X[:, 11:13])

# Transform the data using the fitted imputer
X[:, 11:13] = imputer.transform(X[:, 11:13])



#splitting dataset into training set and test set

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.25)

#feature scaling

from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)

#exploring the dataset

import matplotlib.pyplot as plt
def draw_histograms(dataframe, features, rows, cols):
    fig=plt.figure(figsize=(20,20))
    for i, feature in enumerate(features):
        ax=fig.add_subplot(rows,cols,i+1)
        dataframe[feature].hist(bins=20,ax=ax,facecolor='midnightblue')
        ax.set_title(feature+" Distribution",color='DarkRed')

    fig.tight_layout()
    plt.show()
draw_histograms(dataset,dataset.columns,6,3)


dataset.num.value_counts()
import seaborn as sn
sn.countplot(x='num',data=dataset)



from sklearn.linear_model import LogisticRegression
classifier =LogisticRegression()
classifier.fit(X_train,Y_train)


#Saving the model to disk
import joblib
filename = 'Logistic_regression_model.pkl'
joblib.dump(classifier,filename)

#Predict the test set results

y_Class_pred=classifier.predict(X_test)

#checking the accuracy for predicted results

from sklearn.metrics import accuracy_score
accuracy_score(Y_test,y_Class_pred)

# Making the Confusion Matrix

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, y_Class_pred)

#Interpretation:

from sklearn.metrics import classification_report
print(classification_report(Y_test, y_Class_pred))




##PREDICTION FOR NEW DATASET

Newdataset = pd.read_csv('newdata.csv')
ynew=classifier.predict(Newdataset)
