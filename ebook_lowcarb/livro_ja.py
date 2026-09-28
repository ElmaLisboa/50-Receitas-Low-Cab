# -*- coding: utf-8 -*-
"""日本語版：毎日のロカボレシピ50。"""
import html as H
import re
import livro as pt
import livro_en as layout
from ja_overrides import OVERRIDES

NAMES = [
 "ほうれん草とチーズのオーブンオムレツ", "2分で作れるロカボ電子レンジパン", "バナナとオートミールのパンケーキ（小麦粉なし）",
 "卵・野菜・ベーコンの塩味マフィン", "チーズとトマトのタピオカクレープ", "フライパンで作るチーズパン",
 "クリーミーチキンのコラードラップ", "アボカドと種のクリーミースクランブルエッグ", "プロテインヨーグルトとナッツグラノーラ",
 "シンプルなカリフラワーライス", "ズッキーニ麺の自家製トマトソース", "パルミット麺のガーリックオイル和え",
 "チキンとヨーグルトドレッシングの具だくさんサラダ", "ツナと卵のレモンマヨネーズサラダ", "スパイシー牛ひき肉のレタスラップ",
 "ほぐし干し肉のカリフラワーシェパーズパイ", "なすのボロネーゼラザニア", "牛ひき肉詰めなす",
 "ロカボ青菜スープ（じゃがいもなし）", "ココナッツミルクとかぼちゃのしょうがスープ", "ほぐし鶏肉の野菜スープ",
 "クリームチーズ入りズッキーニポタージュ", "鶏肉のマスタードクリームソース", "レモンとローズマリーのローストチキン",
 "ロカボチキン炒め", "きのこソースのステーキ", "牛ひき肉とズッキーニのトマト煮",
 "オニオンステーキとガーリックバター", "チーズ入りミートボールのトマトソース", "ほぐし豚スペアリブ",
 "サーモンのレモンバター焼き", "アーモンド衣のティラピア", "ガーリックシュリンプ", "タラとカリフラワーのオリーブ煮",
 "ココナッツミルクとパルミットの魚のムケカ", "レモンハーブのグリルいか",
 "カリフラワークラストのモッツァレラピザ", "なすのパルミジャーナ（パン粉なし）", "ロカボフェイジョアーダ（豆なし）",
 "エアフライヤーのチーズパン", "ツナとクリームチーズのズッキーニ詰め", "ロカボ寿司（きゅうりロール）",
 "牛ひき肉のキャベツロール", "チョコレートアボカドムース", "エリスリトールのココナッツフラン",
 "スプーンで食べるロカボチョコクリーム", "ベリーのロカボチーズケーキ", "ナッツとチョコレートのロカボクッキー",
 "ココナッツオイルのチョコレートトリュフ", "ロカボピーナッツ菓子（パソッカ風）"
]

CAT = {
 "Café da manhã e lanches rápidos": ("朝食と簡単スナック", "いつものパンに頼らず、手軽で満足感のあるレシピで一日を始めましょう。卵、チーズ、アーモンド粉やココナッツ粉、果物をバランスよく使います。ほとんどが実際の作業時間15分以内です。"),
 "Almoços completos": ("満足感のあるランチ", "一つの鍋で作れる料理、午後までお腹を支えるサラダ、そしてごはんやパスタの賢い代替品。ダイエット食とは思えない味に仕上がります。"),
 "Sopas e caldos": ("スープとブロス", "寒い夜や持ち運び用に。じゃがいもや小麦粉を使わず、クリーミーな味わいを楽しめます。"),
 "Carnes e aves": ("肉と鶏肉", "ロカボ料理の土台となるたんぱく質。香ばしく、ジューシーで、本格的なソースと合わせます。"),
 "Peixes e frutos do mar": ("魚介料理", "日曜日のサーモンから平日の魚介料理まで。良質な脂質、短い調理時間、レストランのような味わいです。"),
 "Jantares em até 30 minutos de bancada": ("30分で作る夕食", "夜のルールは、番組が終わる前に夕食を完成させること。一つのフライパン、オーブン、エアフライヤーで作れます。"),
 "Sobremesas sem açúcar": ("砂糖なしのデザート", "本格的なデザートに精製糖は必要ありません。カカオ、ココナッツ、ナッツ、甘味料で味わいを作ります。"),
}

PHRASES = [("pimenta-do-reino", "黒こしょう"), ("cheiro-verde", "刻みハーブ"), ("couve manteiga", "コラードグリーン"),
 ("couve-flor", "カリフラワー"), ("couve", "ケール"), ("abobrinha", "ズッキーニ"), ("berinjela", "なす"),
 ("palmito pupunha", "パルミット"), ("palmito", "パルミット"), ("tomate pelado", "ホールトマト"),
 ("creme de leite fresco", "生クリーム"), ("creme de leite", "生クリーム"), ("cream cheese", "クリームチーズ"),
 ("requeijão", "クリームチーズ"), ("muçarela", "モッツァレラ"), ("queijo parmesão", "パルメザンチーズ"), ("queijo", "チーズ"),
 ("farinha de amêndoas", "アーモンドプードル"), ("farinha de coco", "ココナッツフラワー"), ("farinha de linhaça dourada", "金色の亜麻仁粉"),
 ("polvilho azedo", "サワーキャッサバスターチ"), ("goma de tapioca", "タピオカ粉"), ("leite de coco", "ココナッツミルク"),
 ("carne seca", "ほぐし干し肉"), ("carne moída", "牛ひき肉"), ("frango desfiado", "ほぐし鶏肉"), ("peito de frango", "鶏むね肉"),
 ("ovos mexidos", "スクランブルエッグ"), ("ovos cozidos", "ゆで卵"), ("ovo cozido", "ゆで卵"), ("castanha-de-caju", "カシューナッツ"),
 ("castanha do pará", "ブラジルナッツ"), ("castanhas", "ナッツ"), ("manteiga de amendoim", "ピーナッツバター"), ("pasta de amendoim", "ピーナッツバター"),
 ("amendoim", "ピーナッツ"), ("morangos", "いちご"), ("morango", "いちご"), ("abacate", "アボカド"), ("abóbora", "かぼちゃ"),
 ("pepino", "きゅうり"), ("tomate", "トマト"), ("cebola", "玉ねぎ"), ("alho", "にんにく"), ("dentes", "にんにく片"),
 ("dente", "にんにく片"), ("salsão", "セロリ"), ("vagem", "いんげん"), ("cenoura", "にんじん"), ("pimentão", "パプリカ"),
 ("cogumelos", "きのこ"), ("shimeji", "しめじ"), ("salmão", "サーモン"), ("camarão", "えび"), ("camarões", "えび"),
 ("tilápia", "ティラピア"), ("bacalhau", "タラ"), ("lula", "いか"), ("costelinha", "豚スペアリブ"), ("linguiça", "ソーセージ"),
 ("bacon", "ベーコン"), ("presunto cru", "生ハム"), ("presunto", "ハム"), ("iogurte", "ヨーグルト"), ("azeitona", "オリーブ"),
 ("azeitonas", "オリーブ"), ("azeite", "オリーブオイル"), ("vinagre de maçã", "りんご酢"), ("vinagre de vinho tinto", "赤ワインビネガー"),
 ("mostarda dijon", "ディジョンマスタード"), ("mostarda", "マスタード"), ("shoyu", "しょうゆ"), ("molho de tomate", "トマトソース"),
 ("molho", "ソース"), ("caldo de legumes", "野菜ブロス"), ("caldo de galinha", "チキンブロス"), ("caldo de carne", "ビーフブロス"),
 ("páprica defumada", "スモークパプリカ"), ("páprica", "パプリカパウダー"), ("orégano", "オレガノ"), ("manjericão", "バジル"),
 ("salsinha", "パセリ"), ("cebolinha", "青ねぎ"), ("coentro", "パクチー"), ("alecrim", "ローズマリー"), ("gengibre", "しょうが"),
 ("canela", "シナモン"), ("cacau em pó", "無糖ココアパウダー"), ("cacau", "ココア"), ("coco ralado", "ココナッツファイン"),
 ("coco em flocos", "ココナッツフレーク"), ("sementes de girassol", "ひまわりの種"), ("sementes de abóbora", "かぼちゃの種"),
 ("sementes de chia", "チアシード"), ("sementes", "種"), ("farinha", "粉"), ("açúcar", "砂糖"), ("adoçante", "甘味料"),
 ("essência", "エッセンス"), ("fermento em pó", "ベーキングパウダー"), ("em pó", "パウダー"), ("sem açúcar", "砂糖不使用"),
 ("sem farinha", "粉なし"), ("sem sementes", "種なし"), ("sem pele", "皮なし"), ("a gosto", "適量"), ("para servir", "盛り付け用"),
 ("para finalizar", "仕上げ用"), ("em cubos", "角切り"), ("em rodelas", "輪切り"), ("em fatias", "薄切り"), ("em tiras", "細切り"),
 ("picada", "みじん切り"), ("picado", "みじん切り"), ("picadas", "みじん切り"), ("picados", "みじん切り"), ("ralada", "すりおろし"),
 ("ralado", "すりおろし"), ("raladas", "すりおろし"), ("ralados", "すりおろし"), ("escorrido", "水気を切った"), ("escorrida", "水気を切った"),
 ("escorridas", "水気を切った"), ("desfiado", "ほぐした"), ("desfiada", "ほぐした"), ("desfiados", "ほぐした"), ("espremida", "水気をしぼった"),
 ("espremido", "水気をしぼった"), ("congelado", "冷凍"), ("derretida", "溶かした"), ("derretido", "溶かした"), ("cozida", "ゆでた"),
 ("cozido", "ゆでた"), ("quente", "熱い"), ("morno", "温かい"), ("crocante", "カリッとした"), ("cremoso", "クリーミーな"),
 ("cremosa", "クリーミーな"), ("xíc.", "カップ"), ("col. sopa", "大さじ"), ("col. chá", "小さじ"), ("col.", "大さじ")]

