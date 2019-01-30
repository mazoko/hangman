# (1)好きなアーティストのリスト
ArtistList = ["椎名林檎", "鬼束ちひろ", "Cocco", "天野月子"]

# (2)タプルのリスト
IttakotoAru1 = ("北海道", "141", "43")
IttakotoAru2 = ("沖縄", "127", "26")
IttakotoAru3 = ("富山", "137", "36")
IttakotoAru3 = ("兵庫", "135", "34")
IttakotoAruList = [IttakotoAru1, IttakotoAru2, IttakotoAru3, IttakotoAru3]

# (3)モテギズ辞書
MotegiDic = {"名前":"茂木静里花", "身長":"159cm", "好きな色":"青"}

# (4)モテギズ辞書から、入力されたキーに対応するバリューを表示
inputKey = input("表示する項目を選んで入力してください(名前 or 身長 or 好きな色)")
print(MotegiDic[str(inputKey)])

# (5)アーティスト辞書（キー：アーティスト名、バリュー：そのアーティストの曲(リスト))
# アーティストの曲(リスト
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

