# 引数をfloat型に変換して返す
def StringToFloat(str):
    """
    引数をfloat型に変換して返す
    :param str  : string型  変換前
    :return     : float型   変換後
    """
    try:
        return float(str)
    except ValueError:
        print("入力値が数値ではありません")

inputNum = input("数値を入力してください：")
floatNum = StringToFloat(inputNum)
print(floatNum)