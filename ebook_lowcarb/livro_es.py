# -*- coding: utf-8 -*-
"""Edición en español neutro LATAM de 50 Recetas Low Carb para el Día a Día."""
import html as H
import re
import livro as pt
from es_overrides import OVERRIDES

# Los nombres se adaptan a un español neutro latinoamericano. Se conserva "low carb"
# porque es el término comercial más reconocible en los mercados objetivo.
NOMBRES = [
 "Omelet al horno con espinaca y queso",
 "Pan low carb de microondas (2 minutos)",
 "Panqueques de banana con avena (sin harina)",
 "Muffins salados de huevo, verduras y tocino",
 "Tortilla de tapioca en sartén con queso y tomate",
 "Pan de queso en sartén",
 "Wrap de col rizada con pollo cremoso",
 "Huevos revueltos cremosos con aguacate y semillas",
 "Yogur proteico con granola de frutos secos",
 "Arroz de coliflor sencillo",
 "Fideos de calabacín con salsa de tomate casera",
 "Espaguetis de palmito al ajillo",
 "Ensalada completa de pollo con aderezo de yogur",
 "Ensalada de atún con huevo y mayonesa de limón",
 "Wrap de lechuga con carne molida picante",
 "Pastel de coliflor con carne seca",
 "Lasaña de berenjena a la boloñesa",
 "Berenjena rellena de carne molida",
 "Caldo verde low carb (sin papa)",
 "Sopa de calabaza con leche de coco y jengibre",
 "Sopa de verduras con pollo deshebrado",
 "Crema de calabacín con queso crema",
 "Pollo a la plancha con salsa de mostaza y crema",
 "Muslos de pollo al horno con limón y romero",
 "Pollo salteado estilo oriental low carb",
 "Filete con salsa de champiñones",
 "Carne molida con calabacín y tomate",
 "Bistec encebollado con mantequilla de ajo",
 "Albóndigas rellenas de queso en salsa de tomate",
 "Costillitas de cerdo deshebradas",
 "Salmón al horno con mantequilla de limón",
 "Tilapia empanizada con harina de almendras",
 "Camarones al ajillo",
 "Bacalao con coliflor y aceitunas",
 "Cazuela de pescado con leche de coco y palmito",
 "Calamares a la plancha con limón y hierbas",
 "Pizza de coliflor con mozzarella y albahaca",
 "Berenjena a la parmesana (sin empanizar)",
 "Feijoada low carb (sin frijoles)",
 "Pan de queso en freidora de aire",
 "Calabacín relleno de atún y queso crema",
 "Sushi low carb (rollitos de pepino)",
 "Rollitos de col rellenos de carne molida",
 "Mousse de chocolate con aguacate",
 "Flan de coco con eritritol",
 "Crema de chocolate tipo brigadeiro",
 "Cheesecake low carb de frutos rojos",
 "Galletas low carb de nueces y chocolate",
 "Trufas de chocolate con aceite de coco",
 "Dulce de cacahuate tipo paçoca low carb",
]

CAT = {
 "Café da manhã e lanches rápidos": ("Desayunos y tentempiés rápidos", "Empieza el día con recetas prácticas y saciantes, sin depender del pan tradicional. Este capítulo reúne huevos, quesos, harinas de almendras o coco y frutas en porciones equilibradas. La mayoría de las opciones requiere hasta 15 minutos de preparación activa."),
 "Almoços completos": ("Almuerzos completos", "Platos de una sola olla, ensaladas que sostienen toda la tarde y sustitutos del arroz y la pasta, sin aspecto de comida de dieta."),
 "Sopas e caldos": ("Sopas y caldos", "Para las noches frías y para llevar: cremosidad sin papa y sin harina de trigo."),
 "Carnes e aves": ("Carnes y aves", "La proteína es la base de un buen menú low carb: aquí aparece dorada, jugosa y con salsas de verdad; nada de pollo seco de comida preparada."),
 "Peixes e frutos do mar": ("Pescados y mariscos", "Del salmón del domingo a las sardinas del lunes: grasas buenas, preparación rápida y sabor de restaurante."),
 "Jantares em até 30 minutos de bancada": ("Cenas listas en hasta 30 minutos", "La regla de la noche: la cena queda lista antes de que termine el episodio. Recetas de una olla, una bandeja o una freidora de aire."),
 "Sobremesas sem açúcar": ("Postres sin azúcar", "Un postre de verdad no necesita azúcar refinada: cacao, coco, nueces y endulzantes que no engañan al paladar."),
}

