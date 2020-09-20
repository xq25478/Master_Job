# data analysis and wrangling
import pandas as pd 
import numpy as np 
import random as rnd 

#visualization 
import seaborn as sns
import matplotlib.pyplot as plt 

#machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC,LinearSVC
from sklearn.ensemble import RandomForestClassifier 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB 
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier

#########################数据获取##############################
train_df = pd.read_csv(r'E:\GitHub\Job\Machine Learning\kaggle\Titanic Machine Learning from Disaster\train.csv')
test_df  = pd.read_csv(r'E:\GitHub\Job\Machine Learning\kaggle\Titanic Machine Learning from Disaster\test.csv')
combine = [train_df,test_df]

print(train_df.columns.values)


