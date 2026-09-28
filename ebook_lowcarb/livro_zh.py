# -*- coding: utf-8 -*-
"""简体中文版：每日低碳食谱50。"""
import html as H
import re
import livro as pt
import livro_en as layout
from zh_overrides import OVERRIDES

NAMES=[
 "菠菜芝士烤蛋饼", "2分钟微波炉低碳面包", "香蕉燕麦煎饼（无面粉）", "鸡蛋蔬菜培根咸玛芬", "芝士番茄木薯薄饼", "平底锅芝士面包",
 "奶油鸡肉羽衣甘蓝卷", "牛油果种子奶油炒蛋", "高蛋白酸奶坚果燕麦脆", "简易菜花米", "自制番茄酱西葫芦面", "蒜香油炒棕榈心面",
 "酸奶酱鸡肉全营养沙拉", "金枪鱼鸡蛋柠檬蛋黄酱沙拉", "香辣牛肉生菜卷", "干牛肉菜花焗烤", "博洛涅塞茄子千层面", "牛肉末填茄子",
 "低碳绿汤（无土豆）", "椰奶姜香南瓜汤", "手撕鸡蔬菜汤", "奶油奶酪西葫芦浓汤", "芥末奶油酱烤鸡", "柠檬迷迭香烤鸡腿",
 "低碳炒鸡肉", "蘑菇酱牛排", "番茄西葫芦牛肉末", "洋葱黄油牛排", "芝士夹心肉丸番茄酱", "手撕猪肋排",
 "柠檬黄油烤三文鱼", "杏仁粉脆皮罗非鱼", "蒜香虾仁", "橄榄菜花鳕鱼", "椰奶棕榈心鱼肉炖锅", "柠檬香草烤鱿鱼",
 "马苏里拉罗勒菜花披萨", "无面包糠茄子帕玛森", "低碳巴西黑豆炖肉（无豆）", "空气炸锅芝士面包", "金枪鱼奶油奶酪填西葫芦", "低碳黄瓜寿司卷",
 "牛肉卷心菜卷", "牛油果巧克力慕斯", "赤藓糖醇椰香布丁", "低碳勺吃巧克力奶油", "低碳莓果芝士蛋糕", "坚果巧克力低碳饼干",
 "椰子油巧克力松露", "低碳花生糖（巴西花生糖风味）"
]
CAT={
 "Café da manhã e lanches rápidos":("早餐与快捷小食","用实用又有饱腹感的食谱开始一天，不必依赖传统面包。本章结合鸡蛋、奶酪、杏仁粉或椰子粉以及水果，分量均衡。大多数食谱的主动准备时间不超过15分钟。"),
 "Almoços completos":("营养午餐","一锅料理、能让你整个下午保持饱腹的沙拉，以及米饭和面条的聪明替代品——好吃得不像减脂餐。"),
 "Sopas e caldos":("汤与高汤","适合寒冷夜晚和外带午餐：不用土豆和小麦粉，也能享受浓郁顺滑的口感。"),
 "Carnes e aves":("肉类与禽类","蛋白质是优质低碳菜单的基础：焦香、多汁，搭配真正的酱汁，而不是干柴的便当鸡肉。"),
 "Peixes e frutos do mar":("鱼类与海鲜","从周日三文鱼到工作日的快手海鲜：优质脂肪、短时间烹调和餐厅级风味。"),
 "Jantares em até 30 minutos de bancada":("30分钟晚餐","晚餐规则是：剧集结束前就能上桌。用一口锅、一只烤盘或空气炸锅完成。"),
 "Sobremesas sem açúcar":("无糖甜点","真正的甜点不需要精制糖：可可、椰子、坚果和不会掩盖食材风味的代糖就够了。"),
}
PHRASES=[
 ("pimenta-do-reino","黑胡椒"),("pimenta-branca","白胡椒"),("low carb","低碳"),("cheiro-verde","鲜香草"),("couve manteiga","羽衣甘蓝"),("couve-flor","菜花"),("couve","羽衣甘蓝"),("abobrinha","西葫芦"),("berinjela","茄子"),("palmito pupunha","棕榈心"),("palmito","棕榈心"),("tomate pelado","去皮番茄"),
 ("creme de leite fresco","淡奶油"),("creme de leite","淡奶油"),("cream cheese","奶油奶酪"),("requeijão","奶油奶酪"),("muçarela","马苏里拉奶酪"),("queijo parmesão","帕玛森奶酪"),("queijo","奶酪"),("farinha de amêndoas","杏仁粉"),("farinha de coco","椰子粉"),("farinha de linhaça dourada","金色亚麻籽粉"),("polvilho azedo","酸味木薯淀粉"),("goma de tapioca","木薯粉"),("leite de coco","椰奶"),
 ("carne seca","干牛肉"),("carne moída","牛肉末"),("frango desfiado","手撕鸡肉"),("peito de frango","鸡胸肉"),("ovos mexidos","炒蛋"),("ovos cozidos","煮鸡蛋"),("ovo cozido","煮鸡蛋"),("castanha-de-caju","腰果"),("castanha do pará","巴西坚果"),("castanhas","坚果"),("manteiga de amendoim","花生酱"),("pasta de amendoim","花生酱"),("amendoim","花生"),("morangos","草莓"),("morango","草莓"),("abacate","牛油果"),("abóbora","南瓜"),
 ("pepino","黄瓜"),("tomate","番茄"),("cebola","洋葱"),("alho","大蒜"),("dentes","瓣"),("dente","瓣"),("salsão","芹菜"),("vagem","四季豆"),("cenoura","胡萝卜"),("pimentão","甜椒"),("cogumelos","蘑菇"),("shimeji","真姬菇"),("salmão","三文鱼"),("camarão","虾仁"),("camarões","虾仁"),("tilápia","罗非鱼"),("bacalhau","鳕鱼"),("lula","鱿鱼"),("costelinha","猪肋排"),("linguiça","香肠"),("bacon","培根"),("presunto cru","生火腿"),("presunto","火腿"),("iogurte","酸奶"),("azeitona","橄榄"),("azeitonas","橄榄"),("azeite","橄榄油"),
 ("vinagre de maçã","苹果醋"),("vinagre de vinho tinto","红酒醋"),("mostarda dijon","第戎芥末"),("mostarda","芥末"),("shoyu","酱油"),("molho de tomate","番茄酱"),("molho","酱汁"),("caldo de legumes","蔬菜高汤"),("caldo de galinha","鸡肉高汤"),("caldo de carne","牛肉高汤"),
 ("páprica defumada","烟熏红椒粉"),("páprica","红椒粉"),("orégano","牛至"),("manjericão","罗勒"),("salsinha","欧芹"),("cebolinha","葱花"),("coentro","香菜"),("alecrim","迷迭香"),("gengibre","姜"),("canela","肉桂"),("cacau em pó","无糖可可粉"),("cacau","可可"),("coco ralado","椰蓉"),("coco em flocos","椰子片"),("sementes de girassol","葵花籽"),("sementes de abóbora","南瓜籽"),("sementes de chia","奇亚籽"),("sementes","种子"),("farinha","面粉"),("açúcar","糖"),("adoçante","代糖"),("essência","香草精"),("fermento em pó","泡打粉"),("em pó","粉"),("sem açúcar","无糖"),("sem farinha","无面粉"),("sem sementes","去籽"),("sem pele","去皮"),("a gosto","适量"),("para servir","食用时用"),("para finalizar","最后用"),
 ("em cubos","切丁"),("em rodelas","切片"),("em fatias","切片"),("em tiras","切丝"),("picada","切碎"),("picado","切碎"),("picadas","切碎"),("picados","切碎"),("ralada","擦碎"),("ralado","擦碎"),("raladas","擦碎"),("ralados","擦碎"),("escorrido","沥干"),("escorrida","沥干"),("escorridas","沥干"),("desfiado","手撕"),("desfiada","手撕"),("desfiados","手撕"),("espremida","挤干"),("espremido","挤干"),("congelado","冷冻"),("derretida","融化"),("derretido","融化"),("cozida","煮熟"),("cozido","煮熟"),("quente","热的"),("morno","温热的"),("crocante","酥脆的"),("cremoso","奶油般的"),("cremosa","奶油般的"),("xíc.","杯"),("col. sopa","大勺"),("col. chá","小勺"),("col.","大勺")]
