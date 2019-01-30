import math

# りんごクラス
class Apple:
    def __init__(self, w, c, s, k):
        self.weight = w         # 重さ
        self.color = c          # 色
        self.sweetness = s      # 甘さ
        self.kind = k           # 品種

# 円クラス
class Circle:
    def __init__(self, r):
        self.radius = r         # 半径

    # 面積計算メソッド
    def area(self):
        # 半径 * 半径 * π
        return self.radius ** 2 * math.pi

# 三角形クラス
class Triangle:
    def __init__(self, b, h):
        self.base = b           # 底辺
        self.height = h         # 高さ
    
    # 面積計算メソッド
    def area(self):
        # 底辺 * 高さ / 2
        return self.base * self.height / 2

triangle1 = Triangle(8, 9)
triangleArea1 = triangle1.area()
print("三角形1の面積は {0} cm2".format(str(triangleArea1)))

# 六角形クラス
class Hexagon:
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        self.side4 = s4
        self.side5 = s5
        self.side6 = s6
    
    # 外周計算メソッド
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4 + self.side5 + self.side6

hexagon1 = Hexagon(1, 2, 1, 2, 1, 2)
gaisyuu = hexagon1.calculate_perimeter()
print("六角形1の外周は {0} cm".format(str(gaisyuu)))
