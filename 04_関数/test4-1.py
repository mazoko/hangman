# 引数を二乗して返す
def Squaring(number):
    int_num = int(number)
    int_num = int_num ** 2
    return int_num

number = input("数値を入力してください：")
print(Squaring(number))