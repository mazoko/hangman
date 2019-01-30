# (5)リストに含まれる数字の組み合わせで掛け算
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
listAns = []

for item1 in list1:
    for item2 in list2:
        listAns.append(item1 * item2)

# 要素数が16になるはず
print(listAns)