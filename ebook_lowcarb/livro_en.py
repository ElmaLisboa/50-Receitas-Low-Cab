# -*- coding: utf-8 -*-
"""International English edition of 50 Low-Carb Recipes for Everyday Life."""
import html as H
import re
import livro as pt

NAMES = [
 "Baked Spinach and Cheese Omelet", "2-Minute Low-Carb Microwave Bread", "Banana Oat Pancakes (No Flour)",
 "Savory Egg, Vegetable and Bacon Muffins", "Skillet Tapioca Crepe with Cheese and Tomato", "Skillet Cheese Bread",
 "Creamy Chicken Collard Wrap", "Creamy Scrambled Eggs with Avocado and Seeds", "Protein Yogurt with Nut Granola",
 "Simple Cauliflower Rice", "Zucchini Noodles with Homemade Tomato Sauce", "Garlic and Oil Palm Heart Noodles",
 "Complete Chicken Salad with Yogurt Dressing", "Tuna Salad with Egg and Lemon Mayonnaise", "Spicy Ground Beef Lettuce Wrap",
 "Cauliflower Shepherd's Pie with Shredded Beef", "Eggplant Lasagna Bolognese", "Stuffed Eggplant with Ground Beef",
 "Low-Carb Kale Soup (No Potato)", "Pumpkin Soup with Coconut Milk and Ginger", "Vegetable Soup with Shredded Chicken",
 "Creamy Zucchini Soup with Cream Cheese", "Grilled Chicken with Mustard Cream Sauce", "Oven-Roasted Chicken Thighs with Lemon and Rosemary",
 "Low-Carb Chicken Stir-Fry", "Steak with Mushroom Sauce", "Ground Beef with Zucchini and Tomato",
 "Steak with Caramelized Onions and Garlic Butter", "Cheese-Stuffed Meatballs in Tomato Sauce", "Pulled Pork Ribs",
 "Baked Salmon with Lemon Butter", "Almond-Crusted Tilapia", "Garlic Shrimp", "Cod with Cauliflower and Olives",
 "Fish Moqueca with Coconut Milk and Hearts of Palm", "Grilled Calamari with Lemon and Herbs",
 "Cauliflower Crust Pizza with Mozzarella and Basil", "Eggplant Parmesan (No Breading)", "Low-Carb Feijoada (No Beans)",
 "Air-Fryer Cheese Bread", "Tuna and Cream Cheese Stuffed Zucchini", "Low-Carb Sushi (Cucumber Rolls)",
 "Cabbage Rolls with Ground Beef", "Chocolate Avocado Mousse", "Coconut Flan with Erythritol",
 "Spoonable Low-Carb Chocolate Cream", "Low-Carb Berry Cheesecake", "Low-Carb Nut and Chocolate Cookies",
 "Chocolate Truffles with Coconut Oil", "Low-Carb Peanut Brittle (Paçoca Style)"
]

CAT = {
 "Café da manhã e lanches rápidos": ("Breakfast and Quick Snacks", "Start the day with practical, satisfying recipes that do not rely on traditional bread. This chapter brings together eggs, cheese, almond or coconut flour, and fruit in balanced portions. Most options require up to 15 minutes of active preparation."),
 "Almoços completos": ("Complete Lunches", "One-pot dishes, salads that keep you satisfied through the afternoon, and smart substitutes for rice and pasta — without tasting like diet food."),
 "Sopas e caldos": ("Soups and Broths", "For cold evenings and packed lunches: creamy comfort without potatoes or wheat flour."),
 "Carnes e aves": ("Meat and Poultry", "Protein is the foundation of a good low-carb menu: browned, juicy, and served with real sauces — never dry meal-prep chicken."),
 "Peixes e frutos do mar": ("Fish and Seafood", "From Sunday salmon to a quick weekday sardine option: good fats, fast preparation, and restaurant-level flavor."),
 "Jantares em até 30 minutos de bancada": ("Dinners Ready in 30 Minutes", "The evening rule: dinner is ready before the episode ends. One-pan, one-tray, and air-fryer recipes for busy nights."),
 "Sobremesas sem açúcar": ("Sugar-Free Desserts", "A real dessert does not need refined sugar: cocoa, coconut, nuts, and sweeteners that do not fool your palate."),
}

