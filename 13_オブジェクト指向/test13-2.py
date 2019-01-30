# 正方形クラス
class Square:
    def __init__(self, s):
        self.side = s

    # 外周計算メソッド
    def calculate_perimeter(self):
        return self.side * 4
    
    # 値変更メソッド
    def change_side(self, s):
        self.side = self.side + s

# 正方形のインスタンス生成
square1 = Square(5)

print("変更前の正方形の一辺は {0} cm！".format(str(square1.side)))

square1.change_side(2)
print("変更後の正方形の一辺は {0} cm！".format(str(square1.side)))

square1.change_side(-3)
print("変更後の正方形の一辺は {0} cm！".format(str(square1.side)))