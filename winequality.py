# -*- coding: utf-8 -*-
"""WineQuality.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gq9Ixb2c9uWIGF-8YdIYD84_aNV8GPrH
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv('/content/winequality-red.csv')
data.shape
data.isnull().sum()

data.describe()

#number of values for each quality
sns.catplot(x='quality', data=data, kind='count')

sns.barplot(x='volatile acidity',y='quality',data=data)

sns.barplot(x='citric acid',y='quality',data=data)

#correlation
corr = data.corr()
#constructing a heatmap to understand the correlation between the columns
sns.heatmap(corr,cbar=True, square = True, fmt = '.1f',cmap='Blues',annot_kws={'size':10} ,annot=True)

X = data.drop('quality',axis=1)
#label binarization
Y = data['quality'].apply(lambda y: 1 if y>=7 else 0)

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=2)

forest = RandomForestClassifier()
forest.fit(x_train,y_train)

p = forest.predict(x_test)
print(accuracy_score(y_test,p))

#testing the model
ip = [7.3,0.65,0.0,1.2,0.065,15.0,21.0,0.9946,3.39,0.47,10.0]
pred = forest.predict([ip])
if pred[0]==1:
  print('Good Quality Wine')
else:
  print('Bad Quality Wine')