PHRASES = [
 ("Faça dois de uma vez", "Make two at a time"), ("o segundo dura", "the second lasts"),
 ("e vira café da manhã", "and becomes breakfast"), ("a técnica", "the technique"),
 ("pimenta-do-reino", "black pepper"), ("noz-moscada", "nutmeg"), ("café da manhã", "breakfast"),
 ("cheiro-verde", "fresh herbs"), ("couve manteiga", "collard greens"),
 ("couve-flor", "cauliflower"), ("couve", "kale"), ("abobrinha", "zucchini"), ("berinjela", "eggplant"),
 ("palmito pupunha", "palm hearts"), ("palmito", "hearts of palm"), ("tomate pelado", "peeled whole tomatoes"),
 ("creme de leite fresco", "heavy cream"), ("creme de leite", "heavy cream"), ("cream cheese", "cream cheese"),
 ("requeijão", "cream cheese"), ("muçarela", "mozzarella"), ("queijo parmesão", "Parmesan cheese"),
 ("queijo", "cheese"), ("farinha de amêndoas", "almond flour"), ("farinha de coco", "coconut flour"),
 ("farinha de linhaça dourada", "golden flaxseed meal"), ("polvilho azedo", "sour cassava starch"),
 ("goma de tapioca", "tapioca gum"), ("leite de coco", "coconut milk"), ("carne seca", "shredded dried beef"),
 ("carne moída", "ground beef"), ("frango desfiado", "shredded chicken"), ("peito de frango", "chicken breast"),
 ("ovos mexidos", "scrambled eggs"), ("ovos cozidos", "hard-boiled eggs"), ("ovo cozido", "hard-boiled egg"),
 ("castanha-de-caju", "cashews"), ("castanha do pará", "Brazil nuts"), ("castanhas", "nuts"),
 ("manteiga de amendoim", "peanut butter"), ("pasta de amendoim", "peanut butter"), ("amendoim", "peanuts"),
 ("morangos", "strawberries"), ("morango", "strawberry"), ("abacate", "avocado"), ("abóbora", "pumpkin"),
 ("pepino", "cucumber"), ("tomate", "tomato"), ("cebola", "onion"), ("alho", "garlic"),
 ("dentes", "cloves"), ("dente", "clove"), ("salsão", "celery"), ("vagem", "green beans"),
 ("cenoura", "carrot"), ("pimentão", "bell pepper"), ("cogumelos", "mushrooms"), ("shimeji", "shimeji mushrooms"),
 ("salmão", "salmon"), ("camarão", "shrimp"), ("camarões", "shrimp"), ("tilápia", "tilapia"),
 ("bacalhau", "cod"), ("lula", "calamari"), ("costelinha", "ribs"), ("linguiça", "sausage"),
 ("bacon", "bacon"), ("presunto cru", "prosciutto"), ("presunto", "ham"), ("iogurte", "yogurt"),
 ("azeitona", "olive"), ("azeitonas", "olives"), ("azeite", "olive oil"),
 ("vinagre de maçã", "apple cider vinegar"), ("vinagre de vinho tinto", "red wine vinegar"),
 ("mostarda dijon", "Dijon mustard"), ("mostarda", "mustard"), ("shoyu", "soy sauce"),
 ("molho de tomate", "tomato sauce"), ("molho", "sauce"), ("caldo de legumes", "vegetable broth"),
 ("caldo de galinha", "chicken broth"), ("caldo de carne", "beef broth"), ("páprica defumada", "smoked paprika"),
 ("páprica", "paprika"), ("orégano", "oregano"), ("manjericão", "basil"), ("salsinha", "parsley"),
 ("cebolinha", "scallions"), ("coentro", "cilantro"), ("alecrim", "rosemary"), ("gengibre", "ginger"),
 ("canela", "cinnamon"), ("cacau em pó", "unsweetened cocoa powder"), ("cacau", "cocoa"),
 ("coco ralado", "shredded coconut"), ("coco em flocos", "coconut flakes"), ("sementes de girassol", "sunflower seeds"),
 ("sementes de abóbora", "pumpkin seeds"), ("sementes de chia", "chia seeds"), ("sementes", "seeds"),
 ("espinafre", "spinach"), ("fresco", "fresh"), ("fresca", "fresh"), ("sal", "salt"), ("pimenta", "pepper"),
 ("secar", "dry"), ("refratário", "baking dish"), ("aos", "to the"), ("manhã", "morning"),
 ("farinha", "flour"), ("açúcar", "sugar"), ("adoçante", "sweetener"), ("essência", "extract"),
 ("fermento em pó", "baking powder"), ("em pó", "powder"), ("sem açúcar", "unsweetened"),
 ("sem farinha", "flourless"), ("sem sementes", "seedless"), ("sem pele", "skinless"),
 ("a gosto", "to taste"), ("para servir", "to serve"), ("para finalizar", "to finish"),
 ("em cubos", "diced"), ("em rodelas", "sliced"), ("em fatias", "sliced"), ("em tiras", "cut into strips"),
 ("picada", "chopped"), ("picado", "chopped"), ("picadas", "chopped"), ("picados", "chopped"),
 ("ralada", "grated"), ("ralado", "grated"), ("raladas", "grated"), ("ralados", "grated"),
 ("escorrido", "drained"), ("escorrida", "drained"), ("escorridas", "drained"),
 ("desfiado", "shredded"), ("desfiada", "shredded"), ("desfiados", "shredded"),
 ("espremida", "squeezed"), ("espremido", "squeezed"), ("congelado", "frozen"), ("derretida", "melted"),
 ("derretido", "melted"), ("cozida", "cooked"), ("cozido", "cooked"), ("quente", "hot"),
 ("morno", "warm"), ("crocante", "crispy"), ("cremoso", "creamy"), ("cremosa", "creamy"),
 ("xíc.", "cup"), ("col. sopa", "tbsp"), ("col. chá", "tsp"), ("col.", "tbsp"),
]

