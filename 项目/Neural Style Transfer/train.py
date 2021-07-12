'''
@brirf:使用densenet主干网络进行设计
@author:Mr.XQ
@date:2021/03/29
@densenet:
12 layers
0:conv -----
1:bn
2:relu
3:pool
4:denseblock -----
5:transition
6:denseblock -----
7:transition
8:denseblock -----
9:transition
10:denseblock -----
11:bn
'''

from __future__ import print_function

import random

import torch.optim as optim

import torchvision.models as models
import copy
from loss import ContentLoss, GramMatrix, StyleLoss

import torchvision.transforms as transforms
from torch.autograd import Variable

import os
from PIL import Image
import numpy as np
from ssim import ssim
import torch
import torch.nn as nn


# model define
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
use_cuda = torch.cuda.is_available()

# image path
content_path = 'contents/'
style_path = 'styles/'
content_imgs = os.listdir(content_path)
styles_imgs = os.listdir(style_path)#[str(i) for i in range(1,5)]
random.shuffle(content_imgs)
EPOCH = 300
CONTENT_WEIGHT = 1
STYLE_WEIGHT = 1000
SSIM_WEIGHT = 25
INITIALIZE_NOISE = False
dtype = torch.cuda.FloatTensor if use_cuda else torch.FloatTensor
output_path = 'result'
# desired size of the output image
imsize = 256 if use_cuda else 128  # use small size if no gpu
all = len(content_imgs)*len(styles_imgs)
cnt = 0

# desired layers
content_layers_default = ['conv_8']
style_layers_default = ['conv_0', 'conv_4', 'conv_6','conv_8','conv_10']

def weights_init_normal(m):
    classname = m.__class__.__name__
    if classname.find("Conv") != -1:
        torch.nn.init.normal_(m.weight.data, 0.0, 0.02)
    elif classname.find("BatchNorm2d") != -1:
        torch.nn.init.normal_(m.weight.data, 1.0, 0.02)
        torch.nn.init.constant_(m.bias.data, 0.0)

def image_loader(image_name, imsize):
    loader = transforms.Compose([
        transforms.Resize((imsize, imsize)),  # scale imported image
        transforms.ToTensor()])  # transform it into a torch tensor

    image = Image.open(image_name).convert('RGB')
    #print(image)
    image = Variable(loader(image))
    # fake batch dimension required to fit network's input dimensions
    image = image.unsqueeze(0)
    return image

def image_loader_gray(image_name, imsize):
    loader = transforms.Compose([

        transforms.Resize((imsize, imsize)),  # scale imported image
        transforms.ToTensor(),
    ])

    image = Image.open(image_name).convert('L')
    image = np.asarray(image)
    image = np.asarray([image,image,image])
    image = Image.fromarray(np.uint8(image).transpose(1,2,0))
    image = Variable(loader(image))
    # fake batch dimension required to fit network's input dimensions
    image = image.unsqueeze(0)
    return image

def save_image(tensor, size, input_size, fname='transferred.png'):
    unloader = transforms.ToPILImage()  # reconvert into PIL image

    image = tensor.clone().cpu()  # we clone the tensor to not do changes on it
    image = image.view(size)
    image = unloader(image).resize(input_size)
    out_path = os.path.join(output_path, fname)
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    image.save(out_path)

def get_style_model_and_losses(cnn, style_img, content_img, style_weight=1000, content_weight=1, content_layers=content_layers_default, style_layers=style_layers_default):
    cnn = copy.deepcopy(cnn)
    Net = nn.Sequential()  # the new Sequential module network
    gram = GramMatrix()  # we need a gram module in order to compute style targets
    content_losses = []
    style_losses = []
    if use_cuda:
        Net = Net.cuda()
        gram = gram.cuda()
    i = 0
    for layer in list(cnn):
        #rint(layer)
        name = "conv_" + str(i)
        Net.add_module(name, layer)
        if name in content_layers:
            # add content loss:
            target = Net(content_img).clone()
            #print('content',target.shape)
            content_loss = ContentLoss(target, content_weight)
            Net.add_module("content_loss_" + str(i), content_loss)
            content_losses.append(content_loss)
        if name in style_layers:
            # add style loss:
            target_feature = Net(style_img).clone()
            #print('style', target_feature.shape)
            target_feature_gram = gram(target_feature)
            style_loss = StyleLoss(target_feature_gram, style_weight)
            Net.add_module("style_loss_" + str(i), style_loss)
            style_losses.append(style_loss)
        i += 1
    #print(Net)
    return Net, style_losses, content_losses

def get_input_param_optimizer(input_img):
    # this line to show that input is a parameter that requires a gradient
    input_param = nn.Parameter(input_img.data)
    optimizer = optim.LBFGS([input_param])
    return input_param, optimizer

def run_style_transfer(cnn, content_img, style_img, input_img, num_steps=300, style_weight=1000, content_weight=1):
    """Run the style transfer."""
    print('Building the style transfer model..')
    Net, style_losses, content_losses = get_style_model_and_losses(cnn, style_img, content_img, style_weight, content_weight)
    input_param, optimizer = get_input_param_optimizer(input_img)

    print('Optimizing..')
    run = [0]
    while run[0] <= num_steps:

        def closure():
            # correct the values of updated input image
            input_param.data.clamp_(0, 1)

            optimizer.zero_grad()
            Net(input_param)
            style_score = 0
            content_score = 0
            score_loss = ssim(input_param,content_img, val_range=255)
            #print('Score%f'%(score_loss))

            for sl in style_losses:
                style_score += sl.backward()
            for cl in content_losses:
                content_score += cl.backward()

            run[0] += 1
            if run[0] % 50 == 0:
                print("run {}:".format(run))
                print('Style Loss : {:4f} Content Loss: {:4f}'.format(style_score.item(), content_score.item()))

            return style_score + content_score + score_loss*SSIM_WEIGHT

        optimizer.step(closure)

    # a last correction...
    input_param.data.clamp_(0, 1)

    return input_param.data

for _c in content_imgs:
    for _s in styles_imgs:
        cnt += 1
        print("Processing:%d/%d"%(cnt,all))
        CONTENT_PATH = content_path + _c
        STYLE_PATH = style_path + _s

        name_content, ext = os.path.splitext(os.path.basename(CONTENT_PATH))
        name_style, _ = os.path.splitext(os.path.basename(STYLE_PATH))
        fname = name_content+'-'+name_style+ext
        out_path = os.path.join(output_path,fname)

        if not os.path.exists(out_path):
            style_img = image_loader(STYLE_PATH, imsize).type(dtype)
            content_img = image_loader(CONTENT_PATH, imsize).type(dtype)
            input_img = image_loader(CONTENT_PATH, imsize).type(dtype)
            #input_img = Variable(torch.randn(content_img.data.size())).type(dtype)
            input_size = Image.open(CONTENT_PATH).size
            assert style_img.size() == content_img.size(), \
                "we need to import style and content images of the same size"
            cnn = models.densenet121(pretrained=True)
            cnn.apply(weights_init_normal)
            model = cnn.features
            # move it to the GPU if possible:
            if use_cuda:
                model = model.cuda()
            output = run_style_transfer(model, content_img, style_img, input_img, EPOCH, STYLE_WEIGHT, CONTENT_WEIGHT)
            name_content, ext = os.path.splitext(os.path.basename(CONTENT_PATH))
            name_style, _ = os.path.splitext(os.path.basename(STYLE_PATH))
            fname = name_content+'-'+name_style+ext

            save_image(output, size=input_img.data.size()[1:], input_size=input_size, fname=fname)