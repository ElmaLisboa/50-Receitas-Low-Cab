# -*- coding: utf-8 -*-
"""Nederlandse editie: 50 Low-Carb-Recepten voor elke dag."""
import html as H
import re
import livro as pt
import livro_en as layout
from nl_overrides import OVERRIDES

NAMES = [
 "Spinazie-kaasomelet uit de oven", "Low-carb magnetronbrood in 2 minuten", "Bananenpannenkoekjes met havermout",
 "Hartige muffins met ei, groenten en spek", "Tapiocacrep uit de koekenpan met kaas en tomaat", "Kaaspaneerbrood uit de koekenpan",
 "Romige kipwrap met boerenkool", "Romige roereieren met avocado en zaden", "Eiwitrijke yoghurt met notengranola",
 "Eenvoudige bloemkoolrijst", "Courgettenoedels met huisgemaakte tomatensaus", "Palmhartnoedels met knoflook en olie",
 "Complete kipsalade met yoghurtdressing", "Tonijnsalade met ei en citroenmayonaise", "Pittige gehaktwrap met sla",
 "Low-carb bloemkool-ovenschotel met draadjesvlees", "Auberginelasagne bolognese", "Gevulde aubergine met gehakt",
 "Low-carb boerenkoolsoep zonder aardappel", "Pompoensoep met kokosmelk en gember", "Groentesoep met pulled chicken",
 "Romige courgettesoep met roomkaas", "Gegrilde kip met romige mosterdsaus", "Geroosterde kippendijen met citroen en rozemarijn",
 "Low-carb kip uit de wok", "Steak met champignonsaus", "Gehakt met courgette en tomaat",
 "Biefstuk met gekaramelliseerde ui en knoflookboter", "Gehaktballen gevuld met kaas in tomatensaus", "Pulled pork-ribbetjes",
 "Zalm uit de oven met citroenboter", "Amandelkorst voor tilapia", "Knoflookgarnalen", "Kabeljauw met bloemkool en olijven",
 "Vis-moqueca met kokosmelk en palmharten", "Gegrilde inktvis met citroen en kruiden",
 "Bloemkoolpizza met mozzarella en basilicum", "Aubergine parmigiana zonder paneerlaag", "Low-carb feijoada zonder bonen",
 "Kaaspaneerbrood uit de airfryer", "Gevulde courgette met tonijn en roomkaas", "Low-carb sushi — komkommerrolletjes",
 "Koolrolletjes met gehakt", "Chocolademousse met avocado", "Kokosflan met erythritol",
 "Low-carb chocoladeroom om te lepelen", "Low-carb cheesecake met rood fruit", "Low-carb koekjes met noten en chocolade",
 "Chocoladetruffels met kokosolie", "Low-carb pindasnoepjes in paçoca-stijl"
]

CAT = {
 "Café da manhã e lanches rápidos": ("Ontbijt en snelle snacks", "Begin de dag met praktische, vullende recepten zonder afhankelijk te zijn van traditioneel brood. Dit hoofdstuk combineert eieren, kaas, amandel- of kokosmeel en fruit in uitgebalanceerde porties. De meeste recepten vragen maximaal 15 minuten actieve bereiding."),
 "Almoços completos": ("Complete lunches", "Eenpansgerechten, salades die je de hele middag verzadigen en slimme vervangers voor rijst en pasta — zonder dat het naar dieeteten smaakt."),
 "Sopas e caldos": ("Soepen en bouillons", "Voor koude avonden en maaltijden onderweg: romig comfort zonder aardappel of tarwemeel."),
 "Carnes e aves": ("Vlees en gevogelte", "Eiwit is de basis van een goed low-carbmenu: mooi gebruind, sappig en met echte sauzen — nooit droge kip uit een meal-prepbox."),
 "Peixes e frutos do mar": ("Vis en zeevruchten", "Van zalm op zondag tot snelle zeevruchten doordeweeks: goede vetten, weinig bereidingstijd en restaurantwaardige smaak."),
 "Jantares em até 30 minutos de bancada": ("Avondmaaltijden in 30 minuten", "De avondregel: het eten staat op tafel voordat de aflevering is afgelopen. Recepten voor één pan, één bakplaat of de airfryer."),
 "Sobremesas sem açúcar": ("Desserts zonder suiker", "Een echt dessert heeft geen geraffineerde suiker nodig: cacao, kokos, noten en zoetstoffen die de smaak niet bedriegen."),
}

