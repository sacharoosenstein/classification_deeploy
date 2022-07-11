from sklearn import datasets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import joblib
import shap 
import dill

ex2 = joblib.load(filename='explainer/explainer.dill')


#Load dataset
iris = datasets.load_iris()
data=pd.DataFrame({
    'sepal_length':iris.data[:,0],
    'sepal_width':iris.data[:,1],
    'petal_length':iris.data[:,2],
    'petal_width':iris.data[:,3],
    'species':iris.target
})
data.head()

X=data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]  # Features
y=data['species']  # Labels

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% training and 30% test
print(X.shape)
shap_values2 = ex2.shap_values(X_test)
print(shap_values2)