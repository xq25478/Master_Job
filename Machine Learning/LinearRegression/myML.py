import numpy as np

def computerCost(X,y,theta,regularization=False,r=0.01):
    """计算代价函数
    :type X 样本 y 标签 theta w矩阵
    :retype 代价值
    """
    m = len(y)
    regular =  r*np.dot(np.transpose(theta),theta) if regularization else 0.0
    J = (np.transpose(X*theta-y) * (X*theta-y) + regular )/(2*m)
    return J

def gradientDescent(X,y,theta,alpha,num_iters,regularization=False,r=0.01):
    """梯度下降算法实现
    :type X 样本 y 标签 theta w 参数矩阵 alpha 学习率 num_iters 迭代次数
    :retype
    """
    m = len(y)
    n = len(theta)

    temp = np.matrix(np.zeros((n,num_iters)))
    J_history = np.zeros((num_iters,1))

    for i in range(num_iters):
        h = np.dot(X,theta)
        regular = r*theta if regularization else 0
        temp[:,i] =  theta - ((alpha/m)*(np.dot(np.transpose(X),h-y) + regular))
        theta = temp[:,i]
        J_history[i] = computerCost(X,y,theta,regularization,r)

    return theta,J_history        

if __name__ == '__main__':
    print('module--myML')
    print('author:XiaoQi')
    print('date:2020.09.10')
    print('LinearRegression train functions')