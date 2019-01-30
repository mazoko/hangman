# 必須引数3、オプション引数2
def PrintStrings(str1, str2, str3, str4 = "それ！", str5 = "そいや！"):
    """
    引数の文字列を出力する
    :param str1  : string型  第一声
    :param str2  : string型  第二声
    :param str3  : string型  第三声
    :param str4  : string型  第四声 オプション引数
    :param str5  : string型  第五声 オプション引数
    """
    print(str1 + str2 + str3 + str4 + str5)

str1 = input("1つ目の掛け声を入力してください：")
str2 = input("2つ目の掛け声を入力してください：")
str3 = input("3つ目の掛け声を入力してください：")
PrintStrings(str1, str2, str3)

str1 = input("1つ目の掛け声を入力してください：")
str2 = input("2つ目の掛け声を入力してください：")
str3 = input("3つ目の掛け声を入力してください：")
str4 = input("4つ目の掛け声を入力してください：")
str5 = input("5つ目の掛け声を入力してください：")
PrintStrings(str1, str2, str3, str4, str5)