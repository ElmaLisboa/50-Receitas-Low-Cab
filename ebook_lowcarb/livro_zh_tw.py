# -*- coding: utf-8 -*-
"""繁體中文版：每日低碳食譜50。"""
import html as H
import re
import livro as pt
import livro_en as layout
from zh_tw_overrides import OVERRIDES

NAMES=[
 "菠菜芝士烤蛋餅", "2分鐘微波爐低碳麵包", "香蕉燕麥煎餅（無麵粉）", "雞蛋蔬菜培根鹹瑪芬", "芝士番茄木薯薄餅", "平底鍋芝士麵包",
 "奶油雞肉羽衣甘藍卷", "牛油果種子奶油炒蛋", "高蛋白酸奶堅果燕麥脆", "簡易菜花米", "自制番茄醬西葫蘆面", "蒜香油炒棕櫚心面",
 "酸奶醬雞肉全營養沙拉", "金槍魚雞蛋檸檬蛋黃醬沙拉", "香辣牛肉生菜卷", "幹牛肉菜花焗烤", "博洛涅塞茄子千層麵", "牛肉末填茄子",
 "低碳綠湯（無土豆）", "椰奶姜香南瓜湯", "手撕雞蔬菜湯", "奶油乳酪西葫蘆濃湯", "芥末奶油醬烤雞", "檸檬迷迭香烤雞腿",
 "低碳炒雞肉", "蘑菇醬牛排", "番茄西葫蘆牛肉末", "洋蔥黃油牛排", "芝士夾心肉丸番茄醬", "手撕豬肋排",
 "檸檬黃油烤三文魚", "杏仁粉脆皮羅非魚", "蒜香蝦仁", "橄欖菜花鱈魚", "椰奶棕櫚心魚肉燉鍋", "檸檬香草烤魷魚",
 "馬蘇裡拉羅勒菜花披薩", "無麵包糠茄子帕瑪森", "低碳巴西黑豆燉肉（無豆）", "空氣炸鍋芝士麵包", "金槍魚奶油乳酪填西葫蘆", "低碳黃瓜壽司卷",
 "牛肉捲心菜卷", "牛油果巧克力慕斯", "赤蘚糖醇椰香布丁", "低碳勺吃巧克力奶油", "低碳莓果芝士蛋糕", "堅果巧克力低碳餅乾",
 "椰子油巧克力松露", "低碳花生糖（巴西花生糖風味）"
]
CAT={
 "Café da manhã e lanches rápidos":("早餐與快捷小食","用實用又有飽腹感的食譜開始一天，不必依賴傳統麵包。本章結合雞蛋、乳酪、杏仁粉或椰子粉以及水果，分量均衡。大多數食譜的主動準備時間不超過15分鐘。"),
 "Almoços completos":("營養午餐","一鍋料理、能讓你整個下午保持飽腹的沙拉，以及米飯和麵條的聰明替代品——好吃得不像減脂餐。"),
 "Sopas e caldos":("湯與高湯","適合寒冷夜晚和外帶午餐：不用土豆和小麥粉，也能享受濃郁順滑的口感。"),
 "Carnes e aves":("肉類與禽類","蛋白質是優質低碳選單的基礎：焦香、多汁，搭配真正的醬汁，而不是乾柴的便當雞肉。"),
 "Peixes e frutos do mar":("魚類與海鮮","從週日三文魚到工作日的快手海鮮：優質脂肪、短時間烹調和餐廳級風味。"),
 "Jantares em até 30 minutos de bancada":("30分鐘晚餐","晚餐規則是：劇集結束前就能上桌。用一口鍋、一隻烤盤或空氣炸鍋完成。"),
 "Sobremesas sem açúcar":("無糖甜點","真正的甜點不需要精製糖：可可、椰子、堅果和不會掩蓋食材風味的代糖就夠了。"),
}
PHRASES=[
 ("pimenta-do-reino","黑胡椒"),("pimenta-branca","白胡椒"),("low carb","低碳"),("cheiro-verde","鮮香草"),("couve manteiga","羽衣甘藍"),("couve-flor","菜花"),("couve","羽衣甘藍"),("abobrinha","西葫蘆"),("berinjela","茄子"),("palmito pupunha","棕櫚心"),("palmito","棕櫚心"),("tomate pelado","去皮番茄"),
 ("creme de leite fresco","淡奶油"),("creme de leite","淡奶油"),("cream cheese","奶油乳酪"),("requeijão","奶油乳酪"),("muçarela","馬蘇裡拉乳酪"),("queijo parmesão","帕瑪森乳酪"),("queijo","乳酪"),("farinha de amêndoas","杏仁粉"),("farinha de coco","椰子粉"),("farinha de linhaça dourada","金色亞麻籽粉"),("polvilho azedo","酸味木薯澱粉"),("goma de tapioca","木薯粉"),("leite de coco","椰奶"),
 ("carne seca","幹牛肉"),("carne moída","牛肉末"),("frango desfiado","手撕雞肉"),("peito de frango","雞胸肉"),("ovos mexidos","炒蛋"),("ovos cozidos","煮雞蛋"),("ovo cozido","煮雞蛋"),("castanha-de-caju","腰果"),("castanha do pará","巴西堅果"),("castanhas","堅果"),("manteiga de amendoim","花生醬"),("pasta de amendoim","花生醬"),("amendoim","花生"),("morangos","草莓"),("morango","草莓"),("abacate","牛油果"),("abóbora","南瓜"),
 ("pepino","黃瓜"),("tomate","番茄"),("cebola","洋蔥"),("alho","大蒜"),("dentes","瓣"),("dente","瓣"),("salsão","芹菜"),("vagem","四季豆"),("cenoura","胡蘿蔔"),("pimentão","甜椒"),("cogumelos","蘑菇"),("shimeji","真姬菇"),("salmão","三文魚"),("camarão","蝦仁"),("camarões","蝦仁"),("tilápia","羅非魚"),("bacalhau","鱈魚"),("lula","魷魚"),("costelinha","豬肋排"),("linguiça","香腸"),("bacon","培根"),("presunto cru","生火腿"),("presunto","火腿"),("iogurte","酸奶"),("azeitona","橄欖"),("azeitonas","橄欖"),("azeite","橄欖油"),
 ("vinagre de maçã","蘋果醋"),("vinagre de vinho tinto","紅酒醋"),("mostarda dijon","第戎芥末"),("mostarda","芥末"),("shoyu","醬油"),("molho de tomate","番茄醬"),("molho","醬汁"),("caldo de legumes","蔬菜高湯"),("caldo de galinha","雞肉高湯"),("caldo de carne","牛肉高湯"),
 ("páprica defumada","煙燻紅椒粉"),("páprica","紅椒粉"),("orégano","牛至"),("manjericão","羅勒"),("salsinha","歐芹"),("cebolinha","蔥花"),("coentro","香菜"),("alecrim","迷迭香"),("gengibre","姜"),("canela","肉桂"),("cacau em pó","無糖可可粉"),("cacau","可可"),("coco ralado","椰蓉"),("coco em flocos","椰子片"),("sementes de girassol","葵花籽"),("sementes de abóbora","南瓜籽"),("sementes de chia","奇亞籽"),("sementes","種子"),("farinha","麵粉"),("açúcar","糖"),("adoçante","代糖"),("essência","香草精"),("fermento em pó","泡打粉"),("em pó","粉"),("sem açúcar","無糖"),("sem farinha","無麵粉"),("sem sementes","去籽"),("sem pele","去皮"),("a gosto","適量"),("para servir","食用時用"),("para finalizar","最後用"),
 ("em cubos","切丁"),("em rodelas","切片"),("em fatias","切片"),("em tiras","切絲"),("picada","切碎"),("picado","切碎"),("picadas","切碎"),("picados","切碎"),("ralada","擦碎"),("ralado","擦碎"),("raladas","擦碎"),("ralados","擦碎"),("escorrido","瀝乾"),("escorrida","瀝乾"),("escorridas","瀝乾"),("desfiado","手撕"),("desfiada","手撕"),("desfiados","手撕"),("espremida","擠幹"),("espremido","擠幹"),("congelado","冷凍"),("derretida","融化"),("derretido","融化"),("cozida","煮熟"),("cozido","煮熟"),("quente","熱的"),("morno","溫熱的"),("crocante","酥脆的"),("cremoso","奶油般的"),("cremosa","奶油般的"),("xíc.","杯"),("col. sopa","大勺"),("col. chá","小勺"),("col.","大勺")]
