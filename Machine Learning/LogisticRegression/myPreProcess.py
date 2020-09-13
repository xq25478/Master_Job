import numpy as np
from matplotlib import pyplot as plt
import scipy.io as spio

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

def mapFeature(X1,X2):
    """映射为多项式
    """
    degree = 2
    out = np.ones((X1.shape[0],1))
    '''
    这里以degree=2为例，映射为1,x1,x2,x1^2,x1,x2,x2^2
    '''
    for i in np.arange(1,degree+1):
        for j in range(i+1):
            temp = X1**(i-j)*(X2**j)
            out = np.hstack((out,temp.reshape(-1,1)))
    return out

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

#画决策边界
def plotDecisionBoundary(theta,X,y):
    pos = np.where(y==1)    #找到y==1的坐标位置
    neg = np.where(y==0)    #找到y==0的坐标位置
    #作图
    plt.figure(figsize=(15,12))
    plt.plot(X[pos,0],X[pos,1],'ro')        # red o
    plt.plot(X[neg,0],X[neg,1],'bo')        # blue o
    plt.title("DecisionBoundary")
    
    u = np.linspace(-1,1.5,50)  #根据具体的数据，这里需要调整
    v = np.linspace(-1,1.5,50)
    
    z = np.zeros((len(u),len(v)))
    for i in range(len(u)):
        for j in range(len(v)):
            z[i,j] = np.dot(mapFeature(u[i].reshape(1,-1),v[j].reshape(1,-1)),theta)    # 计算对应的值，需要map
    
    z = np.transpose(z)
    plt.contour(u,v,z,[0,0.01])   # 画等高线，范围在[0,0.01]，即近似为决策边界
    #plt.legend()
    plt.show()

# 加载mat文件
def loadmat_data(fileName):
    return spio.loadmat(fileName)

# 显示100个数字
def display_data(imgData):
    sum = 0
    '''
    显示100个数（若是一个一个绘制将会非常慢，可以将要画的数字整理好，放到一个矩阵中，显示这个矩阵即可）
    - 初始化一个二维数组
    - 将每行的数据调整成图像的矩阵，放进二维数组
    - 显示即可
    '''
    pad = 1
    display_array = -np.ones((pad+10*(20+pad),pad+10*(20+pad)))
    for i in range(10):
        for j in range(10):
            display_array[pad+i*(20+pad):pad+i*(20+pad)+20,pad+j*(20+pad):pad+j*(20+pad)+20] = (imgData[sum,:].reshape(20,20,order="F"))    # order=F指定以列优先，在matlab中是这样的，python中需要指定，默认以行
            sum += 1
            
    plt.imshow(display_array,cmap='gray')   #显示灰度图像
    plt.axis('off')
    plt.show()



if __name__ == '__main__':
    print('module:myPreProcess')
    print('author:XiaoQi')
    print('date:2020.09.10')
    print('LinearRegression PreProcess functions')