VERBS = [
 ("Não lave", "Do not wash"), ("Não mexa", "Do not stir"), ("Não deixe", "Do not leave"),
 ("Leve ao micro-ondas", "Microwave"), ("Leve ao forno", "Bake"), ("Leve à geladeira", "Refrigerate"),
 ("Leve ao congelador", "Freeze"), ("Volte à panela", "Return to the pan"), ("Volte o", "Return the"),
 ("Refogue", "Sauté"), ("Junte", "Add"), ("Acrescente", "Add"), ("Bata", "Beat"),
 ("Misture", "Mix"), ("Incorpore", "Fold in"), ("Asse", "Bake"), ("Cozinhe", "Cook"),
 ("Aqueça", "Heat"), ("Despeje", "Pour"), ("Tempere", "Season"), ("Sirva", "Serve"),
 ("Finalize", "Finish"), ("Reserve", "Set aside"), ("Deixe", "Let"), ("Corte", "Cut"),
 ("Retire", "Remove"), ("Frite", "Fry"), ("Grelhe", "Grill"), ("Sele", "Sear"),
 ("Passe", "Coat"), ("Abra", "Open"), ("Modele", "Shape"), ("Distribua", "Divide"),
 ("Cubra", "Cover"), ("Regue", "Drizzle"), ("Acomode", "Arrange"), ("Processe", "Process"),
 ("Rale", "Grate"), ("Esprema", "Squeeze"), ("Poche", "Poach"), ("Monte", "Assemble"),
 ("Amasse", "Mash"), ("Doure", "Brown"), ("Derreta", "Melt"), ("Toste", "Toast"),
 ("Salgue", "Salt"), ("Envolva", "Coat"), ("Aperte", "Press"), ("Ajuste", "Adjust"),
 ("Mantenha", "Keep"), ("Aguarde", "Wait"), ("Espalhe", "Spread"),
]

