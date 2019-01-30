# (5)リストの文字列を結合
# 半角スペースで結合し、ピリオド前の半角スペースはピリオドのみに置換する
stringList = ["The", "fox", "jumped", "over", "the", "fence", "."]
string = " ".join(stringList).replace(" .", ".")
print(string)