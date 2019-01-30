def Quotient(num):
    """
    引数(整数)を2で割った値(整数)を返す
    :param num  : int型  整数
    :return     : int型  引数を2で割った値(整数)
    """
    return num // 2

def Product(num):
    """
    引数(整数)に4を掛けた値を返す
    :param num  : int型  整数
    :return     : int型  引数(整数)に4を掛けた値
    """
    return num * 4

inputNum = input("数値を入力してください：")

QuotientAns = Quotient(int(inputNum))
print("2で割った結果(剰余なし):" + str(QuotientAns))

ProductAns = Product(QuotientAns)
print("さらに4を掛けた結果:" + str(ProductAns))