WORDS=[
 ("minutos","分鐘"),("minuto","分鐘"),("segundos","秒"),("segundo","秒"),("horas","小時"),("hora","小時"),("dias","天"),("dia","天"),("meses","個月"),("geladeira","冰箱"),("congelador","冷凍室"),("forno","烤箱"),("micro-ondas","微波爐"),("frigideira","平底鍋"),("panela","鍋"),("liquidificador","攪拌機"),("garfo","叉子"),("ralador","擦絲器"),("descascador","削皮器"),("espiralizador","螺旋切絲器"),("papel-toalha","廚房紙"),("papel-manteiga","烘焙紙"),("papel-alumínio","鋁箔"),("assadeira","烤盤"),("refratário","耐熱盤"),("forminhas","小模具"),("marmita","便當盒"),("pote","容器"),("potes","容器"),("saco","袋"),("torradeira","烤麵包機"),("airfryer","空氣炸鍋"),("banho-maria","隔水"),("água","水"),("óleo","油"),("fogo","火"),("pimenta","胡椒"),("sal","鹽"),("noz-moscada","肉豆蔻"),("baunilha","香草"),("eritritol","赤蘚糖醇"),("xilitol","木糖醇"),("pão","麵包"),("arroz","米飯"),("aveia","燕麥"),("farelo","麩皮"),("banana","香蕉"),("maçã","蘋果"),("chocolate","巧克力"),("mel","蜂蜜"),("massa","麵糊"),("recheio","餡料"),("ingredientes","材料"),("receita","食譜"),("prato","菜餚"),("porção","份"),("porções","份"),("dica","提示"),("versão","版本"),("fresco","新鮮"),("fresca","新鮮"),("opcional","可選"),("grande","大"),("grandes","大"),("pequeno","小"),("pequena","小"),("médio","中等"),("média","中等"),("alto","大火"),("alta","高"),("baixo","小火"),("baixa","低"),("bem","充分"),("mais","更多"),("menos","更少"),("muito","很多"),("muita","很多"),("pouco","少量"),("cada","每"),("lado","面"),("cima","上面"),("fundo","底部"),("meio","中間"),("centro","中心"),("dentro","裡面"),("fora","外面"),("antes","之前"),("depois","之後"),("ainda","仍然"),("sempre","總是"),("nunca","不要"),("tudo","全部"),("mesma","相同"),("duas","兩個"),("dois","兩個"),("uma","一份"),("um","一份"),("ou","或"),("e","和"),("com","與"),("sem","無"),("em","在"),("no","在"),("na","在"),("de","的"),("do","的"),("da","的"),("dos","的"),("das","的"),("para","用於"),("por","經過"),("até","直到"),("que","讓"),("não","不"),("mas","但是"),("se","如果"),("só","只")]
