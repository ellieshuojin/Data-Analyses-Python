# introduction
# the data set pima-indians-diabetes.csv contains data from 768 Pima Indian females. There are 8 clinical features, as well as the target attribute (whether an individual is diabetic). The goal is to predict a good classifier of clinical outcome.

# importing libraries
import pandas as pd 
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report 

diabetes = pd.DataFrame(pd.read_csv('pima-indians-diabetes.csv', header = None)) # importing data and creating dataframe
diabetes.iloc[:,1:8] = diabetes.iloc[:,1:8].replace(0, np.nan) # replacing 0s with NaN (except the first column and the last column since they correspond to real values)
diabetesNan = diabetes.iloc[:, [0, 1, 5, 6, 7, 8]] # creating new subset of data
diabetesData = diabetesNan.dropna() # dropping rows with missing values
diabetesFeatures = np.array(diabetesData.iloc[:, 0:5]) # identifying features
diabetesTargets= np.array(diabetesData.iloc[:, -1]) # identifying target (diabetic or non-diabetic)
TargetNames = ['Non-diabetic', 'Diabetic']
FeatureNames = ['Times pregnant', 'Plasma glucose', 'BMI', 'Diabetes pedigree', 'Age']

X_train, X_test, y_train, y_test = train_test_split(diabetesFeatures, # creating testing dataset
                                                    diabetesTargets,
                                                    random_state = 0,
                                                    test_size=0.33)

diabetesLR = LogisticRegression() # running logistic regression
diabetesLR.fit(X_train, y_train) # fitting regression model to testing dataset
y_pred = diabetesLR.predict(X_test) # predicted values from logistic regression

print('Confusion Matrix')
print(confusion_matrix(y_test,y_pred))
print('\n')
print('Classification Report')
print(classification_report(y_test, y_pred, target_names=TargetNames))
print('\n')
print('Feature \t\tOdds Ratio')
for i,iFeature in enumerate(FeatureNames):
    print('%-16s' % iFeature, end='')
    print('\t %8.3f' % np.exp(diabetesLR.coef_[0,i]))