# Traducción de expresiones culinarias frecuentes. Se aplica primero por frases largas
# y después por palabras completas para evitar traducciones dentro de otras palabras.
PHRASES = [
 ("salada com molho separado", "ensalada con aderezo por separado"),
 ("molho separado", "aderezo por separado"), ("molho junto", "aderezo junto"),
 ("na marmita", "en el recipiente"), ("grão-de-bico", "garbanzos"),
 ("pimenta-do-reino", "pimienta negra"), ("cheiro-verde", "hierbas frescas picadas"),
 ("couve manteiga", "col rizada"), ("couve-flor", "coliflor"), ("couve", "col rizada"),
 ("abobrinha", "calabacín"), ("berinjela", "berenjena"), ("palmito pupunha", "palmito"),
 ("tomate pelado", "tomates pelados"), ("creme de leite fresco", "crema para batir"),
 ("creme de leite", "crema de leche"), ("cream cheese", "queso crema"),
 ("requeijão", "queso crema"), ("muçarela", "mozzarella"),
 ("queijo parmesão", "queso parmesano"), ("queijo ralado", "queso rallado"),
 ("queijo", "queso"), ("farinha de amêndoas", "harina de almendras"),
 ("farinha de coco", "harina de coco"), ("farinha de linhaça dourada", "harina de linaza dorada"),
 ("polvilho azedo", "almidón de yuca agrio"), ("goma de tapioca", "goma de tapioca"),
 ("leite de coco", "leche de coco"), ("leite condensado", "leche condensada"),
 ("leite em pó", "leche en polvo"), ("carne seca", "carne seca"),
 ("carne moída", "carne molida"), ("frango desfiado", "pollo deshebrado"),
 ("peito de frango", "pechuga de pollo"), ("ovos mexidos", "huevos revueltos"),
 ("ovos cozidos", "huevos cocidos"), ("ovo cozido", "huevo cocido"),
 ("uvas-passas", "pasas"), ("castanha-de-caju", "anacardos"),
 ("castanha do pará", "nueces de Brasil"), ("castanhas", "frutos secos"),
 ("manteiga de amendoim", "mantequilla de cacahuate"), ("pasta de amendoim", "mantequilla de cacahuate"),
 ("amendoim", "cacahuate"), ("morangos", "fresas"), ("morango", "fresa"),
 ("banana", "banana"), ("abacate", "aguacate"), ("abóbora", "calabaza"),
 ("pepino", "pepino"), ("tomate", "tomate"), ("cebola", "cebolla"),
 ("alho", "ajo"), ("dentes", "dientes"), ("dente", "diente"),
 ("salsão", "apio"), ("vagem", "ejotes"), ("cenoura", "zanahoria"),
 ("pimentão", "pimiento"), ("cogumelos", "champiñones"), ("shimeji", "shimeji"),
 ("salmão", "salmón"), ("camarão", "camarón"), ("camarões", "camarones"),
 ("atum", "atún"), ("gomo", "gajo"), ("gomos", "gajos"),
 ("tilápia", "tilapia"), ("bacalhau", "bacalao"), ("lula", "calamar"),
 ("costelinha", "costillitas"), ("linguiça", "longaniza"), ("linguiça portuguesa", "chorizo portugués"),
 ("calabresa", "longaniza"), ("paio", "chorizo"), ("bacon", "tocino"),
 ("presunto cru", "jamón serrano"), ("presunto", "jamón"), ("iogurte", "yogur"),
 ("azeitona", "aceituna"), ("azeitonas", "aceitunas"), ("azeite", "aceite de oliva"),
 ("vinagre de maçã", "vinagre de manzana"), ("vinagre de vinho tinto", "vinagre de vino tinto"),
 ("mostarda dijon", "mostaza Dijon"), ("mostarda", "mostaza"), ("shoyu", "salsa de soya"),
 ("molho de tomate", "salsa de tomate"), ("molho de tomate caseiro", "salsa de tomate casera"),
 ("molho", "salsa"), ("caldo de legumes", "caldo de verduras"), ("caldo de galinha", "caldo de pollo"),
 ("caldo de carne", "caldo de carne"), ("páprica defumada", "pimentón ahumado"),
 ("páprica", "pimentón"), ("orégano", "orégano"), ("manjericão", "albahaca"),
 ("salsinha", "perejil"), ("cebolinha", "cebollín"), ("coentro", "cilantro"),
 ("alecrim", "romero"), ("gengibre", "jengibre"), ("canela", "canela"),
 ("cacau em pó", "cacao en polvo"), ("cacau", "cacao"), ("chocolate", "chocolate"),
 ("coco ralado", "coco rallado"), ("coco em flocos", "coco en hojuelas"),
 ("sementes de girassol", "semillas de girasol"), ("sementes de abóbora", "semillas de calabaza"),
 ("sementes de chia", "semillas de chía"), ("sementes", "semillas"),
 ("farinha", "harina"), ("açúcar", "azúcar"), ("adoçante", "endulzante"),
 ("eritritol", "eritritol"), ("xilitol", "xilitol"), ("baunilha", "vainilla"),
 ("essência", "esencia"), ("fermento em pó", "polvo para hornear"),
 ("em pó", "en polvo"), ("sem açúcar", "sin azúcar"), ("sem farinha", "sin harina"),
 ("sem sementes", "sin semillas"), ("sem pele", "sin piel"), ("sem sal", "sin sal"),
 ("sem caroço", "sin semillas"), ("a gosto", "al gusto"), ("para servir", "para servir"),
 ("para finalizar", "para terminar"), ("para rechear", "para rellenar"),
 ("em cubos", "en cubos"), ("em rodelas", "en rodajas"), ("em fatias", "en rebanadas"),
 ("em tiras", "en tiras"), ("picada", "picada"), ("picado", "picado"),
 ("picadas", "picadas"), ("picados", "picados"), ("ralada", "rallada"), ("ralado", "rallado"),
 ("raladas", "ralladas"), ("ralados", "rallados"), ("escorrido", "escurrido"),
 ("escorrida", "escurrida"), ("escorridas", "escurridas"), ("desfiado", "deshebrado"),
 ("desfiada", "deshebrada"), ("desfiados", "deshebrados"), ("espremida", "exprimida"),
 ("espremido", "exprimido"), ("maduro", "maduro"), ("maduros", "maduros"),
 ("fresco", "fresco"), ("fresca", "fresca"), ("congelado", "congelado"),
 ("derretida", "derretida"), ("derretido", "derretido"), ("cozida", "cocida"),
 ("cozido", "cocido"), ("quente", "caliente"), ("morno", "tibio"),
 ("crocante", "crujiente"), ("cremoso", "cremoso"), ("cremosa", "cremosa"),
 ("xíc.", "taza"), ("col. sopa", "cda."), ("col. chá", "cdta."),
 ("col.", "cda."), ("L de", "l de"), ("unid.", "unidad"),
]