VERBS = [("Não lave", "洗わないでください"), ("Não mexa", "混ぜないでください"), ("Não deixe", "そのままにしないでください"), ("Leve ao micro-ondas", "電子レンジにかけます"),
 ("Leve ao forno", "オーブンで焼きます"), ("Leve à geladeira", "冷蔵庫で冷やします"), ("Leve ao congelador", "冷凍庫に入れます"), ("Volte à panela", "鍋に戻します"),
 ("Volte o", "戻します"), ("Refogue", "炒めます"), ("Junte", "加えます"), ("Acrescente", "加えます"), ("Bata", "混ぜます"), ("Misture", "混ぜます"),
 ("Incorpore", "混ぜ込みます"), ("Asse", "焼きます"), ("Cozinhe", "加熱します"), ("Aqueça", "温めます"), ("Despeje", "流し入れます"),
 ("Tempere", "味付けします"), ("Sirva", "盛り付けます"), ("Finalize", "仕上げます"), ("Reserve", "取り分けます"), ("Deixe", "置きます"),
 ("Corte", "切ります"), ("Retire", "取り出します"), ("Frite", "焼きます"), ("Grelhe", "グリルします"), ("Sele", "強火で焼き付けます"),
 ("Passe", "つけます"), ("Abra", "開きます"), ("Modele", "成形します"), ("Distribua", "分け入れます"), ("Cubra", "かぶせます"),
 ("Regue", "かけます"), ("Acomode", "並べます"), ("Processe", "フードプロセッサーにかけます"), ("Rale", "すりおろします"), ("Esprema", "しぼります"),
 ("Poche", "ポーチドにします"), ("Monte", "重ねます"), ("Amasse", "つぶします"), ("Doure", "きつね色にします"), ("Derreta", "溶かします"),
 ("Toste", "炒ります"), ("Salgue", "塩をします"), ("Envolva", "包みます"), ("Aperte", "押さえます"), ("Ajuste", "味を調えます"),
 ("Mantenha", "保ちます"), ("Aguarde", "待ちます"), ("Espalhe", "広げます")]

WORD_MAP=[("ovos","卵"),("ovo","卵"),("sal","塩"),("pimenta","こしょう"),("limão","レモン"),("ervas","ハーブ"),("frango","鶏肉"),("carne","肉"),("salada","サラダ"),("folhas","葉"),("folha","葉"),("suco","果汁"),("peixe","魚"),("especiarias","スパイス"),("use","使います"),("torrado","ローストした"),("barato","安価な"),("igualmente","同様に"),("pronto","完成"),("forrada","敷いた"),("papel-manteiga","クッキングシート"),("puxar","引き上げる"),("dá","与える"),("assa","焼きます"),("cor","色"),("textura","食感"),("não","ない"),("fazer","作る"),("coloque","入れます"),("grelhando","焼きながら"),("trocando","交換して"),("arroz","ごはん"),("latas","缶"),("refogado","炒めた具"),("queijos","チーズ類"),("manteiga","バター"),("fermento","ベーキングパウダー"),("natural","プレーン"),("tomilho","タイム"),("cominho","クミン"),("parmesão","パルメザン"),("maionese","マヨネーズ"),("louro","ローリエ"),("calabresa","スパイシーソーセージ"),("forma","型"),("assadeira","天板"),("versão","バージョン"),("pouco","少し"),("gordura","脂質"),("banho-maria","湯煎"),("gelado","冷たい"),
 ("minutos","分"),("minuto","分"),("pequeno","小さい"),("pequena","小さい"),("untado","油を塗った"),("untada","油を塗った"),("firmar","固まる"),("dura","持つ"),
 ("segundo","2つ目"),("mesma","同じ"),("técnica","方法"),("sabor","味"),("gosto","味"),("vez","回"),("dias","日間"),("amanhã","明日"),("mais","さらに"),("neutro","あっさり"),
 ("centro","中心"),("porção","1人分"),("atum","ツナ"),("trocando","交換して"),("leve","軽い"),("faça","作ります"),("qualquer","どんな"),("tire","取り出します"),
 ("geladeira","冷蔵庫"),("óleo","油"),("fogo","火"),("panela","フライパン"),("forno","オーブン"),("água","水"),("receita","レシピ"),("pote","容器"),("potes","容器"),
 ("depois","その後"),("ainda","まだ"),("muita","たくさんの"),("muito","とても"),("crua","生の"),("cru","生の"),("recheie","詰めます"),("rechear","詰める"),
 ("escorra","水気を切ります"),("desligue","火を止めます"),("fervente","沸騰した"),("dica","コツ"),("troque","代えます"),("caneca","マグカップ"),("duas","2つ"),("grão-de-bico","ひよこ豆")]

