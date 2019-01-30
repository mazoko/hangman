# (2)cubedモジュールを作って関数を書く→このモジュールをほかのモジュールからインポートして関数を呼び出す
def GetCubed(number):
    try:
        int_num = int(number)
        return int_num ** 3
    except ValueError:
        return "数値変換できないデータが渡されました。(number = " + number + ")"