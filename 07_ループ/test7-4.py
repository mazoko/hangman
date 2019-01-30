# (4)数字当てプログラム
correctNum = [2, 3, 5, 7]

while True:
    inputItem = input("数字を当てよう！(終了:q) 入力:")
    if inputItem == "q":
        print("　終了します")
        break
    elif inputItem.isdecimal():
        if int(inputItem) in correctNum:
            print("　【あたり！】")
        else:
            print("　【はずれ…】")
    else:
        print("　数字を入力するか、qで終了します")
    