# レシピ本文には細かな調理語や説明語も多く含まれるため、残りの語彙を
# まとめて日本語化します。これにより、材料名だけでなく手順・コツ・代替案も
# ポルトガル語の断片を残さず読める形にします。
EXTRA_MAP=[
 ("de","の"),("para","ために"),("que","こと"),("por","で"),("até","まで"),("aos","に"),("ao","に"),("à","に"),
 ("sopa","スープ"),("sal","塩"),("alho","にんにく"),("azeite","オリーブオイル"),("cebola","玉ねぎ"),("pimenta","こしょう"),
 ("col","大さじ"),("xíc","カップ"),("chá","小さじ"),("g","g"),("ml","ml"),("kg","kg"),("minutos","分"),("minuto","分"),
 ("cozinhe","加熱します"),("cozinhar","加熱する"),("junte","加えます"),("misture","混ぜます"),("refogue","炒めます"),("refogando","炒めながら"),("refogo","炒め"),
 ("bata","混ぜます"),("bater","混ぜる"),("asse","焼きます"),("assado","焼いた"),("assa","焼きます"),("doure","焼き色をつけます"),("dourar","焼き色をつける"),("dourado","焼き色のついた"),("dourarem","焼き色がつくまで"),
 ("deixe","置きます"),("deixar","置く"),("deixando","置きながら"),("deixa","置きます"),("acrescente","加えます"),("acrescenta","加えます"),("adicione","加えます"),("adicionar","加える"),
 ("tempere","味付けします"),("tempera","味付けします"),("finalize","仕上げます"),("finalizar","仕上げる"),("sirva","盛り付けます"),("servir","盛り付ける"),("reserve","取り分けます"),("reservar","取り分ける"),
 ("corte","切ります"),("cortar","切る"),("cortadas","切った"),("cortados","切った"),("fatie","薄切りにします"),("fatiada","薄切りにした"),("fatiado","薄切りにした"),("pique","刻みます"),("picada","みじん切り"),("picado","みじん切り"),("picadas","みじん切り"),("picados","みじん切り"),
 ("ralar","すりおろす"),("rale","すりおろします"),("ralada","すりおろした"),("ralado","すりおろした"),("raladas","すりおろした"),("ralados","すりおろした"),("ralador","おろし金"),
 ("escorra","水気を切ります"),("escorrido","水気を切った"),("escorrida","水気を切った"),("escorridas","水気を切った"),("seque","水気をふきます"),("secar","水気を取る"),("seca","乾いた"),("seco","乾いた"),("secos","乾いた"),
 ("desfie","ほぐします"),("desfiar","ほぐす"),("desfiado","ほぐした"),("desfiada","ほぐした"),("desfiados","ほぐした"),("desmancha","崩れます"),("despeje","流し入れます"),("despejar","流し入れる"),
 ("aqueça","温めます"),("aquecer","温める"),("esquente","温めます"),("ferva","沸騰させます"),("ferver","沸騰させる"),("fervente","沸騰した"),("afervente","さっとゆでます"),("fermento","ベーキングパウダー"),
 ("derreta","溶かします"),("derreter","溶かす"),("derretida","溶かした"),("derretido","溶かした"),("derrete","溶けます"),("esfrie","冷まします"),("esfriar","冷ます"),("esfriar","冷ます"),("amorne","少し冷まします"),("amornar","少し冷ます"),
 ("frite","揚げ焼きにします"),("fritar","揚げ焼きにする"),("grelhe","グリルします"),("grelhar","グリルする"),("grelhando","焼きながら"),("sele","強火で焼き付けます"),("selar","焼き付ける"),("toste","炒ります"),("tostar","炒る"),("salteie","炒めます"),("salteado","炒めた"),("salteados","炒めた"),
 ("passe","つけます"),("passar","つける"),("empanar","衣をつける"),("polvilhe","振りかけます"),("polvilho","キャッサバ粉"),("regue","かけます"),("regar","かける"),("acomode","並べます"),("acomodar","並べる"),("disponha","並べます"),("distribua","分け入れます"),
 ("cubra","かぶせます"),("cobertura","トッピング"),("tampe","ふたをします"),("tampe","ふたをします"),("tampe","ふたをします"),("enrole","巻きます"),("enrolar","巻く"),("envolva","包みます"),("envolver","包む"),("dobre","折ります"),("dobrar","折る"),("feche","閉じます"),("fechada","閉じた"),("fechado","閉じた"),
 ("modele","成形します"),("modelar","成形する"),("modelada","成形した"),("modele","成形します"),("aperte","押さえます"),("apertando","押さえながら"),("amasse","つぶします"),("amassar","つぶす"),("sove","こねます"),("sovar","こねる"),
 ("processe","フードプロセッサーにかけます"),("processar","フードプロセッサーにかける"),("processada","処理した"),("processado","処理した"),("pulse","数回回します"),("pulsos","回"),("bata","混ぜます"),("batido","混ぜた"),("batida","混ぜた"),
 ("coloque","入れます"),("colocar","入れる"),("retire","取り出します"),("retirar","取り出す"),("tire","取り出します"),("tirar","取り出す"),("volte","戻します"),("voltar","戻す"),("vire","裏返します"),("virar","裏返す"),("virando","裏返しながら"),
 ("desligue","火を止めます"),("desligado","火を止めた"),("reduza","弱めます"),("reduzir","減らす"),("aumente","強めます"),("aumentar","強める"),("mantenha","保ちます"),("manter","保つ"),("aguarde","待ちます"),("espera","待ちます"),("espere","待ちます"),
 ("mistura","混ぜたもの"),("misturado","混ぜた"),("ingredientes","材料"),("recheio","具"),("recheie","詰めます"),("rechear","詰める"),("massa","生地"),("molho","ソース"),("caldo","ブロス"),("prato","料理"),("porção","1人分"),("porções","分量"),
 ("bem","しっかり"),("mais","さらに"),("menos","少なめ"),("muito","とても"),("muita","たくさんの"),("pouco","少し"),("pouca","少し"),("grande","大きい"),("grandes","大きい"),("pequeno","小さい"),("pequena","小さい"),("pequenas","小さい"),("médio","中くらい"),("média","中くらい"),("médias","中くらい"),("alto","強い"),("alta","高い"),("baixo","弱い"),("baixa","弱い"),("fundo","底"),("cima","上"),("lado","側"),("lados","両側"),("centro","中心"),("meio","中央"),("parte","部分"),("dentro","中"),("fora","外"),("sobre","上に"),("entre","間に"),("junto","一緒に"),("separado","別に"),("separados","別々に"),
 ("minutos","分"),("minuto","分"),("segundos","秒"),("segundo","秒"),("horas","時間"),("hora","時間"),("dias","日間"),("dia","日"),("meses","か月"),("vezes","回"),("vez","回"),("tempo","時間"),("quando","とき"),("depois","その後"),("antes","前に"),("ainda","まだ"),("já","すでに"),("sempre","いつも"),("nunca","決して〜ない"),("imediatamente","すぐに"),("durante","〜の間"),("primeiro","最初に"),("último","最後に"),("restante","残り"),("metade","半分"),("mínimo","最低"),
 ("firme","固い"),("firmar","固まる"),("firmarem","固まるまで"),("crocante","カリッとした"),("cremoso","クリーミーな"),("cremosa","クリーミーな"),("macia","やわらかい"),("moles","やわらかい"),("úmido","しっとりした"),("úmida","しっとりした"),("quente","熱い"),("gelada","冷たい"),("gelado","冷たい"),("morna","温かい"),("cru","生の"),("crua","生の"),("cruas","生の"),("cozido","ゆでた"),("cozida","ゆでた"),("cozidos","ゆでた"),("congelado","冷凍した"),("congeladas","冷凍した"),("fresco","新鮮な"),("fresca","新鮮な"),("maduro","熟した"),("maduros","熟した"),("muito","とても"),("natural","プレーン"),("opcional","お好みで"),
 ("sabor","味"),("gosto","味"),("cor","色"),("textura","食感"),("ponto","状態"),("segredo","コツ"),("técnica","方法"),("jeito","方法"),("necessário","必要"),("obrigatório","必須"),("cuidado","注意"),("atenção","注意"),("caso","場合"),("versão","バージョン"),("base","ベース"),("neutra","プレーンな"),("principal","メイン"),("completo","満足感のある"),("completa","満足感のある"),("curinga","万能"),("característico","特徴的な"),("tradicional","伝統的な"),("caseiro","手作りの"),("caseira","手作りの"),("sofisticada","上品な"),("barato","安価な"),("igualmente","同様に"),
 ("fazer","作る"),("faça","作ります"),("faz","します"),("fica","なります"),("ficar","なる"),("ficarem","なるまで"),("é","です"),("está","です"),("estar","いる"),("tem","あります"),("ter","持つ"),("pode","できます"),("poder","できる"),("deve","必要があります"),("ser","である"),("dá","与えます"),("dão","与えます"),("dar","与える"),("parece","見えます"),("parecer","見える"),("precisa","必要です"),("precisar","必要とする"),("evita","防ぎます"),("impede","防ぎます"),("aceita","合います"),("resolve","解決します"),("engana","ごまかします"),
 ("não","ない"),("nem","も〜ない"),("mas","ただし"),("só","だけ"),("como","ように"),("isso","これ"),("ela","それ"),("ele","それ"),("eles","それら"),("todos","すべて"),("toda","すべての"),("outros","他の"),("mesma","同じ"),("mesmos","同じ"),("qualquer","どんな"),("cada","各"),("duas","2つの"),("dois","2つの"),("uma","1つの"),("um","1つの"),
 ("pão","パン"),("arroz","ごはん"),("massa","生地"),("aveia","オートミール"),("farelo","ふすま"),("banana","バナナ"),("maçã","りんご"),("morangos","いちご"),("frutas","果物"),("abacate","アボカド"),("amendoim","ピーナッツ"),("castanhas","ナッツ"),("amêndoa","アーモンド"),("amêndoas","アーモンド"),("caju","カシューナッツ"),("pará","ブラジルナッツ"),("chocolate","チョコレート"),("cacau","ココア"),("açúcar","砂糖"),("adoçante","甘味料"),("adoçantes","甘味料"),("baunilha","バニラ"),("mel","はちみつ"),("café","朝食"),
 ("frango","鶏肉"),("peito","むね肉"),("sobrecoxas","鶏もも肉"),("carne","肉"),("carnes","肉類"),("moída","ひき肉"),("bifes","ステーキ"),("bife","ステーキ"),("filé","フィレ"),("filés","フィレ"),("alcatra","ランプ肉"),("contrafilé","サーロイン"),("patinho","赤身ひき肉"),("acém","肩肉"),("porco","豚肉"),("costelinha","スペアリブ"),("copa-lombo","豚肩ロース"),("bacon","ベーコン"),("linguiça","ソーセージ"),("calabresa","チョリソー"),("presunto","ハム"),("galinha","鶏"),("peixe","魚"),("peixes","魚"),("salmão","サーモン"),("camarão","えび"),("camarões","えび"),("bacalhau","タラ"),("tilápia","ティラピア"),("lula","いか"),("polvo","たこ"),("pescada","白身魚"),("badejo","ハタ"),("robalo","スズキ"),("atum","ツナ"),("sardinha","いわし"),("kani","かにかま"),
 ("couve","ケール"),("folhas","葉"),("folha","葉"),("espinafre","ほうれん草"),("alface","レタス"),("repolho","キャベツ"),("acelga","スイスチャード"),("salsão","セロリ"),("legumes","野菜"),("cenoura","にんじん"),("abobrinha","ズッキーニ"),("abobrinhas","ズッキーニ"),("berinjela","なす"),("berinjelas","なす"),("abóbora","かぼちゃ"),("cabotiá","かぼちゃ"),("pimentão","パプリカ"),("pimentões","パプリカ"),("tomate","トマト"),("tomates","トマト"),("cebola","玉ねぎ"),("alho","にんにく"),("dentes","にんにく片"),("dente","にんにく片"),("pepino","きゅうり"),("vagem","いんげん"),("cogumelos","きのこ"),("palmito","パルミット"),("pupunha","パルミット"),("couve-flor","カリフラワー"),("azeitonas","オリーブ"),("azeitona","オリーブ"),("olivas","オリーブ"),
 ("ervas","ハーブ"),("salsinha","パセリ"),("salsa","パセリ"),("cebolinha","青ねぎ"),("coentro","パクチー"),("manjericão","バジル"),("alecrim","ローズマリー"),("tomilho","タイム"),("gengibre","しょうが"),("orégano","オレガノ"),("cominho","クミン"),("louro","ローリエ"),("canela","シナモン"),("noz-moscada","ナツメグ"),("páprica","パプリカ"),("mostarda","マスタード"),("shoyu","しょうゆ"),("vinagre","酢"),("dendê","デンデ油"),("sal","塩"),("pimenta-do-reino","黒こしょう"),("pimenta-branca","白こしょう"),("temperos","調味料"),("especiarias","スパイス"),("cheiro-verde","刻みハーブ"),
 ("queijo","チーズ"),("queijos","チーズ類"),("muçarela","モッツァレラ"),("parmesão","パルメザン"),("requeijão","クリームチーズ"),("cream","クリーム"),("leite","ミルク"),("creme","クリーム"),("iogurte","ヨーグルト"),("manteiga","バター"),("óleo","油"),("coco","ココナッツ"),("polpa","果肉"),("sementes","種"),("flocos","フレーク"),("linhaça","亜麻仁"),("chia","チアシード"),("gordura","脂質"),("carbo","糖質"),("carbos","糖質"),("proteína","たんぱく質"),("sódio","ナトリウム"),
 ("papel-toalha","キッチンペーパー"),("papel-manteiga","クッキングシート"),("papel-alumínio","アルミホイル"),("assadeira","天板"),("refratário","耐熱皿"),("frigideira","フライパン"),("panela","鍋"),("liquidificador","ミキサー"),("espátula","ヘラ"),("garfo","フォーク"),("ralador","おろし金"),("descascador","ピーラー"),("espiralizador","スパイラライザー"),("escorredor","ざる"),("forminhas","小さな型"),("marmita","弁当"),("pote","容器"),("potes","容器"),("saco","袋"),("torradeira","トースター"),("micro-ondas","電子レンジ"),("forno","オーブン"),("geladeira","冷蔵庫"),("congelador","冷凍庫"),("airfryer","エアフライヤー"),("banho-maria","湯煎"),
 ("quadrado","四角い"),("bolinhas","小さな粒"),("grumos","ダマ"),("fatias","薄切り"),("rodelas","輪切り"),("tiras","細切り"),("cubos","角切り"),("anéis","輪切り"),("buquês","小房"),("lascas","薄片"),("fios","細切り"),("conchas","スプーン1杯"),("pitada","ひとつまみ"),("raspas","皮のすりおろし"),("casca","皮"),("pele","皮"),("espinhas","骨"),("caroço","種"),("grãos","粒"),("grão-de-bico","ひよこ豆"),
 ("saco","袋"),("vidro","瓶"),("lata","缶"),("latas","缶"),("tampado","ふたをした"),("tampa","ふた"),("superfície","表面"),("bordas","縁"),("laterais","側面"),("parede","壁"),("aro","型の側面"),("fresta","隙間"),("frestas","隙間"),("camadas","層"),("base","土台"),("cobertura","トッピング"),("recheio","具"),
 ("suficiente","十分"),("necessário","必要"),("opcional","お好みで"),("a gosto","適量"),("pronto","完成"),("pronta","完成"),("barato","安い"),("igual","同じ"),("igualmente","同様に"),("limpo","きれいな"),("branco","白い"),("branca","白い"),("verde","緑の"),("verde-viva","鮮やかな緑"),("vermelho","赤い"),("vermelhas","赤い"),("roxa","紫の"),("amarela","黄色い"),("escuro","濃い"),("marrom","茶色"),("dourado","黄金色の"),("rosa","ピンク"),("arenoso","砂状の"),("pastosa","ペースト状の"),("borrachudo","ゴムのような"),("aveludado","なめらかな"),
 ("manteiga","バター"),("fermento","ベーキングパウダー"),("natural","プレーン"),("tomilho","タイム"),("cominho","クミン"),("parmesão","パルメザン"),("maionese","マヨネーズ"),("louro","ローリエ"),("calabresa","チョリソー"),("forma","型"),("versão","バージョン"),("pouco","少し"),("gordura","脂質"),("gelado","冷たい"),("espinafre","ほうれん草"),("marmita","弁当"),
]

