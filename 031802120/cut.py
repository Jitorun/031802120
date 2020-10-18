# -*- coding: utf-8 -*-
# 将无框字符里的每个字母分割成9张子图，保存到各自分好类的文件夹里
import os
from PIL import Image


# 切图
def cut_image(image):
    width, height = image.size
    item_width = int(width / 3)
    box_list = []
    # (left, upper, right, lower)
    for i in range(0, 3):
        for j in range(0, 3):
            box = (j * item_width, i * item_width, (j + 1) * item_width, (i + 1) * item_width)
            box_list.append(box)

    image_list = [image.crop(box) for box in box_list]

    return image_list


# 保存
def save_images(image_list,num):
    index = 0
    for image in image_list:
        image.save('letter1/'+str(num) + '/' + str(index) + '.png', 'PNG')
        index += 1


if __name__ == '__main__':
    file_path = "D:/031802120/031802120/"
    Trainneed = os.listdir(file_path)  # 遍历每个子文件夹里的每张图片
    Trainneednumber = len(Trainneed)  # 每个子文件里的图片个数
    num = 1
    for i in range(0, Trainneednumber):
        image = Image.open(file_path + Trainneed[i])
        image_list = cut_image(image)
        save_images(image_list,num)
        num=num+1