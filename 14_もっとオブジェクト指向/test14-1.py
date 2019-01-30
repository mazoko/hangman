# 図形クラス
class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a shape!!")

# 正方形クラス(図形クラスを継承)
class Square(Shape):
    # 作成済み正方形リスト
    square_list = []

    def __init__(self, s):
        self.side = s

        # リストにインスタンスを追加
        self.square_list.append(self)

    # 外周計算メソッド
    def calculate_perimeter(self):
        return self.side * 4
    
    # 値変更メソッド
    def change_side(self, s):
        self.side = self.side + s
    
    # 
    def __repr__(self):
        return "{0} by {0} by {0} by {0}".format(self.side)

# 正方形のインスタンス生成
square1 = Square(2)
square2 = Square(3)
square3 = Square(4)

print(Square.square_list)

# 渡されたふたつのパラメータが同じものだったらTrue、そうでなければFalseを返す関数
def equals(obj1, obj2):
    if obj1 is obj2:
        return True
    else:
        return False

square11 = square1
square21 = Square(3)

print(equals(square1, square11))    # コピーなのでTrue
print(equals(square2, square21))    # 同じ値を渡した別のオブジェクトなのでFalse