EXTRA_MAP2=[
 ("eritritol","エリスリトール"),("xilitol","キシリトール"),("finas","細い"),("fina","細い"),("mexendo","混ぜながら"),("vira","裏返します"),("purê","ピューレ"),("congele","冷凍します"),("Congele","冷凍します"),("solta","出ます"),("soltam","出ます"),("tudo","すべて"),("azedo","酸味のある"),("curtos","短い"),("grosso","粗い"),("refogada","炒めた"),("vapor","蒸気"),("liso","なめらか"),("fio","糸状"),("se","もし"),("mãos","手"),("mão","手"),("doce","甘い"),("wrap","ラップ"),("charuto","ロール"),("demais","〜すぎる"),("mexer","混ぜる"),("mexa","混ぜます"),("queimar","焦がす"),("queima","焦げます"),("amaciar","柔らかくする"),("amacia","柔らかくします"),("cozinha","キッチン"),("mesmo","同じ"),("diluído","薄めた"),("postas","切り身"),("comum","普通の"),("direto","直接"),("lâminas","薄片"),("Guarde","保存します"),("guarde","保存します"),("bolhas","粒"),("resseca","乾きます"),("antiaderente","こびりつかない"),("molhada","濡れた"),("choque","ショック"),("térmico","温度の"),("cozimento","加熱"),("granola","グラノーラ"),("castanha","ナッツ"),("papel","紙"),("konjac","こんにゃく"),("laminados","薄切り"),("laminado","薄切り"),("some","なくなります"),("variadas","さまざまな"),("recheando","詰めながら"),("excesso","過剰"),("ralo","薄い"),("gratinar","グラタンにする"),("enxágue","すすぎます"),("entra","入ります"),("final","最後"),("estiver","〜なら"),("perfil","特徴"),("pedaço","ひとかけ"),("sobrepor","重ねる"),("assim","このように"),("nos","その中に"),("descansar","休ませる"),("sair","出る"),("colher","スプーン"),("amido","でんぷん"),("formar","作る"),("pressão","圧力"),("soltar","外す"),("Dessalgue","塩抜きします"),("salgadas","塩味の"),("firma","固まります"),("pizza","ピザ"),("paio","ソーセージ"),("laranja","オレンジ"),("lá","そこ"),("gergelim","ごま"),("wasabi","わさび"),("crus","生の"),("completamente","完全に"),("chantilly","ホイップクリーム"),("cheesecake","チーズケーキ"),("temperatura","温度"),("ambiente","室温"),("manhã","朝"),("bom","良い"),("você","あなた"),("untar","油を塗る"),("sumirem","なくなるまで"),("potência","出力"),("Desenforme","型から外します"),("pintada","色づいた"),("adoça","甘くします"),("madura","熟した"),("aparecerem","現れるまで"),("zip","ジッパー付き"),("reaqueça","温め直します"),("saturada","飽和した"),("muffin","マフィン"),("crepioca","クレピオカ"),("racha","割れます"),("rasa","すり切り"),("tapioca","タピオカ"),("homogêneo","均一な"),("puxa-puxa","伸びる食感"),("catupiry","カトゥピリ"),("desmontar","崩れる"),("dobrando","折りながら"),("calor","熱"),("termina","仕上げます"),("espuma","泡"),("Arraste","引き寄せます"),("repetindo","繰り返しながら"),("perto","近く"),("telefone","電話"),("amarga","苦くなります"),("Granola","グラノーラ"),("lote","まとめて"),("triplique","3倍にします"),("guarde","保存します"),("integral","全粒"),("mix","ミックス"),("tigela","ボウル"),("Adoce","甘味を加えます"),("paladar","味覚"),("papa","ペースト"),("guarda","保存できます"),("sobra","残り物"),("tamanho","大きさ"),("senão","そうでなければ"),("espiralizada","スパイラル状にした"),("corta","切ります"),("afina","薄くします"),("encorpar","とろみをつける"),("rapidamente","手早く"),("aguado","水っぽい"),("espaguete","スパゲッティ"),("evaporar","蒸発させる"),("murcha","しんなりします"),("grelhado","焼いた"),("gomos","くし形"),("tigelas","ボウル"),("comer","食べる"),("crocância","歯ごたえ"),("delicadamente","やさしく"),("rasga","破れます"),("americana","アメリカ風"),("inteiras","丸ごとの"),("quebrando","割りながら"),("líquido","液体"),("dessalgada","塩抜きした"),("lasanha","ラザニア"),("terminando","仕上げながら"),("cascas","皮"),("queimada","焦げた"),("metades","半分"),("embutido","加工肉"),("portuguesa","ポルトガル風"),("maço","束"),("nessa","この"),("amolecer","柔らかくする"),("controle","調整"),("fase","段階"),("indução","IH"),("curry","カレー"),("thai","タイ風"),("ordem","順番"),("dureza","固さ"),("jantar","夕食"),("planejamento","計画"),("devolva","戻します"),("talhar","分離する"),("separar","分ける"),("torresmo","豚皮チップ"),("crouton","クルトン"),("dijon","ディジョン"),("equilibrar","整える"),("acidez","酸味"),("engrossar","とろみをつける"),("banhe","かけます"),("próprio","それ自体の"),("últimos","最後の"),("acompanhamento","付け合わせ"),("ramos","枝"),("amassados","つぶした"),("marinada","マリネ液"),("outro","別の"),("transparente","透明な"),("conte","数えます"),("torrada","トースト"),("milho","とうもろこし"),("levas","回分"),("continuar","続ける"),("amontoe","積み重ねます"),("cozinham","加熱されます"),("altos","高い"),("mignon","ミニョン"),("paris","パリ風"),("começo","最初"),("cria","作ります"),("primeiros","最初の"),("crosta","焼き皮"),("salgado","塩味の"),("caramelizar","キャラメル化する"),("almôndega","ミートボール"),("aberta","開いた"),("vazando","漏れながら"),("substituída","置き換えた"),("palma","手のひら"),("cubo","立方体"),("almôndegas","ミートボール"),("Temperatura","温度"),("longo","長い"),("desfia","ほぐれます"),("esfregue","すり込みます"),("marinar","マリネする"),("ideal","理想的"),("garfos","フォーク"),("pressionado","押さえた"),("intenso","強い"),("endro","ディル"),("opacar","くすませる"),("cara","面"),("aderir","付着する"),("passou","過ぎた"),("disso","これより"),("rosar","ピンク色にする"),("vinho","ワイン"),("rosados","ピンク色の"),("dessalgado","塩抜きした"),("pretas","黒い"),("mantendo","保ちながら"),("moqueca","ムケカ"),("balançar","揺する"),("larga","幅広い"),("janelas","窓"),("elas","それら"),("borracha","ゴム"),("pré","事前に"),("apenas","だけ"),("grelha","グリル"),("quase","ほぼ"),("fumegando","煙が出るまで"),("Espremer","しぼる"),("inegociável","必須"),("discos","円形"),("pré-assados","先に焼いた"),("pano","布"),("disco","円形"),("fino","薄い"),("montar","組み立てる"),("esponjosa","ふんわりした"),("absorve","吸収します"),("todo","すべて"),("camada","層"),("único","一つの"),("Prepare","準備します"),("cozinhando","加熱しながら"),("substitui","置き換えます"),("feijão","豆"),("expressa","簡単な"),("costela","リブ"),("acompanhar","添える"),("pedaços","かけら"),("interior","内側"),("elástico","弾力のある"),("somando","加えながら"),("untadas","油を塗った"),("cesta","バスケット"),("encostar","触れさせる"),("outra","別の"),("vem","来ます"),("miolo","中身"),("canoas","ボート形"),("rolinho","ロール"),("japonês","日本風"),("longas","長い"),("mandolina","マンドリン"),("talo","茎"),("faca","ナイフ"),("fecha","閉じます"),("rasgar","破る"),("charutos","ロール"),("hortelã","ミント"),("inteiro","丸ごと"),("separe","分けます"),("vegetal","野菜"),("fruta","果物"),("três","3"),("etapas","段階"),("pudim","プリン"),("mexido","混ぜた"),("Caramelize","キャラメル化します"),("imitar","再現する"),("caramelo","キャラメル"),("tradicional","伝統的な"),("desenformar","型から外す"),("brilho","つや"),("triturada","砕いた"),("vermelhas","赤い"),("congeladas","冷凍した"),("forre","敷きます"),("removível","取り外し可能な"),("tremer","揺れる"),("levemente","軽く"),("aquecidas","温めた"),("Esfriar","冷ます"),("rachadura","ひび"),("vilão","原因"),("cruzado","交差した"),("puxar","引き上げる"),("achatadas","平たくした"),("dourarem","焼き色がつくまで"),("saem","出ます"),("endurecem","固まります"),("achando","思いながら"),("estão","です"),("congele","冷凍します"),("gotas","滴"),("brilhante","つやのある"),("suficiente","十分"),("pare","止めます"),("paçoca","パソッカ"),("local","場所"),("farofa","炒った粉"),("pasta","ペースト"),("forrado","敷いた"),("quadrados","四角形"),("separe","分けます"),("cubra","かぶせます"),("IH","電磁調理器"),("parar","止める"),("desgruda","はがれます"),("inclinar","傾ける"),("transfira","移します"),("trufa","トリュフ"),("perde","失います"),
]

