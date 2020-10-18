# 将得到的题目的图片与处理好的字母子图进行匹配，返回待处理的矩阵
from PIL import Image
import math
import operator
from functools import reduce
import os


temp = [
        1, 2, 3,
        4, 5, 6,
        7, 8, 9]
win = [0, 1, 2,
       3, 4, 5,
       6, 7, 8]
flag = [1, 1, 1, 1, 1, 1, 1, 1, 1]
flag2 = [1, 1, 1, 1, 1, 1, 1, 1, 1]


# 将图片转化成3*3矩阵
def pictureCompare(path):
    count = 0
    TrainFiles = os.listdir(path)  # 遍历每个子文件夹
    Train_Number = len(TrainFiles)  # 子文件夹个数
    for k in range(0, Train_Number):
        Trainneed = os.listdir(path + '/' + TrainFiles[k])  # 遍历每个子文件夹里的每张图片
        Trainneednumber = len(Trainneed)  # 每个子文件里的图片个数
        for i in range(0, Trainneednumber):
            for j in range(0,9):
                if image_contrast(path + '/' + TrainFiles[k] + '/' + Trainneed[i],str(j)+".png") == 0:
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
    return win,temp


def image_contrast(img1, img2):

    image1 = Image.open(img1)
    image2 = Image.open(img2)

    h1 = image1.histogram()
    h2 = image2.histogram()

    result = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
    return result


