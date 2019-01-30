# 長方形クラス
class Rectangle:
    def __init__(self, h, w):
        self.height = h
        self.width = w
    
    # 外周計算メソッド
    def calculate_perimeter(self):
        return self.height * 2 + self.width * 2

# 正方形クラス
class Square:
    def __init__(self, s):
        self.side = s

    # 外周計算メソッド
    def calculate_perimeter(self):
        return self.side * 4

# 長方形のインスタンス生成
rectangle1 = Rectangle(2, 3)
rGaisyuu = rectangle1.calculate_perimeter()

# 正方形のインスタンス生成
square1 = Square(2)
sGaisyuu = square1.calculate_perimeter()

print("長方形の外周は {0} cm！".format(str(rGaisyuu)))
print("正方形の外周は {0} cm！".format(str(sGaisyuu)))