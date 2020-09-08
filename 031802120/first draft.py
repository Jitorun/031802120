import jieba
import re
from gensim import corpora,models,similarities
def read_in_copy_txt(txtname):
    global copyword
    file=open(txtname,"r",encoding="utf-8")
    r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\n。！, ]+'
    copyword=file.read()
    copyword=re.sub(r,'',copyword)
    file.close()
    print(copyword)
def read_in_original_txt(txtname):
    global original
    file=open(txtname,"r",encoding="utf-8")
    r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\n。！， ]+'
    original=file.read()
    original=re.sub(r,'',original)
    print(original)
    file.close()
def dojiebacopy():
    global copytxt
    # copy_txt.append(copyword)
    copytxt = [word for word in jieba.cut(copyword)]
   # copytxt.append(doc_list)
    print(copytxt)
def dojiebaoriginal():
    global originaltxt
    originaltxt=[]
    #originaltxt.append(original)
    originaltxt=[word for word in jieba.cut(original)]
    #originaltxt.append(doc_list)
    print(originaltxt)
read_in_copy_txt("copy.txt")
read_in_original_txt("original-text.txt")
dojiebacopy()
dojiebaoriginal()
#jieba后抄袭文件为copytxt
#jieba后原来文件为originaltxt
