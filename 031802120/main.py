import re
import difflib
def read_in_copy_txt(txtname):
    global copyword
    file=open(txtname,"r",encoding="utf-8")
    r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\n。！， ]+'
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
def string_similar(s1,s2):
    return difflib.SequenceMatcher(None,s1,s2).quick_ratio()
read_in_copy_txt("orig_0.8_mix.txt")
read_in_original_txt("orig.txt")
print(string_similar(copyword,original))