WORD_MAP = [
 ("faça", "make"), ("aceita", "works with"), ("qualquer", "any"), ("tire", "remove"),
 ("ovos", "eggs"), ("ovo", "egg"), ("refogado", "sautéed mixture"), ("queijos", "cheeses"),
 ("minutos", "minutes"), ("minuto", "minute"), ("pequeno", "small"), ("pequena", "small"),
 ("untado", "greased"), ("untada", "greased"), ("firmar", "set"), ("dura", "lasts"),
 ("segundo", "second"), ("mesma", "same"), ("técnica", "technique"), ("sabor", "flavor"),
 ("colher", "spoon"), ("gosto", "taste"), ("vez", "time"), ("dias", "days"), ("amanhã", "tomorrow"),
 ("mais", "more"), ("neutro", "neutral"), ("centro", "center"), ("porção", "serving"), ("atum", "tuna"),
 ("trocando", "swapping"), ("leve", "light"),
 ("bifes", "steaks"), ("bife", "steak"), ("geladeira", "refrigerator"), ("óleo", "oil"),
 ("fogo", "heat"), ("panela", "pan"), ("forno", "oven"), ("água", "water"),
 ("ainda", "still"), ("receita", "recipe"), ("pote", "container"), ("potes", "containers"),
 ("caneca", "mug"), ("versão", "version"), ("refogo", "sauté"), ("dourar", "brown"),
 ("cruas", "raw"), ("crua", "raw"), ("cru", "raw"), ("depois", "then"), ("muita", "a lot of"), ("muito", "very"), ("é", "is"), ("fica", "is"), ("ficar", "become"),
 ("soltam", "release"), ("solta", "releases"), ("vira", "becomes"),
 ("virar", "become"), ("recheie", "fill"), ("rechear", "fill"), ("escorra", "drain"),
 ("escorredor", "colander"), ("trocar", "swap"), ("desligue", "turn off"), ("desligado", "off"),
 ("fervente", "boiling"), ("louro", "bay leaf"), ("pano de prato", "kitchen towel"),
 ("dica", "tip"), ("troque", "swap"), ("cozinha", "kitchen"), ("marmita", "lunch container"),
 ("suco", "juice"), ("tigelas", "bowls"), ("duas", "two"), ("grão-de-bico", "chickpeas"),
]


