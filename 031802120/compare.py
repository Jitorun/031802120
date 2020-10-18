from PIL import Image
import math
import operator
from functools import reduce
import os
import numpy as np
import os
import cv
import heapq
import copy
import re
import datetime
temp=[
    1,2,3,
    4,5,6,
    7,8,9]
win=[0,1,2,
     3,4,5,
     6,7,8]
flag =[1,1,1,1,1,1,1,1,1]
flag2=[1,1,1,1,1,1,1,1,1]
def createDatabase(path):
    # 查看路径下所有文件
    count = 0
    TrainFiles = os.listdir(path)  # 遍历每个子文件夹
    # 计算有几个文件(图片命名都是以 序号.jpg方式)
    Train_Number = len(TrainFiles)  # 子文件夹个数
    # 把所有图片转为1维并存入X_train中
    for k in range(0, Train_Number):
        Trainneed = os.listdir(path + '/' + TrainFiles[k])  # 遍历每个子文件夹里的每张图片
        Trainneednumber = len(Trainneed)  # 每个子文件里的图片个数
        for i in range(0, Trainneednumber):
            for j in range(0,9):
                #print(image_contrast(path + '/' + TrainFiles[k] + '/' + Trainneed[i], str(j) + ".png"))
                if image_contrast(path + '/' + TrainFiles[k] + '/' + Trainneed[i],str(j)+".png") == 0:
                    #print(path + '/' + TrainFiles[k] + '/' + Trainneed[i])
                    #print(temp)
                    temp[j]=i
                    flag[j]=0
    for t in range(0,9):
        if flag[t]==1:
            temp[t]=9
    for i in range(0,9):
        for j in range(0,9):
            if temp[i]==j:
                flag2[temp[i]]=0
    for i in range(0,9):
        if flag2[i]!=0:
            win[i]=9
    print(win)






def image_contrast(img1, img2):

    image1 = Image.open(img1)
    image2 = Image.open(img2)

    h1 = image1.histogram()
    h2 = image2.histogram()

    result = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
    return result

if __name__ == '__main__':
    createDatabase("D:/031802120/031802120/data")
    print(temp)
    with open("./infile.txt","w") as f:
        f.write("3\n")
        f.write(" ".join(str(i) for i in temp))
    # coding=utf-8
    '''
    n = 1
    for i in range(NUMBER):
        l = []
        for j in range(NUMBER):
            l.append(n)
            n += 1
        GOAL.append(l)
        #print(GOAL)
    GOAL[NUMBER - 1][NUMBER - 1] = 0
    #print(GOAL)
    '''
    #GOAL = [[0, 1, 9], [3, 4, 5], [6, 7, 8]]

    ##构建A
    #a = A.A(A.Node([[0 , 9 , 1], [3 , 4 , 5], [6, 7, 8]]), A.Node([[0, 1, 999], [3, 4, 5], [6, 7, 8]]));
    ##开始寻路
    #if a.start():
    #    a.showPath()
    #else:
    #    print("no way")