# Langere voedseluitdrukkingen eerst vervangen.
PHRASES = [
 ("pimenta-do-reino", "zwarte peper"), ("cheiro-verde", "verse kruiden"), ("couve manteiga", "boerenkool"),
 ("couve-flor", "bloemkool"), ("couve", "boerenkool"), ("abobrinha", "courgette"), ("berinjela", "aubergine"),
 ("palmito pupunha", "palmharten"), ("palmito", "palmharten"), ("tomate pelado", "gepelde tomaten"),
 ("creme de leite fresco", "room"), ("creme de leite", "room"), ("cream cheese", "roomkaas"), ("requeijão", "roomkaas"),
 ("muçarela", "mozzarella"), ("queijo parmesão", "Parmezaanse kaas"), ("queijo", "kaas"),
 ("farinha de amêndoas", "amandelmeel"), ("farinha de coco", "kokosmeel"), ("farinha de linhaça dourada", "goudkleurig lijnzaadmeel"),
 ("polvilho azedo", "zure tapiocazetmeel"), ("goma de tapioca", "tapiocagom"), ("leite de coco", "kokosmelk"),
 ("carne seca", "gedroogd draadjesvlees"), ("carne moída", "gehakt"), ("frango desfiado", "pulled chicken"), ("peito de frango", "kipfilet"),
 ("ovos mexidos", "roereieren"), ("ovos cozidos", "gekookte eieren"), ("ovo cozido", "gekookt ei"), ("castanha-de-caju", "cashewnoten"),
 ("castanha do pará", "paranoten"), ("castanhas", "noten"), ("manteiga de amendoim", "pindakaas"), ("pasta de amendoim", "pindakaas"),
 ("amendoim", "pinda's"), ("morangos", "aardbeien"), ("morango", "aardbei"), ("abacate", "avocado"), ("abóbora", "pompoen"),
 ("pepino", "komkommer"), ("tomate", "tomaat"), ("cebola", "ui"), ("alho", "knoflook"), ("dentes", "teentjes"), ("dente", "teentje"),
 ("salsão", "bleekselderij"), ("vagem", "sperziebonen"), ("cenoura", "wortel"), ("pimentão", "paprika"), ("cogumelos", "champignons"),
 ("shimeji", "shimejipaddenstoelen"), ("salmão", "zalm"), ("camarão", "garnaal"), ("camarões", "garnalen"), ("tilápia", "tilapia"),
 ("bacalhau", "kabeljauw"), ("lula", "inktvis"), ("costelinha", "varkensribbetjes"), ("linguiça", "worst"), ("bacon", "spek"),
 ("presunto cru", "rauwe ham"), ("presunto", "ham"), ("iogurte", "yoghurt"), ("azeitona", "olijf"), ("azeitonas", "olijven"),
 ("azeite", "olijfolie"), ("vinagre de maçã", "appelazijn"), ("vinagre de vinho tinto", "rodewijnazijn"),
 ("mostarda dijon", "Dijonmosterd"), ("mostarda", "mosterd"), ("shoyu", "sojasaus"), ("molho de tomate", "tomatensaus"),
 ("molho", "saus"), ("caldo de legumes", "groentebouillon"), ("caldo de galinha", "kippenbouillon"), ("caldo de carne", "runderbouillon"),
 ("páprica defumada", "gerookt paprikapoeder"), ("páprica", "paprikapoeder"), ("orégano", "oregano"), ("manjericão", "basilicum"),
 ("salsinha", "peterselie"), ("cebolinha", "bosui"), ("coentro", "koriander"), ("alecrim", "rozemarijn"), ("gengibre", "gember"),
 ("canela", "kaneel"), ("cacau em pó", "ongezoet cacaopoeder"), ("cacau", "cacao"), ("coco ralado", "geraspte kokos"),
 ("coco em flocos", "kokosvlokken"), ("sementes de girassol", "zonnebloempitten"), ("sementes de abóbora", "pompoenpitten"),
 ("sementes de chia", "chiazaad"), ("sementes", "zaden"), ("farinha", "meel"), ("açúcar", "suiker"), ("adoçante", "zoetstof"),
 ("essência", "vanille-extract"), ("fermento em pó", "bakpoeder"), ("em pó", "poeder"), ("sem açúcar", "zonder suiker"),
 ("sem farinha", "zonder meel"), ("sem sementes", "zonder pitten"), ("sem pele", "zonder vel"), ("a gosto", "naar smaak"),
 ("para servir", "om te serveren"), ("para finalizar", "voor de afwerking"), ("em cubos", "in blokjes"), ("em rodelas", "in plakjes"),
 ("em fatias", "in plakken"), ("em tiras", "in reepjes"), ("picada", "fijngehakt"), ("picado", "fijngehakt"), ("picadas", "fijngehakt"),
 ("picados", "fijngehakt"), ("ralada", "geraspt"), ("ralado", "geraspt"), ("raladas", "geraspt"), ("ralados", "geraspt"),
 ("escorrido", "uitgelekt"), ("escorrida", "uitgelekt"), ("escorridas", "uitgelekt"), ("desfiado", "uit elkaar getrokken"),
 ("desfiada", "uit elkaar getrokken"), ("desfiados", "uit elkaar getrokken"), ("espremida", "uitgeknepen"), ("espremido", "uitgeknepen"),
 ("congelado", "bevroren"), ("derretida", "gesmolten"), ("derretido", "gesmolten"), ("cozida", "gekookt"), ("cozido", "gekookt"),
 ("quente", "warm"), ("morno", "lauwwarm"), ("crocante", "knapperig"), ("cremoso", "romig"), ("cremosa", "romig"),
 ("xíc.", "kopje"), ("col. sopa", "eetlepel"), ("col. chá", "theelepel"), ("col.", "eetlepel")]