def translate_text(value, steps=False):
    s = str(value)
    for a, b in sorted(PHRASES, key=lambda x: len(x[0]), reverse=True):
        s = re.sub(r"(?<!\w)" + re.escape(a) + r"(?!\w)", b, s, flags=re.IGNORECASE)
    for a, b in sorted(VERBS, key=lambda x: len(x[0]), reverse=True):
        s = re.sub(r"^(" + re.escape(a) + r")\b", b, s, flags=re.IGNORECASE)
    connectors = [(" até ", " until "), (" com ", " with "), (" sem ", " without "),
                  (" em ", " in "), (" no ", " in the "), (" na ", " in the "),
                  (" dos ", " of the "), (" das ", " of the "), (" do ", " of the "),
                  (" da ", " of the "), (" ao ", " to the "), (" à ", " to the "),
                  (" de ", " of "), (" por ", " for "), (" a ", " the "),
                  (" e ", " and "), (" ou ", " or ")]
    for a, b in sorted(connectors, key=lambda x: len(x[0]), reverse=True): s = s.replace(a, b)
    fixes = [("minutos em fogo baixo", "minutes over low heat"), ("minutos de cada lado", "minutes per side"),
             ("fogo baixo", "low heat"), ("fogo alto", "high heat"), ("fogo médio", "medium heat"),
             ("até ficar", "until it is"), ("até encorpar", "until thickened"), ("até dourar", "until golden"),
             ("até firmar", "until set"), ("até secar", "until dry"), ("até amaciar", "until tender"),
             ("na geladeira", "in the refrigerator"), ("no forno", "in the oven"),
             ("no micro-ondas", "in the microwave"), ("no liquidificador", "in the blender"),
             ("com as mãos", "with your hands"), ("de um dia para o outro", "overnight"),
             ("por no mínimo", "for at least"), ("no mínimo", "at least"),
             ("de uma vez", "at once"), ("at the time", "at once"),
             ("dry the water", "evaporate the water"), ("baking dish small greased", "small greased baking dish"),
             ("cup of spinach chopped", "cup chopped spinach"), ("of cheese mozzarella grated", "of grated mozzarella cheese")]
    for a, b in fixes: s = s.replace(a, b)
    for a, b in fixes: s = s.replace(a, b)
    for a, b in sorted(VERBS, key=lambda x: len(x[0]), reverse=True):
        s = re.sub(r"(?<!\w)" + re.escape(a) + r"(?!\w)", b.lower(), s, flags=re.IGNORECASE)
    for a, b in sorted(WORD_MAP, key=lambda x: len(x[0]), reverse=True):
        s = re.sub(r"(?<!\w)" + re.escape(a) + r"(?!\w)", b, s, flags=re.IGNORECASE)
    # Portuguese standalone articles and connectors that remain after phrase conversion.
    articles = [("dos", "of the"), ("das", "of the"), ("do", "of the"), ("da", "of the"),
                ("os", "the"), ("as", "the"), ("uma", "a"), ("duas", "two"), ("dois", "two"),
                ("um", "a"), ("com", "with"), ("sem", "without"), ("em", "in"),
                ("no", "in the"), ("na", "in the"), ("e", "and"), ("ou", "or"), ("o", "the")]
    for a, b in articles:
        s = re.sub(r"(?<!\w)" + re.escape(a) + r"(?!\w)", b, s, flags=re.IGNORECASE)
    s = s.replace("the 180", "at 180").replace("the 190", "at 190").replace("the 200", "at 200")
    s = s.replace("the taste", "to taste")
    s = s.replace("becomes breakfast of tomorrow", "becomes tomorrow's breakfast")
    s = s.replace("until dry the water", "until the water evaporates")
    s = s.replace("in the baking dish small greased", "in a small greased baking dish")
    s = s.replace("in baking dish small greased", "in a small greased baking dish")
    s = s.replace("the center set", "the center sets")
    s = s.replace("zucchini grated and squeezed", "grated and squeezed zucchini")
    s = s.replace("Mix the sautéed mixture and the cheese to the eggs", "Mix the sautéed mixture and cheese into the eggs")
    s = re.sub(r"(?<!\w)([2-9]\d*) cup\b", r"\1 cups", s)
    s = re.sub(r"(?<!\w)([2-9]\d*) tbsp\b", r"\1 tbsp", s)
    return s

PT_TO_EN = {r["d"][0]: NAMES[r["num"] - 1] for r in pt.RECEITAS}
RECIPES = []
for r in pt.RECEITAS:
    d = r["d"]
    name, prep, total, servings, kcal, carbs, protein, fat, ingredients, steps, tip, swap = d
    RECIPES.append({"num": r["num"], "id": r["id"], "cat": CAT[r["cat"]][0],
                    "d": (PT_TO_EN[name], prep, total, servings, kcal, carbs, protein, fat,
                          [translate_text(x) for x in ingredients], [translate_text(x, True) for x in steps],
                          translate_text(tip, True), translate_text(swap, True))})

SELECTION = []
for cat_pt, intro_pt, names in pt.SELECAO:
    cat_en, intro_en = CAT[cat_pt]
    SELECTION.append((cat_en, intro_en, [PT_TO_EN[n] for n in names]))

CSS = pt.CSS.replace("50 Receitas Low Carb para o Dia a Dia", "50 Low-Carb Recipes for Everyday Life")