# Los pasos, el consejo y la sustitución de cada receta están redactados a mano
# en es_overrides.py. Motivo: el español y el portugués comparten mucho léxico
# pero no la sintaxis, así que sustituir palabra por palabra producía frases
# híbridas invendibles ("enxágue y seque bem", "é obrigatório: sin isso").
# Este traductor se ocupa SOLO de las listas de ingredientes, que son frases
# nominales cortas donde un mapa léxico sí funciona.
# --- Vocabulário acrescentado na revisão: plurais, cortes, utensílios e
# --- adjetivos que o mapa original não cobria.
PHRASES += [
 ("alface americana", "lechuga iceberg"), ("frutas vermelhas", "frutos rojos"),
 ("pimenta calabresa", "hojuelas de chile"), ("pimenta-branca", "pimienta blanca"),
 ("noz-moscada", "nuez moscada"), ("sal grosso", "sal gruesa"),
 ("farelo de aveia", "salvado de avena"), ("amido de milho", "fécula de maíz"),
 ("azeite de dendê", "aceite de dendê"), ("azeite comum", "aceite de oliva normal"),
 ("cogumelos paris", "champiñones"), ("filé-mignon", "filete mignon"),
 ("copa-lombo", "cabeza de lomo"), ("camarão limpo", "camarones limpios"),
 ("folha de louro", "hoja de laurel"), ("folhas de louro", "hojas de laurel"),
 ("creme azedo", "crema agria"), ("em temperatura ambiente", "a temperatura ambiente"),
 ("para cobertura", "para cubrir"), ("para enrolar", "para cubrir"),
 ("para acompanhar", "para acompañar"), ("ao meio", "por la mitad"),
 ("em fios", "en tiras"), ("abóbora cabotiá", "calabaza kabocha"),
 ("pepino japonês", "pepino japonés"), ("couve refogada", "col rizada sofrita"),
 ("ovos", "huevos"), ("ovo", "huevo"), ("parmesão", "parmesano"),
 ("berinjelas", "berenjenas"), ("abobrinhas", "calabacines"), ("cebolas", "cebollas"),
 ("cenouras", "zanahorias"), ("pimentões", "pimientos"), ("limões", "limones"),
 ("abacates", "aguacates"), ("pepinos", "pepinos"), ("amêndoas", "almendras"),
 ("amêndoa", "almendra"), ("sobrecoxas", "muslos"), ("sobrecoxa", "muslo"),
 ("alcatra", "lomo"), ("contrafilé", "sirloin"), ("costelas", "costillas"),
 ("costela", "costilla"), ("filés", "filetes"), ("filé", "filete"),
 ("postas", "medallones"), ("posta", "medallón"), ("anéis", "anillos"),
 ("buquês", "floretes"), ("buquê", "florete"), ("grãos", "granos"),
 ("ramos", "ramas"), ("ramo", "rama"), ("maço", "manojo"),
 ("pedaços", "trozos"), ("pedaço", "trozo"), ("raspas", "ralladura"),
 ("vidros", "frascos"), ("vidro", "frasco"), ("espaguete", "espagueti"),
 ("fios", "tiras"), ("fatias", "rebanadas"), ("fatia", "rebanada"),
 ("fatiada", "en rebanadas"), ("fatiado", "en rebanadas"),
 ("rodelas", "rodajas"), ("rodela", "rodaja"), ("laminados", "en láminas"),
 ("laminado", "en láminas"), ("amassados", "machacados"), ("amassado", "machacado"),
 ("lata", "lata"), ("latas", "latas"), ("alface", "lechuga"), ("repolho", "col"),
 ("espinafre", "espinaca"), ("fermento", "polvo para hornear"),
 ("farelo", "salvado"), ("aveia", "avena"), ("torresmo", "chicharrón"),
 ("crouton", "crutones"), ("gergelim", "ajonjolí"), ("hortelã", "menta"),
 ("tomilho", "tomillo"), ("endro", "eneldo"), ("cominho", "comino"),
 ("laranja", "naranja"), ("acompanhar", "acompañar"), ("cobertura", "cobertura"),
 ("badejo", "mero"), ("pescada", "merluza"), ("peixes", "pescados"),
 ("peixe", "pescado"), ("patinho", "pulpa"), ("acém", "aguja"),
 ("porco", "cerdo"), ("pele", "piel"), ("folha", "hoja"),
 ("dessalgadas", "desaladas"), ("dessalgada", "desalada"),
 ("dessalgado", "desalado"), ("dessalgados", "desalados"),
 ("refogadas", "sofritas"), ("refogada", "sofrita"), ("refogado", "sofrito"),
 ("inteiras", "enteras"), ("inteira", "entera"), ("inteiros", "enteros"),
 ("vermelhas", "rojas"), ("vermelha", "roja"), ("vermelhos", "rojos"),
 ("vermelho", "rojo"), ("pretas", "negras"), ("preta", "negra"),
 ("roxa", "morada"), ("roxo", "morado"), ("médias", "medianas"),
 ("média", "mediana"), ("médios", "medianos"), ("médio", "mediano"),
 ("pequenas", "pequeñas"), ("pequena", "pequeña"), ("pequenos", "pequeños"),
 ("pequeno", "pequeño"), ("limpos", "limpios"), ("limpa", "limpia"),
 ("limpo", "limpio"), ("mix", "mezcla"), ("bem", "bien"), ("pitada", "pizca"),
 ("processada", "procesada"), ("processado", "procesado"),
 ("processadas", "procesadas"), ("processados", "procesados"),
]


