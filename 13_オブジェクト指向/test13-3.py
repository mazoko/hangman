# 図形クラス
class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a shape!!")

# 長方形クラス(図形クラスを継承)
class Rectangle(Shape):
    def __init__(self, h, w):
        self.height = h
        self.width = w
    
    # 外周計算メソッド
    def calculate_perimeter(self):
        return self.height * 2 + self.width * 2

# 正方形クラス(図形クラスを継承)
class Square(Shape):
    def __init__(self, s):
        self.side = s

    # 外周計算メソッド
    def calculate_perimeter(self):
        return self.side * 4
    
    # 値変更メソッド
    def change_side(self, s):
        self.side = self.side + s

# 長方形のインスタンス生成
rectangle1 = Rectangle(2, 3)
rectangle1.what_am_i()

# 正方形のインスタンス生成
square1 = Square(2)
square1.what_am_i()