FRONT = """
<section class="frente legal"><h2>Credits and Legal Notice</h2><div class="filete"></div>
<p><b>50 Low-Carb Recipes for Everyday Life</b> — 1st edition, 2026.<br>Practical Kitchen Series · volume 1.</p>
<p>All rights reserved. No part of this material may be reproduced without written permission. This ebook is a digital product intended for the purchaser: share only the official sales link.</p>
<div class="quadro"><b>IMPORTANT NOTICE:</b> nutritional information (calories, carbohydrates, protein, and fat) is an <b>estimate per serving</b>, calculated from the ingredient list and food-composition tables. Values vary by brand, ingredient size, and equipment. This book is educational and <b>does not replace</b> advice from a physician or registered dietitian. People with diabetes, kidney disease, pregnant or breastfeeding people, and anyone taking continuous medication should consult a qualified professional before adopting a carbohydrate-restricted eating pattern. Erythritol and xylitol are safe for most people in moderate amounts; excess may cause digestive discomfort. Xylitol is toxic to dogs — keep desserts away from pets.</div>
<p><b>Measurements used in this book:</b> 1 cup = 240 ml · 1 tbsp = 15 ml · 1 tsp = 5 ml · a level tablespoon is not heaped · ovens are preheated unless stated otherwise.</p>
<p class="legal">Layout and illustrative photographs created for editorial purposes.</p></section>
<section class="frente"><h2>Welcome to Your Low-Carb Kitchen</h2><div class="filete"></div>
<p>You did not buy a diet book. You bought <b>50 ready-to-use answers</b> to the question that can derail any eating routine: <i>“What should I cook today?”</i>.</p>
<p>Low carb does not mean living on sad salads. It means enjoying a creamy omelet, a lasagna you can slice, a Sunday feijoada, and even cheesecake — swapping refined flour and sugar for ingredients that satisfy, without cooking two separate meals.</p>
<p>Every recipe was selected for three reasons: <b>easy-to-find ingredients</b>, <b>realistic time for busy people</b>, and <b>leftovers that solve tomorrow’s meal</b>.</p>
<div class="quadro"><b>The golden rule of this book:</b> carbohydrates are accents, not the foundation. They add flavor and color — tomato, carrot, fruit — while the foundation is always protein, good fat, and vegetables.</div>
<p>Cook one new recipe a day for seven weeks and you will have a repertoire that can rescue any Monday. Enjoy.</p></section>
<section class="frente"><h2>How to Use This Book</h2><div class="filete"></div>
<p><b>1. Start at the end.</b> Check the “7-Day Menu” bonus and the shopping list before going to the store. Cooking without a plan is the fastest way to order takeout on Thursday.</p>
<p><b>2. Double the right recipe.</b> Most lunch and dinner recipes make two servings: the second becomes tomorrow’s lunch.</p>
<p><b>3. Use the boxes.</b> Each recipe includes a <b>Cooking Tip</b> and a <b>Smart Swap</b> to help you adapt without leaving the low-carb approach.</p>
<p><b>4. Do not chase zero carbs.</b> The nutritional numbers are there to help you choose, not to turn food into a prison.</p>
<p><b>5. Freeze with confidence.</b> Recipes with freezing notes were designed for individual portions and sealed containers.</p></section>
<section class="frente"><h2>Substitutions That Save Any Pantry</h2><div class="filete"></div>
<p>Low carb is also a game of smart swaps. Keep this table handy:</p>
<table><tr><th>Remove</th><th>Use instead</th><th>Note</th></tr>
<tr><td>Refined sugar</td><td><b>Erythritol or xylitol</b></td><td>1:1; xylitol is slightly sweeter</td></tr><tr><td>Wheat flour</td><td><b>Almond flour + 1 egg</b></td><td>use half the amount; egg provides structure</td></tr>
<tr><td>White rice</td><td><b>Riced cauliflower</b></td><td>sauté raw over high heat for 5–6 minutes</td></tr><tr><td>Pasta</td><td><b>Zucchini, hearts of palm, or konjac</b></td><td>sauté for 90 seconds to 3 minutes</td></tr>
<tr><td>Potato</td><td><b>Cauliflower, turnip, or roasted radish</b></td><td>for mash and broths; use pumpkin moderately</td></tr><tr><td>Prepared sauce</td><td><b>Peeled tomatoes + seasoning</b></td><td>simmer over low heat for 20 minutes</td></tr></table>
<h2 style="margin-top:6mm">Pantry Staples</h2><div class="lista2"><ul><li>Almond flour and unsweetened shredded coconut</li><li>Erythritol or xylitol and 100% cocoa</li><li>Unsweetened coconut milk and cream</li><li>Olive oil, coconut oil, and butter</li><li>Eggs and cheeses: mozzarella, Parmesan, cream cheese</li><li>Cauliflower, zucchini, eggplant, cabbage, and kale</li><li>Canned peeled tomatoes and olives</li><li>Chicken, ground beef, fish, and canned tuna</li><li>Nuts, lemons, fresh herbs, and smoked paprika</li><li>Chia seeds and golden flaxseed meal</li></ul></div></section>
"""

