# 根据json请求获取题目图片文件
import json
from urllib.request import urlopen
import base64
def get_json():
    response = urlopen("http://47.102.118.1:8089/api/problem?stuid=031802120").read().decode('utf-8')
    data = json.loads(response)
    photo = data["img"]
    imag = base64.b64decode(photo)
    fh = open("pit.jpg","wb")
    fh.write(imag)
    fh.close()
def cut_photo(photo):
    photo