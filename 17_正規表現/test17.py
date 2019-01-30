# 正規表現を扱うためのモジュール:regular expression
import re

# 単純な一致
l1 = "Beautiful is better than ugly."
matches1_1 = re.findall("Beautiful", l1)                    # 完全一致
matches1_2 = re.findall("beautiful", l1, re.IGNORECASE)     # IGNORECASE:大文字小文字関係なく

# 前方一致、後方一致
l2 = """Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
matches2_1 = re.findall("^If", l2, re.MULTILINE)            # MULTILINE:複数行、^:前方一致
matches2_2 = re.findall("idea.$", l2, re.MULTILINE)         # MULTILINE:複数行、.:ワイルドカード、$:後方一致

# 複数文字との一致
l3 = "Two too"
matches3_1 = re.findall("t[wo]o", l3, re.IGNORECASE)        # IGNORECASE:大文字小文字関係なく、[]:カッコ内のいずれかに一致

# 数値との一致
l4 = "123 hi 34 hello."
matches4_1 = re.findall("\d", l4, re.IGNORECASE)            # IGNORECASE:大文字小文字関係なく、\d:数値に一致

# 繰り返し1
l5 = "two twoo not too."
matches5_1 = re.findall("two*", l5)                         # *:直前のパターンを0回以上繰り返し(oを0回以上繰り返し)

# 繰り返し2
l6 = "__hello__there"
matches6_1 = re.findall("__.*__", l6)                       # *:直前のパターンを0回以上繰り返し(.を0回以上繰り返し)

# 繰り返し3
# *:一番長い文字列に一致する
l7 = "__hi__bye__hi__there"
matches7_1 = re.findall("__.*__", l7)                       # *:直前のパターンを0回以上繰り返し(.を0回以上繰り返し)

# 繰り返し4
# *?:一番短い文字列に一致する
l8 = "__one__ __two__ __three__"
matches8_1 = re.findall("__.*?__", l8)                      # *:直前のパターンを0回以上繰り返し(.を0回以上繰り返し)

# エスケープ
l9 = "I love $"
matches9_1 = re.findall("\\$", l9)                           # \\:直後のパターンを特別な文字ではなく、そのものの文字として扱う

print(matches9_1)