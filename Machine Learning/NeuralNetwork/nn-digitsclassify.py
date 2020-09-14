import numpy as np
from scipy import io as spio
from scipy import optimize
from matplotlib import pyplot as plt 

from sklearn import datasets
from sklearn.preprocessing import StandardScaler
import time 

from myPreProcess import loadmat_data,randInitializeWeights,display_data
from myML import nnCostFunction,nnGradient,predict

class NerualNetWork():
    def __init__(self,f_dir,input_layer_size,hidden_layer_size,out_put_layer):
        self.data = loadmat_data(f_dir)
        self.input_layer_size = input_layer_size
        self.hidden_layer_size = hidden_layer_size
        self.out_put_layer = out_put_layer

    def numpy_fit(self):
        X = self.data['X']
        y = self.data['y']
        m,_= X.shape

        ##　随机显示几行数据
        rand_indices = [t for t in [np.random.randint(0, m) for _ in range(100)]]  # 生成100个0-m的随机数
        #display_data(X[rand_indices,:])     # 显示100个数字    

        Lambda = 1
        initial_theta1 = randInitializeWeights(self.input_layer_size,self.hidden_layer_size)
        initial_theta2 = randInitializeWeights(self.hidden_layer_size,self.out_put_layer)

        initial_nn_params = np.vstack((initial_theta1.reshape(-1,1),initial_theta2.reshape(-1,1)))# 展开theta

        start = time.time()
        result = optimize.fmin_cg(nnCostFunction,initial_nn_params,fprime=nnGradient,args=(self.input_layer_size,self.hidden_layer_size,self.out_put_layer,X,y,Lambda))
        print('running time',time.time()-start)
        print(result)
        '''可视化 Theta1'''
        length = result.shape[0]
        Theta1 = result[0:self.hidden_layer_size*(self.input_layer_size+1)].reshape(self.hidden_layer_size,self.input_layer_size+1)
        Theta2 = result[self.hidden_layer_size*(self.input_layer_size+1):length].reshape(self.out_put_layer,self.hidden_layer_size+1)    
        display_data(Theta1[:,1:length])
        display_data(Theta2[:,1:length])
        '''预测'''
        p = predict(Theta1,Theta2,X)
        print (u"Accuracy:%f%%"%np.mean(np.float64(p == y.reshape(-1,1))*100))    
        res = np.hstack((p,y.reshape(-1,1)))
        np.savetxt("predict.csv", res, delimiter=',')

model = NerualNetWork(r'E:\GitHub\Job\Machine Learning\NeuralNetwork\data_digits.mat',400,25,10)
model.numpy_fit()