OU = "\x00OU\x00"

# Sustituciones que el mapa palabra por palabra no puede resolver porque el
# español exige otro género, otro número u otro orden que el portugués.
ING_EXACT = [
 ("1 xíc. de espinafre picado (fresco ou congelado, espremido)",
  "1 taza de espinaca picada (fresca o congelada, exprimida)"),
 ("1/2 xíc. de vagem picada", "1/2 taza de ejotes picados"),
 ("1/2 xíc. de castanha-de-caju torrada", "1/2 taza de anacardos tostados"),
 ("5 morangos picados", "5 fresas picadas"),
 ("400 g de camarão limpo", "400 g de camarones limpios"),
 ("1 xíc. de frutas vermelhas congeladas", "1 taza de frutos rojos congelados"),
 ("1/2 abobrinha ralada e espremida", "1/2 calabacín rallado y exprimido"),
 ("2 col. sopa de cebolinha picada", "2 cdas. de cebollín picado"),
 ("cebolinha picada, sal e pimenta", "cebollín picado, sal y pimienta"),
 ("4 xíc. de folhas variadas", "4 tazas de hojas verdes variadas"),
 ("3 abobrinhas médias", "3 calabacines medianos"),
 ("sal, pimenta e salsa picada", "sal, pimienta y perejil picado"),
 ("1 dente de alho ralado, salsa, sal e pimenta",
  "1 diente de ajo rallado, perejil, sal y pimienta"),
 ("1 repolho médio", "1 col mediana"),
 ("2 bifes de alcatra ou contrafilé", "2 bistecs de lomo o sirloin"),
 ("mix de castanhas picadas (pará, caju, amêndoa)",
  "mezcla de frutos secos picados (nueces de Brasil, anacardos, almendras)"),
 ("2 bifes altos de filé-mignon ou alcatra", "2 bistecs gruesos de filete mignon o lomo"),
 ("1 col. sopa de amido de milho diluído em 3 de água (opcional)",
  "1 cda. de fécula de maíz disuelta en 3 cdas. de agua (opcional)"),
 ("1 1/2 xíc. de farinha de amêndoas", "1 1/2 tazas de harina de almendras"),
 ("1 1/2 xíc. de amendoim torrado sem pele e sem sal",
  "1 1/2 tazas de cacahuate tostado sin piel y sin sal"),
]


def translate_text(value):
    """Traduce un ingrediente del portugués al español neutro LATAM."""
    s = str(value)
    for a, b in ING_EXACT:
        s = s.replace(a, b)
    # La conjunción "ou" se protege con un centinela antes de cualquier pasada.
    # Si se convierte en "o" demasiado pronto, el corrector de género la
    # confunde con el artículo masculino y produce "mantequilla el aceite de coco".
    s = re.sub(r"(?<!\w)ou(?!\w)", OU, s, flags=re.IGNORECASE)
    # Las frases largas van primero para no traducir dentro de otras palabras.
    for a, b in sorted(PHRASES, key=lambda x: len(x[0]), reverse=True):
        s = re.sub(r"(?<!\w)" + re.escape(a) + r"(?!\w)", b, s, flags=re.IGNORECASE)
    for a, b in sorted(WORD_MAP, key=lambda x: len(x[0]), reverse=True):
        s = re.sub(r"(?<!\w)" + re.escape(a) + r"(?!\w)", b, s, flags=re.IGNORECASE)
    # Artículos y conectores. "ou" queda fuera: se restituye al final.
    articles = [("do", "del"), ("da", "de la"), ("os", "los"), ("as", "las"),
                ("uma", "una"), ("duas", "dos"), ("dois", "dos"), ("um", "un"),
                ("com", "con"), ("sem", "sin"), ("em", "en"), ("no", "en el"),
                ("na", "en la"), ("e", "y")]
    for a, b in articles:
        s = re.sub(r"(?<!\w)" + re.escape(a) + r"(?!\w)", b, s, flags=re.IGNORECASE)
    s = s.replace(OU, "o")
    # Plurales de medida: "3 cda." -> "3 cdas.".
    # O lookahead original usava \b depois do ponto, que nunca casava
    # ("." e " " são ambos não-palavra), então nada era pluralizado.
    # E (?<!\w) deixava passar o "2" de "1/2 taza", pluralizando frações.
    s = re.sub(r"(?<![\w/.])([2-9]\d*) taza(?![\w])", r"\1 tazas", s)
    s = re.sub(r"(?<![\w/.])([2-9]\d*) cda\.", r"\1 cdas.", s)
    s = re.sub(r"(?<![\w/.])([2-9]\d*) cdta\.", r"\1 cdtas.", s)
    s = s.replace("g cada)", "g cada uno)")
    return s


