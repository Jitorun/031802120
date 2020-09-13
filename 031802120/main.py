import re
import difflib
import sys
parameter1=sys.argv[1]
parameter2=sys.argv[2]
parameter3=sys.argv[3]
def read_in_copy_txt(txtname):
    global copyword
    file=open(txtname,"r",encoding="utf-8")
    r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\n。！， ]+'
    copyword=file.read()
    copyword=re.sub(r,'',copyword)
    file.close()
    #print(copyword)
def read_in_original_txt(txtname):
    global original
    file=open(txtname,"r",encoding="utf-8")
    r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\n。！， ]+'
    original=file.read()
    original=re.sub(r,'',original)
    #print(original)
    file.close()
def string_similar(s1,s2):
    return difflib.SequenceMatcher(None,s1,s2).quick_ratio()
def print_txt(txtname):
    temp_txt = open(txtname,'w')
    functionName()
    a=("%.2f" % string_similar(copyword,original))
    temp_txt.write(str(a))
def functionName():
    if copyword=="" or original=="":
        raise "存在空白文档"
def main():
    read_in_original_txt(parameter1)
    read_in_copy_txt(parameter2)
    print_txt(parameter3)

if __name__== "__main__":
    main()


