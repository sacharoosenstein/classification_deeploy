from sklearn import datasets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import joblib
import shap 
import dill

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
#Create a Classifier
clf=RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)

#Create shap explainer
explainer = shap.KernelExplainer(clf.predict, X_train)
#shap_values = explainer.shap_values(X_test.iloc[0,:])
#print(explainer)
#shap.force_plot(explainer.expected_value[0], shap_values[0], X_test.iloc[0,:])

#Save model as pickle 
filename = 'model/model.joblib'
joblib.dump(clf , filename)

#Save explainer as pickle
ex_filename = 'explainer/explainer.dill'
joblib.dump(explainer, ex_filename)