WORDS=[
 ("minutos","分钟"),("minuto","分钟"),("segundos","秒"),("segundo","秒"),("horas","小时"),("hora","小时"),("dias","天"),("dia","天"),("meses","个月"),("geladeira","冰箱"),("congelador","冷冻室"),("forno","烤箱"),("micro-ondas","微波炉"),("frigideira","平底锅"),("panela","锅"),("liquidificador","搅拌机"),("garfo","叉子"),("ralador","擦丝器"),("descascador","削皮器"),("espiralizador","螺旋切丝器"),("papel-toalha","厨房纸"),("papel-manteiga","烘焙纸"),("papel-alumínio","铝箔"),("assadeira","烤盘"),("refratário","耐热盘"),("forminhas","小模具"),("marmita","便当盒"),("pote","容器"),("potes","容器"),("saco","袋"),("torradeira","烤面包机"),("airfryer","空气炸锅"),("banho-maria","隔水"),("água","水"),("óleo","油"),("fogo","火"),("pimenta","胡椒"),("sal","盐"),("noz-moscada","肉豆蔻"),("baunilha","香草"),("eritritol","赤藓糖醇"),("xilitol","木糖醇"),("pão","面包"),("arroz","米饭"),("aveia","燕麦"),("farelo","麸皮"),("banana","香蕉"),("maçã","苹果"),("chocolate","巧克力"),("mel","蜂蜜"),("massa","面糊"),("recheio","馅料"),("ingredientes","材料"),("receita","食谱"),("prato","菜肴"),("porção","份"),("porções","份"),("dica","提示"),("versão","版本"),("fresco","新鲜"),("fresca","新鲜"),("opcional","可选"),("grande","大"),("grandes","大"),("pequeno","小"),("pequena","小"),("médio","中等"),("média","中等"),("alto","大火"),("alta","高"),("baixo","小火"),("baixa","低"),("bem","充分"),("mais","更多"),("menos","更少"),("muito","很多"),("muita","很多"),("pouco","少量"),("cada","每"),("lado","面"),("cima","上面"),("fundo","底部"),("meio","中间"),("centro","中心"),("dentro","里面"),("fora","外面"),("antes","之前"),("depois","之后"),("ainda","仍然"),("sempre","总是"),("nunca","不要"),("tudo","全部"),("mesma","相同"),("duas","两个"),("dois","两个"),("uma","一份"),("um","一份"),("ou","或"),("e","和"),("com","与"),("sem","无"),("em","在"),("no","在"),("na","在"),("de","的"),("do","的"),("da","的"),("dos","的"),("das","的"),("para","用于"),("por","经过"),("até","直到"),("que","让"),("não","不"),("mas","但是"),("se","如果"),("só","只")]
