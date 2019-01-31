class Stack:
    def __init__(self):
        self.items = []
    
    # 空リスト判定
    def is_empty(self):
        return self.items == []

    # リスト末尾にアイテムを追加
    def push(self, item):
        self.items.append(item)

    # リスト末尾からアイテムを取得、削除
    def pop(self):
        return self.items.pop()

    # リスト末尾のアイテムを確認
    def peek(self):
        last = len(self.items) - 1
        return self.items[last]
    
    # リストの長さを確認
    def size(self):
        return len(self.items)

# (1)"yesterday"を逆順にする
word = "yesterday"

stack1 = Stack()
for c in word:
    stack1.push(c)

re = ""
while stack1.size():
    re += stack1.pop()

print("そのまま： " + word)
print("逆順　　： " + re)

# (2)[1,2,3,4,5]の要素を逆順にした新しいリストを作成する
stack2 = Stack()

list_before = [1,2,3,4,5]
for i in list_before:
    stack2.push(i)

list_after = []
while stack2.size():
    list_after.append(stack2.pop())

print(list_before)
print(list_after)