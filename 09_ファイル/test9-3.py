# (3)CSV出力
import os
import csv

list = [["top Gun", "Risky Business", "Minority Report"],
        ["Titanic", "The Revenant", "Inception"],
        ["Training Day", "Man of Fire", "Flight"]]

# C:\Users\motegi-m1-serika\Documents\python\09_ファイルというパスを生成する
path = os.path.join("C:\\", "Users", "motegi-m1-serika", "Documents", "python", "09_ファイル", "test3(utf-8).txt")

with open(path, "w", encoding = "utf-8", newline = '') as f:
    w = csv.writer(f, delimiter = ",")
    for listRow in list:
        w.writerow(listRow)