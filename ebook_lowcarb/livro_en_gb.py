# -*- coding: utf-8 -*-
"""British English (en-GB) edition of 50 Low-Carb Recipes for Everyday Life.
Porting britânico escrito à mão a partir do modelo EN (livro_en.py + en_overrides):
títulos, capítulos, front/back matter e rótulos do template revistos em en-GB
(flavour/colour, courgette, aubergine, prawns, beef mince, yoghurt, omelette,
lasagne, savoury, biscuits, Serves em vez de Yield, lang='en-GB').
O texto das receitas vem de en_gb_overrides (delta fail-loudly sobre o corpus EN).
"""
import html as H
import re
import livro as pt

NAMES = [
 "Baked Spinach and Cheese Omelette", "2-Minute Low-Carb Microwave Bread", "Banana Oat Pancakes (No Flour)",
 "Savoury Egg, Vegetable and Bacon Muffins", "Stovetop Tapioca Crepe with Cheese and Tomato", "Stovetop Cheese Bread",
 "Creamy Chicken Collard Wrap", "Creamy Scrambled Eggs with Avocado and Seeds", "Protein Yoghurt with Nut Granola",
 "Simple Cauliflower Rice", "Courgette Noodles with Homemade Tomato Sauce", "Garlic and Oil Palm Heart Noodles",
 "Complete Chicken Salad with Yoghurt Dressing", "Tuna Salad with Egg and Lemon Mayonnaise", "Spicy Beef Mince Lettuce Wrap",
 "Cauliflower Shepherd's Pie with Shredded Beef", "Aubergine Lasagne Bolognese", "Stuffed Aubergine with Beef Mince",
 "Low-Carb Kale Soup (No Potato)", "Pumpkin Soup with Coconut Milk and Ginger", "Vegetable Soup with Shredded Chicken",
 "Creamy Courgette Soup with Cream Cheese", "Pan-Fried Chicken with Mustard Cream Sauce", "Oven-Roasted Chicken Thighs with Lemon and Rosemary",
 "Low-Carb Chicken Stir-Fry", "Steak with Mushroom Sauce", "Beef Mince with Courgette and Tomato",
 "Steak with Caramelised Onions and Garlic Butter", "Cheese-Stuffed Meatballs in Tomato Sauce", "Pulled Pork Ribs",
 "Baked Salmon with Lemon Butter", "Almond-Crusted Tilapia", "Garlic Prawns", "Cod with Cauliflower and Olives",
 "Fish Moqueca with Coconut Milk and Hearts of Palm", "Griddled Calamari with Lemon and Herbs",
 "Cauliflower Crust Pizza with Mozzarella and Basil", "Aubergine Parmesan (No Breadcrumbs)", "Low-Carb Feijoada (No Beans)",
 "Air-Fryer Cheese Bread", "Tuna and Cream Cheese Stuffed Courgette", "Low-Carb Sushi (Cucumber Rolls)",
 "Cabbage Rolls with Beef Mince", "Chocolate Avocado Mousse", "Coconut Flan with Erythritol",
 "Spoonable Low-Carb Chocolate Cream", "Low-Carb Berry Cheesecake", "Low-Carb Nut and Chocolate Biscuits",
 "Chocolate Truffles with Coconut Oil", "Low-Carb Peanut Brittle (Paçoca Style)"
]

CAT = {
 "Café da manhã e lanches rápidos": ("Breakfast and Quick Snacks", "Start the day with practical, satisfying recipes that do not rely on traditional bread. This chapter brings together eggs, cheese, almond or coconut flour and fruit in balanced portions. Most options require up to 15 minutes of active preparation."),
 "Almoços completos": ("Complete Lunches", "One-pot dishes, salads that keep you satisfied through the afternoon and smart substitutes for rice and pasta — without tasting like diet food."),
 "Sopas e caldos": ("Soups and Broths", "For cold evenings and packed lunches: creamy comfort without potatoes or wheat flour."),
 "Carnes e aves": ("Meat and Poultry", "Protein is the foundation of a good low-carb menu: browned, juicy and served with real sauces — never dry meal-prep chicken."),
 "Peixes e frutos do mar": ("Fish and Seafood", "From Sunday salmon to a quick weekday sardine option: good fats, fast preparation and restaurant-level flavour."),
 "Jantares em até 30 minutos de bancada": ("Dinners Ready in 30 Minutes", "The evening rule: dinner is ready before the episode ends. One-pan, one-tray and air-fryer recipes for busy nights."),
 "Sobremesas sem açúcar": ("Sugar-Free Desserts", "A real dessert does not need refined sugar: cocoa, coconut, nuts and sweeteners that do not fool your palate."),
}