def translate_text(value,steps=False):
 s=str(value)
 for a,b in sorted(PHRASES,key=lambda x:len(x[0]),reverse=True):s=re.sub(r"(?<!\w)"+re.escape(a)+r"(?!\w)",b,s,flags=re.IGNORECASE)
 for a,b in sorted(VERBS,key=lambda x:len(x[0]),reverse=True):s=re.sub(r"^("+re.escape(a)+r")\b",b,s,flags=re.IGNORECASE)
 for a,b in [(" até "," まで "),(" com "," と "),(" sem "," なしで "),(" em "," で "),(" no "," に "),(" na "," に "),(" dos "," の "),(" das "," の "),(" do "," の "),(" da "," の "),(" e ","、"), (" ou "," または "),(" de "," の "),(" por "," で ")]:s=s.replace(a,b)
 for a,b in [("minutos em fogo baixo","弱火で分"),("fogo baixo","弱火"),("fogo alto","強火"),("fogo médio","中火"),("até ficar","まで"),("até dourar","きつね色になるまで"),("até firmar","固まるまで"),("até secar","水分がなくなるまで"),("na geladeira","冷蔵庫で"),("no forno","オーブンで"),("no micro-ondas","電子レンジで"),("no liquidificador","ミキサーで"),("com as mãos","手で"),("de um dia para o outro","一晩"),("por no mínimo","最低")]:s=s.replace(a,b)
 for a,b in sorted(VERBS,key=lambda x:len(x[0]),reverse=True):s=re.sub(r"(?<!\w)"+re.escape(a)+r"(?!\w)",b,s,flags=re.IGNORECASE)
 for a,b in sorted(WORD_MAP+EXTRA_MAP+EXTRA_MAP2,key=lambda x:len(x[0]),reverse=True):s=re.sub(r"(?<!\w)"+re.escape(a)+r"(?!\w)",b,s,flags=re.IGNORECASE)
 # ポルトガル語の冠詞・接続語を日本語の助詞に置き換えます。
 articles=[("dos","の"),("das","の"),("do","の"),("da","の"),("os","その"),("as","その"),("uma","1つの"),("duas","2つの"),("dois","2つの"),("um","1つの"),("com","と"),("sem","なしで"),("em","で"),("no","に"),("na","に"),("e","、"),("ou","または"),("o","その"),("a","その"),("de","の"),("para","ために"),("que","こと"),("por","で"),("até","まで")]
 for a,b in articles:s=re.sub(r"(?<!\w)"+re.escape(a)+r"(?!\w)",b,s,flags=re.IGNORECASE)
 if not steps:
  # 材料欄だけは数量と修飾語の順序を日本語らしく整えます。
  s=s.replace(" 大さじ の "," 大さじ ").replace(" 小さじ の "," 小さじ ").replace(" カップ の "," カップ ").replace(" g の ","g ").replace(" ml の ","ml ")
  s=re.sub(r"(\d[\d/.-]*)\s+(大さじ|小さじ|カップ)\s+",r"\2\1 ",s)
  s=re.sub(r"(\d[\d/.-]*)\s+(卵|バナナ|玉ねぎ|アボカド|きゅうり|トマト|レモン)\b",r"\2\1個",s)
  s=re.sub(r"(\d[\d/.-]*)\s+にんにく片\s+の\s+にんにく",r"にんにく\1片",s)
  s=s.replace("チーズ モッツァレラ","モッツァレラチーズ").replace("チーズ パルメザン","パルメザンチーズ").replace("チーズ クリーム","クリームチーズ")
  s=s.replace("油 の ココナッツ","ココナッツオイル").replace(" の ココナッツ"," ココナッツ")
  s=s.replace("ために 油を塗る","（型に塗る用）").replace("で 温度 室温","（室温）")
  s=s.replace("果物 赤い 冷凍した","冷凍ベリー").replace("エッセンス の バニラ","バニラエッセンス")
  s=s.replace("すりおろし","（すりおろし）").replace("みじん切り","（みじん切り）").replace("水気をしぼった","（水気をしぼった）")
 return s

