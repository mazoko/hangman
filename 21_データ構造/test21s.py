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

# インスタンス生成
stack = Stack()
# 空リスト判定
print(stack.is_empty())

# アイテム追加
stack.push("item1")
# 空リスト判定
print(stack.is_empty())

# アイテムを取得、削除
item = stack.pop()
print(item)
print(stack.is_empty())

#for i in range(1, 6):
#    stack.push(i)

# リスト末尾のアイテムを確認
#print(stack.peek())
# リストの長さを確認
#print(stack.size())

# 「Hello」を逆順にする
for i in "Hello":
    stack.push(i)

reverse = ""
while stack.size():
    reverse += stack.pop()

print(reverse)