EXTRA=[
 ("manteiga","黃油"),("natural","原味"),("mix","混合堅果"),("low","低碳"),("carb","碳水"),("limão","檸檬"),("suco","檸檬汁"),("ovo","雞蛋"),("ovos","雞蛋"),("pitada","一小撮"),("lata","罐"),("latas","罐"),("parmesão","帕瑪森乳酪"),("cominho","孜然"),("folhas","葉子"),("folha","葉子"),("buquês","小朵"),("abobrinhas","西葫蘆"),("atum","金槍魚"),("berinjelas","茄子"),("calabresa","辣香腸"),("finas","薄的"),("fina","薄的"),("coco","椰子"),("frango","雞肉"),("alface","生菜"),("tomates","番茄"),("vidro","玻璃罐"),("laminados","切片"),("laminado","切片"),("variadas","混合"),("pedaço","塊"),("filés","魚片"),("filé","魚片"),("tomilho","百里香"),("raspas","皮屑"),("bifes","牛排"),("alcatra","牛臀肉"),("salsa","歐芹"),("postas","魚塊"),("processada","處理好的"),("cru","生的"),("crua","生的"),("crus","生的"),("espinafre","菠菜"),("untar","抹油"),("madura","熟的"),("maduro","熟的"),("maduros","熟的"),("fermento","泡打粉"),("rasa","平勺"),("fatias","薄片"),("rodelas","圓片"),("crepioca","木薯薄餅"),("integral","全脂"),("americana","美式"),("creme","奶油"),("azedo","酸味"),("portuguesa","葡式"),("cabotiá","慄味南瓜"),("crouton","麵包丁"),("amido","澱粉"),("altos","厚的"),("paris","蘑菇"),("batido","打散"),("limpo","清理好的"),("comum","普通"),("acompanhar","搭配"),("enrolar","捲起"),("frescas","新鮮"),("grosso","粗的"),("fatiada","切片"),("fatiado","切片"),("rechear","填餡"),("grelhado","烤好的"),("louro","月桂葉"),("caldo","高湯"),("carnes","肉類"),("cobertura","表面"),("caseiro","自制"),("caseira","自制"),("espaguete","義大利麵"),("fios","細絲"),("repolho","捲心菜"),("hortelã","薄荷"),("moqueca","巴西魚燉鍋"),("peixe","魚"),("firme","緊實"),("badejo","石斑魚"),("pescada","無須鱈"),("robalo","鱸魚"),("dendê","棕櫚油"),("anéis","圈"),("grãos","顆粒"),("inteiras","完整的"),("japonês","日式"),("gergelim","芝麻"),("gomos","瓣"),("gotas","滴"),("ramos","枝"),("maço","把"),("milho","玉米"),("laranja","橙子"),("lascas","薄片"),("pele","皮"),("refogada","炒好的"),("roxa","紫色"),("verde","綠色"),("vermelho","紅色"),("vermelhas","紅色"),("pretas","黑色"),("torrada","烤過的"),("torrado","烤過的"),("torresmo","豬皮脆片"),("endro","蒔蘿"),("ervas","香草"),("cortadas","切好的"),("congeladas","冷凍的"),("diluído","調開的"),("dessalgada","脫鹽的"),("dessalgado","脫鹽的"),("amassados","搗碎的"),("ambiente","室溫"),("temperatura","溫度"),("inteiro","整顆"),("médias","中等大小"),("sobrecoxas","雞腿"),("contrafilé","西冷牛排"),("filé-mignon","菲力牛排"),("patinho","瘦牛肉末"),("acém","牛肩肉"),("copa-lombo","豬肩肉"),("porco","豬肉"),("costela","肋排"),("paio","巴西香腸"),("maionese","蛋黃醬"),("wasabi","芥末"),("granola","堅果燕麥脆"),("cheesecake","芝士蛋糕"),("pizza","披薩"),("wrap","捲餅"),("konjac","魔芋"),("pará","巴西堅果"),("caju","腰果"),("amêndoa","杏仁"),("frutas","水果"),("massa","麵糰"),("ao","到"),("na","在"),("A","一"),("O","一"),("E","和")]

