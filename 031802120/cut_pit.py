# -*- coding: utf-8 -*-
# 将获取到的九宫格题目切割成9张子图
from PIL import Image
# 切图
def cut_image(image):
    width, height = image.size
    item_width = int(width / 3)
    box_list = []
    for i in range(0, 3):
        for j in range(0, 3):
            box = (j * item_width, i * item_width, (j + 1) * item_width, (i + 1) * item_width)
            box_list.append(box)
    image_list = [image.crop(box) for box in box_list]
    return image_list


# 保存
def save_images(image_list):
    index = 0
    for image in image_list:
        image.save( str(index) + '.png', 'PNG')
        index += 1


if __name__ == '__main__':
    file_path = "pit.jpg"
    image = Image.open(file_path)
    image_list = cut_image(image)
    save_images(image_list)