PT_TO_JA={r["d"][0]:NAMES[r["num"]-1] for r in pt.RECEITAS}
RECIPES=[]
for r in pt.RECEITAS:
 d=r["d"];name,prep,total,servings,kcal,carbs,protein,fat,ingredients,steps,tip,swap=d
 override=OVERRIDES.get(r["num"])
 ja_steps,ja_tip,ja_swap=override if override else ([translate_text(x,True) for x in steps],translate_text(tip,True),translate_text(swap,True))
 RECIPES.append({"num":r["num"],"id":r["id"],"cat":CAT[r["cat"]][0],"d":(PT_TO_JA[name],prep,total,servings,kcal,carbs,protein,fat,[translate_text(x) for x in ingredients],ja_steps,ja_tip,ja_swap)})
SELECTION=[]
for cat_pt,intro_pt,names in pt.SELECAO:
 cat_ja,intro_ja=CAT[cat_pt];SELECTION.append((cat_ja,intro_ja,[PT_TO_JA[n] for n in names]))
CSS=layout.CSS.replace("50 Low-Carb Recipes for Everyday Life","毎日のロカボレシピ50")+"\nbody, p, li, td, th, .meta, .dica, .troca { font-family: 'Noto Sans CJK JP', 'Noto Sans CJK SC', sans-serif; } h1, h2, h3 { font-family: 'Noto Serif CJK JP', 'Noto Serif CJK SC', serif; } @page { margin-bottom: 6mm; } .dica { padding: 2mm 3mm; margin-top: 1.5mm; font-size: 7.7pt; } .troca { padding: 0.8mm 3mm; margin-top: 0.8mm; font-size: 7.3pt; line-height: 1.4; }"