BONUS = """
<section class="frente"><h2>Bonus 1 — 7-Day Menu</h2><div class="filete"></div><p>A realistic first-week plan: filling breakfasts, lunches that become dinner, and a sweet option at the right time. Numbers refer to recipes in this book.</p>
<table><tr><th>Day</th><th>Breakfast</th><th>Lunch</th><th>Snack</th><th>Dinner</th></tr><tr><td class="dia">Mon</td><td>01 · baked omelet</td><td>10 + 23 · cauliflower rice with chicken</td><td>09 · yogurt granola</td><td>37 · cauliflower pizza</td></tr><tr><td class="dia">Tue</td><td>05 · tapioca crepe</td><td>17 · eggplant lasagna</td><td>06 · cheese bread</td><td>31 · salmon + 44 · mousse</td></tr><tr><td class="dia">Wed</td><td>02 · microwave bread</td><td>11 · zucchini noodles</td><td>45 · coconut flan</td><td>35 · fish moqueca</td></tr><tr><td class="dia">Thu</td><td>07 · collard wrap</td><td>13 · complete chicken salad</td><td>08 · avocado eggs</td><td>26 · steak with mushrooms</td></tr><tr><td class="dia">Fri</td><td>03 · banana pancakes</td><td>16 · cauliflower shepherd's pie</td><td>09 · yogurt granola</td><td>33 · garlic shrimp</td></tr><tr><td class="dia">Sat</td><td>04 · savory muffins</td><td>18 · stuffed eggplant</td><td>46 · chocolate cream</td><td>42 · low-carb sushi</td></tr><tr><td class="dia">Sun</td><td>06 · cheese bread</td><td>30 · pulled pork ribs</td><td>47 · cheesecake</td><td>19 · kale soup + 28 · steak</td></tr></table><p class="legal">Adjust portions to your needs. This menu is an educational suggestion, not a prescription.</p></section>
<section class="frente"><h2>Bonus 2 — First-Week Shopping List</h2><div class="filete"></div><p>Print this list and take it to the store. It is designed for two people:</p><div class="lista2"><ul class="check"><li>2 dozen eggs</li><li>1 kg chicken breast + 8 thighs</li><li>1 kg ground beef + 500 g steak</li><li>600 g salmon or firm fish + 400 g shrimp</li><li>2 cans tuna</li><li>500 g mozzarella + Parmesan + cream cheese</li><li>Heavy cream</li><li>2 containers unsweetened coconut milk</li><li>Cauliflower, zucchini, eggplant, cabbage, and kale</li><li>Fresh tomatoes + 2 cans peeled tomatoes</li><li>Avocado, bananas, strawberries, and lemons</li><li>Onions, garlic, ginger, herbs, smoked paprika</li><li>Olives, hearts of palm, nuts, and peanuts</li><li>Almond flour, shredded coconut, and chia</li><li>Erythritol or xylitol, 100% cocoa, and 85% chocolate</li><li>Olive oil, butter, and coconut oil</li><li>Soy sauce and mustard</li></ul></div><div class="quadro"><b>Shopping rule:</b> visit produce and the meat counter first; leave packaged products for last and always check the label.</div></section>
<section class="frente"><h2>Before You Close the Kitchen</h2><div class="filete"></div><p>You now have 50 recipes designed for real life: easy-to-find ingredients, one-pot methods, and planned leftovers. The difference between this ebook and a more organized week is one small decision: <b>your next meal</b>.</p><p>Choose one recipe for tonight, make it, and share it with someone. Shared food is easier to repeat.</p><div class="quadro"><b>UPCOMING PRACTICAL KITCHEN VOLUMES:</b> Volume 2 — <i>Low-Carb Meals for the Week</i> · Volume 3 — <i>Sugar-Free Party Desserts</i>.</div></section>
"""

