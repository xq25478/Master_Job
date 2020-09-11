#-*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
from myPreProcess import loadTxtAndCsvData,loadNpyData,featureNormalize,plot2D,plotJ
from myML import computerCost,gradientDescent
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

class LinearRegression:
    def __init__(self,file_dir,alpha,num_iters = 400):
        self.alpha = alpha
        self.num_iters = num_iters
        self.f_dir = file_dir

    def numpy_fit(self):
        """训练函数
        """
        print('step1:loading data')
        data = loadTxtAndCsvData(self.f_dir,',',dataType=np.float64)  #数据读取
        X = data[:,0:-1]
        y = data[:,-1]
        m = len(y)
        col = data.shape[1]

        X,mu,sigma = featureNormalize(X)
        #plot2D(X)
        X = np.hstack((np.ones((m,1)),X)) # 在X前面加一列1 

        print('step2:running gradient descent')
        theta = np.zeros((col,1))
        y = y.reshape(-1,1)
        theta,J_history = gradientDescent(X,y,theta,self.alpha,self.num_iters)
        plotJ(J_history,self.num_iters)
        return mu,sigma,theta

    def sklearnFit(self):
        """使用sklearn库进行学习
        """
        data = loadTxtAndCsvData(self.f_dir,',',dataType=np.float64)  #数据读取
        X = np.array(data[:,0:-1],dtype=np.float64)
        y = np.array(data[:,-1],dtype=np.float64)

        #归一化操作
        scaler = StandardScaler()
        scaler.fit(X)
        x_train = scaler.transform(X)
        x_test  = np.array([1650,3])
        x_test  = scaler.transform(x_test.reshape(1,-1))

        #线性模型模拟
        model = linear_model.LinearRegression()
        model.fit(x_train,y)

        #预测结果
        result = model.predict(x_test)
        print(model.coef_)       # Coefficient of the features 决策函数中的特征系数
        print(model.intercept_)  # 又名bias偏置,若设置为False，则为0
        print(result)            # 预测结果   

    def predict(self,mu,sigma,theta):
        """预测
        """
        result = 0
        # 注意归一化
        predict = np.array([1650,3])
        norm_predict = (predict-mu)/sigma
        final_predict = np.hstack((np.ones((1)),norm_predict))
        
        result = np.dot(final_predict,theta)    # 预测结果
        return result

if __name__ == "__main__":
    print('*************numpy machine learning***********')
    lr = LinearRegression("./data.txt",0.01,600)
    mu,sigma,theta = lr.numpy_fit()
    print ("theta:\n",theta)
    print ("predict:%f"%lr.predict(mu, sigma, theta))

    print('*************sklearn machine learning***********')
    lr.sklearnFit()