# Texto das receitas: porting britânico escrito à mão sobre o corpus EN.
# Cada linha que difere do en-US vive em en_gb_overrides (INGREDIENTS_GB /
# OVERRIDES_GB); o resto é herdado do dicionário EN por merge determinístico.
# Linha PT sem cobertura derruba o build com KeyError em vez de vazar idioma.
from en_gb_overrides import INGREDIENTS, OVERRIDES

def ingredient(line):
    s = str(line)
    if s not in INGREDIENTS:
        raise KeyError("Ingredient line without British English translation: %r" % s)
    return INGREDIENTS[s]

def override(num):
    if num not in OVERRIDES:
        raise KeyError("Recipe %d without British English text (en_gb_overrides.OVERRIDES)" % num)
    return OVERRIDES[num]

PT_TO_EN = {r["d"][0]: NAMES[r["num"] - 1] for r in pt.RECEITAS}
RECIPES = []
for r in pt.RECEITAS:
    d = r["d"]
    name, prep, total, servings, kcal, carbs, protein, fat, ingredients, steps, tip, swap = d
    passos, dica, troca = override(r["num"])
    assert len(passos) == len(steps), "receita %d: %d passos em en-GB para %d em português" % (r["num"], len(passos), len(steps))
    RECIPES.append({"num": r["num"], "id": r["id"], "cat": CAT[r["cat"]][0],
                    "d": (PT_TO_EN[name], prep, total, servings, kcal, carbs, protein, fat,
                          [ingredient(x) for x in ingredients], passos, dica, troca)})

SELECTION = []
for cat_pt, intro_pt, names in pt.SELECAO:
    cat_en, intro_en = CAT[cat_pt]
    SELECTION.append((cat_en, intro_en, [PT_TO_EN[n] for n in names]))

CSS = pt.CSS.replace("50 Receitas Low Carb para o Dia a Dia", "50 Low-Carb Recipes for Everyday Life")