EXTRA=[
 ("manteiga","黄油"),("natural","原味"),("mix","混合坚果"),("low","低碳"),("carb","碳水"),("limão","柠檬"),("suco","柠檬汁"),("ovo","鸡蛋"),("ovos","鸡蛋"),("pitada","一小撮"),("lata","罐"),("latas","罐"),("parmesão","帕玛森奶酪"),("cominho","孜然"),("folhas","叶子"),("folha","叶子"),("buquês","小朵"),("abobrinhas","西葫芦"),("atum","金枪鱼"),("berinjelas","茄子"),("calabresa","辣香肠"),("finas","薄的"),("fina","薄的"),("coco","椰子"),("frango","鸡肉"),("alface","生菜"),("tomates","番茄"),("vidro","玻璃罐"),("laminados","切片"),("laminado","切片"),("variadas","混合"),("pedaço","块"),("filés","鱼片"),("filé","鱼片"),("tomilho","百里香"),("raspas","皮屑"),("bifes","牛排"),("alcatra","牛臀肉"),("salsa","欧芹"),("postas","鱼块"),("processada","处理好的"),("cru","生的"),("crua","生的"),("crus","生的"),("espinafre","菠菜"),("untar","抹油"),("madura","熟的"),("maduro","熟的"),("maduros","熟的"),("fermento","泡打粉"),("rasa","平勺"),("fatias","薄片"),("rodelas","圆片"),("crepioca","木薯薄饼"),("integral","全脂"),("americana","美式"),("creme","奶油"),("azedo","酸味"),("portuguesa","葡式"),("cabotiá","栗味南瓜"),("crouton","面包丁"),("amido","淀粉"),("altos","厚的"),("paris","蘑菇"),("batido","打散"),("limpo","清理好的"),("comum","普通"),("acompanhar","搭配"),("enrolar","卷起"),("frescas","新鲜"),("grosso","粗的"),("fatiada","切片"),("fatiado","切片"),("rechear","填馅"),("grelhado","烤好的"),("louro","月桂叶"),("caldo","高汤"),("carnes","肉类"),("cobertura","表面"),("caseiro","自制"),("caseira","自制"),("espaguete","意大利面"),("fios","细丝"),("repolho","卷心菜"),("hortelã","薄荷"),("moqueca","巴西鱼炖锅"),("peixe","鱼"),("firme","紧实"),("badejo","石斑鱼"),("pescada","无须鳕"),("robalo","鲈鱼"),("dendê","棕榈油"),("anéis","圈"),("grãos","颗粒"),("inteiras","完整的"),("japonês","日式"),("gergelim","芝麻"),("gomos","瓣"),("gotas","滴"),("ramos","枝"),("maço","把"),("milho","玉米"),("laranja","橙子"),("lascas","薄片"),("pele","皮"),("refogada","炒好的"),("roxa","紫色"),("verde","绿色"),("vermelho","红色"),("vermelhas","红色"),("pretas","黑色"),("torrada","烤过的"),("torrado","烤过的"),("torresmo","猪皮脆片"),("endro","莳萝"),("ervas","香草"),("cortadas","切好的"),("congeladas","冷冻的"),("diluído","调开的"),("dessalgada","脱盐的"),("dessalgado","脱盐的"),("amassados","捣碎的"),("ambiente","室温"),("temperatura","温度"),("inteiro","整颗"),("médias","中等大小"),("sobrecoxas","鸡腿"),("contrafilé","西冷牛排"),("filé-mignon","菲力牛排"),("patinho","瘦牛肉末"),("acém","牛肩肉"),("copa-lombo","猪肩肉"),("porco","猪肉"),("costela","肋排"),("paio","巴西香肠"),("maionese","蛋黄酱"),("wasabi","芥末"),("granola","坚果燕麦脆"),("cheesecake","芝士蛋糕"),("pizza","披萨"),("wrap","卷饼"),("konjac","魔芋"),("pará","巴西坚果"),("caju","腰果"),("amêndoa","杏仁"),("frutas","水果"),("massa","面团"),("ao","到"),("na","在"),("A","一"),("O","一"),("E","和")]

