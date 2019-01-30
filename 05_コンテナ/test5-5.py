# (5)アーティスト辞書（キー：アーティスト名、バリュー：そのアーティストの曲(リスト))

# randomモジュールのインポート
import random

# アーティストの曲(リスト)
RingoTuneList = ["本能", "浴室", "青春の瞬き", "長く短い祭り", "至上の人生", "自由へ道連れ"]
ChihiroTuneList = ["月光", "私とワルツを", "流星群", "Beautiful Fighter"]
CoccoTuneList = ["あなたへの月", "カウントダウン", "音速パンチ", "星に願いを", "My Dear Pig", "水鏡"]
TsukikoTuneList = ["ゼロの調律", "菩提樹", "箱庭", "B.G.", "人形", "スナイパー"]

# アーティスト辞書
ArtistDic = {
    "椎名林檎":RingoTuneList, 
    "鬼束ちひろ":ChihiroTuneList, 
    "Cocco":CoccoTuneList, 
    "天野月子":TsukikoTuneList}

while True:
    inputKey = input("歌手の曲を勝手にオススメしますね！！(終了:q)\r\n(椎名林檎 or 鬼束ちひろ or Cocco or 天野月子) 入力：")

    # 未入力でない場合
    if inputKey != "":
        # 終了キーが入力された場合
        if inputKey == "q":
            print("オススメを終わりますね")
            break
        # 入力されたアーティストが存在する場合
        elif inputKey in ArtistDic:
            tuneList = ArtistDic[str(inputKey)]
            print("あなたへのオススメはこちら！【" + random.choice(tuneList) + "】\r\n")
        # 入力されたアーティストが存在しない場合
        else:
            print("知らない子ですね･･･\r\n")
    # 未入力の場合
    else:
        print("未入力ですね\r\n")