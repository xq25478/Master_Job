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

# 随机初始化权重theta
def randInitializeWeights(L_in,L_out):
    W = np.zeros((L_out,1+L_in))
    epsilon_init = (6.0/(L_out+L_in))**0.5
    W = np.random.rand(L_out,1+L_in)*2*epsilon_init-epsilon_init
    return W

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
    print('date:2020.09.14')
    print('NerualNetwork PreProcess functions')
