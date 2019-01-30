# (8)クォート文字を含む文字列を作成
stringQ = "クォート(\")を含む文字列はこう作る！\r\nクォート(\")の前にバックスラッシュ(\\)！\r\nちなみに改行は「\\r\\n」！"
print(stringQ)

# (9)文字列を連結
string = "three"
string1 = "three" + "three" + "three"
string2 = "three" * 3
print("string1:" + string1 + "\r\nstring2:" + string2)

# (10)文字列をスライス
stringBfr = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
# 「、」が出現するインデックスを取得し、先頭からそのインデックスまでを取得
indexNum = stringBfr.index("、")
stringAft = stringBfr[0 : indexNum]
print(stringAft)