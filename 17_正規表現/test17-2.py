import os
import re


l1 = ""

# パスを生成する
path1 = os.path.join("C:\\", "Users", "motegi-m1-serika", "Documents", "python", "17_正規表現", "zen.txt")
with open(path1, "r", encoding = "cp932") as f:
    l1 = f.read()
    
m1 = re.findall("Dutch", l1)
print(m1)

l2 = "Arizona 479, 501, 870. California 209, 213, 650."
m2 = re.findall("\\d{1,}", l2)
print(m2)

l3 ="The ghost that says boo haunts the loo."
m3 = re.findall(".oo", l3)
print(m3)