FRONT="""
<section class="frente legal"><h2>クレジットと注意事項</h2><div class="filete"></div><p><b>毎日のロカボレシピ50</b> — 2026年 第1版。<br>実用キッチンシリーズ 第1巻。</p><p>本書の全部または一部を、書面による許可なく複製することを禁じます。本書は購入者向けのデジタル商品です。</p><div class="quadro"><b>重要なお知らせ：</b>栄養成分（カロリー、炭水化物、たんぱく質、脂質）は材料表と食品成分表から算出した<b>1人分の目安</b>です。メーカー、材料の大きさ、調理器具によって変わります。本書は教育目的であり、医師や管理栄養士の指導に代わるものではありません。糖尿病、腎疾患のある方、妊娠中・授乳中の方、継続的に薬を服用している方は、糖質を制限する前に専門家へご相談ください。キシリトールは犬に有害です。ペットの手の届かない場所に保管してください。</div><p><b>本書の単位：</b>1カップ＝240ml · 大さじ＝15ml · 小さじ＝5ml · オーブンは特に記載がない限り予熱します。</p></section>
<section class="frente"><h2>ロカボキッチンへようこそ</h2><div class="filete"></div><p>これは単なるダイエット本ではありません。食生活を続けるうえで必ず出てくる質問、<i>「今日は何を作ろう？」</i>への<b>50の答え</b>です。</p><p>ロカボは、寂しいサラダだけを食べることではありません。満足感のあるオムレツ、切り分けられるラザニア、日曜日のフェイジョアーダ、そしてチーズケーキまで。小麦粉や砂糖を、満足感のある材料に置き換えて楽しみます。</p><div class="quadro"><b>本書の基本ルール：</b>炭水化物は主役ではなくアクセント。味と色を加え、主役はたんぱく質、良質な脂質、野菜です。</div><p>7週間、毎日一つ新しいレシピを作れば、忙しい月曜日も乗り切れるレパートリーが身につきます。召し上がれ。</p></section>
<section class="frente"><h2>本書の使い方</h2><div class="filete"></div><p><b>1. 最後から始める。</b>買い物前に「7日間メニュー」と買い物リストを確認しましょう。</p><p><b>2. ちょうどよく多めに作る。</b>昼食と夕食の多くは2人分。残りは翌日の昼食になります。</p><p><b>3. ボックスを活用する。</b>各レシピに料理のコツと代替案があります。</p><p><b>4. 炭水化物ゼロを目指さない。</b>栄養成分は選択を助けるためのものです。</p><p><b>5. 冷凍を活用する。</b>冷凍の説明があるレシピは1人分で保存できます。</p></section>
<section class="frente"><h2>材料の代替表</h2><div class="filete"></div><p>材料を賢く置き換える方法をまとめました。</p><table><tr><th>省く材料</th><th>代わりに使うもの</th><th>ポイント</th></tr><tr><td>精製糖</td><td><b>エリスリトールまたはキシリトール</b></td><td>同量。キシリトールは少し甘め</td></tr><tr><td>小麦粉</td><td><b>アーモンドプードル＋卵1個</b></td><td>半量を使い、卵でつなぐ</td></tr><tr><td>白米</td><td><b>カリフラワーライス</b></td><td>生のまま強火で5〜6分炒める</td></tr><tr><td>パスタ</td><td><b>ズッキーニ、パルミット、こんにゃく麺</b></td><td>90秒〜3分炒める</td></tr><tr><td>じゃがいも</td><td><b>カリフラワー、かぶ、焼きラディッシュ</b></td><td>マッシュやスープに</td></tr></table><h2 style="margin-top:6mm">常備したい材料</h2><div class="lista2"><ul><li>アーモンドプードル、無糖ココナッツファイン</li><li>エリスリトール、キシリトール、100％ココア</li><li>無糖ココナッツミルク、生クリーム</li><li>オリーブオイル、ココナッツオイル、バター</li><li>卵、モッツァレラ、パルメザン、クリームチーズ</li><li>カリフラワー、ズッキーニ、なす、キャベツ、ケール</li><li>ホールトマト缶、オリーブ</li><li>鶏肉、牛ひき肉、魚、ツナ缶</li><li>ナッツ、レモン、ハーブ、スモークパプリカ</li></ul></div></section>
"""
BONUS="""
<section class="frente"><h2>ボーナス1 — 7日間メニュー</h2><div class="filete"></div><p>最初の1週間を無理なく過ごすメニューです。レシピ番号は本書の番号です。</p><table><tr><th>曜日</th><th>朝食</th><th>昼食</th><th>間食</th><th>夕食</th></tr><tr><td class="dia">月</td><td>01 · オムレツ</td><td>10＋23 · カリフラワーライスと鶏肉</td><td>09 · ヨーグルト</td><td>37 · カリフラワーピザ</td></tr><tr><td class="dia">火</td><td>05 · タピオカクレープ</td><td>17 · なすのラザニア</td><td>06 · チーズパン</td><td>31 · サーモン＋44 · ムース</td></tr><tr><td class="dia">水</td><td>02 · 電子レンジパン</td><td>11 · ズッキーニ麺</td><td>45 · ココナッツフラン</td><td>35 · 魚のムケカ</td></tr><tr><td class="dia">木</td><td>07 · コラードラップ</td><td>13 · チキンサラダ</td><td>08 · アボカド卵</td><td>26 · きのこステーキ</td></tr><tr><td class="dia">金</td><td>03 · バナナパンケーキ</td><td>16 · カリフラワーシェパーズパイ</td><td>09 · ヨーグルト</td><td>33 · ガーリックシュリンプ</td></tr><tr><td class="dia">土</td><td>04 · 塩味マフィン</td><td>18 · 詰めなす</td><td>46 · チョコクリーム</td><td>42 · ロカボ寿司</td></tr><tr><td class="dia">日</td><td>06 · チーズパン</td><td>30 · ほぐし豚スペアリブ</td><td>47 · チーズケーキ</td><td>19 · 青菜スープ＋28 · ステーキ</td></tr></table></section>
<section class="frente"><h2>ボーナス2 — 1週間分の買い物リスト</h2><div class="filete"></div><p>印刷して買い物に持っていきましょう。2人分を想定しています。</p><div class="lista2"><ul class="check"><li>卵2ダース</li><li>鶏むね肉1kg＋鶏もも8本</li><li>牛ひき肉1kg＋ステーキ500g</li><li>サーモンまたは白身魚600g＋えび400g</li><li>ツナ缶2個</li><li>モッツァレラ500g＋パルメザン＋クリームチーズ</li><li>生クリーム</li><li>無糖ココナッツミルク2パック</li><li>カリフラワー、ズッキーニ、なす、キャベツ、ケール</li><li>トマト＋ホールトマト缶2個</li><li>アボカド、バナナ、いちご、レモン</li><li>玉ねぎ、にんにく、しょうが、ハーブ、パプリカ</li><li>オリーブ、パルミット、ナッツ、ピーナッツ</li><li>アーモンドプードル、ココナッツ、チアシード</li><li>エリスリトール、キシリトール、ココア、85％チョコ</li><li>オリーブオイル、バター、ココナッツオイル</li><li>しょうゆ、マスタード</li></ul></div></section>
<section class="frente"><h2>キッチンを閉じる前に</h2><div class="filete"></div><p>これで、毎日のための50レシピがそろいました。手に入りやすい材料、簡単な調理、計画的な作り置き。変化を始めるのは、<b>次の一食</b>です。</p><p>今夜作るレシピを一つ選び、誰かと一緒に味わってください。</p><div class="quadro"><b>実用キッチンの次巻：</b>第2巻 — <i>1週間分のロカボ料理</i> · 第3巻 — <i>砂糖なしのパーティーデザート</i>。</div></section>
"""
COVER="""<section class="capa"><div class="txt"><div class="kicker">実用キッチンシリーズ · 第1巻</div><h1>毎日の<br><span class="hl">ロカボレシピ50</span></h1><div class="sub">小麦粉なし、砂糖なし、無理なくおいしく</div></div><div class="faixa"><span class="marca">実用キッチン</span><span>糖質は控えめ、毎日は豊かに</span></div></section>"""
BACK="""<section class="contra"><div class="in"><h2>「また月曜日から」​​を終わらせよう。</h2><p>朝食から夕食、寒い日のスープ、砂糖なしのデザートまで。二度調理せず、毎日のロカボ生活を支える50レシピを収録しました。</p><ul><li><b>50の完全レシピ</b>：時間、分量、1人分の栄養目安付き</li><li>すべてのレシピに<b>料理のコツ</b></li><li>材料を変えられる<b>代替案</b></li><li>印刷できる<b>7日間メニューと買い物リスト</b></li><li>粉、砂糖、ごはん、パスタの<b>代替表</b></li></ul><p>手に入りやすい材料。現実的な時間。ダイエットを感じさせない味。</p><div class="marca">実用キッチン</div></div></section>"""