WORD_MAP = [
 ("minutos", "minuten"), ("minuto", "minuut"), ("segundos", "seconden"), ("segundo", "seconde"), ("horas", "uur"), ("hora", "uur"),
 ("dias", "dagen"), ("dia", "dag"), ("meses", "maanden"), ("geladeira", "koelkast"), ("congelador", "vriezer"), ("forno", "oven"),
 ("micro-ondas", "magnetron"), ("frigideira", "koekenpan"), ("panela", "pan"), ("liquidificador", "blender"), ("garfo", "vork"),
 ("ralador", "rasp"), ("descascador", "dunschiller"), ("espiralizador", "spiraalsnijder"), ("papel-toalha", "keukenpapier"),
 ("papel-manteiga", "bakpapier"), ("papel-alumínio", "aluminiumfolie"), ("assadeira", "bakplaat"), ("refratário", "ovenschaal"),
 ("forminhas", "vormpjes"), ("marmita", "lunchbox"), ("pote", "pot"), ("potes", "potten"), ("saco", "zak"), ("torradeira", "broodrooster"),
 ("airfryer", "airfryer"), ("banho-maria", "au bain-marie"), ("água", "water"), ("óleo", "olie"), ("fogo", "vuur"), ("açúcar", "suiker"),
 ("pimenta", "peper"), ("sal", "zout"), ("noz-moscada", "nootmuskaat"), ("baunilha", "vanille"), ("eritritol", "erythritol"), ("xilitol", "xylitol"),
 ("pão", "brood"), ("arroz", "rijst"), ("aveia", "havermout"), ("farelo", "zemelen"), ("banana", "banaan"), ("maçã", "appel"),
 ("chocolate", "chocolade"), ("mel", "honing"), ("queijos", "kazen"), ("massa", "deeg"), ("recheio", "vulling"), ("ingredientes", "ingrediënten"),
 ("receita", "recept"), ("prato", "gerecht"), ("porção", "portie"), ("porções", "porties"), ("dica", "tip"), ("versão", "versie"),
 ("fresco", "vers"), ("natural", "naturel"), ("opcional", "optioneel"), ("grande", "groot"), ("grandes", "grote"), ("pequeno", "klein"),
 ("pequena", "klein"), ("médio", "middelgroot"), ("média", "middelgrote"), ("alto", "hoog"), ("alta", "hoog"), ("baixo", "laag"), ("baixa", "laag"),
 ("bem", "goed"), ("mais", "meer"), ("menos", "minder"), ("muito", "veel"), ("muita", "veel"), ("pouco", "weinig"), ("cada", "elke"),
 ("lado", "kant"), ("cima", "boven"), ("fundo", "bodem"), ("meio", "midden"), ("centro", "midden"), ("dentro", "binnenkant"), ("fora", "buiten"),
 ("antes", "voordat"), ("depois", "daarna"), ("ainda", "nog"), ("sempre", "altijd"), ("nunca", "nooit"), ("tudo", "alles"), ("mesma", "zelfde"),
 ("duas", "twee"), ("dois", "twee"), ("uma", "een"), ("um", "een"), ("ou", "of"), ("e", "en"), ("com", "met"), ("sem", "zonder"),
 ("em", "in"), ("no", "in de"), ("na", "in de"), ("de", "van"), ("do", "van de"), ("da", "van de"), ("dos", "van de"), ("das", "van de"),
 ("para", "voor"), ("por", "gedurende"), ("até", "tot"), ("que", "die"), ("não", "niet"), ("mas", "maar"), ("se", "als"), ("só", "alleen"),
]