WORD_MAP = [
 ("faça", "haz"), ("aceita", "acepta"), ("qualquer", "cualquier"), ("tire", "retira"),
 ("bifes", "bistecs"), ("bife", "bistec"), ("gelado", "frío"), ("geladeira", "refrigerador"), ("óleo", "aceite"),
 ("fogo", "fuego"), ("panela", "olla"), ("forno", "horno"), ("água", "agua"),
 ("ainda", "aún"), ("receita", "receta"), ("pote", "recipiente"), ("potes", "recipientes"),
 ("caneca", "taza"), ("versão", "versión"), ("refogo", "sofrito"), ("dourar", "dorar"),
 ("cruas", "crudas"), ("crua", "cruda"), ("cru", "crudo"), ("depois", "después"),
 ("muita", "mucha"), ("muito", "mucho"), ("leve", "ligera"), ("soltam", "sueltan"),
 ("vira", "se convierte"), ("virar", "convertirse"), ("recheie", "rellena"), ("rechear", "rellenar"),
 ("escorra", "escurre"), ("escorredor", "colador"), ("trocar", "cambiar"), ("desligue", "apaga"),
 ("desligado", "apagado"), ("fervente", "hirviendo"), ("louro", "laurel"), ("trocando", "cambiando"),
 ("pano de prato", "paño de cocina"), ("calor", "calor"), ("frango", "pollo"), ("peito", "pechuga"), ("grelhe", "cocina a la plancha"),
 ("grelhado", "a la plancha"), ("grelhada", "a la plancha"), ("folhas", "hojas"),
 ("limão", "limón"), ("pimenta", "pimienta"), ("ervas", "hierbas"),
 ("salada", "ensalada"), ("saladas", "ensaladas"), ("marmita", "recipiente"),
 ("suco", "jugo"), ("sucos", "jugos"), ("tigelas", "tazones"), ("duas", "dos"),
 ("aumente", "aumenta"), ("some", "suma"), ("maionese", "mayonesa"), ("manteiga", "mantequilla"),
 ("dica", "consejo"), ("troque", "cambia"), ("troca", "cambio"),
 ("murcha", "se marchita"), ("murchar", "marchitarse"), ("cozinha", "cocina"),
 ("cozinhar", "cocinar"), ("preparo", "preparación"), ("rende", "rinde"),
 ("dificuldade", "dificultad"), ("porção", "porción"), ("gorduras", "grasas"),
]

# Recria os dados das receitas: nomes e ingredientes traduzidos por mapa,
# enquanto passos, dica e troca vêm redigidos à mão de es_overrides.py.
PT_TO_ES = {r["d"][0]: NOMBRES[r["num"] - 1] for r in pt.RECEITAS}
RECETAS = []
for r in pt.RECEITAS:
    d = r["d"]
    nome, prep, tot, porc, kcal, carb, prot, gord, ings, passos, dica, troca = d
    passos_es, dica_es, troca_es = OVERRIDES[r["num"]]
    assert len(passos_es) == len(passos), (r["num"], len(passos_es), len(passos))
    RECETAS.append({
        "num": r["num"], "id": r["id"], "cat": CAT[r["cat"]][0],
        "d": (PT_TO_ES[nome], prep, tot, porc, kcal, carb, prot, gord,
              [translate_text(x) for x in ings],
              passos_es, dica_es, troca_es)
    })
POR_NUM = {r["num"]: r for r in RECETAS}

# Categoria e receitas na ordem editorial do original.
SELECAO = []
for cat_pt, intro_pt, nomes in pt.SELECAO:
    cat_es, intro_es = CAT[cat_pt]
    SELECAO.append((cat_es, intro_es, [PT_TO_ES[n] for n in nomes]))

CSS = pt.CSS.replace("50 Receitas Low Carb para o Dia a Dia", "50 Recetas Low Carb para el Día a Día")

