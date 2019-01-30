# 騎手クラス
class Rider:
    def __init__(self, n):
        self.name = n

# 馬クラス
class Horse:
    def __init__(self, n, r):
        self.name = n
        self.rider = r

# 騎手クラスのインスタンス生成
rider1 = Rider("アレキサンダー")

# 馬クラスのインスタンス生成
horse1 = Horse("ブケファラス", rider1)

print("{0}「ぼくの騎手は {1} ！」".format(horse1.name, horse1.rider.name))