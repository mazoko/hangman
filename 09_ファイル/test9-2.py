# (2)ファイル書き込み
import os

# C:\Users\motegi-m1-serika\Documents\python\09_ファイルというパスを生成する
path = os.path.join("C:\\", "Users", "motegi-m1-serika", "Documents", "python", "09_ファイル", "test2(utf-8).txt")

name = input("お名前を教えてください。入力:")
inputWord1 = "質問1: " + name
inputWord2 = "質問2: " + input("好きな色を教えてください。入力:")
inputWord3 = "質問3: " + input("好きな食べ物を教えてください。入力:")
print("ご協力ありがとうございました(^^)")

path = os.path.join("C:\\", "Users", "motegi-m1-serika", "Documents", "python", "09_ファイル", "test2(utf-8)_" + name + ".txt")

with open(path, "w", encoding = "utf-8") as f:
    f.write(inputWord1 + "\n")
    f.write(inputWord2 + "\n")
    f.write(inputWord3 + "\n")