def translate_ingredient(value):
 s=str(value)
 for a,b in sorted(PHRASES,key=lambda x:len(x[0]),reverse=True):s=re.sub(r"(?<!\w)"+re.escape(a)+r"(?!\w)",b,s,flags=re.IGNORECASE)
 for a,b in sorted(WORDS+EXTRA,key=lambda x:len(x[0]),reverse=True):s=re.sub(r"(?<!\w)"+re.escape(a)+r"(?!\w)",b,s,flags=re.IGNORECASE)
 s=s.replace(" 的 "," ").replace(" 的"," ").replace("em pó","粉")
 s=re.sub(r"(\d[\d/.-]*)\s+(大勺|小勺|杯)\s+",r"\1\2 ",s)
 s=s.replace("1份 雞蛋","雞蛋1個").replace("2份 雞蛋","雞蛋2個").replace("  的 "," ")
 return s.strip()

PT_TO_ZH={r["d"][0]:NAMES[r["num"]-1] for r in pt.RECEITAS}
RECIPES=[]
for r in pt.RECEITAS:
 d=r["d"];name,prep,total,servings,kcal,carbs,protein,fat,ingredients,steps,tip,swap=d
 st,tip_z,sw=OVERRIDES[r["num"]]
 RECIPES.append({"num":r["num"],"id":r["id"],"cat":CAT[r["cat"]][0],"d":(PT_TO_ZH[name],prep,total,servings,kcal,carbs,protein,fat,[translate_ingredient(x) for x in ingredients],st,tip_z,sw)})
SELECTION=[]
for cat_pt,intro,names in pt.SELECAO:
 c,i=CAT[cat_pt];SELECTION.append((c,i,[PT_TO_ZH[n] for n in names]))
