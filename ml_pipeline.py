#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 07:54:51 2021

@author: srikanth
"""

import numpy as np 
import pandas as pd 

training_data = pd.read_csv('storepurchasedata.csv')
training_data.describe()

X = training_data.iloc[:, :-1].values
y = training_data.iloc[:, -1].values

# split the data for training and testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =.20,random_state=0)

# feature scaling 
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier
# minkowski is for ecledian distance
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)

# Model training
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
y_prob = classifier.predict_proba(X_test)[:,1]


from sklearn.metrics import confusion_matrix
# check the accuracy of the model

cm = confusion_matrix(y_test, y_pred)

from sklearn.metrics import classification_report

print(classification_report(y_test,y_pred))

new_prediction = classifier.predict(sc.transform(np.array([[40,20000]])))
new_prediction_proba = classifier.predict_proba(sc.transform(np.array([[40,20000]])))[:,1]
new_pred = classifier.predict(sc.transform(np.array([[42,50000]])))
new_pred_proba = classifier.predict_proba(sc.transform(np.array([[42,50000]])))[:,1]





