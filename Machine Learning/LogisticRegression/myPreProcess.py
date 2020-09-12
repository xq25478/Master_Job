import numpy as np
from matplotlib import pyplot as plt

def loadTxtAndCsvData(filename:str,split:str,dataType = np.float64):
    """ 加载txt csv数据格式的文件
    :type filename:str split:str datatype:np.float64
    :retype data
    """
    return np.loadtxt(filename,delimiter=split,dtype=dataType)

def loadNpyData(filename:str):
    """ 加载npy数据格式的文件
    :type filename:str
    :retype data
    """  
    return np.load(filename)

def featureNormalize(X):
    """ 特征归一化
    :type X:原始数据
    :retype 归一化的数据
    """    
    X_norm = np.array(X)
    mu    = np.zeros((1,X.shape[1]))
    sigma = np.zeros((1,X.shape[1]))

    mu    = np.mean(X_norm,0)  #每一列的平均值
    sigma = np.std(X_norm,0) #每一列的标准差

    for i in range(X.shape[1]): #每一行归一化
        X_norm[:,i] = (X_norm[:,i]-mu[i])/sigma[i]

    return X_norm,mu,sigma

#二维画图
def plot_data(X,y):
    pos = np.where(y==1)    #找到y==1的坐标位置
    neg = np.where(y==0)    #找到y==0的坐标位置
    #作图
    plt.figure(figsize=(15,12))
    plt.plot(X[pos,0],X[pos,1],'ro')        # red o
    plt.plot(X[neg,0],X[neg,1],'bo')        # blue o
    plt.title("classes")
    plt.show()

def plotJ(J_history,num_iters):
    """代价曲线图
    :type J_his 代价值 num_iters 当前迭代次数
    :rtype NOne
    """
    x = np.arange(1,num_iters+1)
    plt.plot(x,J_history)
    plt.xlabel(u"iters") # 注意指定字体，要不然出现乱码问题
    plt.ylabel(u"Cost")
    plt.title(u"Cost vs Iters")
    plt.show()

if __name__ == '__main__':
    print('module:myPreProcess')
    print('author:XiaoQi')
    print('date:2020.09.10')
    print('LinearRegression PreProcess functions')