CSS=layout.CSS.replace("50 Low-Carb Recipes for Everyday Life","每日低碳食譜50")+"\nbody,p,li,td,th,.meta,.dica,.troca{font-family:'Noto Sans CJK TC','Noto Sans CJK JP',sans-serif}h1,h2,h3{font-family:'Noto Serif CJK TC','Noto Serif CJK JP',serif}@page{margin-bottom:6mm}.dica{padding:2mm 3mm;margin-top:1.5mm;font-size:7.7pt}.troca{padding:.8mm 3mm;margin-top:.8mm;font-size:7.3pt;line-height:1.4}"
FRONT="""
<section class="frente legal"><h2>版權與重要說明</h2><div class="filete"></div><p><b>每日低碳食譜50</b> — 2026年第一版。<br>實用廚房系列 · 第1冊。</p><p>版權所有。未經書面許可，不得複製本書的全部或部分內容。本電子書為面向購買者的數字產品。</p><div class="quadro"><b>重要提示：</b>營養資訊（熱量、碳水化合物、蛋白質和脂肪）是根據配料表和食物成分表計算的<b>每份估算值</b>。不同品牌、食材大小和器具會造成差異。本書僅供教育參考，不能替代醫生或註冊營養師的建議。患有糖尿病、腎臟疾病的人，孕期或哺乳期人群，以及長期服藥者，在採用限制碳水的飲食方式前應諮詢專業人士。木糖醇對狗有毒，請把甜點放在寵物接觸不到的地方。</div><p><b>本書使用的計量：</b>1杯 = 240毫升 · 1大勺 = 15毫升 · 1小勺 = 5毫升 · 除非特別說明，烤箱均需預熱。</p></section>
<section class="frente"><h2>歡迎來到低碳廚房</h2><div class="filete"></div><p>這不是一本嚴格的節食書，而是針對每天都會遇到的問題——<i>“今天做什麼吃？”</i>——準備的<b>50個實用答案</b>。</p><p>低碳生活不意味著只能吃無聊的沙拉。你可以享用奶油般的蛋餅、可以切片的千層麵、週日的燉肉，甚至芝士蛋糕，同時用更有滿足感的食材替代麵粉和糖。</p><div class="quadro"><b>本書的黃金規則：</b>碳水化合物是點綴，不是基礎。基礎永遠是蛋白質、優質脂肪和蔬菜。</div><p>連續七週每天做一道新食譜，你就會擁有能拯救忙碌星期一的料理儲備。祝你好胃口。</p></section>
<section class="frente"><h2>如何使用本書</h2><div class="filete"></div><p><b>1. 先看最後幾頁。</b>去購物前先檢視“7天選單”和購物清單。</p><p><b>2. 把合適的食譜做雙份。</b>大多數午餐和晚餐食譜是兩人份，第二份就是第二天的午餐。</p><p><b>3. 使用提示框。</b>每道食譜都有<b>烹飪提示</b>和<b>聰明替換</b>，幫助你靈活調整材料。</p><p><b>4. 不要追求零碳水。</b>營養資料是幫助選擇的工具，不應變成負擔。</p><p><b>5. 放心冷凍。</b>帶有冷凍說明的食譜適合分裝儲存。</p></section>
<section class="frente"><h2>拯救廚房的替換表</h2><div class="filete"></div><p>低碳飲食也需要聰明地替換食材：</p><table><tr><th>減少或去掉</th><th>替代材料</th><th>說明</th></tr><tr><td>精製糖</td><td><b>赤蘚糖醇或木糖醇</b></td><td>1:1；木糖醇更甜一些</td></tr><tr><td>小麥粉</td><td><b>杏仁粉＋1個雞蛋</b></td><td>用一半分量，雞蛋負責黏合</td></tr><tr><td>白米飯</td><td><b>菜花米</b></td><td>生菜花大火翻炒5至6分鐘</td></tr><tr><td>麵條</td><td><b>西葫蘆、棕櫚心或魔芋</b></td><td>翻炒90秒至3分鐘</td></tr><tr><td>土豆</td><td><b>菜花、蕪菁或烤蘿蔔</b></td><td>適合做泥和湯</td></tr></table><h2 style="margin-top:6mm">建議常備</h2><div class="lista2"><ul><li>杏仁粉和無糖椰蓉</li><li>赤蘚糖醇、木糖醇和100%可可</li><li>無糖椰奶和淡奶油</li><li>橄欖油、椰子油和黃油</li><li>雞蛋、馬蘇裡拉乳酪、帕瑪森乳酪和奶油乳酪</li><li>菜花、西葫蘆、茄子、捲心菜和羽衣甘藍</li><li>罐裝去皮番茄和橄欖</li><li>雞肉、牛肉末、魚和罐裝金槍魚</li><li>堅果、檸檬、鮮香草和煙燻紅椒粉</li></ul></div></section>
"""
BONUS="""
<section class="frente"><h2>加餐1 — 7天選單</h2><div class="filete"></div><p>適合第一週的現實計劃：有飽腹感的早餐、可以變成晚餐的午餐，以及恰到好處的甜點。</p><table><tr><th>星期</th><th>早餐</th><th>午餐</th><th>加餐</th><th>晚餐</th></tr><tr><td class="dia">一</td><td>01 · 蛋餅</td><td>10＋23 · 菜花米配雞肉</td><td>09 · 酸奶堅果脆</td><td>37 · 菜花披薩</td></tr><tr><td class="dia">二</td><td>05 · 木薯薄餅</td><td>17 · 茄子千層麵</td><td>06 · 芝士麵包</td><td>31 · 三文魚＋44 · 慕斯</td></tr><tr><td class="dia">三</td><td>02 · 微波爐麵包</td><td>11 · 西葫蘆面</td><td>45 · 椰香布丁</td><td>35 · 魚肉燉鍋</td></tr><tr><td class="dia">四</td><td>07 · 羽衣甘藍卷</td><td>13 · 雞肉沙拉</td><td>08 · 牛油果雞蛋</td><td>26 · 蘑菇牛排</td></tr><tr><td class="dia">五</td><td>03 · 香蕉煎餅</td><td>16 · 菜花焗烤</td><td>09 · 酸奶堅果脆</td><td>33 · 蒜香蝦</td></tr><tr><td class="dia">六</td><td>04 · 鹹瑪芬</td><td>18 · 填餡茄子</td><td>46 · 巧克力奶油</td><td>42 · 低碳壽司</td></tr><tr><td class="dia">日</td><td>06 · 芝士麵包</td><td>30 · 手撕豬肋排</td><td>47 · 芝士蛋糕</td><td>19 · 綠湯＋28 · 牛排</td></tr></table></section>
<section class="frente"><h2>加餐2 — 第一週購物清單</h2><div class="filete"></div><p>列印這份清單並帶去超市，分量按兩人計算：</p><div class="lista2"><ul class="check"><li>雞蛋2打</li><li>雞胸肉1公斤＋雞腿8只</li><li>牛肉末1公斤＋牛排500克</li><li>三文魚或緊實白魚600克＋蝦仁400克</li><li>金槍魚罐頭2個</li><li>馬蘇裡拉乳酪500克＋帕瑪森乳酪＋奶油乳酪</li><li>淡奶油</li><li>無糖椰奶2盒</li><li>菜花、西葫蘆、茄子、捲心菜和羽衣甘藍</li><li>新鮮番茄＋去皮番茄罐頭2個</li><li>牛油果、香蕉、草莓和檸檬</li><li>洋蔥、大蒜、姜、香草和煙燻紅椒粉</li><li>橄欖、棕櫚心、堅果和花生</li><li>杏仁粉、椰蓉和奇亞籽</li><li>赤蘚糖醇或木糖醇、可可和85%巧克力</li><li>橄欖油、黃油和椰子油</li><li>醬油和芥末</li></ul></div></section>
<section class="frente"><h2>關上廚房之前</h2><div class="filete"></div><p>現在你已經擁有50道為真實生活設計的食譜：容易買到的材料、簡單的做法和有計劃的剩菜。這個電子書與更有條理的一週之間，只差一個小決定：<b>下一頓飯吃什麼</b>。</p><p>今晚選一道食譜，動手做出來，並和別人一起分享。一起吃飯更容易堅持。</p><div class="quadro"><b>實用廚房後續書冊：</b>第2冊——<i>一週低碳餐</i> · 第3冊——<i>無糖節日甜點</i>。</div></section>
"""
COVER="""<section class="capa"><div class="txt"><div class="kicker">實用廚房系列 · 第1冊</div><h1>每日<br><span class="hl">低碳食譜50</span></h1><div class="sub">適合每一天——無麵粉、無糖，輕鬆又美味</div></div><div class="faixa"><span class="marca">實用廚房</span><span>少一點碳水，多一點生活滋味</span></div></section>"""
BACK="""<section class="contra"><div class="in"><h2>別再每個星期一重新開始。</h2><p>本書收錄50道低碳食譜，讓你不用做兩套飯也能堅持：撐過上午的早餐、可以變成晚餐的午餐、寒冷夜晚的熱湯，以及無需內疚的甜點。</p><ul><li><b>50道完整食譜</b>，包含時間、份量和每份估算營養值；</li><li>每道食譜都有<b>烹飪提示</b>；</li><li>可以靈活調整材料的<b>聰明替換</b>；</li><li><b>7天選單</b>和可列印購物清單；</li><li>麵粉、糖、米飯和麵條的<b>替換表</b>。</li></ul><p>容易買到的材料。現實的烹飪時間。不像節食餐的味道。</p><div class="marca">實用廚房</div></div></section>"""

