import re
import difflib
import sys
import jieba
import jieba.analyse
parameter1=sys.argv[1]  #
parameter2=sys.argv[2]  # SYS读入（命令行输入）
parameter3=sys.argv[3]  #
def read_txt(txtname):
    file=open(txtname,"r",encoding="utf-8")
    r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\n。！， ]+'
    word=file.read()
    word=re.sub(r,'',word) #去除标点符号
    file.close()
    return word
def print_txt(txtname):
    temp_txt = open(txtname,'w')
    functionName()
    ans=("%.2f" % jaccard())
    temp_txt.write(str(ans))
def functionName():
    if read_txt(parameter1)=="" or read_txt(parameter2)=="":
        raise "存在空白文档"
def main():
    read_txt(parameter1)
    read_txt(parameter2)
    print_txt(parameter3)
def do_jieba(name):
    jieba.analyse.set_stop_words("stopword.txt") #去停用词
    word=jieba.cut(name)
    result=jieba.analyse.extract_tags("".join(word),topK=50)
    return result
def jaccard():
    word1 = do_jieba(read_txt(parameter1)) #进行jieba分词
    word2 = do_jieba(read_txt(parameter2))
    len_mixed = len(list(set(word1).intersection(set(word2))))
    len_union = len(list(set(word1).union(set(word2))))
    if len_union != 0:
        temp = float(len_mixed) / len_union
        return temp
    else:
        return 0

if __name__== "__main__":
    main()


