import jieba
import gensim
def read_in_copy_txt(txtname):
    global copyword
    file=open(txtname,"r",encoding="utf-8")
    copyword=file.read()
    file.close()
def read_in_original_txt(txtname):
    global original
    file=open(txtname,"r",encoding="utf-8")
    original=file.read()
    file.close()
def dojiebacopy():
    global copytxt
    copytxt=[]
    #copy_txt.append(copyword)
    for doc in copyword:
        doc_list=[word for word in jieba.cut(doc)]
        copytxt.append(doc_list)
    print(copytxt)
def dojiebaoriginal():
    global originaltxt
    originaltxt=[]
    #originaltxt.append(original)
    for doc in original:
        doc_list=[word for word in jieba.cut(doc)]
        originaltxt.append(doc_list)
    print(originaltxt)
read_in_copy_txt("copy.txt")
read_in_original_txt("original-text.txt")
dojiebacopy()
dojiebaoriginal()
#jieba后抄袭文件为copytxt
#jieba后原来文件为originaltxt