def recipe_html(r):
 num,rid,d=r["num"],r["id"],r["d"];name,prep,total,servings,kcal,carbs,protein,fat,ingredients,steps,tip,swap=d
 ing=''.join('<li>%s</li>'%H.escape(x) for x in ingredients);pas=''.join('<li>%s</li>'%H.escape(x) for x in steps)
 return '<section class="receita" id="%s"><header><div class="num">%02d</div><div class="titulo"><h3>%s</h3></div></header><img class="foto" src="imagens/receita-%02d.jpg" alt="%s"><div class="meta"><span><b>準備</b> %d分鐘</span><span><b>總計</b> %d分鐘</span><span><b>份量</b> %s</span><span><b>難度</b> 簡單</span></div><div class="nutris"><span><b>%d</b>千卡 / 每份</span><span><b>%d克</b>碳水</span><span><b>%d克</b>蛋白質</span><span><b>%d克</b>脂肪</span></div><div class="corpo"><div><h4>材料</h4><ul class="ing">%s</ul></div><div><h4>做法</h4><ol class="passos">%s</ol></div></div><div class="dica"><b>烹飪提示：</b> %s</div><div class="troca"><b>↺ 聰明替換：</b> %s</div></section>'%(rid,num,H.escape(name),num,H.escape(name),prep,total,H.escape(str(servings)),kcal,carbs,protein,fat,ing,pas,H.escape(tip),H.escape(swap))