EXTRA_MAP = [
 ("manteiga", "boter"), ("limão", "citroen"), ("suco", "sap"), ("ovo", "ei"), ("ovos", "eieren"), ("pitada", "snufje"),
 ("lata", "blik"), ("latas", "blikjes"), ("parmesão", "Parmezaanse kaas"), ("cominho", "komijn"), ("folhas", "bladeren"),
 ("folha", "blad"), ("buquês", "roosjes"), ("abobrinhas", "courgettes"), ("atum", "tonijn"), ("berinjelas", "aubergines"),
 ("calabresa", "chorizo"), ("finas", "dunne"), ("fina", "dunne"), ("coco", "kokos"), ("frango", "kip"), ("alface", "sla"),
 ("tomates", "tomaten"), ("vidro", "pot"), ("laminados", "in plakjes"), ("laminado", "in plakjes"), ("variadas", "gemengde"),
 ("pedaço", "stuk"), ("filés", "filets"), ("filé", "filet"), ("tomilho", "tijm"), ("raspas", "rasp"), ("bifes", "steaks"),
 ("alcatra", "rumpsteak"), ("salsa", "peterselie"), ("postas", "visfilets"), ("processada", "verwerkte"), ("processado", "verwerkt"),
 ("cru", "rauw"), ("crua", "rauw"), ("crus", "rauwe"), ("espinafre", "spinazie"), ("untar", "invetten"), ("madura", "rijpe"),
 ("maduro", "rijp"), ("maduros", "rijpe"), ("fermento", "bakpoeder"), ("rasa", "afgestreken"), ("fatias", "plakken"), ("rodelas", "plakjes"),
 ("crepioca", "tapiocacrep"), ("pasta", "pasta"), ("pasta de amendoim", "pindakaas"), ("pimentões", "paprika's"), ("louro", "laurier"),
 ("caldo", "bouillon"), ("carnes", "vlees"), ("cobertura", "topping"), ("caseiro", "huisgemaakt"), ("caseira", "huisgemaakt"),
 ("espaguete", "spaghetti"), ("fios", "reepjes"), ("repolho", "kool"), ("hortelã", "munt"), ("moqueca", "moqueca"), ("peixe", "vis"),
 ("firme", "stevig"), ("badejo", "tandbaars"), ("pescada", "heek"), ("robalo", "zeebaars"), ("dendê", "dendê-olie"), ("anéis", "ringen"),
 ("gordura", "vet"), ("grãos", "korrels"), ("grelhado", "gegrild"), ("gros​so", "grof"), ("grosso", "grof"), ("inteiras", "hele"),
 ("japonês", "Japanse"), ("gergelim", "sesam"), ("gomos", "partjes"), ("gotas", "druppels"), ("ramos", "takjes"), ("maço", "bos"),
 ("milho", "mais"), ("laranja", "sinaasappel"), ("lascas", "vlokken"), ("pele", "vel"), ("rechear", "vullen"), ("refogada", "gebakken"),
 ("roxa", "rode"), ("verde", "groene"), ("vermelho", "rode"), ("vermelhas", "rode"), ("pretas", "zwarte"), ("torrada", "geroosterd"),
 ("torrado", "geroosterd"), ("torresmo", "knapperig varkensvel"), ("endro", "dille"), ("ervas", "kruiden"), ("fatiada", "in plakken"),
 ("cortadas", "gesneden"), ("congeladas", "bevroren"), ("diluído", "aangelengd"), ("dessalgada", "ontzout"), ("dessalgado", "ontzout"),
 ("amassados", "geplette"), ("ambiente", "omgeving"), ("temperatura", "temperatuur"), ("inteiro", "heel"), ("médias", "middelgrote"),
 ("sobrecoxas", "kippendijen"), ("contrafilé", "entrecote"), ("filé-mignon", "ossenhaas"), ("patinho", "mager gehakt"), ("acém", "runderstoofvlees"),
 ("copa-lombo", "varkensnek"), ("porco", "varkensvlees"), ("costela", "rib"), ("paio", "worst"), ("maionese", "mayonaise"),
 ("wasabi", "wasabi"), ("granola", "granola"), ("cheesecake", "cheesecake"), ("pizza", "pizza"), ("wrap", "wrap"), ("airfryer", "airfryer"),
 ("konjac", "konjac"), ("pará", "paranoten"), ("caju", "cashewnoten"), ("amêndoa", "amandel"), ("frutas", "fruit"), ("massa", "deeg"),
 ("calabresa", "chorizo"), ("couve", "boerenkool"), ("couve-flor", "bloemkool"), ("ao", "aan het"), ("na", "in de"), ("A", "de"), ("O", "de"),
 ("E", "en"), ("integral", "vol"), ("americana", "Amerikaanse"), ("creme", "room"), ("azedo", "zure"), ("portuguesa", "Portugese"),
 ("cabotiá", "hokkaido"), ("crouton", "crouton"), ("amido", "maïzena"), ("altos", "dikke"), ("paris", "Parijse"), ("batido", "losgeklopt"),
 ("limpo", "schoongemaakt"), ("comum", "gewone"), ("acompanhar", "erbij"), ("enrolar", "om te rollen"), ("frescas", "verse"), ("madura", "rijpe"),
 ("grosso", "dikke"), ("grosse", "dikke"), ("fatiada", "in plakken"), ("fatiado", "in plakken"), ("rechear", "vullen"), ("grelhado", "gegrild"),
]