def recipe_html(r):
 num,rid,d=r["num"],r["id"],r["d"];name,prep,total,servings,kcal,carbs,protein,fat,ingredients,steps,tip,swap=d
 ing=''.join('<li>%s</li>'%H.escape(x) for x in ingredients);pas=''.join('<li>%s</li>'%H.escape(x) for x in steps)
 return '<section class="receita" id="%s"><header><div class="num">%02d</div><div class="titulo"><h3>%s</h3></div></header><img class="foto" src="imagens/receita-%02d.jpg" alt="%s"><div class="meta"><span><b>調理時間</b> %d分</span><span><b>合計</b> %d分</span><span><b>分量</b> %s</span><span><b>難易度</b> 簡単</span></div><div class="nutris"><span><b>%d</b>kcal / 1人分</span><span><b>%d g</b>炭水化物</span><span><b>%d g</b>たんぱく質</span><span><b>%d g</b>脂質</span></div><div class="corpo"><div><h4>材料</h4><ul class="ing">%s</ul></div><div><h4>作り方</h4><ol class="passos">%s</ol></div></div><div class="dica"><b>料理のコツ：</b> %s</div><div class="troca"><b>↺ 代替アイデア：</b> %s</div></section>'%(rid,num,H.escape(name),num,H.escape(name),prep,total,H.escape(str(servings)),kcal,carbs,protein,fat,ing,pas,H.escape(tip),H.escape(swap))

def toc_html(pmap=None):
 out=['<section class="frente"><h2>目次</h2><div class="filete"></div><div class="sum"><table>'];idx=0
 for cat,intro,names in SELECTION:
  out.append('<tr><td class="cat" colspan="4">%s</td></tr>'%H.escape(cat))
  for name in names:
   idx+=1;pg=str(pmap[idx]) if pmap else '';out.append('<tr><td class="num">%02d</td><td><a href="#r%02d">%s</a></td><td class="dots"></td><td class="pg">%s</td></tr>'%(idx,idx,H.escape(name),pg))
 out.append('</table></div></section>');return ''.join(out)

def body_html():
 out=[]
 for chapter,(cat,intro,names) in enumerate(SELECTION,1):
  out.append('<section class="abre"><img class="capfoto" src="imagens/capitulo-%02d.jpg" alt="%sの章の画像"><div class="tag">第%02d章</div><h2>%s</h2><div class="filete"></div><p>%s</p></section>'%(chapter,H.escape(cat),chapter,H.escape(cat),H.escape(intro)))
  for r in RECIPES:
   if r["cat"]==cat:out.append(recipe_html(r))
 return ''.join(out)

def render(pmap=None):return "<!DOCTYPE html><html lang='ja'><head><meta charset='utf-8'><style>%s</style></head><body>%s%s%s%s%s%s</body></html>"%(CSS,COVER,FRONT,toc_html(pmap),body_html(),BONUS,BACK)

def build():
 from weasyprint import HTML
 import fitz
 open('ebook_ja_probe.html','w').write(render(None));HTML(filename='ebook_ja_probe.html').write_pdf('ebook_ja_probe.pdf')
 d=fitz.open('ebook_ja_probe.pdf');pmap={}
 for i in range(d.page_count):
  text=d[i].get_text();norm=text.replace(' ','')
  if '材料' in norm and '作り方' in norm:
   m=re.search(r'(?m)^(\d{2})\n',text)
   if m and 1<=int(m.group(1))<=50:pmap[int(m.group(1))]=i+1
 assert len(pmap)==50,(len(pmap),sorted(set(range(1,51))-set(pmap)))
 open('50-ロカボレシピ-ja.html','w').write(render(pmap));HTML(filename='50-ロカボレシピ-ja.html').write_pdf('50-ロカボレシピ-ja.pdf')
 print('日本語PDFを作成しました：',len(pmap),'レシピ')

if __name__=='__main__':build()