# Textos editoriais da edição hispânica.
FRENTE = """
<section class="frente legal">
  <h2>Créditos y aviso legal</h2><div class="filete"></div>
  <p><b>50 Recetas Low Carb para el Día a Día</b> — 1.ª edición, 2026.<br>
  Serie Cocina Práctica · volumen 1.</p>
  <p>Todos los derechos reservados. Se prohíbe la reproducción total o parcial de este material por cualquier medio sin autorización escrita. Este ebook es un producto digital destinado al comprador: comparte únicamente el enlace oficial de venta.</p>
  <div class="quadro"><b>AVISO IMPORTANTE:</b> la información nutricional (calorías, carbohidratos, proteínas y grasas) es una <b>estimación por porción</b>, calculada a partir de la lista de ingredientes y tablas de composición de alimentos. Puede variar según la marca, el tamaño de los alimentos y los utensilios. Este libro tiene carácter educativo y <b>no sustituye</b> la orientación de un médico o nutricionista. Las personas con diabetes, enfermedad renal, mujeres embarazadas, en periodo de lactancia o quienes toman medicamentos de forma continua deben consultar a un profesional antes de adoptar una alimentación restringida en carbohidratos. Los endulzantes como eritritol y xilitol son seguros para la mayoría de las personas en cantidades moderadas; en exceso pueden causar molestias digestivas. El xilitol es tóxico para los perros: mantén los postres fuera del alcance de las mascotas.</div>
  <p><b>Medidas usadas en este libro:</b> 1 taza = 240 ml · 1 cda. = 15 ml · 1 cdta. = 5 ml · 1 cda. rasa = sin montañita · horno siempre precalentado, salvo indicación contraria.</p>
  <p class="legal">Diagramación y fotografías ilustrativas generadas con fines editoriales.</p>
</section>

<section class="frente">
  <h2>Bienvenido a tu cocina low carb</h2><div class="filete"></div>
  <p>No compraste un libro de dieta. Compraste <b>50 respuestas listas</b> para la pregunta que puede arruinar cualquier cambio de alimentación: <i>“¿qué preparo hoy?”</i>.</p>
  <p>Comer low carb no significa vivir de ensaladas tristes. Significa disfrutar una omelet cremosa, una lasaña que se corta en porciones, una feijoada de domingo y hasta un cheesecake, cambiando la harina y el azúcar por ingredientes que sacian, sin cocinar dos veces.</p>
  <p>Las recetas fueron elegidas con tres criterios: <b>ingredientes fáciles de encontrar</b>, <b>tiempo real de una persona ocupada</b> y <b>sobras que resuelven el día siguiente</b>.</p>
  <div class="quadro"><b>La regla de oro de este libro:</b> el carbohidrato es un acento, no la base del plato. Aparece para aportar sabor y color —tomate, zanahoria, fruta—, mientras la base es siempre proteína, grasa buena y verduras.</div>
  <p>Prepara una receta nueva al día durante siete semanas y tendrás un repertorio capaz de salvar cualquier lunes. Buen provecho.</p>
</section>

<section class="frente">
  <h2>Cómo usar este libro en la práctica</h2><div class="filete"></div>
  <p><b>1. Empieza por el final.</b> Revisa el bono “Menú de 7 días” y la lista de compras antes de ir al supermercado. Cocinar sin plan es la forma más rápida de pedir comida a domicilio el jueves.</p>
  <p><b>2. Duplica la receta correcta.</b> Casi todas las recetas de almuerzo y cena rinden dos porciones: la segunda es el almuerzo de mañana.</p>
  <p><b>3. Usa los recuadros.</b> Cada receta tiene un <b>Consejo de cocina</b> y un <b>Cambio inteligente</b> para adaptar la preparación sin salir del estilo low carb.</p>
  <p><b>4. No persigas cero carbohidratos.</b> Las cantidades nutricionales están para ayudarte a elegir, no para convertir la comida en una prisión.</p>
  <p><b>5. Congela sin miedo.</b> Las recetas con indicaciones de congelación fueron pensadas para porciones individuales y recipientes cerrados.</p>
</section>

<section class="frente">
  <h2>Sustituciones que salvan cualquier despensa</h2><div class="filete"></div>
  <p>Comer low carb también es saber hacer cambios. Memoriza esta tabla y nunca volverás a depender de la harina y el azúcar:</p>
  <table>
    <tr><th>Retira de la receta</th><th>Usa en su lugar</th><th>Proporción / observación</th></tr>
    <tr><td>Azúcar refinada</td><td><b>Eritritol o xilitol</b></td><td>1:1; el xilitol endulza un poco más</td></tr>
    <tr><td>Harina de trigo</td><td><b>Harina de almendras + 1 huevo</b></td><td>usa la mitad de la cantidad; el huevo da estructura</td></tr>
    <tr><td>Arroz blanco</td><td><b>Coliflor procesada</b></td><td>saltea cruda a fuego alto durante 5–6 minutos</td></tr>
    <tr><td>Pasta</td><td><b>Calabacín, palmito o konjac</b></td><td>saltea de 90 segundos a 3 minutos</td></tr>
    <tr><td>Papa</td><td><b>Coliflor, nabo o rábano asado</b></td><td>para purés y caldos; usa la calabaza con moderación</td></tr>
    <tr><td>Salsa preparada</td><td><b>Tomate entero pelado + condimentos</b></td><td>cocina a fuego bajo durante 20 minutos</td></tr>
  </table>
  <h2 style="margin-top:6mm">Despensa comodín</h2>
  <div class="lista2"><ul>
    <li>Harina de almendras y coco rallado sin azúcar</li><li>Eritritol o xilitol y cacao 100%</li>
    <li>Leche y crema de coco sin azúcar</li><li>Aceite de oliva, aceite de coco y mantequilla</li>
    <li>Huevos y quesos: mozzarella, parmesano, queso crema</li><li>Coliflor, calabacín, berenjena, repollo y col rizada</li>
    <li>Tomate entero pelado en lata y aceitunas</li><li>Pollo, carne molida, pescado y atún en lata</li>
    <li>Frutos secos, limones, hierbas frescas y pimentón ahumado</li><li>Semillas de chía y linaza dorada</li>
  </ul></div>
</section>
"""

