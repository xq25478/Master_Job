import numpy as np
import matplotlib.pyplot as plt 
import scipy.io as spio
from scipy import optimize
from myPreProcess import loadmat_data,display_data
from myML import  predict_oneVsAll,oneVsAll
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class LogisticRegression_OneVsAll:
    def __init__(self,f_dir):
        self.data = loadmat_data(f_dir)

    def numpy_fit(self):
        X = self.data['X']
        y = self.data['y']
        num_labels = 10
        m = X.shape[0],X.shape[1]
        ##　随机显示几行数据
        rand_indices = [t for t in [np.random.randint(x-x, m) for x in range(100)]]  # 生成100个0-m的随机数
        display_data(X[rand_indices,:])     # 显示100个数字

        Lambda = 0.1
        #y = y.reshape(-1,1)
        all_theta = oneVsAll(X, y, num_labels, Lambda)  # 计算所有的theta
        p = predict_oneVsAll(all_theta,X,num_labels)               # 预测
        # 将预测结果和真实结果保存到文件中
        #res = np.hstack((p,y.reshape(-1,1)))
        #np.savetxt("predict.csv", res, delimiter=',')
        
        print(u"acc of numpy %f%%"%np.mean(np.float64(p == y.reshape(-1,1))*100))

    def scikit_fit(self):
        X = self.data['X']
        y = self.data['y']
        x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

        #归一化
        scaler = StandardScaler()
        x_train = scaler.fit_transform(x_train)
        x_test = scaler.fit_transform(x_test)
        y_train = np.ravel(y_train)
        y_test = np.ravel(y_test)
        """
        np.ravel   将多维数组降为一维 返回视图 修改原数组
        np.flatten 将多维数组降为一维 不修改原数组
        """
        model = LogisticRegression()

        #划分为训练集和测试集
        model.fit(x_train,y_train) #拟合
        predict = model.predict(x_test)
        print(u"acc of sklearn %f%%"%np.mean(np.float64(predict == y_test)*100))


lr = LogisticRegression_OneVsAll(r'E:\GitHub\Job\Machine Learning\LogisticRegression\data_digits.mat')
# lr.numpy_fit()
lr.scikit_fit()