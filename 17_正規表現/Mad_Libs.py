import re

letter = """キリンは大昔から __複数名詞__ の興味の対象でした。
キリンは __複数名詞__ の中で一番背が高いですが、
科学者たちはそのような長い __体の一部__ をどうやって獲得したのか説明できません。
キリンの身長は __数値__ __単位__ 近くあり、
その高さのほとんどは脚と __体の一部__ によるものです。
"""

def mad_libs(l):
    # 問題文を表示
    print(l)

    # __で囲まれた単語をすべて取得
    hint_list = re.findall("__.*?__", l)

    # __で囲まれた単語がある場合
    if hint_list is not None:
        for hint in hint_list:
            quest = "{0} を入力：".format(hint)
            ans = input(quest)

            # 文章内の該当箇所を答えで置換
            l = l.replace(hint, ans, 1)
            
        print("\n")

        # 文章内の改行を除去
        # l = l.replace("\n", "")

        # 文章を表示
        print(l)

    # __で囲まれた単語がない場合
    else:
        print("穴埋め箇所はありません")

mad_libs(letter)