BONUS = """
<section class="frente">
  <h2>Bono 1 — Menú de 7 días</h2><div class="filete"></div>
  <p>Un plan realista para la primera semana: desayunos completos, almuerzos que se convierten en cena y un postre en el momento adecuado. Los números corresponden a las recetas de este libro.</p>
  <table>
    <tr><th>Día</th><th>Desayuno</th><th>Almuerzo</th><th>Tentempié</th><th>Cena</th></tr>
    <tr><td class="dia">Lun</td><td>01 · Omelet al horno</td><td>10 + 23 · arroz de coliflor con pollo</td><td>09 · yogur con granola</td><td>37 · pizza de coliflor</td></tr>
    <tr><td class="dia">Mar</td><td>05 · tortilla de tapioca</td><td>17 · lasaña de berenjena</td><td>06 · pan de queso</td><td>31 · salmón + 44 · mousse</td></tr>
    <tr><td class="dia">Mié</td><td>02 · pan de microondas</td><td>11 · fideos de calabacín</td><td>45 · flan de coco</td><td>35 · cazuela de pescado</td></tr>
    <tr><td class="dia">Jue</td><td>07 · wrap de col rizada</td><td>13 · ensalada completa de pollo</td><td>08 · huevos con aguacate</td><td>26 · filete con champiñones</td></tr>
    <tr><td class="dia">Vie</td><td>03 · panqueques de banana</td><td>16 · pastel de coliflor</td><td>09 · yogur con granola</td><td>33 · camarones al ajillo</td></tr>
    <tr><td class="dia">Sáb</td><td>04 · muffins salados</td><td>18 · berenjena rellena</td><td>46 · crema de chocolate</td><td>42 · sushi low carb</td></tr>
    <tr><td class="dia">Dom</td><td>06 · pan de queso</td><td>30 · costillitas deshebradas</td><td>47 · cheesecake</td><td>19 · caldo verde + 28 · bistec encebollado</td></tr>
  </table>
  <p class="legal">Las porciones deben ajustarse a tus necesidades. Este menú es una sugerencia educativa, no una prescripción.</p>
</section>

<section class="frente">
  <h2>Bono 2 — Lista de compras de la primera semana</h2><div class="filete"></div>
  <p>Imprime esta lista y llévala al supermercado. Está pensada para dos personas:</p>
  <div class="lista2"><ul class="check">
    <li>2 docenas de huevos</li><li>1 kg de pechuga de pollo + 8 muslos</li><li>1 kg de carne molida + 500 g de filete</li>
    <li>600 g de salmón o pescado firme + 400 g de camarones</li><li>2 latas de atún</li><li>500 g de mozzarella + parmesano + queso crema</li>
    <li>Crema para batir y crema de leche</li><li>2 envases de leche de coco sin azúcar</li><li>Coliflor, calabacín, berenjena, repollo y col rizada</li>
    <li>Tomates maduros + 2 latas de tomate entero pelado</li><li>Aguacate, bananas, fresas y limones</li><li>Cebolla, ajo, jengibre, hierbas y pimentón ahumado</li>
    <li>Aceitunas, palmito, frutos secos y cacahuates</li><li>Harina de almendras, coco rallado y chía</li><li>Eritritol o xilitol, cacao 100% y chocolate 85%</li>
    <li>Aceite de oliva, mantequilla y aceite de coco</li><li>Salsa de soya y mostaza</li>
  </ul></div>
  <div class="quadro"><b>Regla del mercado:</b> recorre primero frutas, verduras y carnes; deja los productos empacados para el final y revisa siempre la etiqueta.</div>
</section>

<section class="frente">
  <h2>Antes de cerrar la cocina</h2><div class="filete"></div>
  <p>Ahora tienes 50 recetas pensadas para la vida real: ingredientes fáciles de encontrar, una sola olla y sobras planeadas. Lo que separa este ebook de una semana más organizada es una decisión pequeña: <b>tu próxima comida</b>.</p>
  <p>Elige una receta para esta noche, prepárala y compártela con alguien. La comida que se comparte se vuelve más fácil de repetir.</p>
  <div class="quadro"><b>PRÓXIMOS VOLÚMENES DE COCINA PRÁCTICA:</b> Volumen 2 — <i>Comidas low carb para la semana</i> · Volumen 3 — <i>Postres de fiesta sin azúcar</i>.</div>
</section>
"""

CAPA = """
<section class="capa"><div class="txt">
    <div class="kicker">Serie Cocina Práctica · vol. 1</div>
    <h1>50 RECETAS<br><span class="hl">LOW CARB</span></h1>
    <div class="sub">para el día a día — sin harina, sin azúcar y sin sacrificar el sabor</div>
  </div>
  <div class="faixa"><span class="marca">COCINA PRÁCTICA</span><span>menos carbohidratos, más vida real</span></div>
</section>"""

