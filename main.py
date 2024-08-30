'''
Author: SingleBiu
Date: 2024-08-30 09:47:57
LastEditors: SingleBiu
LastEditTime: 2024-08-30 10:07:31
FilePath: \Code\main.py
Description: 

Copyright (c) 2024 by Sakifox@foxmail.com, All Rights Reserved. 
'''

import os
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
# jupyter环境
# %matplotlib inline
# 指定图片大小
plt.figure(figsize=(200, 200))
# 读取当前目录
pwd = os.getcwd()
# 源图片名
str = "Chisato.jpg"
# 输出图片名
str_cgd = "Chisato_changed.jpg"

# DEBUG
# print(pwd+"\\"+str)

pic = plt.imread(pwd+"\\"+str)
# 指定马赛克程度，数字越大越模糊
pic = pic[::4, ::4]
# 设置坐标轴，方便对照取色
plt.grid(axis="y")
plt.grid(axis="x")
# 设置坐标轴取值0-41是范围，0.5是单位长(精度)  0，41，0.5
plt.xticks(np.arange(0, 500, 0.5))
plt.yticks(np.arange(0, 500, 0.5))
# 坐标显示，起始值颠倒对图片有旋转效果
plt.xlim(0,60)
plt.ylim(80,0)
plt.imshow(pic)
# 保存图片
plt.savefig(pwd+"\\"+str_cgd)