def translate_ingredient(value):
 s=str(value)
 for a,b in sorted(PHRASES,key=lambda x:len(x[0]),reverse=True):
  s=re.sub(r"(?<!\w)"+re.escape(a)+r"(?!\w)",b,s,flags=re.IGNORECASE)
 for a,b in sorted(WORD_MAP+EXTRA_MAP,key=lambda x:len(x[0]),reverse=True):
  s=re.sub(r"(?<!\w)"+re.escape(a)+r"(?!\w)",b,s,flags=re.IGNORECASE)
 # Resterende Portugese voorzetsels en enkele Nederlandse maatnotaties opschonen.
 for a,b in [(" de "," "),(" do "," "),(" da "," "),(" dos "," "),(" das "," "),(" com "," met "),(" sem "," zonder "),(" em "," "),(" no "," "),(" na "," "),(" para "," voor "),(" a gosto"," naar smaak")]: s=s.replace(a,b)
 s=re.sub(r"(\d[\d/.-]*)\s+(eetlepel|theelepel|kopje)\s+",r"\2 \1 ",s)
 s=re.sub(r"(\d[\d/.-]*)\s+g\s+",r"\1 g ",s)
 # Nederlandse volgorde voor hoeveelheden en ingrediënten.
 s=re.sub(r"^(kopje|eetlepel|theelepel)\s+([\d/.-]+)\s+van\s+",r"\2 \1 ",s)
 s=re.sub(r"^([\d/.-]+)\s+(kopje|eetlepel|theelepel)\s+van\s+",r"\1 \2 ",s)
 s=s.replace(" van "," ").replace("  van "," ")
 s=re.sub(r"^(\d+|[2-9]/\d+)\s+eetlepel\b",r"\1 eetlepels",s)
 s=s.replace("teentjes knoflook", "teentjes knoflook").replace("kaas mozzarella", "mozzarella").replace("kaas Parmezaanse", "Parmezaanse kaas")
 s=s.replace(" goed rijpe", " rijpe").replace("fijngehakt", "fijngehakt").replace("geraspt", "geraspt").replace("cru", "rauw")
 s=s.replace("vanille-extract vanille", "vanille-extract").replace("olie van kokos", "kokosolie")
 s=s.replace("voor invetten", "om in te vetten").replace("om te vetten", "om in te vetten")
 return s.strip()

PT_TO_NL={r["d"][0]:NAMES[r["num"]-1] for r in pt.RECEITAS}
RECIPES=[]
for r in pt.RECEITAS:
 d=r["d"];name,prep,total,servings,kcal,carbs,protein,fat,ingredients,steps,tip,swap=d
 steps_nl,tip_nl,swap_nl=OVERRIDES[r["num"]]
 RECIPES.append({"num":r["num"],"id":r["id"],"cat":CAT[r["cat"]][0],"d":(PT_TO_NL[name],prep,total,servings,kcal,carbs,protein,fat,[translate_ingredient(x) for x in ingredients],steps_nl,tip_nl,swap_nl)})
SELECTION=[]
for cat_pt,intro_pt,names in pt.SELECAO:
 cat_nl,intro_nl=CAT[cat_pt];SELECTION.append((cat_nl,intro_nl,[PT_TO_NL[n] for n in names]))

CSS=layout.CSS.replace("50 Low-Carb Recipes for Everyday Life","50 Low-Carb-Recepten voor elke dag")+"\nbody, p, li, td, th, .meta, .dica, .troca { font-family: 'DejaVu Sans', sans-serif; } h1, h2, h3 { font-family: 'DejaVu Serif', serif; } @page { margin-bottom: 6mm; } .dica { padding: 2mm 3mm; margin-top: 1.5mm; font-size: 7.7pt; } .troca { padding: 0.8mm 3mm; margin-top: 0.8mm; font-size: 7.3pt; line-height: 1.4; }"

