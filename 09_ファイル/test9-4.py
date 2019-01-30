# (3)CSV出力(日本語)
import os
import csv

list = [["トップガン", "リスキービジネス", "マイノリティレポート"],
        ["タイタニック", "レヴェナント", "インセプション"],
        ["トレーニングディ", "マンオブファイア", "フライト"]]

# C:\Users\motegi-m1-serika\Documents\python\09_ファイルというパスを生成する
path = os.path.join("C:\\", "Users", "motegi-m1-serika", "Documents", "python", "09_ファイル", "test4(utf-8).txt")

with open(path, "w", encoding = "utf-8", newline = '') as f:
    w = csv.writer(f, delimiter = ",")
    for listRow in list:
        w.writerow(listRow)