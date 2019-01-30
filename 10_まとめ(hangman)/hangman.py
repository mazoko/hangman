import random

# ハングマン
def hangman(word):
    wrong = 0                           # 間違えた回数
    stages = [  "",                     # ステージ
                "_______      ",
                "|      |     ",
                "|      ○     ",
                "|     /|\\    ",
                "|      |     ",
                "|     / \\    ",
                "|            "]
    rletters = list(word)               # 正解ワードを一文字ずつリストに格納
    board = ["_"] * len(word)           # ボード(正解ワードの文字列分の「_」)
    win = False                         # 勝ち判定フラグ

    print("ハングマンにようこそ")

    # 間違えた回数がステージの長さより短い間ループ
    while wrong < len(stages) - 1:
        # 入力された文字をcharに格納
        char = input("\n" + "単語を1文字ずつ予想してね 入力：")

        # 正解ワードを一文字ずつ格納したリストにcharが含まれている場合
        if char in rletters:
            cind = rletters.index(char)             # charが出現するインデックスを取得
            board[cind] = char                      # ボードの該当箇所をcharに置き換え
            rletters[cind] = "$"                    # 正解ワードの該当箇所を「$」に置き換え

         # 正解ワードを一文字ずつ格納したリストにcharが含まれていない場合
        else:
            wrong += 1                              # 間違えた回数をカウントアップ
        
        print(" ".join(board))                      # ボードを表示
        e = wrong + 1
        print("\n".join(stages[0:e]))               # 間違えた回数分、ハングマンのステージを描画

        # ボードに「_」が含まれていない場合
        if "_" not in board:            
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True                              # 勝ち判定フラグを「True」に設定
            break

    # 勝ち判定フラグが「True」でない場合
    if not win:
        print("\n".join(stages[0:wrong+1]))         # 間違えた回数分、ハングマンのステージを描画
        print("あなたの負け！正解は{}".format(word))

# 正解ワードを「cat」としてハングマンを実行
# hangman("cat")

# 正解ワードを配列からランダムに取得してハングマンを実行
AMATEUR = ["cat", "dog", "egg"]
NORMAL = ["bear", "moon", "note"]
VETERAN = ["alive", "human", "night"]
PROFESSIONAL = ["answer", "bullet", "danger"]

while True:
    mode = input("モード選択！(終了：q)\nAMATEUR = a, NORMAL = n, VETERAN = v, PROFESSIONAL = p\n入力：")
    ans = ""
    strMode = ""
    
    if mode == "q":
        print("終了します")
        break
    elif mode == "a":
        ind  = random.randint(0, len(AMATEUR)-1)
        ans = AMATEUR[ind]
        strMode = "AMATEUR"
    elif mode == "n":
        ind  = random.randint(0, len(NORMAL)-1)
        ans = NORMAL[ind]
        strMode = "NORMAL"
    elif mode == "v":
        ind  = random.randint(0, len(VETERAN)-1)
        ans = VETERAN[ind]
        strMode = "VETERAN"
    elif mode == "p":
        ind  = random.randint(0, len(PROFESSIONAL)-1)
        ans = PROFESSIONAL[ind]
        strMode = "PROFESSIONAL"
    else:
        print("モード選択エラー")

    if ans != "":
        print("選択モード【" + strMode + "】")
        hangman(ans)