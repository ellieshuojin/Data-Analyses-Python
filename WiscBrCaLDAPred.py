import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report


# loading the data, extracting features and targets
BrCaData = pd.read_csv('WiscBrCa_clean.csv')
BrCaFeatures = np.array(BrCaData.iloc[:,1:10])
BrCaTargets = np.int_(np.array(BrCaData.iloc[:,10]) /2 -1)  # 0: benign, 1: malignant
featureNames = np.array(BrCaData.columns[1:10])
targetNames = ['Benign','Malignant']

X = BrCaFeatures
y = BrCaTargets

# spliting the data into training and testing data sets#
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

# Fitting the LDA to the training data
BrCaLDA = LinearDiscriminantAnalysis(n_components=2)
X_train_LDA = BrCaLDA.fit_transform(X_train,y_train)

print("Scalings")
print(BrCaLDA.scalings_[:,0])
print("\n")

# Classification on the testing data
X_test_LDA = BrCaLDA.transform(X_test)
y_pred = BrCaLDA.predict(X_test)

# Confusion matrix
print("Confusion Matrix")
print(confusion_matrix(y_test,y_pred))
print("\n")

# classification report
print("Classification Report")
print(classification_report(y_test, y_pred, target_names=targetNames))
