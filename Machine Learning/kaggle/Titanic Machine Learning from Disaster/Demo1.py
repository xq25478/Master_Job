#--coding **utf-8**--#
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
from sklearn.ensemble import RandomForestClassifier
from matplotlib import pyplot as plt 

# 特征可视化
def barPlot(variable):
    """input:variable
    :Usage
    # variables = ['Survived','Sex','Pclass','Embarked','SibSp','Parch']
    # for var in variables:
    #     barPlot(var)
    """
    var = train_data[variable]
    val = var.value_counts()

    plt.figure(figsize=(16,9))
    plt.bar(val.index,val)
    plt.title(variable)
    plt.ylabel('Frequency')
    plt.show()
    print("{}:\n{}".format(variable,val))

def randomForestClassifier():
    """using randomForest to classify
    """
    print('---------------------------------------------------')
    print('Model:RandomForestClassifier')
    # 数据预处理
    y = train_data['Survived']
    features = ['Pclass','Sex','SibSp',"Parch"] #采用如下特征进行构造随机森林
    X = pd.get_dummies(train_data[features])
    X_test = pd.get_dummies(test_data[features])
    # 采用随机森林分类器来实现
    model = RandomForestClassifier(n_estimators=100,max_depth=5,random_state=1)
    model.fit(X,y)
    predictions = model.predict(X_test)
    out = pd.DataFrame({'PassengerId':test_data.PassengerId,'Survived':predictions})
    out.to_csv(r'E:\GitHub\Job\Machine Learning\kaggle\Titanic Machine Learning from Disaster\Demo1_randomForestClassifier.csv',index = False)
    print('Saved in csv file!')

if __name__ == '__main__':
    # 数据加载
    train_data = pd.read_csv(r'E:\GitHub\Job\Machine Learning\kaggle\Titanic Machine Learning from Disaster\train.csv')
    test_data  = pd.read_csv(r'E:\GitHub\Job\Machine Learning\kaggle\Titanic Machine Learning from Disaster\test.csv')
    # print(train_data.head())
    # print(test_data.head())
    randomForestClassifier()