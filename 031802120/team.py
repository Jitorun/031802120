import json
from codecs import decode
from urllib.request import urlopen
import base64
def get_json():
    swap=[]
    response = urlopen("http://47.102.118.1:8089/api/problem?stuid=031802120").read().decode('utf-8')
    data = json.loads(response)
    photo = data["img"]
    imag = base64.b64decode(photo)
    fh = open("pit.jpg","wb")
    fh.write(imag)
    fh.close()
    js = open("json_get.txt","w")
    step = str(data["step"])
    swap=data["swap"]
    #print(swap)
    js.write(step+"\n")
    js.write("\n".join(str(i) for i in swap))
    js.close()
if __name__ == '__main__':
    get_json()