def translate_ingredient(value):
 s=str(value)
 for a,b in sorted(PHRASES,key=lambda x:len(x[0]),reverse=True):s=re.sub(r"(?<!\w)"+re.escape(a)+r"(?!\w)",b,s,flags=re.IGNORECASE)
 for a,b in sorted(WORDS+EXTRA,key=lambda x:len(x[0]),reverse=True):s=re.sub(r"(?<!\w)"+re.escape(a)+r"(?!\w)",b,s,flags=re.IGNORECASE)
 s=s.replace(" 的 "," ").replace(" 的"," ").replace("em pó","粉")
 s=re.sub(r"(\d[\d/.-]*)\s+(大勺|小勺|杯)\s+",r"\1\2 ",s)
 s=s.replace("1份 鸡蛋","鸡蛋1个").replace("2份 鸡蛋","鸡蛋2个").replace("  的 "," ")
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
CSS=layout.CSS.replace("50 Low-Carb Recipes for Everyday Life","每日低碳食谱50")+"\nbody,p,li,td,th,.meta,.dica,.troca{font-family:'Noto Sans CJK SC','Noto Sans CJK JP',sans-serif}h1,h2,h3{font-family:'Noto Serif CJK SC','Noto Serif CJK JP',serif}@page{margin-bottom:6mm}.dica{padding:2mm 3mm;margin-top:1.5mm;font-size:7.7pt}.troca{padding:.8mm 3mm;margin-top:.8mm;font-size:7.3pt;line-height:1.4}"
FRONT="""
<section class="frente legal"><h2>版权与重要说明</h2><div class="filete"></div><p><b>每日低碳食谱50</b> — 2026年第一版。<br>实用厨房系列 · 第1册。</p><p>版权所有。未经书面许可，不得复制本书的全部或部分内容。本电子书为面向购买者的数字产品。</p><div class="quadro"><b>重要提示：</b>营养信息（热量、碳水化合物、蛋白质和脂肪）是根据配料表和食物成分表计算的<b>每份估算值</b>。不同品牌、食材大小和器具会造成差异。本书仅供教育参考，不能替代医生或注册营养师的建议。患有糖尿病、肾脏疾病的人，孕期或哺乳期人群，以及长期服药者，在采用限制碳水的饮食方式前应咨询专业人士。木糖醇对狗有毒，请把甜点放在宠物接触不到的地方。</div><p><b>本书使用的计量：</b>1杯 = 240毫升 · 1大勺 = 15毫升 · 1小勺 = 5毫升 · 除非特别说明，烤箱均需预热。</p></section>
<section class="frente"><h2>欢迎来到低碳厨房</h2><div class="filete"></div><p>这不是一本严格的节食书，而是针对每天都会遇到的问题——<i>“今天做什么吃？”</i>——准备的<b>50个实用答案</b>。</p><p>低碳生活不意味着只能吃无聊的沙拉。你可以享用奶油般的蛋饼、可以切片的千层面、周日的炖肉，甚至芝士蛋糕，同时用更有满足感的食材替代面粉和糖。</p><div class="quadro"><b>本书的黄金规则：</b>碳水化合物是点缀，不是基础。基础永远是蛋白质、优质脂肪和蔬菜。</div><p>连续七周每天做一道新食谱，你就会拥有能拯救忙碌星期一的料理储备。祝你好胃口。</p></section>
<section class="frente"><h2>如何使用本书</h2><div class="filete"></div><p><b>1. 先看最后几页。</b>去购物前先查看“7天菜单”和购物清单。</p><p><b>2. 把合适的食谱做双份。</b>大多数午餐和晚餐食谱是两人份，第二份就是第二天的午餐。</p><p><b>3. 使用提示框。</b>每道食谱都有<b>烹饪提示</b>和<b>聪明替换</b>，帮助你灵活调整材料。</p><p><b>4. 不要追求零碳水。</b>营养数据是帮助选择的工具，不应变成负担。</p><p><b>5. 放心冷冻。</b>带有冷冻说明的食谱适合分装保存。</p></section>
<section class="frente"><h2>拯救厨房的替换表</h2><div class="filete"></div><p>低碳饮食也需要聪明地替换食材：</p><table><tr><th>减少或去掉</th><th>替代材料</th><th>说明</th></tr><tr><td>精制糖</td><td><b>赤藓糖醇或木糖醇</b></td><td>1:1；木糖醇更甜一些</td></tr><tr><td>小麦粉</td><td><b>杏仁粉＋1个鸡蛋</b></td><td>用一半分量，鸡蛋负责黏合</td></tr><tr><td>白米饭</td><td><b>菜花米</b></td><td>生菜花大火翻炒5至6分钟</td></tr><tr><td>面条</td><td><b>西葫芦、棕榈心或魔芋</b></td><td>翻炒90秒至3分钟</td></tr><tr><td>土豆</td><td><b>菜花、芜菁或烤萝卜</b></td><td>适合做泥和汤</td></tr></table><h2 style="margin-top:6mm">建议常备</h2><div class="lista2"><ul><li>杏仁粉和无糖椰蓉</li><li>赤藓糖醇、木糖醇和100%可可</li><li>无糖椰奶和淡奶油</li><li>橄榄油、椰子油和黄油</li><li>鸡蛋、马苏里拉奶酪、帕玛森奶酪和奶油奶酪</li><li>菜花、西葫芦、茄子、卷心菜和羽衣甘蓝</li><li>罐装去皮番茄和橄榄</li><li>鸡肉、牛肉末、鱼和罐装金枪鱼</li><li>坚果、柠檬、鲜香草和烟熏红椒粉</li></ul></div></section>
"""
BONUS="""
<section class="frente"><h2>加餐1 — 7天菜单</h2><div class="filete"></div><p>适合第一周的现实计划：有饱腹感的早餐、可以变成晚餐的午餐，以及恰到好处的甜点。</p><table><tr><th>星期</th><th>早餐</th><th>午餐</th><th>加餐</th><th>晚餐</th></tr><tr><td class="dia">一</td><td>01 · 蛋饼</td><td>10＋23 · 菜花米配鸡肉</td><td>09 · 酸奶坚果脆</td><td>37 · 菜花披萨</td></tr><tr><td class="dia">二</td><td>05 · 木薯薄饼</td><td>17 · 茄子千层面</td><td>06 · 芝士面包</td><td>31 · 三文鱼＋44 · 慕斯</td></tr><tr><td class="dia">三</td><td>02 · 微波炉面包</td><td>11 · 西葫芦面</td><td>45 · 椰香布丁</td><td>35 · 鱼肉炖锅</td></tr><tr><td class="dia">四</td><td>07 · 羽衣甘蓝卷</td><td>13 · 鸡肉沙拉</td><td>08 · 牛油果鸡蛋</td><td>26 · 蘑菇牛排</td></tr><tr><td class="dia">五</td><td>03 · 香蕉煎饼</td><td>16 · 菜花焗烤</td><td>09 · 酸奶坚果脆</td><td>33 · 蒜香虾</td></tr><tr><td class="dia">六</td><td>04 · 咸玛芬</td><td>18 · 填馅茄子</td><td>46 · 巧克力奶油</td><td>42 · 低碳寿司</td></tr><tr><td class="dia">日</td><td>06 · 芝士面包</td><td>30 · 手撕猪肋排</td><td>47 · 芝士蛋糕</td><td>19 · 绿汤＋28 · 牛排</td></tr></table></section>
<section class="frente"><h2>加餐2 — 第一周购物清单</h2><div class="filete"></div><p>打印这份清单并带去超市，分量按两人计算：</p><div class="lista2"><ul class="check"><li>鸡蛋2打</li><li>鸡胸肉1公斤＋鸡腿8只</li><li>牛肉末1公斤＋牛排500克</li><li>三文鱼或紧实白鱼600克＋虾仁400克</li><li>金枪鱼罐头2个</li><li>马苏里拉奶酪500克＋帕玛森奶酪＋奶油奶酪</li><li>淡奶油</li><li>无糖椰奶2盒</li><li>菜花、西葫芦、茄子、卷心菜和羽衣甘蓝</li><li>新鲜番茄＋去皮番茄罐头2个</li><li>牛油果、香蕉、草莓和柠檬</li><li>洋葱、大蒜、姜、香草和烟熏红椒粉</li><li>橄榄、棕榈心、坚果和花生</li><li>杏仁粉、椰蓉和奇亚籽</li><li>赤藓糖醇或木糖醇、可可和85%巧克力</li><li>橄榄油、黄油和椰子油</li><li>酱油和芥末</li></ul></div></section>
<section class="frente"><h2>关上厨房之前</h2><div class="filete"></div><p>现在你已经拥有50道为真实生活设计的食谱：容易买到的材料、简单的做法和有计划的剩菜。这个电子书与更有条理的一周之间，只差一个小决定：<b>下一顿饭吃什么</b>。</p><p>今晚选一道食谱，动手做出来，并和别人一起分享。一起吃饭更容易坚持。</p><div class="quadro"><b>实用厨房后续书册：</b>第2册——<i>一周低碳餐</i> · 第3册——<i>无糖节日甜点</i>。</div></section>
"""
COVER="""<section class="capa"><div class="txt"><div class="kicker">实用厨房系列 · 第1册</div><h1>每日<br><span class="hl">低碳食谱50</span></h1><div class="sub">适合每一天——无面粉、无糖，轻松又美味</div></div><div class="faixa"><span class="marca">实用厨房</span><span>少一点碳水，多一点生活滋味</span></div></section>"""
BACK="""<section class="contra"><div class="in"><h2>别再每个星期一重新开始。</h2><p>本书收录50道低碳食谱，让你不用做两套饭也能坚持：撑过上午的早餐、可以变成晚餐的午餐、寒冷夜晚的热汤，以及无需内疚的甜点。</p><ul><li><b>50道完整食谱</b>，包含时间、份量和每份估算营养值；</li><li>每道食谱都有<b>烹饪提示</b>；</li><li>可以灵活调整材料的<b>聪明替换</b>；</li><li><b>7天菜单</b>和可打印购物清单；</li><li>面粉、糖、米饭和面条的<b>替换表</b>。</li></ul><p>容易买到的材料。现实的烹饪时间。不像节食餐的味道。</p><div class="marca">实用厨房</div></div></section>"""