FRONT = """
<section class="frente legal"><h2>Credits and Legal Notice</h2><div class="filete"></div>
<p><b>50 Low-Carb Recipes for Everyday Life</b> — 1st edition, 2026.<br>Practical Kitchen Series · volume 1.</p>
<p>All rights reserved. No part of this material may be reproduced without written permission. This ebook is a digital product intended for the purchaser: share only the official sales link.</p>
<div class="quadro"><b>IMPORTANT NOTICE:</b> nutritional information (calories, carbohydrates, protein and fat) is an <b>estimate per serving</b>, calculated from the ingredient list and food-composition tables. Values vary by brand, ingredient size, and equipment. This book is educational and <b>does not replace</b> advice from a doctor or a registered dietitian. People with diabetes, kidney disease, pregnant or breastfeeding people and anyone taking continuous medication should consult a qualified professional before adopting a carbohydrate-restricted eating pattern. Erythritol and xylitol are safe for most people in moderate amounts; excess may cause digestive discomfort. Xylitol is toxic to dogs — keep desserts away from pets.</div>
<p><b>Measurements used in this book:</b> 1 cup = 240 ml · 1 tbsp = 15 ml · 1 tsp = 5 ml · a level tablespoon is not heaped · ovens are preheated unless stated otherwise.</p>
<p class="legal">Layout and illustrative photographs created for editorial purposes.</p></section>
<section class="frente"><h2>Welcome to Your Low-Carb Kitchen</h2><div class="filete"></div>
<p>You did not buy a diet book. You bought <b>50 ready-to-use answers</b> to the question that can derail any eating routine: <i>“What should I cook today?”</i>.</p>
<p>Low carb does not mean living on sad salads. It means enjoying a creamy omelette, a lasagne you can slice, a Sunday feijoada, and even cheesecake — swapping refined flour and sugar for ingredients that satisfy, without cooking two separate meals.</p>
<p>Every recipe was selected for three reasons: <b>easy-to-find ingredients</b>, <b>realistic time for busy people</b>, and <b>leftovers that solve tomorrow’s meal</b>.</p>
<div class="quadro"><b>The golden rule of this book:</b> carbohydrates are accents, not the foundation. They add flavour and colour — tomato, carrot, fruit — while the foundation is always protein, good fat and vegetables.</div>
<p>Cook one new recipe a day for seven weeks and you will have a repertoire that can rescue any Monday. Enjoy.</p></section>
<section class="frente"><h2>How to Use This Book</h2><div class="filete"></div>
<p><b>1. Start at the end.</b> Check the “7-Day Menu” bonus and the shopping list before you go to the shops. Cooking without a plan is the fastest way to order a takeaway on Thursday.</p>
<p><b>2. Double the right recipe.</b> Most lunch and dinner recipes make two servings: the second becomes tomorrow’s lunch.</p>
<p><b>3. Use the boxes.</b> Each recipe includes a <b>Cooking Tip</b> and a <b>Smart Swap</b> to help you adapt without leaving the low-carb approach.</p>
<p><b>4. Do not chase zero carbs.</b> The nutritional numbers are there to help you choose, not to turn food into a prison.</p>
<p><b>5. Freeze with confidence.</b> Recipes with freezing notes were designed for individual portions and sealed containers.</p></section>
<section class="frente"><h2>Substitutions That Save Any Pantry</h2><div class="filete"></div>
<p>Low carb is also a game of smart swaps. Keep this table handy:</p>
<table><tr><th>Remove</th><th>Use instead</th><th>Note</th></tr>
<tr><td>Refined sugar</td><td><b>Erythritol or xylitol</b></td><td>1:1; xylitol is slightly sweeter</td></tr><tr><td>Wheat flour</td><td><b>Almond flour + 1 egg</b></td><td>use half the amount; egg provides structure</td></tr>
<tr><td>White rice</td><td><b>Cauliflower rice</b></td><td>sauté raw over high heat for 5–6 minutes</td></tr><tr><td>Pasta</td><td><b>Courgette, hearts of palm or konjac</b></td><td>sauté for 90 seconds to 3 minutes</td></tr>
<tr><td>Potato</td><td><b>Cauliflower, turnip or roasted radish</b></td><td>for mash and soups; use pumpkin moderately</td></tr><tr><td>Prepared sauce</td><td><b>Peeled tomatoes + seasoning</b></td><td>simmer over low heat for 20 minutes</td></tr></table>
<h2 style="margin-top:6mm">Pantry Staples</h2><div class="lista2"><ul><li>Almond flour and unsweetened shredded coconut</li><li>Erythritol or xylitol and 100% cocoa</li><li>Unsweetened coconut milk and cream</li><li>Olive oil, coconut oil and butter</li><li>Eggs and cheeses: mozzarella, Parmesan, cream cheese</li><li>Cauliflower, courgette, aubergine, cabbage and kale</li><li>Tinned peeled tomatoes and olives</li><li>Chicken, beef mince, fish and tinned tuna</li><li>Nuts, lemons, fresh herbs and smoked paprika</li><li>Chia seeds and golden flaxseed meal</li></ul></div></section>
"""

