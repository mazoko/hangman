import time
import random

class Queue:
    def __init__(self):
        self.items = []
    
    # 空リスト判定
    def is_empty(self):
        return self.items == []

    # えんきゅー    ：リスト先頭にアイテムを追加
    def enqueue(self, item):
        self.items.insert(0, item)

    # できゅー      ：リスト末尾からアイテムを取得、削除
    def dequeue(self):
        return self.items.pop()
    
    # リストの長さを確認
    def size(self):
        return len(self.items)
"""
# インスタンス生成
queue = Queue()
# 空リスト判定
print(queue.is_empty())

# アイテム追加
queue.enqueue("item1")
# 空リスト判定
print(queue.is_empty())

# アイテムを取得、削除
item = queue.dequeue()
print(item)
print(queue.is_empty())

#for i in range(1, 6):
#    queue.enqueue(i)

# リストの長さを確認
#print(queue.size())


# 「Hello」を逆順にしない
for i in "Hello":
    queue.enqueue(i)

reverse = ""
while queue.size():
    reverse += queue.dequeue()

print(reverse)
"""


# チケット行列
# till_show ：映画開始までの時間
# max_time  ：一人のチケット購入にかかる最大時間
def sumulate_line(till_show, max_time):
    pq = Queue()        # 購入待ちの人間キュー
    tix_sold = []       # チケットが無事買えた人間リスト

    nop = 100           # number of persons：人数

    # キューに人数分の要素を追加！
    for i in range(1, nop+1):
        pq.enqueue("person" + "{:03}".format(i))

    now = time.time()           # 現在時刻    
    t_end = now + till_show     # 現在時刻 + 映画開始までの時間

#    print("now  : " + str(now))
#    print("t_end: " + str(t_end))

    # 映画開始時間を過ぎる、または行列が捌けるまでループ
    while now < t_end and not pq.is_empty():
        now = time.time()       # 現在時刻更新
#        print(now)

        r = random.randint(0, max_time)         # チケット購入にかかる時間をランダムで設定
        time.sleep(r)                           # 購入中……

        person = pq.dequeue()                   # 購入待ち行列から脱出
        print(person + "「チケット買えたで」 (購入時間：" + str(r) + ")")
        tix_sold.append(person)                 # 無事買えたリストに記録 

    # 無事買えた人間リストを返す
    return tix_sold


ts = 10 # till_show ：映画開始までの時間
mt = 1  # max_time  ：一人のチケット購入にかかる最大時間
sold = sumulate_line(ts, mt)
print(sold)