def recipe_html(r):
 num,rid,d=r["num"],r["id"],r["d"];name,prep,total,servings,kcal,carbs,protein,fat,ingredients,steps,tip,swap=d
 ing=''.join('<li>%s</li>'%H.escape(x) for x in ingredients);pas=''.join('<li>%s</li>'%H.escape(x) for x in steps)
 return '<section class="receita" id="%s"><header><div class="num">%02d</div><div class="titulo"><h3>%s</h3></div></header><img class="foto" src="imagens/receita-%02d.jpg" alt="%s"><div class="meta"><span><b>准备</b> %d分钟</span><span><b>总计</b> %d分钟</span><span><b>份量</b> %s</span><span><b>难度</b> 简单</span></div><div class="nutris"><span><b>%d</b>千卡 / 每份</span><span><b>%d克</b>碳水</span><span><b>%d克</b>蛋白质</span><span><b>%d克</b>脂肪</span></div><div class="corpo"><div><h4>材料</h4><ul class="ing">%s</ul></div><div><h4>做法</h4><ol class="passos">%s</ol></div></div><div class="dica"><b>烹饪提示：</b> %s</div><div class="troca"><b>↺ 聪明替换：</b> %s</div></section>'%(rid,num,H.escape(name),num,H.escape(name),prep,total,H.escape(str(servings)),kcal,carbs,protein,fat,ing,pas,H.escape(tip),H.escape(swap))