BONUS = """
<section class="frente"><h2>Bonus 1 — 7-Day Menu</h2><div class="filete"></div><p>A realistic first-week plan: filling breakfasts, lunches that become dinner and a sweet option at the right time. Numbers refer to recipes in this book.</p>
<table><tr><th>Day</th><th>Breakfast</th><th>Lunch</th><th>Snack</th><th>Dinner</th></tr><tr><td class="dia">Mon</td><td>01 · baked omelette</td><td>10 + 23 · cauliflower rice with chicken</td><td>09 · yoghurt granola</td><td>37 · cauliflower pizza</td></tr><tr><td class="dia">Tue</td><td>05 · tapioca crepe</td><td>17 · aubergine lasagne</td><td>06 · cheese bread</td><td>31 · salmon + 44 · mousse</td></tr><tr><td class="dia">Wed</td><td>02 · microwave bread</td><td>11 · courgette noodles</td><td>45 · coconut flan</td><td>35 · fish moqueca</td></tr><tr><td class="dia">Thu</td><td>07 · collard wrap</td><td>13 · complete chicken salad</td><td>08 · avocado eggs</td><td>26 · steak with mushrooms</td></tr><tr><td class="dia">Fri</td><td>03 · banana pancakes</td><td>16 · cauliflower shepherd's pie</td><td>09 · yoghurt granola</td><td>33 · garlic prawns</td></tr><tr><td class="dia">Sat</td><td>04 · savoury muffins</td><td>18 · stuffed aubergine</td><td>46 · chocolate cream</td><td>42 · low-carb sushi</td></tr><tr><td class="dia">Sun</td><td>06 · cheese bread</td><td>30 · pulled pork ribs</td><td>47 · cheesecake</td><td>19 · kale soup + 28 · steak</td></tr></table><p class="legal">Adjust portions to your needs. This menu is an educational suggestion, not a prescription.</p></section>
<section class="frente"><h2>Bonus 2 — First-Week Shopping List</h2><div class="filete"></div><p>Print this list and take it to the supermarket. It is designed for two people:</p><div class="lista2"><ul class="check"><li>2 dozen eggs</li><li>1 kg chicken breast + 8 thighs</li><li>1 kg beef mince + 500 g steak</li><li>600 g salmon or firm fish + 400 g prawns</li><li>2 tins tuna</li><li>500 g mozzarella + Parmesan + cream cheese</li><li>Double cream</li><li>2 containers unsweetened coconut milk</li><li>Cauliflower, courgette, aubergine, cabbage and kale</li><li>Fresh tomatoes + 2 tins peeled tomatoes</li><li>Avocado, bananas, strawberries and lemons</li><li>Onions, garlic, ginger, herbs, smoked paprika</li><li>Olives, hearts of palm, nuts and peanuts</li><li>Almond flour, shredded coconut and chia</li><li>Erythritol or xylitol, 100% cocoa and 85% chocolate</li><li>Olive oil, butter and coconut oil</li><li>Soy sauce and mustard</li></ul></div><div class="quadro"><b>Shopping rule:</b> visit the fruit and veg counter and the meat counter first; leave the packaged products until last and always check the label.</div></section>
<section class="frente"><h2>Before You Close the Kitchen</h2><div class="filete"></div><p>You now have 50 recipes designed for real life: easy-to-find ingredients, one-pot methods and planned leftovers. The difference between this ebook and a more organised week is one small decision: <b>your next meal</b>.</p><p>Choose one recipe for tonight, make it and share it with someone. Shared food is easier to repeat.</p><div class="quadro"><b>UPCOMING PRACTICAL KITCHEN VOLUMES:</b> Volume 2 — <i>Low-Carb Meals for the Week</i> · Volume 3 — <i>Sugar-Free Party Desserts</i>.</div></section>
"""

COVER = """<section class="capa"><div class="txt"><div class="kicker">Practical Kitchen Series · vol. 1</div><h1>50 RECIPES<br><span class="hl">LOW CARB</span></h1><div class="sub">for everyday life — no flour, no sugar, no sacrifice</div></div><div class="faixa"><span class="marca">PRACTICAL KITCHEN</span><span>less carbs, more real life</span></div></section>"""
BACK = """<section class="contra"><div class="in"><h2>Stop starting your diet every Monday.</h2><p>This book brings together 50 recipes for staying low carb without cooking twice: breakfasts that carry you through the morning, lunches that become dinner, soups for cold nights and desserts that need no apology.</p><ul><li><b>50 complete recipes</b> with time, number of servings and estimated macros per serving;</li><li><b>Cooking Tip</b> in every recipe to prevent the most common mistake;</li><li><b>Smart Swap</b> ideas for adapting ingredients;</li><li><b>7-Day Menu</b> and a printable shopping list;</li><li><b>Substitution table</b> for flour, sugar, rice and pasta.</li></ul><p>Easy-to-find ingredients. Realistic time. Food for people who do not want to feel on a diet.</p><div class="marca">PRACTICAL KITCHEN</div></div></section>"""


