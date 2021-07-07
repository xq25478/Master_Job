# AlexNet(2012)
- 首次将卷积神经网络引入到图像分类任务当中去
- 5(conv+relu)+3(full)+maxpooling 
    -   kernel size 11x11 5x5 3x3
- multi trainging / relu / dropout / local response normalization / overlapping pooling
- data augmentataion: 224x224 patcaes causing trainset x2048

# VGGNet(2014)
- 全部代替为3x3卷积 11(8+3)-19(16+3) deeper!
    - 加入更多激活函数 增加模型的非线性
    - 更小的参数量
- 加入1x1卷积 
    - 减小模型的通道数
    - 加入更多激活函数

# GoogLeNet(2015)

# ResNet(2015)


