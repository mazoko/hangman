
from random import shuffle


# カードクラス
class Card:

    # カードの絵柄：スペード / ハート / ダイヤ / クラブ
    suits = ["spades(★)", "hearts(★★)", "diamonds(★★★)", "clubs(★★★★)"]

    # カードの数字：2~10 / ジャック(11) / クイーン(12) / キング(13) / エース(1)
    # 最初の2つをNoneにして、values[2]で"2"が取得できるようインデックスを調整
    values = [None, None,
              "2", "3", "4", "5", "6", "7", "8", "9", "10",
              "Jack(11)", "Queen(12)", "King(13)", "Ace(1)"]

    # 初期化
    def __init__(self, s, v):
        self.suit = s   # 絵柄
        self.value = v  # 数字

    # 大小比較1(selfの方が小さい場合、True)
    def __lt__(self, c2):
        # 数字が同じ場合
        if self.value == c2.value:
            # 絵柄で比較した結果を返す
            return self.suit < c2.suit

        # 数字で比較した結果を返す
        return self.value < c2.value

    # 大小比較2(selfの方が大きい場合、True)
    def __gt__(self, c2):
        # 数字が同じ場合
        if self.value == c2.value:
            # 絵柄で比較した結果を返す
            return self.suit > c2.suit

        # 数字で比較した結果を返す
        return self.value > c2.value

    # print出力
    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v

# 山札クラス
class Deck:

    # 初期化
    def __init__(self):
        self.cards = []  # 山札リスト

        for s in range(4):              # カードの絵柄分ループ
            for v in range(2, 15):      # カードの数字分ループ

                # 山札リストにカードを1枚加える
                self.cards.append(Card(s, v))

        # 山札リストをシャッフル
        shuffle(self.cards)

    # 山札リストからカードを引く
    def draw(self):

        # 山札リストの中身が0の場合
        if len(self.cards) == 0:

            # Noneを返す          
            return  

        # 引いたカードを返し、山札リストから削除
        return self.cards.pop()

# プレイヤークラス
class Player:

    # 初期化
    def __init__(self, n):
        self.wins = 0       # 勝利回数
        self.card = None    # 引いたカード
        self.name = n       # プレイヤー名

# ゲームクラス
class Game:

    # 初期化
    def __init__(self):
        name1 = input("プレイヤー1の名前：")
        name2 = input("プレイヤー2の名前：")

        self.p1 = Player(name1)  # プレイヤー1
        self.p2 = Player(name2)  # プレイヤー2

        self.deck = Deck()      # 山札

    # ラウンドの勝敗を表示
    def print_round_winner(self, winner):
        msg = "このラウンドは【{0}】が勝ちました".format(winner.name)
        print(msg)

    # カードを引いた結果を表示
    def print_draw(self, p1, p2):
        msg = "{0} のカード： {1}\n{2} のカード： {3}".format(p1.name, p1.card, p2.name, p2.card)
        print(msg)

    # ゲーム実行
    def play_game(self):
        cards = self.deck.cards
        print("ゲーム開始！")

        while len(cards) >= 2:
            msg = "q で終了、それ以外のキーでカードを1枚引きます："
            res = input(msg)

            if res == "q":
                break

            # 引いたカード
            self.p1.card = self.deck.draw()
            self.p2.card = self.deck.draw()

            # カードを引いた結果を表示
            self.print_draw(self.p1, self.p2)

            if self.p1.card > self.p2.card:
                self.p1.wins += 1

                # ラウンドの勝敗を表示
                self.print_round_winner(self.p1)

            else:
                self.p2.wins += 1

                # ラウンドの勝敗を表示
                self.print_round_winner(self.p2)

        win = self.game_winner(self.p1, self.p2)
        print("ゲーム終了、{0}です！".format(win))

    # ゲームの勝敗を返す
    def game_winner(self, p1, p2):
        if p1.wins > p2.wins:
            return "【{0}】の勝利".format(p1.name)
        if p1.wins < p2.wins:
            return "【{0}】の勝利".format(p2.name)
        return "引き分け"


game = Game()
game.play_game()