CONTRA = """
<section class="contra"><div class="in">
  <h2>Deja de empezar la dieta cada lunes.</h2>
  <p>Este libro reúne 50 recetas para mantener una rutina low carb sin cocinar dos veces: desayunos que sostienen la mañana, almuerzos que se convierten en cena, sopas para las noches frías y postres que no necesitan disculpas.</p>
  <ul>
    <li><b>50 recetas completas</b> con tiempo, rendimiento y macros estimadas por porción;</li>
    <li><b>Consejo de cocina</b> en cada receta para evitar el error más común;</li>
    <li><b>Cambio inteligente</b> para adaptar los ingredientes;</li>
    <li><b>Menú de 7 días</b> y lista de compras lista para imprimir;</li>
    <li><b>Tabla de sustituciones</b> para harina, azúcar, arroz y pasta.</li>
  </ul>
  <p>Ingredientes fáciles de encontrar. Tiempo de una persona ocupada. Sabor de quien no se siente a dieta.</p>
  <div class="marca">COCINA PRÁCTICA</div>
</div></section>"""


def receta_html(r, markers=True):
    num, rid, d = r["num"], r["id"], r["d"]
    nome, prep, tot, porc, kcal, carb, prot, gord, ings, passos, dica, troca = d
    marc = '<span class="marcador">@@%s@@</span>' % rid if markers else ""
    ing = "".join("<li>%s</li>" % H.escape(i) for i in ings)
    pas = "".join("<li>%s</li>" % H.escape(p) for p in passos)
    return """
<section class="receita" id="%s">%s
  <header><div class="num">%02d</div><div class="titulo"><h3>%s</h3></div></header>
  <img class="foto" src="imagens/receita-%02d.jpg" alt="%s">
  <div class="meta"><span><b>Preparación</b> %d min</span><span><b>Total</b> %d min</span><span><b>Rinde</b> %s</span><span><b>Dificultad</b> fácil</span></div>
  <div class="nutris"><span><b>%d</b>kcal / porción</span><span><b>%d g</b>carbohidratos</span><span><b>%d g</b>proteínas</span><span><b>%d g</b>grasas</span></div>
  <div class="corpo"><div><h4>Ingredientes</h4><ul class="ing">%s</ul></div><div><h4>Modo de preparación</h4><ol class="passos">%s</ol></div></div>
  <div class="dica"><b>CONSEJO DE COCINA:</b> %s</div>
  <div class="troca"><b>↺ CAMBIO INTELIGENTE:</b> %s</div>
</section>""" % (rid, marc, num, H.escape(nome), num, H.escape(nome), prep, tot, H.escape(str(porc)), kcal, carb, prot, gord, ing, pas, H.escape(dica), H.escape(troca))


def sumario_html(pmap=None):
    out = ['<section class="frente"><h2>Índice</h2><div class="filete"></div><div class="sum"><table>']
    idx = 0
    for cat_nome, cat_intro, nomes in SELECAO:
        out.append('<tr><td class="cat" colspan="4">%s</td></tr>' % H.escape(cat_nome))
        for nome in nomes:
            idx += 1
            pg = "%d" % pmap[idx] if pmap else ""
            out.append('<tr><td class="num">%02d</td><td><a href="#r%02d">%s</a></td><td class="dots"></td><td class="pg">%s</td></tr>' % (idx, idx, H.escape(nome), pg))
    out.append("</table></div></section>")
    return "".join(out)


def corpo_html(markers=False):
    out = []
    for cap_num, (cat_nome, cat_intro, nomes) in enumerate(SELECAO, 1):
        out.append('<section class="abre"><img class="capfoto" src="imagens/capitulo-%02d.jpg" alt="Imagen del capítulo %s"><div class="tag">Capítulo %02d</div><h2>%s</h2><div class="filete"></div><p>%s</p></section>' % (cap_num, H.escape(cat_nome), cap_num, H.escape(cat_nome), H.escape(cat_intro)))
        for r in RECETAS:
            if r["cat"] == cat_nome: out.append(receta_html(r, markers=markers))
    return "".join(out)


def render_html(pmap=None, markers=False):
    return ("<!DOCTYPE html><html lang='es'><head><meta charset='utf-8'><style>%s</style></head><body>%s%s%s%s%s%s</body></html>" % (CSS, CAPA, FRENTE, sumario_html(pmap), corpo_html(markers), BONUS, CONTRA))


def build():
    from weasyprint import HTML
    import fitz
    # Sonda sin marcadores para que el sumario lea las páginas reales.
    open("ebook_es_probe.html", "w").write(render_html(None, False))
    HTML(filename="ebook_es_probe.html").write_pdf("ebook_es_probe.pdf")
    d = fitz.open("ebook_es_probe.pdf")
    pmap = {}
    for i in range(d.page_count):
        text = d[i].get_text(); norm = text.replace(" ", "")
        if "INGREDIENTES" in norm and "MODODEPREPARACIÓN" in norm:
            m = re.search(r"(?m)^(\d{2})\n", text)
            if m and 1 <= int(m.group(1)) <= 50: pmap[int(m.group(1))] = i + 1
    assert len(pmap) == 50, (len(pmap), sorted(set(range(1, 51)) - set(pmap)))
    open("50-recetas-low-carb-es.html", "w").write(render_html(pmap, False))
    HTML(filename="50-recetas-low-carb-es.html").write_pdf("50-recetas-low-carb-es.pdf")
    print("PDF en español generado:", len(pmap), "recetas con páginas asignadas")


if __name__ == "__main__":
    build()