FRONT="""
<section class="frente legal"><h2>Colofon en belangrijke informatie</h2><div class="filete"></div><p><b>50 Low-Carb-Recepten voor elke dag</b> — eerste editie, 2026.<br>Praktische Keuken · deel 1.</p><p>Alle rechten voorbehouden. Niets uit dit digitale boek mag zonder schriftelijke toestemming worden gekopieerd. Dit ebook is bestemd voor de koper.</p><div class="quadro"><b>BELANGRIJKE INFORMATIE:</b> de voedingswaarden (calorieën, koolhydraten, eiwitten en vetten) zijn <b>schattingen per portie</b>, berekend op basis van de ingrediëntenlijst en voedingswaardetabellen. Merken, productgrootte en bereidingswijze kunnen de waarden veranderen. Dit boek is educatief en vervangt geen advies van een arts of diëtist. Mensen met diabetes of nierproblemen, zwangere of borstvoedende mensen en iedereen die langdurig medicijnen gebruikt, moet deskundig advies vragen voordat koolhydraatbeperkt eten wordt gestart. Xylitol is giftig voor honden; houd zoetigheden buiten bereik van huisdieren.</div><p><b>Maten in dit boek:</b> 1 kopje = 240 ml · 1 eetlepel = 15 ml · 1 theelepel = 5 ml · ovens worden voorverwarmd tenzij anders vermeld.</p></section>
<section class="frente"><h2>Welkom in je low-carbkeuken</h2><div class="filete"></div><p>Dit is geen streng dieetboek. Het zijn <b>50 praktische antwoorden</b> op de vraag die elke eetgewoonte kan laten ontsporen: <i>“Wat zal ik vandaag koken?”</i></p><p>Low carb betekent niet dat je alleen saaie salades eet. Je krijgt romige omeletten, lasagne, een feestelijke stoofpot en zelfs cheesecake — met slimme vervangers voor meel en suiker, zonder twee aparte maaltijden te koken.</p><div class="quadro"><b>De gouden regel:</b> koolhydraten zijn een accent, niet de basis. De basis bestaat uit eiwit, goede vetten en groenten.</div><p>Kook zeven weken lang elke dag één nieuw recept en je hebt een repertoire dat zelfs een drukke maandag redt. Eet smakelijk.</p></section>
<section class="frente"><h2>Zo gebruik je dit boek</h2><div class="filete"></div><p><b>1. Begin achterin.</b> Bekijk het 7-dagenmenu en de boodschappenlijst voordat je boodschappen doet.</p><p><b>2. Maak de juiste portie dubbel.</b> De meeste lunch- en dinergerechten zijn voor twee personen; de tweede portie is de lunch van morgen.</p><p><b>3. Gebruik de kaders.</b> Elk recept bevat een <b>Kooktip</b> en een <b>Slimme vervanging</b> om ingrediënten aan te passen.</p><p><b>4. Jaag niet op nul koolhydraten.</b> De voedingswaarden helpen je kiezen; ze zijn geen gevangenis.</p><p><b>5. Vries met vertrouwen in.</b> Recepten met bewaartips zijn gemaakt voor individuele porties.</p></section>
<section class="frente"><h2>Vervangingen voor elke voorraadkast</h2><div class="filete"></div><p>Low carb draait ook om slimme wissels:</p><table><tr><th>Laat weg</th><th>Gebruik in plaats daarvan</th><th>Opmerking</th></tr><tr><td>Geraffineerde suiker</td><td><b>Erythritol of xylitol</b></td><td>1 op 1; xylitol is iets zoeter</td></tr><tr><td>Tarwemeel</td><td><b>Amandelmeel + 1 ei</b></td><td>gebruik de helft; ei geeft binding</td></tr><tr><td>Witte rijst</td><td><b>Bloemkoolrijst</b></td><td>5–6 minuten rauw op hoog vuur roerbakken</td></tr><tr><td>Pasta</td><td><b>Courgette, palmharten of konjac</b></td><td>90 seconden tot 3 minuten roerbakken</td></tr><tr><td>Aardappel</td><td><b>Bloemkool, knolraap of geroosterde radijs</b></td><td>voor puree en bouillon</td></tr></table><h2 style="margin-top:6mm">Handige voorraad</h2><div class="lista2"><ul><li>Amandelmeel en ongezoete geraspte kokos</li><li>Erythritol, xylitol en 100% cacao</li><li>Ongezoete kokosmelk en room</li><li>Olijfolie, kokosolie en boter</li><li>Eieren, mozzarella, Parmezaanse kaas en roomkaas</li><li>Bloemkool, courgette, aubergine, kool en boerenkool</li><li>Gepelde tomaten uit blik en olijven</li><li>Kip, gehakt, vis en tonijn uit blik</li><li>Noten, citroenen, verse kruiden en gerookt paprikapoeder</li></ul></div></section>
"""
BONUS="""
<section class="frente"><h2>Bonus 1 — 7-dagenmenu</h2><div class="filete"></div><p>Een realistisch plan voor de eerste week: vullende ontbijten, lunches die avondeten worden en op het juiste moment iets zoets.</p><table><tr><th>Dag</th><th>Ontbijt</th><th>Lunch</th><th>Snack</th><th>Avondeten</th></tr><tr><td class="dia">Ma</td><td>01 · omelet</td><td>10 + 23 · bloemkoolrijst met kip</td><td>09 · yoghurt met granola</td><td>37 · bloemkoolpizza</td></tr><tr><td class="dia">Di</td><td>05 · tapiocacrep</td><td>17 · auberginelasagne</td><td>06 · kaasbrood</td><td>31 · zalm + 44 · mousse</td></tr><tr><td class="dia">Wo</td><td>02 · magnetronbrood</td><td>11 · courgettenoedels</td><td>45 · kokosflan</td><td>35 · vis-moqueca</td></tr><tr><td class="dia">Do</td><td>07 · boerenkoolwrap</td><td>13 · kipsalade</td><td>08 · avocado-eieren</td><td>26 · steak met champignons</td></tr><tr><td class="dia">Vr</td><td>03 · bananenpannenkoekjes</td><td>16 · bloemkoolschotel</td><td>09 · yoghurt met granola</td><td>33 · knoflookgarnalen</td></tr><tr><td class="dia">Za</td><td>04 · hartige muffins</td><td>18 · gevulde aubergine</td><td>46 · chocoladeroom</td><td>42 · low-carb sushi</td></tr><tr><td class="dia">Zo</td><td>06 · kaasbrood</td><td>30 · pulled pork</td><td>47 · cheesecake</td><td>19 · boerenkoolsoep + 28 · biefstuk</td></tr></table></section>
<section class="frente"><h2>Bonus 2 — Boodschappenlijst voor de eerste week</h2><div class="filete"></div><p>Print deze lijst en neem hem mee. De hoeveelheden zijn bedoeld voor twee personen:</p><div class="lista2"><ul class="check"><li>2 dozijn eieren</li><li>1 kg kipfilet + 8 kippendijen</li><li>1 kg gehakt + 500 g steak</li><li>600 g zalm of stevige vis + 400 g garnalen</li><li>2 blikjes tonijn</li><li>500 g mozzarella + Parmezaanse kaas + roomkaas</li><li>Room</li><li>2 pakken ongezoete kokosmelk</li><li>Bloemkool, courgettes, aubergines, kool en boerenkool</li><li>Verse tomaten + 2 blikken gepelde tomaten</li><li>Avocado's, bananen, aardbeien en citroenen</li><li>Uien, knoflook, gember, kruiden en gerookt paprikapoeder</li><li>Olijven, palmharten, noten en pinda's</li><li>Amandelmeel, geraspte kokos en chia</li><li>Erythritol of xylitol, cacao en chocolade van 85%</li><li>Olijfolie, boter en kokosolie</li><li>Sojasaus en mosterd</li></ul></div></section>
<section class="frente"><h2>Voor je de keuken afsluit</h2><div class="filete"></div><p>Je hebt nu 50 recepten voor het echte leven: makkelijk verkrijgbare ingrediënten, eenvoudige bereiding en geplande restjes. Het verschil tussen dit ebook en een beter georganiseerde week begint met één kleine beslissing: <b>je volgende maaltijd</b>.</p><p>Kies vanavond één recept, maak het en deel het met iemand. Samen eten maakt herhalen makkelijker.</p><div class="quadro"><b>VOLGENDE DELEN VAN PRAKTISCHE KEUKEN:</b> Deel 2 — <i>Low-carbmaaltijden voor de week</i> · Deel 3 — <i>Feestelijke desserts zonder suiker</i>.</div></section>
"""
COVER="""<section class="capa"><div class="txt"><div class="kicker">Praktische Keuken · deel 1</div><h1>50 LOW-CARB-<br><span class="hl">RECEPTEN</span></h1><div class="sub">voor elke dag — zonder meel, zonder suiker, zonder gedoe</div></div><div class="faixa"><span class="marca">PRAKTISCHE KEUKEN</span><span>minder koolhydraten, meer dagelijks plezier</span></div></section>"""
BACK="""<section class="contra"><div class="in"><h2>Stop met elke maandag opnieuw beginnen.</h2><p>Dit boek verzamelt 50 recepten voor een low-carbritme zonder twee keer te koken: ontbijten die je ochtend dragen, lunches die avondeten worden, soep voor koude avonden en desserts zonder schuldgevoel.</p><ul><li><b>50 complete recepten</b> met tijd, opbrengst en geschatte waarden per portie;</li><li>een <b>Kooktip</b> bij elk recept;</li><li><b>Slimme vervangingen</b> om ingrediënten aan te passen;</li><li>een <b>7-dagenmenu</b> en printbare boodschappenlijst;</li><li>een <b>vervangingstabel</b> voor meel, suiker, rijst en pasta.</li></ul><p>Makkelijk verkrijgbare ingrediënten. Realistische bereidingstijd. Smaak die niet aan dieeteten doet denken.</p><div class="marca">PRAKTISCHE KEUKEN</div></div></section>"""