def toc_html(pmap=None):
 out=['<section class="frente"><h2>目录</h2><div class="filete"></div><div class="sum"><table>'];idx=0
 for cat,intro,names in SELECTION:
  out.append('<tr><td class="cat" colspan="4">%s</td></tr>'%H.escape(cat))
  for name in names:
   idx+=1;pg=str(pmap[idx]) if pmap else '';out.append('<tr><td class="num">%02d</td><td><a href="#r%02d">%s</a></td><td class="dots"></td><td class="pg">%s</td></tr>'%(idx,idx,H.escape(name),pg))
 out.append('</table></div></section>');return ''.join(out)
def body_html():
 out=[]
 for chapter,(cat,intro,names) in enumerate(SELECTION,1):
  out.append('<section class="abre"><img class="capfoto" src="imagens/capitulo-%02d.jpg" alt="%s章节图片"><div class="tag">第%02d章</div><h2>%s</h2><div class="filete"></div><p>%s</p></section>'%(chapter,H.escape(cat),chapter,H.escape(cat),H.escape(intro)))
  for r in RECIPES:
   if r["cat"]==cat:out.append(recipe_html(r))
 return ''.join(out)
def render(pmap=None):return "<!DOCTYPE html><html lang='zh-CN'><head><meta charset='utf-8'><style>%s</style></head><body>%s%s%s%s%s%s</body></html>"%(CSS,COVER,FRONT,toc_html(pmap),body_html(),BONUS,BACK)
def build():
 from weasyprint import HTML
 import fitz
 open('ebook_zh_probe.html','w').write(render(None));HTML(filename='ebook_zh_probe.html').write_pdf('ebook_zh_probe.pdf')
 d=fitz.open('ebook_zh_probe.pdf');pmap={}
 for i in range(d.page_count):
  text=d[i].get_text();norm=text.replace(' ','')
  if '材料' in norm and '做法' in norm:
   m=re.search(r'(?m)^(\d{2})\n',text)
   if m and 1<=int(m.group(1))<=50:pmap[int(m.group(1))]=i+1
 assert len(pmap)==50,(len(pmap),sorted(set(range(1,51))-set(pmap)))
 open('50-低碳食谱-zh.html','w').write(render(pmap));HTML(filename='50-低碳食谱-zh.html').write_pdf('50-低碳食谱-zh.pdf')
 print('中文PDF已生成：',len(pmap),'道食谱')
if __name__=='__main__':build()
