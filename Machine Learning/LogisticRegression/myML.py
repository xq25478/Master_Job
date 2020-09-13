import numpy as np
from scipy import optimize

def sigmoid(z):
    """sigmoid函数
    """
    h = np.zeros((len(z),1))
    h = 1.0/(1.0+np.exp(-z))
    return h

def costFunction(initial_theta,X,y,initial_lambda):
    """计算代价函数
    :type X 样本 y 标签 theta w矩阵 lambda 正则化系数
    :retype 代价值
    """
    m = len(y)
    h = sigmoid(np.dot(X,initial_theta))
    theta1 = initial_theta.copy()
    theta1[0] = 0

    regular = np.dot(np.transpose(theta1),theta1)
    J = (- np.dot(np.transpose(y),np.log(h))-np.dot(np.transpose(1-y),np.log(1-h))  + regular*initial_lambda/2)/m
    return J

def gradientDescent(initial_theta,X,y,initial_lambda):
    """梯度下降算法实现
    :retype
    """
    m = len(y)
    grid = np.zeros((initial_theta.shape[0]))

    h = sigmoid(np.dot(X,initial_theta))
    theta1 = initial_theta.copy()
    theta1[0] = 0 
    grid = np.dot(np.transpose(X),h-y)/m + initial_lambda/m*theta1
    return grid


if __name__ == '__main__':
    print('module--myML')
    print('author:XiaoQi')
    print('date:2020.09.10')
    print('LinearRegression train functions')