'''
The torch package contains data structures for multi-dimensional
tensors and defines mathematical operations over these tensors.
Additionally, it provides many utilities for efficient serializing of
Tensors and arbitrary types, and other useful utilities.
'''
from numpy.lib.stride_tricks import broadcast_arrays
import torch  # 导入torch模块

from torch import nn
from torch import optim
from torch.nn.modules.activation import ReLU
from torch.nn.modules.normalization import LayerNorm
from torchvision import transforms

'''
dataloader 用于将dataset封装成可以迭代得数据结构 用于神经网络得batch训练
'''
from torch.utils.data import DataLoader

"""
pytorch提供了各个特定领域的数据处理库 如torchvision torchtext torchaudio 等等
当中均包含有datasets这个类 ；来处理输入数据
dataset 用于存储数据及其相应的标签
"""
from torchvision import datasets
from torchvision.transforms import ToTensor,Lambda,Compose
import matplotlib.pyplot as plt

"""
To define a neural network in PyTorch, we create a class that inherits from nn.Module. 
We define the layers of the network in the __init__ function and specify how data will pass through the network in the forward function. 
To accelerate operations in the neural network, we move it to the GPU if available.
"""
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork,self).__init__()
        """
        Flattens(展平) a contiguous range of dims into a tensor. For use with :class:`~nn.Sequential`
        """
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28,512),
            nn.ReLU(),
            nn.Linear(512,512),
            nn.ReLU(),
            nn.Linear(512,10),
            nn.ReLU())

    def forward(self,x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

## 第五步 开始训练 
def train(dataloader,model,loss_fn,optimizer):
    size = len(dataloader.dataset)
    for batch,(X,y) in enumerate(dataloader):
        X,y = X.to(device),y.to(device)

        pred = model(X)
        loss = loss_fn(pred,y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch % 100 == 0:
            loss,current = loss.item(),batch*len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")


##  第六步 测试
def test(dataloader,model,loss_fn):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    model.eval()
    test_loss,correct = 0,0
    with torch.no_grad():
        for X,y in dataloader:
            X,y = X.to(device),y.to(device)
            pred = model(X)
            test_loss += loss_fn(pred,y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()
    test_loss /= num_batches
    correct /= size
    print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")

if __name__ == "__main__":
    ## 第一步 下载数据
    train_data = datasets.FashionMNIST(
        root='data',
        train=True,
        download=True,
        transform=ToTensor(),
    )

    test_data = datasets.FashionMNIST(
        root='data',
        train=False,
        download=True,
        transform=ToTensor(),
    )

    ## 第二步 将dataset实例传给dataloader用来创建可迭代得数据实例
    """
    We pass the Dataset as an argument to DataLoader. 
    This wraps an iterable over our dataset, and supports automatic batching, sampling, shuffling and multiprocess data loading. 
    Here we define a batch size of 64, i.e. each element in the dataloader iterable will return a batch of 64 features and labels.
    """
    train_dataloader = DataLoader(train_data, batch_size=64)
    test_dataloader = DataLoader(test_data, batch_size=64)

    ## 第三步 创建模型
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print('Using {} device'.format(device))

    model = NeuralNetwork().to(device)
    print(model)
    ## 第四步 定义损失函数和优化器  重点研究！！！
    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=2e-3)

    epoch = 100
    for t in range(epoch):
        print(f"Epoch {t + 1}\n-------------------------------")
        train(train_dataloader, model, loss_fn, optimizer)
        test(test_dataloader, model, loss_fn)
    print("Done!")


## saving models
torch.save(model.state_dict(),'model.pth')
print("Save PyTorch Model State to model.pth")

## loading models
model = NeuralNetwork()
model.load_state_dict(torch.load("model.pth"))