def recipe_html(r):
 num,rid,d=r["num"],r["id"],r["d"];name,prep,total,servings,kcal,carbs,protein,fat,ingredients,steps,tip,swap=d
 ing=''.join('<li>%s</li>'%H.escape(x) for x in ingredients);pas=''.join('<li>%s</li>'%H.escape(x) for x in steps)
 return '<section class="receita" id="%s"><header><div class="num">%02d</div><div class="titulo"><h3>%s</h3></div></header><img class="foto" src="imagens/receita-%02d.jpg" alt="%s"><div class="meta"><span><b>Bereiding</b> %d min</span><span><b>Totaal</b> %d min</span><span><b>Porties</b> %s</span><span><b>Moeilijkheid</b> makkelijk</span></div><div class="nutris"><span><b>%d</b>kcal / portie</span><span><b>%d g</b>koolhydraten</span><span><b>%d g</b>eiwitten</span><span><b>%d g</b>vetten</span></div><div class="corpo"><div><h4>Ingrediënten</h4><ul class="ing">%s</ul></div><div><h4>Bereiding</h4><ol class="passos">%s</ol></div></div><div class="dica"><b>KOOKTIP:</b> %s</div><div class="troca"><b>↺ SLIMME VERVANGING:</b> %s</div></section>'%(rid,num,H.escape(name),num,H.escape(name),prep,total,H.escape(str(servings)),kcal,carbs,protein,fat,ing,pas,H.escape(tip),H.escape(swap))

