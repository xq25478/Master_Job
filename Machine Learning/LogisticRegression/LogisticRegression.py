import numpy as np   
from scipy import optimize
from myPreProcess import loadTxtAndCsvData,plot_data,mapFeature,plotDecisionBoundary
from myML import gradientDescent,costFunction,sigmoid

class LogisticRegression:
    def __init__(self,file_dir,initial_lambda = 0.1):
        self.f_dir = file_dir
        self.data = loadTxtAndCsvData(self.f_dir,',',dataType=np.float64)  #数据读取
        self.initial_lambda = initial_lambda
    # 预测
    def predict(self,X,theta):
        m = X.shape[0]  #样本数量
        p = np.zeros((m,1))
        p = sigmoid(np.dot(X,theta))    # 预测的结果，是个概率值
        
        for i in range(m):
            if p[i] > 0.5:  #概率大于0.5预测为1，否则预测为0
                p[i] = 1
            else:
                p[i] = 0
        return p

    def fit(self):
        X = self.data[:,0:-1]
        y = self.data[:,-1]
        plot_data(X,y) #作图

        X = mapFeature(X[:,0],X[:,1])  #映射为多项式
        initial_theta = np.zeros((X.shape[1],1)) #初始化theta
        J = costFunction(initial_theta,X,y,self.initial_lambda)
        print(J)
        #result = optimize.fmin(costFunction, initial_theta, args=(X,y,initial_lambda))    #直接使用最小化的方法，效果不好
        '''调用scipy中的优化算法fmin_bfgs（拟牛顿法Broyden-Fletcher-Goldfarb-Shanno）
        - costFunction是自己实现的一个求代价的函数，
        - initial_theta表示初始化的值,
        - fprime指定costFunction的梯度
        - args是其余测参数，以元组的形式传入，最后会将最小化costFunction的theta返回 
        '''
        result = optimize.fmin_bfgs(costFunction, initial_theta, fprime=gradientDescent, args=(X,y,self.initial_lambda))    
        p = self.predict(X, result)   #预测
        print('acc on tarin %f%%'%np.mean(np.float64(p==y)*100))   # 与真实值比较，p==y返回True，转化为float   
        
        X = self.data[:,0:-1]
        y = self.data[:,-1]    
        plotDecisionBoundary(result,X,y)    #画决策边界  

model = LogisticRegression('data2.txt',initial_lambda=0.005)
model.fit()