def recipe_html(r):
    num, rid, d = r["num"], r["id"], r["d"]
    name, prep, total, servings, kcal, carbs, protein, fat, ingredients, steps, tip, swap = d
    ing = "".join("<li>%s</li>" % H.escape(x) for x in ingredients)
    pas = "".join("<li>%s</li>" % H.escape(x) for x in steps)
    return """<section class="receita" id="%s"><header><div class="num">%02d</div><div class="titulo"><h3>%s</h3></div></header><img class="foto" src="imagens/receita-%02d.jpg" alt="%s"><div class="meta"><span><b>Preparation</b> %d min</span><span><b>Total</b> %d min</span><span><b>Serves</b> %s</span><span><b>Difficulty</b> easy</span></div><div class="nutris"><span><b>%d</b>kcal / serving</span><span><b>%d g</b>carbohydrates</span><span><b>%d g</b>protein</span><span><b>%d g</b>fat</span></div><div class="corpo"><div><h4>Ingredients</h4><ul class="ing">%s</ul></div><div><h4>Method</h4><ol class="passos">%s</ol></div></div><div class="dica"><b>COOKING TIP:</b> %s</div><div class="troca"><b>↺ SMART SWAP:</b> %s</div></section>""" % (rid, num, H.escape(name), num, H.escape(name), prep, total, H.escape(str(servings)), kcal, carbs, protein, fat, ing, pas, H.escape(tip), H.escape(swap))


def toc_html(pmap=None):
    out = ['<section class="frente"><h2>Contents</h2><div class="filete"></div><div class="sum"><table>']; idx = 0
    for cat, intro, names in SELECTION:
        out.append('<tr><td class="cat" colspan="4">%s</td></tr>' % H.escape(cat))
        for name in names:
            idx += 1; pg = str(pmap[idx]) if pmap else ""
            out.append('<tr><td class="num">%02d</td><td><a href="#r%02d">%s</a></td><td class="dots"></td><td class="pg">%s</td></tr>' % (idx, idx, H.escape(name), pg))
    out.append('</table></div></section>'); return ''.join(out)


def body_html():
    out = []
    for chapter, (cat, intro, names) in enumerate(SELECTION, 1):
        out.append('<section class="abre"><img class="capfoto" src="imagens/capitulo-%02d.jpg" alt="%s chapter image"><div class="tag">Chapter %02d</div><h2>%s</h2><div class="filete"></div><p>%s</p></section>' % (chapter, H.escape(cat), chapter, H.escape(cat), H.escape(intro)))
        for r in RECIPES:
            if r["cat"] == cat: out.append(recipe_html(r))
    return ''.join(out)


def render(pmap=None):
    return "<!DOCTYPE html><html lang='en-GB'><head><meta charset='utf-8'><style>%s</style></head><body>%s%s%s%s%s%s</body></html>" % (CSS, COVER, FRONT, toc_html(pmap), body_html(), BONUS, BACK)


def build():
    from weasyprint import HTML
    import fitz
    open('ebook_en_gb_probe.html', 'w').write(render(None)); HTML(filename='ebook_en_gb_probe.html').write_pdf('ebook_en_gb_probe.pdf')
    d = fitz.open('ebook_en_gb_probe.pdf'); pmap = {}
    for i in range(d.page_count):
        text = d[i].get_text(); norm = text.replace(' ', '')
        if 'INGREDIENTS' in norm and 'METHOD' in norm:
            m = re.search(r'(?m)^(\d{2})\n', text)
            if m and 1 <= int(m.group(1)) <= 50: pmap[int(m.group(1))] = i + 1
    assert len(pmap) == 50, (len(pmap), sorted(set(range(1, 51)) - set(pmap)))
    open('50-low-carb-recipes-en-GB.html', 'w').write(render(pmap)); HTML(filename='50-low-carb-recipes-en-GB.html').write_pdf('50-low-carb-recipes-en-GB.pdf')
    print('British English PDF generated:', len(pmap), 'recipes mapped')

if __name__ == '__main__': build()