def toc_html(pmap=None):
 out=['<section class="frente"><h2>目錄</h2><div class="filete"></div><div class="sum"><table>'];idx=0
 for cat,intro,names in SELECTION:
  out.append('<tr><td class="cat" colspan="4">%s</td></tr>'%H.escape(cat))
  for name in names:
   idx+=1;pg=str(pmap[idx]) if pmap else '';out.append('<tr><td class="num">%02d</td><td><a href="#r%02d">%s</a></td><td class="dots"></td><td class="pg">%s</td></tr>'%(idx,idx,H.escape(name),pg))
 out.append('</table></div></section>');return ''.join(out)
def body_html():
 out=[]
 for chapter,(cat,intro,names) in enumerate(SELECTION,1):
  out.append('<section class="abre"><img class="capfoto" src="imagens/capitulo-%02d.jpg" alt="%s章節圖片"><div class="tag">第%02d章</div><h2>%s</h2><div class="filete"></div><p>%s</p></section>'%(chapter,H.escape(cat),chapter,H.escape(cat),H.escape(intro)))
  for r in RECIPES:
   if r["cat"]==cat:out.append(recipe_html(r))
 return ''.join(out)
def render(pmap=None):return "<!DOCTYPE html><html lang='zh-Hant-TW'><head><meta charset='utf-8'><style>%s</style></head><body>%s%s%s%s%s%s</body></html>"%(CSS,COVER,FRONT,toc_html(pmap),body_html(),BONUS,BACK)
def build():
 from weasyprint import HTML
 import fitz
 open('ebook_zhtw_probe.html','w').write(render(None));HTML(filename='ebook_zhtw_probe.html').write_pdf('ebook_zhtw_probe.pdf')
 d=fitz.open('ebook_zhtw_probe.pdf');pmap={}
 for i in range(d.page_count):
  text=d[i].get_text();norm=text.replace(' ','')
  if '材料' in norm and '做法' in norm:
   m=re.search(r'(?m)^(\d{2})\n',text)
   if m and 1<=int(m.group(1))<=50:pmap[int(m.group(1))]=i+1
 assert len(pmap)==50,(len(pmap),sorted(set(range(1,51))-set(pmap)))
 open('50-低碳食譜-zh-TW.html','w').write(render(pmap));HTML(filename='50-低碳食譜-zh-TW.html').write_pdf('50-低碳食譜-zh-TW.pdf')
 print('中文PDF已生成：',len(pmap),'道食譜')
if __name__=='__main__':build()