def toc_html(pmap=None):
 out=['<section class="frente"><h2>Inhoud</h2><div class="filete"></div><div class="sum"><table>'];idx=0
 for cat,intro,names in SELECTION:
  out.append('<tr><td class="cat" colspan="4">%s</td></tr>'%H.escape(cat))
  for name in names:
   idx+=1;pg=str(pmap[idx]) if pmap else '';out.append('<tr><td class="num">%02d</td><td><a href="#r%02d">%s</a></td><td class="dots"></td><td class="pg">%s</td></tr>'%(idx,idx,H.escape(name),pg))
 out.append('</table></div></section>');return ''.join(out)

def body_html():
 out=[]
 for chapter,(cat,intro,names) in enumerate(SELECTION,1):
  out.append('<section class="abre"><img class="capfoto" src="imagens/capitulo-%02d.jpg" alt="Afbeelding van hoofdstuk %s"><div class="tag">Hoofdstuk %02d</div><h2>%s</h2><div class="filete"></div><p>%s</p></section>'%(chapter,H.escape(cat),chapter,H.escape(cat),H.escape(intro)))
  for r in RECIPES:
   if r["cat"]==cat:out.append(recipe_html(r))
 return ''.join(out)

def render(pmap=None):return "<!DOCTYPE html><html lang='nl'><head><meta charset='utf-8'><style>%s</style></head><body>%s%s%s%s%s%s</body></html>"%(CSS,COVER,FRONT,toc_html(pmap),body_html(),BONUS,BACK)

def build():
 from weasyprint import HTML
 import fitz
 open('ebook_nl_probe.html','w').write(render(None));HTML(filename='ebook_nl_probe.html').write_pdf('ebook_nl_probe.pdf')
 d=fitz.open('ebook_nl_probe.pdf');pmap={}
 for i in range(d.page_count):
  text=d[i].get_text();norm=text.replace(' ','')
  if 'INGREDIËNTEN' in norm and 'BEREIDING' in norm:
   m=re.search(r'(?m)^(\d{2})\n',text)
   if m and 1<=int(m.group(1))<=50:pmap[int(m.group(1))]=i+1
 assert len(pmap)==50,(len(pmap),sorted(set(range(1,51))-set(pmap)))
 open('50-low-carb-recepten-nl.html','w').write(render(pmap));HTML(filename='50-low-carb-recepten-nl.html').write_pdf('50-low-carb-recepten-nl.pdf')
 print('Nederlandse PDF gemaakt:',len(pmap),'recepten')

if __name__=='__main__':build()
