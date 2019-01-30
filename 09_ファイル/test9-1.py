# (1)ファイル読み込み
import os

# C:\Users\motegi-m1-serika\Documents\python\09_ファイルというパスを生成する
path1 = os.path.join("C:\\", "Users", "motegi-m1-serika", "Documents", "python", "09_ファイル", "test(utf-8).txt")
path2 = os.path.join("C:\\", "Users", "motegi-m1-serika", "Documents", "python", "09_ファイル", "test(sjis).txt")

with open(path1, "r", encoding = "utf-8") as f:
    print(f.read())

with open(path2, "r", encoding = "cp932") as f:
    print(f.read())