COVER = """<section class="capa"><div class="txt"><div class="kicker">Practical Kitchen Series · vol. 1</div><h1>50 RECIPES<br><span class="hl">LOW CARB</span></h1><div class="sub">for everyday life — no flour, no sugar, no sacrifice</div></div><div class="faixa"><span class="marca">PRACTICAL KITCHEN</span><span>less carbs, more real life</span></div></section>"""
BACK = """<section class="contra"><div class="in"><h2>Stop starting your diet every Monday.</h2><p>This book brings together 50 recipes for staying low carb without cooking twice: breakfasts that carry you through the morning, lunches that become dinner, soups for cold nights, and desserts that need no apology.</p><ul><li><b>50 complete recipes</b> with time, yield, and estimated macros per serving;</li><li><b>Cooking Tip</b> in every recipe to prevent the most common mistake;</li><li><b>Smart Swap</b> ideas for adapting ingredients;</li><li><b>7-Day Menu</b> and a printable shopping list;</li><li><b>Substitution table</b> for flour, sugar, rice, and pasta.</li></ul><p>Easy-to-find ingredients. Realistic time. Food for people who do not want to feel on a diet.</p><div class="marca">PRACTICAL KITCHEN</div></div></section>"""


def recipe_html(r):
    num, rid, d = r["num"], r["id"], r["d"]
    name, prep, total, servings, kcal, carbs, protein, fat, ingredients, steps, tip, swap = d
    ing = "".join("<li>%s</li>" % H.escape(x) for x in ingredients)
    pas = "".join("<li>%s</li>" % H.escape(x) for x in steps)
    return """<section class="receita" id="%s"><header><div class="num">%02d</div><div class="titulo"><h3>%s</h3></div></header><img class="foto" src="imagens/receita-%02d.jpg" alt="%s"><div class="meta"><span><b>Preparation</b> %d min</span><span><b>Total</b> %d min</span><span><b>Yield</b> %s</span><span><b>Difficulty</b> easy</span></div><div class="nutris"><span><b>%d</b>kcal / serving</span><span><b>%d g</b>carbohydrates</span><span><b>%d g</b>protein</span><span><b>%d g</b>fat</span></div><div class="corpo"><div><h4>Ingredients</h4><ul class="ing">%s</ul></div><div><h4>Method</h4><ol class="passos">%s</ol></div></div><div class="dica"><b>COOKING TIP:</b> %s</div><div class="troca"><b>↺ SMART SWAP:</b> %s</div></section>""" % (rid, num, H.escape(name), num, H.escape(name), prep, total, H.escape(str(servings)), kcal, carbs, protein, fat, ing, pas, H.escape(tip), H.escape(swap))


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
    return "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'><style>%s</style></head><body>%s%s%s%s%s%s</body></html>" % (CSS, COVER, FRONT, toc_html(pmap), body_html(), BONUS, BACK)


def build():
    from weasyprint import HTML
    import fitz
    open('ebook_en_probe.html', 'w').write(render(None)); HTML(filename='ebook_en_probe.html').write_pdf('ebook_en_probe.pdf')
    d = fitz.open('ebook_en_probe.pdf'); pmap = {}
    for i in range(d.page_count):
        text = d[i].get_text(); norm = text.replace(' ', '')
        if 'INGREDIENTS' in norm and 'METHOD' in norm:
            m = re.search(r'(?m)^(\d{2})\n', text)
            if m and 1 <= int(m.group(1)) <= 50: pmap[int(m.group(1))] = i + 1
    assert len(pmap) == 50, (len(pmap), sorted(set(range(1, 51)) - set(pmap)))
    open('50-low-carb-recipes-en.html', 'w').write(render(pmap)); HTML(filename='50-low-carb-recipes-en.html').write_pdf('50-low-carb-recipes-en.pdf')
    print('English PDF generated:', len(pmap), 'recipes mapped')

if __name__ == '__main__': build()
