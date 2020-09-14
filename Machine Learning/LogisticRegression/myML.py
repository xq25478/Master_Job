import numpy as np
from scipy import optimize

def sigmoid(z):
    """sigmoid函数
    """
    h = np.zeros((len(z),1))
    h = 1.0/(1.0+np.exp(-z))
    return h

def sigmoidGradient(z):
    s = sigmoid(z)
    g = s*(1-s)
    return g

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

# 预测
def predict_oneVsAll(all_theta,X,num_labels):
    m = X.shape[0]
    num_labels = all_theta.shape[0]
    p = np.zeros((m,1))
    X = np.hstack((np.ones((m,1)),X))   #在X最前面加一列1
    
    h = sigmoid(np.dot(X,np.transpose(all_theta)))  #预测

    '''
    返回h中每一行最大值所在的列号
    - np.max(h, axis=1)返回h中每一行的最大值（是某个数字的最大概率）
    - 最后where找到的最大概率所在的列号（列号即是对应的数字）
    '''
    p = np.array(np.where(h[0,:] == np.max(h, axis=1)[0]))  
    for i in np.arange(1, m):
        t = np.array(np.where(h[i,:] == np.max(h, axis=1)[i]))
        p = np.vstack((p,t))
    return p

def oneVsAll(X,y,num_labels,Lambda):
    # 初始化变量
    m,n = X.shape
    all_theta = np.zeros((n+1,num_labels))  # 每一列对应相应分类的theta,共10列
    X = np.hstack((np.ones((m,1)),X))       # X前补上一列1的偏置bias
    class_y = np.zeros((m,num_labels))      # 数据的y对应0-9，需要映射为0/1的关系
    initial_theta = np.zeros((n+1,1))       # 初始化一个分类的theta
    
    # 映射y
    for i in range(num_labels):
        class_y[:,i] = np.int32(y==i).reshape(1,-1) # 注意reshape(1,-1)才可以赋值
    
    #np.savetxt("class_y.csv", class_y[0:600,:], delimiter=',')    
    
    '''遍历每个分类，计算对应的theta值'''
    for i in range(num_labels):
        #optimize.fmin_cg
        result = optimize.fmin_bfgs(costFunction, initial_theta, fprime=gradientDescent, args=(X,class_y[:,i],Lambda)) # 调用梯度下降的优化方法
        all_theta[:,i] = result.reshape(1,-1)   # 放入all_theta中
        
    all_theta = np.transpose(all_theta) 
    return all_theta

if __name__ == '__main__':
    print('module--myML')
    print('author:XiaoQi')
    print('date:2020.09.13')
    print('LogisitcRegression train functions')