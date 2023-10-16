# -*- coding: utf-8 -*-
"""k cross validation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15gMMvbL3GZnZuWGhwBL36U3uB9NDtbp-
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('Social_Network_Ads.csv')

X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.fit_transform(X_test)

from sklearn.svm import SVC
classifier=SVC(kernel='rbf',random_state=0)
classifier.fit(X_train,y_train)

from sklearn.metrics import confusion_matrix,accuracy_score
y_pred=classifier.predict(X_test)
print(confusion_matrix(y_test,y_pred))

print(accuracy_score(y_test,y_pred))

from sklearn.model_selection import cross_val_score
accuracies=cross_val_score(estimator=classifier,X=X_train,y=y_train,cv=10)
print('Accuracy : {:.2f} %'.format(accuracies.mean()*100))
print('Standard deviation : {:.2f} %'.format(accuracies.std()*100))

from sklearn.model_selection import GridSearchCV
parameters=[{'C':[0.25,0.5,0.75,1],'kernel':['linear']},
            {'C':[0.25,0.5,0.75,1],'kernel':['rbf'],'gamma':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]}]
grid_search=GridSearchCV(estimator=classifier,
                         param_grid=parameters,
                         scoring='accuracy',
                         cv=10,
                         n_jobs=-1)
grid_search.fit(X_train,y_train)
best_accuracy=grid_search.best_score_
best_pr=grid_search.best_params_
print('Best Accuracy : {:.2f} %'.format(accuracies.mean()*100))
print('Best Parameters : ',best_pr)



