import numpy as np   
from scipy import optimize
from myPreProcess import loadTxtAndCsvData

class LogisticRegression:
    def __init__(self,file_dir,alpha,num_iters = 400):
        self.alpha = alpha
        self.num_iters = num_iters
        self.f_dir = file_dir
        self.data = loadTxtAndCsvData(self.f_dir,',',dataType=np.float64)  #数据读取

        
