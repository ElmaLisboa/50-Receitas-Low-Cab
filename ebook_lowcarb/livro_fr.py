# -*- coding: utf-8 -*-
"""Édition française de 50 Recettes Low Carb pour le Quotidien."""
import html as H
import re
import livro as pt
import livro_en as layout

NAMES = [
 "Omelette au four aux épinards et au fromage", "Pain low carb au micro-ondes en 2 minutes", "Pancakes à la banane et à l'avoine sans farine",
 "Muffins salés aux œufs, légumes et bacon", "Crêpe de tapioca à la poêle, fromage et tomate", "Pain au fromage à la poêle",
 "Wrap de chou vert au poulet crémeux", "Œufs brouillés crémeux à l'avocat et aux graines", "Yaourt protéiné au granola de fruits secs",
 "Riz de chou-fleur simple", "Nouilles de courgette à la sauce tomate maison", "Nouilles de cœurs de palmier à l'ail et à l'huile",
 "Salade complète de poulet et sauce au yaourt", "Salade de thon, œuf et mayonnaise au citron", "Wrap de laitue au bœuf haché épicé",
 "Hachis de chou-fleur au bœuf effiloché", "Lasagnes d'aubergine à la bolognaise", "Aubergine farcie au bœuf haché",
 "Soupe verte low carb sans pomme de terre", "Soupe de potiron au lait de coco et gingembre", "Soupe de légumes au poulet effiloché",
 "Velouté de courgette au fromage frais", "Poulet grillé sauce moutarde et crème", "Cuisses de poulet rôties au citron et romarin",
 "Poêlée de poulet low carb", "Steak sauce aux champignons", "Bœuf haché aux courgettes et à la tomate",
 "Steak aux oignons et au beurre à l'ail", "Boulettes de viande farcies au fromage, sauce tomate", "Travers de porc effilochés",
 "Saumon au four au beurre citronné", "Tilapia pané à la farine d'amande", "Crevettes à l'ail", "Cabillaud au chou-fleur et aux olives",
 "Moqueca de poisson au lait de coco et cœurs de palmier", "Calamars grillés au citron et aux herbes",
 "Pizza de chou-fleur à la mozzarella et au basilic", "Aubergine parmigiana sans panure", "Feijoada low carb sans haricots",
 "Pain au fromage à la friteuse à air", "Courgette farcie au thon et au fromage frais", "Sushi low carb — rouleaux de concombre",
 "Roulés de chou farcis au bœuf haché", "Mousse au chocolat et à l'avocat", "Flan à la noix de coco et à l'érythritol",
 "Crème au chocolat low carb à la cuillère", "Cheesecake low carb aux fruits rouges", "Cookies low carb aux fruits secs et au chocolat",
 "Truffes au chocolat et à l'huile de coco", "Confiserie de cacahuètes low carb façon paçoca"
]

CAT = {
 "Café da manhã e lanches rápidos": ("Petits-déjeuners et en-cas rapides", "Commencez la journée avec des recettes pratiques et rassasiantes, sans dépendre du pain traditionnel. Ce chapitre réunit œufs, fromages, farines d'amande ou de coco et fruits en portions équilibrées. La plupart des recettes demandent au maximum 15 minutes de préparation active."),
 "Almoços completos": ("Déjeuners complets", "Des plats préparés dans une seule casserole, des salades qui tiennent toute l'après-midi et des alternatives intelligentes au riz et aux pâtes — sans goût de régime."),
 "Sopas e caldos": ("Soupes et bouillons", "Pour les soirées froides et les repas à emporter : une texture crémeuse sans pommes de terre ni farine de blé."),
 "Carnes e aves": ("Viandes et volailles", "Les protéines sont la base d'une bonne alimentation low carb : dorées, juteuses et accompagnées de vraies sauces — jamais un poulet sec de meal prep."),
 "Peixes e frutos do mar": ("Poissons et fruits de mer", "Du saumon du dimanche aux fruits de mer rapides de la semaine : de bonnes graisses, une préparation courte et un goût de restaurant."),
 "Jantares em até 30 minutos de bancada": ("Dîners prêts en 30 minutes", "La règle du soir : le dîner est prêt avant la fin de l'épisode. Des recettes à la poêle, au four ou à la friteuse à air."),
 "Sobremesas sem açúcar": ("Desserts sans sucre", "Un vrai dessert n'a pas besoin de sucre raffiné : cacao, coco, fruits secs et édulcorants qui respectent le goût."),
}

PHRASES = [
 ("não doce", "non sucré"), ("não dá", "ne donne pas"), ("não é", "n'est pas"),
 ("pimenta-do-reino", "poivre noir"), ("cheiro-verde", "herbes fraîches"), ("couve manteiga", "chou vert"),
 ("couve-flor", "chou-fleur"), ("couve", "chou vert"), ("abobrinha", "courgette"), ("berinjela", "aubergine"),
 ("palmito pupunha", "cœurs de palmier"), ("palmito", "cœurs de palmier"), ("tomate pelado", "tomates entières pelées"),
 ("creme de leite fresco", "crème liquide"), ("creme de leite", "crème liquide"), ("cream cheese", "fromage frais"),
 ("requeijão", "fromage frais"), ("muçarela", "mozzarella"), ("queijo parmesão", "parmesan"), ("queijo", "fromage"),
 ("farinha de amêndoas", "farine d'amande"), ("farinha de coco", "farine de coco"), ("farinha de linhaça dourada", "farine de lin doré"),
 ("polvilho azedo", "fécule de manioc aigre"), ("goma de tapioca", "gomme de tapioca"), ("leite de coco", "lait de coco"),
 ("carne seca", "viande séchée effilochée"), ("carne moída", "bœuf haché"), ("frango desfiado", "poulet effiloché"),
 ("peito de frango", "blanc de poulet"), ("ovos mexidos", "œufs brouillés"), ("ovos cozidos", "œufs durs"),
 ("ovo cozido", "œuf dur"), ("castanha-de-caju", "noix de cajou"), ("castanha do pará", "noix du Brésil"),
 ("castanhas", "fruits secs"), ("manteiga de amendoim", "beurre de cacahuète"), ("pasta de amendoim", "beurre de cacahuète"),
 ("amendoim", "cacahuètes"), ("morangos", "fraises"), ("morango", "fraise"), ("abacate", "avocat"), ("abóbora", "potiron"),
 ("pepino", "concombre"), ("tomate", "tomate"), ("cebola", "oignon"), ("alho", "ail"), ("dentes", "gousses"), ("dente", "gousse"),
 ("salsão", "céleri"), ("vagem", "haricots verts"), ("cenoura", "carotte"), ("pimentão", "poivron"), ("cogumelos", "champignons"),
 ("shimeji", "champignons shimeji"), ("salmão", "saumon"), ("camarão", "crevette"), ("camarões", "crevettes"), ("tilápia", "tilapia"),
 ("bacalhau", "cabillaud"), ("lula", "calamar"), ("costelinha", "travers de porc"), ("linguiça", "saucisse"), ("bacon", "lard fumé"),
 ("presunto cru", "jambon cru"), ("presunto", "jambon"), ("iogurte", "yaourt"), ("azeitona", "olive"), ("azeitonas", "olives"),
 ("azeite", "huile d'olive"), ("vinagre de maçã", "vinaigre de cidre"), ("vinagre de vinho tinto", "vinaigre de vin rouge"),
 ("mostarda dijon", "moutarde de Dijon"), ("mostarda", "moutarde"), ("shoyu", "sauce soja"), ("molho de tomate", "sauce tomate"),
 ("molho", "sauce"), ("caldo de legumes", "bouillon de légumes"), ("caldo de galinha", "bouillon de poulet"), ("caldo de carne", "bouillon de bœuf"),
 ("páprica defumada", "paprika fumé"), ("páprica", "paprika"), ("orégano", "origan"), ("manjericão", "basilic"), ("salsinha", "persil"),
 ("cebolinha", "ciboulette"), ("coentro", "coriandre"), ("alecrim", "romarin"), ("gengibre", "gingembre"), ("canela", "cannelle"),
 ("cacau em pó", "cacao en poudre non sucré"), ("cacau", "cacao"), ("coco ralado", "noix de coco râpée"), ("coco em flocos", "copeaux de coco"),
 ("sementes de girassol", "graines de tournesol"), ("sementes de abóbora", "graines de courge"), ("sementes de chia", "graines de chia"),
 ("sementes", "graines"), ("farinha", "farine"), ("açúcar", "sucre"), ("adoçante", "édulcorant"), ("essência", "extrait"),
 ("fermento em pó", "levure chimique"), ("em pó", "en poudre"), ("sem açúcar", "sans sucre"), ("sem farinha", "sans farine"),
 ("sem sementes", "sans pépins"), ("sem pele", "sans peau"), ("a gosto", "selon le goût"), ("para servir", "pour servir"),
 ("para finalizar", "pour terminer"), ("em cubos", "en dés"), ("em rodelas", "en rondelles"), ("em fatias", "en tranches"),
 ("em tiras", "en lamelles"), ("picada", "hachée"), ("picado", "haché"), ("picadas", "hachées"), ("picados", "hachés"),
 ("ralada", "râpée"), ("ralado", "râpé"), ("raladas", "râpées"), ("ralados", "râpés"), ("escorrido", "égoutté"),
 ("escorrida", "égouttée"), ("escorridas", "égouttées"), ("desfiado", "effiloché"), ("desfiada", "effilochée"),
 ("desfiados", "effilochés"), ("espremida", "pressée"), ("espremido", "pressé"), ("congelado", "surgelé"),
 ("derretida", "fondue"), ("derretido", "fondu"), ("cozida", "cuite"), ("cozido", "cuit"), ("quente", "chaud"),
 ("morno", "tiède"), ("crocante", "croustillant"), ("cremoso", "crémeux"), ("cremosa", "crémeuse"),
 ("xíc.", "tasse"), ("col. sopa", "c. à soupe"), ("col. chá", "c. à café"), ("col.", "c. à soupe")]

VERBS = [("Não lave", "Ne lavez pas"), ("Não mexa", "Ne remuez pas"), ("Não deixe", "Ne laissez pas"),
 ("Leve ao micro-ondas", "Passez au micro-ondes"), ("Leve ao forno", "Enfournez"), ("Leve à geladeira", "Réfrigérez"),
 ("Leve ao congelador", "Placez au congélateur"), ("Volte à panela", "Remettez dans la poêle"), ("Volte o", "Remettez le"),
 ("Refogue", "Faites revenir"), ("Junte", "Ajoutez"), ("Acrescente", "Ajoutez"), ("Bata", "Fouettez"), ("Misture", "Mélangez"),
 ("Incorpore", "Incorporez"), ("Asse", "Faites cuire"), ("Cozinhe", "Faites cuire"), ("Aqueça", "Chauffez"), ("Despeje", "Versez"),
 ("Tempere", "Assaisonnez"), ("Sirva", "Servez"), ("Finalize", "Terminez"), ("Reserve", "Réservez"), ("Deixe", "Laissez"),
 ("Corte", "Coupez"), ("Retire", "Retirez"), ("Frite", "Faites frire"), ("Grelhe", "Faites griller"), ("Sele", "Saisissez"),
 ("Passe", "Passez"), ("Abra", "Ouvrez"), ("Modele", "Formez"), ("Distribua", "Répartissez"), ("Cubra", "Couvrez"),
 ("Regue", "Arrosez"), ("Acomode", "Déposez"), ("Processe", "Mixez"), ("Rale", "Râpez"), ("Esprema", "Pressez"),
 ("Poche", "Pochez"), ("Monte", "Assemblez"), ("Amasse", "Écrasez"), ("Doure", "Faites dorer"), ("Derreta", "Faites fondre"),
 ("Toste", "Faites griller"), ("Salgue", "Salez"), ("Envolva", "Enrobez"), ("Aperte", "Pressez"), ("Ajuste", "Rectifiez"),
 ("Mantenha", "Gardez"), ("Aguarde", "Attendez"), ("Espalhe", "Étalez")]

WORD_MAP = [("ovos", "œufs"), ("ovo", "œuf"), ("sal", "sel"), ("pimenta", "poivre"), ("limão", "citron"), ("ervas", "herbes"), ("refogado", "préparation sautée"), ("queijos", "fromages"), ("especiarias", "épices"), ("torrado", "grillées"), ("barato", "bon marché"), ("igualmente", "également"), ("forrada", "tapissée"), ("papel-manteiga", "papier cuisson"), ("puxar", "tirer"), ("cor", "couleur"), ("aos", "aux"), ("só", "seulement"), ("fica", "devient"), ("você", "vous"), ("assa", "cuit au four"), ("dá", "donne"), ("pão", "pain"), ("use", "utilisez"), ("pronto", "prêt"), ("doce", "sucré"), ("é", "est"), ("puxa-puxa", "élastique"), ("massa", "pâte"), ("azedo", "aigre"), ("ele", "il"), ("pastosa", "pâteuse"), ("suco", "jus"), ("frango", "poulet"), ("carne", "viande"), ("salada", "salade"), ("mesmos", "mêmes"), ("mesma", "même"), ("dourado", "doré"), ("dourada", "dorée"), ("creme", "crème"), ("amarela", "jaune"), ("mel", "miel"), ("assadeira", "plaque"), ("últimos", "dernières"), ("pele", "peau"), ("peixe", "poisson"), ("solta", "libère"), ("lascas", "morceaux"), ("pressionado", "pressé"), ("passar do ponto", "trop cuire"), ("cara", "chère"), ("firme", "ferme"), ("como", "comme"), ("anéis", "anneaux"), ("polvo", "poulpe"), ("balançar", "secouer"), ("em cima", "dessus"), ("camadas", "couches"),
 ("minutos", "minutes"), ("minuto", "minute"), ("pequeno", "petit"), ("pequena", "petite"), ("untado", "graissé"), ("untada", "graissée"),
 ("firmar", "prendre"), ("dura", "se conserve"), ("segundo", "seconde"), ("mesma", "même"), ("técnica", "technique"), ("sabor", "goût"),
 ("gosto", "goût"), ("vez", "fois"), ("dias", "jours"), ("amanhã", "demain"), ("mais", "plus"), ("neutro", "neutre"),
 ("centro", "centre"), ("porção", "portion"), ("atum", "thon"), ("trocando", "en changeant"), ("leve", "léger"), ("faça", "faites"),
 ("qualquer", "n'importe quel"), ("tire", "retirez"), ("geladeira", "réfrigérateur"), ("óleo", "huile"), ("fogo", "feu"),
 ("panela", "poêle"), ("forno", "four"), ("água", "eau"), ("receita", "recette"), ("pote", "bocal"), ("potes", "bocaux"),
 ("depois", "ensuite"), ("ainda", "encore"), ("muita", "beaucoup de"), ("muito", "très"), ("crua", "crue"), ("cru", "cru"),
 ("recheie", "remplissez"), ("rechear", "remplir"), ("escorra", "égouttez"), ("desligue", "éteignez"), ("fervente", "bouillante"), ("não", "ne"), ("fazer", "faire"), ("coloque", "placez"), ("coloca", "placez"), ("congele", "congelez"), ("grelhando", "en grillant"), ("trocando", "en changeant"), ("pré-cuit", "précuit"), ("cuita", "cuite"), ("já", "déjà"), ("arroz", "riz"), ("latas", "boîtes"), ("lata", "boîte"), ("dica", "conseil"), ("troque", "remplacez"), ("caneca", "tasse"), ("duas", "deux"), ("grão-de-bico", "pois chiches")]

def translate_text(value, steps=False):
    s=str(value)
    for a,b in sorted(PHRASES,key=lambda x:len(x[0]),reverse=True): s=re.sub(r"(?<!\w)"+re.escape(a)+r"(?!\w)",b,s,flags=re.IGNORECASE)
    for a,b in sorted(VERBS,key=lambda x:len(x[0]),reverse=True): s=re.sub(r"^("+re.escape(a)+r")\b",b,s,flags=re.IGNORECASE)
    connectors=[(" até "," jusqu'à "),(" com "," avec "),(" sem "," sans "),(" em "," dans "),(" no "," dans le "),(" na "," dans la "),(" dos "," des "),(" das "," des "),(" do "," du "),(" da "," de la "),(" e "," et "),(" ou "," ou "),(" de "," de "),(" por "," pendant ")]
    for a,b in sorted(connectors,key=lambda x:len(x[0]),reverse=True):s=s.replace(a,b)
    fixes=[("minutos em fogo baixo","minutes à feu doux"),("fogo baixo","feu doux"),("fogo alto","feu vif"),("fogo médio","feu moyen"),("até ficar","jusqu'à ce que"),("até dourar","jusqu'à ce que ce soit doré"),("até firmar","jusqu'à ce que ce soit pris"),("até secar","jusqu'à évaporation"),("na geladeira","au réfrigérateur"),("no forno","au four"),("no micro-ondas","au micro-ondes"),("no liquidificador","au mixeur"),("com as mãos","avec les mains"),("de um dia para o outro","toute une nuit"),("por no mínimo","pendant au moins")]
    for a,b in fixes:s=s.replace(a,b)
    for a,b in sorted(VERBS,key=lambda x:len(x[0]),reverse=True):s=re.sub(r"(?<!\w)"+re.escape(a)+r"(?!\w)",b.lower(),s,flags=re.IGNORECASE)
    for a,b in sorted(WORD_MAP,key=lambda x:len(x[0]),reverse=True):s=re.sub(r"(?<!\w)"+re.escape(a)+r"(?!\w)",b,s,flags=re.IGNORECASE)
    articles=[("dos","des"),("das","des"),("do","du"),("da","de la"),("os","les"),("as","les"),("uma","une"),("duas","deux"),("dois","deux"),("um","un"),("com","avec"),("sem","sans"),("em","dans"),("no","dans le"),("na","dans la"),("e","et"),("ou","ou"),("o","le"),("a","la")]
    for a,b in articles:s=re.sub(r"(?<!\w)"+re.escape(a)+r"(?!\w)",b,s,flags=re.IGNORECASE)
    return s

PT_TO_FR={r["d"][0]:NAMES[r["num"]-1] for r in pt.RECEITAS}
RECIPES=[]
for r in pt.RECEITAS:
 d=r["d"];name,prep,total,servings,kcal,carbs,protein,fat,ingredients,steps,tip,swap=d
 RECIPES.append({"num":r["num"],"id":r["id"],"cat":CAT[r["cat"]][0],"d":(PT_TO_FR[name],prep,total,servings,kcal,carbs,protein,fat,[translate_text(x) for x in ingredients],[translate_text(x,True) for x in steps],translate_text(tip,True),translate_text(swap,True))})
SELECTION=[]
for cat_pt,intro_pt,names in pt.SELECAO:
 cat_fr,intro_fr=CAT[cat_pt];SELECTION.append((cat_fr,intro_fr,[PT_TO_FR[n] for n in names]))
CSS=layout.CSS.replace("50 Low-Carb Recipes for Everyday Life","50 Recettes Low Carb pour le Quotidien")+"\n@page { margin-bottom: 6mm; } .dica { padding: 2mm 3mm; margin-top: 1.5mm; font-size: 7.7pt; } .troca { padding: 0.8mm 3mm; margin-top: 0.8mm; font-size: 7.3pt; line-height: 1.3; }"

FRONT="""
<section class="frente legal"><h2>Crédits et mentions légales</h2><div class="filete"></div><p><b>50 Recettes Low Carb pour le Quotidien</b> — 1re édition, 2026.<br>Série Cuisine Pratique · volume 1.</p><p>Tous droits réservés. La reproduction totale ou partielle de ce document est interdite sans autorisation écrite. Cet ebook est un produit numérique destiné à l'acheteur.</p><div class="quadro"><b>AVIS IMPORTANT :</b> les informations nutritionnelles sont des <b>estimations par portion</b> et peuvent varier selon la marque, la taille des ingrédients et le matériel. Ce livre est éducatif et <b>ne remplace pas</b> les conseils d'un médecin ou d'un professionnel de la nutrition. Les personnes diabétiques, atteintes d'une maladie rénale, enceintes, allaitantes ou prenant des médicaments de façon continue doivent demander un avis professionnel avant d'adopter une alimentation pauvre en glucides. Le xylitol est toxique pour les chiens : gardez les desserts hors de leur portée.</div><p><b>Mesures utilisées :</b> 1 tasse = 240 ml · 1 c. à soupe = 15 ml · 1 c. à café = 5 ml · four toujours préchauffé, sauf indication contraire.</p></section>
<section class="frente"><h2>Bienvenue dans votre cuisine low carb</h2><div class="filete"></div><p>Vous n'avez pas acheté un livre de régime. Vous avez acheté <b>50 réponses prêtes</b> à la question qui peut faire dérailler toute routine : <i>« Que vais-je cuisiner aujourd'hui ? »</i>.</p><p>Manger low carb ne signifie pas vivre de salades tristes. Cela signifie savourer une omelette crémeuse, des lasagnes qui se tiennent, une feijoada du dimanche et même un cheesecake, avec des ingrédients rassasiants.</p><div class="quadro"><b>La règle d'or :</b> les glucides sont un accent, pas la base. La base est toujours composée de protéines, de bonnes graisses et de légumes.</div><p>Une nouvelle recette par jour pendant sept semaines : vous aurez un répertoire capable de sauver n'importe quel lundi. Bon appétit.</p></section>
<section class="frente"><h2>Comment utiliser ce livre</h2><div class="filete"></div><p><b>1. Commencez par la fin.</b> Consultez le bonus « Menu de 7 jours » et la liste de courses avant de faire vos achats.</p><p><b>2. Doublez la bonne recette.</b> La plupart des déjeuners et dîners donnent deux portions : la seconde devient le déjeuner du lendemain.</p><p><b>3. Utilisez les encadrés.</b> Chaque recette propose un <b>Conseil de cuisine</b> et un <b>Remplacement intelligent</b>.</p><p><b>4. Ne cherchez pas zéro glucide.</b> Les valeurs nutritionnelles vous aident à choisir, elles ne doivent pas transformer le repas en contrainte.</p><p><b>5. Congelez sans crainte.</b> Les recettes avec des indications de congélation sont prévues pour des portions individuelles.</p></section>
<section class="frente"><h2>Les remplacements qui sauvent le garde-manger</h2><div class="filete"></div><p>Le low carb, c'est aussi l'art de remplacer intelligemment :</p><table><tr><th>À retirer</th><th>À utiliser</th><th>Remarque</th></tr><tr><td>Sucre raffiné</td><td><b>Érythritol ou xylitol</b></td><td>1:1 ; le xylitol est un peu plus sucré</td></tr><tr><td>Farine de blé</td><td><b>Farine d'amande + 1 œuf</b></td><td>utiliser la moitié ; l'œuf lie la préparation</td></tr><tr><td>Riz blanc</td><td><b>Chou-fleur en riz</b></td><td>faire revenir cru 5–6 minutes à feu vif</td></tr><tr><td>Pâtes</td><td><b>Courgette, cœurs de palmier ou konjac</b></td><td>faire revenir 90 secondes à 3 minutes</td></tr><tr><td>Pomme de terre</td><td><b>Chou-fleur, navet ou radis rôti</b></td><td>pour les purées et les bouillons</td></tr></table><h2 style="margin-top:6mm">Les indispensables</h2><div class="lista2"><ul><li>Farine d'amande et noix de coco râpée sans sucre</li><li>Érythritol ou xylitol et cacao 100 %</li><li>Lait de coco et crème non sucrés</li><li>Huile d'olive, huile de coco et beurre</li><li>Œufs, mozzarella, parmesan et fromage frais</li><li>Chou-fleur, courgette, aubergine, chou et chou vert</li><li>Tomates pelées en boîte et olives</li><li>Poulet, bœuf haché, poisson et thon en boîte</li><li>Fruits secs, citrons, herbes fraîches et paprika fumé</li></ul></div></section>
"""
BONUS="""
<section class="frente"><h2>Bonus 1 — Menu de 7 jours</h2><div class="filete"></div><p>Un plan réaliste pour la première semaine : des petits-déjeuners rassasiants, des déjeuners qui deviennent le dîner et une touche sucrée au bon moment.</p><table><tr><th>Jour</th><th>Petit-déjeuner</th><th>Déjeuner</th><th>En-cas</th><th>Dîner</th></tr><tr><td class="dia">Lun</td><td>01 · omelette au four</td><td>10 + 23 · riz de chou-fleur au poulet</td><td>09 · yaourt et granola</td><td>37 · pizza de chou-fleur</td></tr><tr><td class="dia">Mar</td><td>05 · crêpe de tapioca</td><td>17 · lasagnes d'aubergine</td><td>06 · pain au fromage</td><td>31 · saumon + 44 · mousse</td></tr><tr><td class="dia">Mer</td><td>02 · pain au micro-ondes</td><td>11 · nouilles de courgette</td><td>45 · flan coco</td><td>35 · moqueca de poisson</td></tr><tr><td class="dia">Jeu</td><td>07 · wrap de chou vert</td><td>13 · salade de poulet</td><td>08 · œufs et avocat</td><td>26 · steak aux champignons</td></tr><tr><td class="dia">Ven</td><td>03 · pancakes à la banane</td><td>16 · hachis de chou-fleur</td><td>09 · yaourt et granola</td><td>33 · crevettes à l'ail</td></tr><tr><td class="dia">Sam</td><td>04 · muffins salés</td><td>18 · aubergine farcie</td><td>46 · crème au chocolat</td><td>42 · sushi low carb</td></tr><tr><td class="dia">Dim</td><td>06 · pain au fromage</td><td>30 · travers de porc</td><td>47 · cheesecake</td><td>19 · soupe verte + 28 · steak</td></tr></table></section>
<section class="frente"><h2>Bonus 2 — Liste de courses de la première semaine</h2><div class="filete"></div><p>Imprimez cette liste et emportez-la au marché. Elle est prévue pour deux personnes :</p><div class="lista2"><ul class="check"><li>2 douzaines d'œufs</li><li>1 kg de blanc de poulet + 8 cuisses</li><li>1 kg de bœuf haché + 500 g de steak</li><li>600 g de saumon ou poisson ferme + 400 g de crevettes</li><li>2 boîtes de thon</li><li>500 g de mozzarella + parmesan + fromage frais</li><li>Crème liquide</li><li>2 briques de lait de coco non sucré</li><li>Chou-fleur, courgettes, aubergines, chou et chou vert</li><li>Tomates fraîches + 2 boîtes de tomates pelées</li><li>Avocats, bananes, fraises et citrons</li><li>Oignons, ail, gingembre, herbes et paprika fumé</li><li>Olives, cœurs de palmier, fruits secs et cacahuètes</li><li>Farine d'amande, noix de coco râpée et chia</li><li>Érythritol ou xylitol, cacao et chocolat à 85 %</li><li>Huile d'olive, beurre et huile de coco</li><li>Sauce soja et moutarde</li></ul></div></section>
<section class="frente"><h2>Avant de fermer la cuisine</h2><div class="filete"></div><p>Vous avez maintenant 50 recettes conçues pour la vraie vie : des ingrédients faciles à trouver, une préparation simple et des restes planifiés. La différence entre cet ebook et une semaine mieux organisée tient à une petite décision : <b>votre prochain repas</b>.</p><p>Choisissez une recette pour ce soir, préparez-la et partagez-la avec quelqu'un. Cuisiner à plusieurs donne envie de recommencer.</p><div class="quadro"><b>PROCHAINS VOLUMES DE CUISINE PRATIQUE :</b> Volume 2 — <i>Repas low carb pour la semaine</i> · Volume 3 — <i>Desserts de fête sans sucre</i>.</div></section>
"""
COVER="""<section class="capa"><div class="txt"><div class="kicker">Série Cuisine Pratique · vol. 1</div><h1>50 RECETTES<br><span class="hl">LOW CARB</span></h1><div class="sub">pour le quotidien — sans farine, sans sucre et sans frustration</div></div><div class="faixa"><span class="marca">CUISINE PRATIQUE</span><span>moins de glucides, plus de vraie vie</span></div></section>"""
BACK="""<section class="contra"><div class="in"><h2>Arrêtez de recommencer le régime chaque lundi.</h2><p>Ce livre réunit 50 recettes pour une routine low carb sans cuisiner deux fois : des petits-déjeuners rassasiants, des déjeuners qui deviennent le dîner, des soupes pour les soirées froides et des desserts sans culpabilité.</p><ul><li><b>50 recettes complètes</b> avec temps, portions et valeurs nutritionnelles estimées ;</li><li><b>Conseil de cuisine</b> pour chaque recette ;</li><li><b>Remplacement intelligent</b> pour adapter les ingrédients ;</li><li><b>Menu de 7 jours</b> et liste de courses imprimable ;</li><li><b>Tableau de remplacement</b> pour farine, sucre, riz et pâtes.</li></ul><p>Des ingrédients faciles à trouver. Un temps réaliste. Le goût d'une cuisine qui ne ressemble pas à un régime.</p><div class="marca">CUISINE PRATIQUE</div></div></section>"""

def recipe_html(r):
 num,rid,d=r["num"],r["id"],r["d"];name,prep,total,servings,kcal,carbs,protein,fat,ingredients,steps,tip,swap=d
 ing=''.join('<li>%s</li>'%H.escape(x) for x in ingredients);pas=''.join('<li>%s</li>'%H.escape(x) for x in steps)
 return '<section class="receita" id="%s"><header><div class="num">%02d</div><div class="titulo"><h3>%s</h3></div></header><img class="foto" src="imagens/receita-%02d.jpg" alt="%s"><div class="meta"><span><b>Préparation</b> %d min</span><span><b>Total</b> %d min</span><span><b>Rendement</b> %s</span><span><b>Difficulté</b> facile</span></div><div class="nutris"><span><b>%d</b>kcal / portion</span><span><b>%d g</b>glucides</span><span><b>%d g</b>protéines</span><span><b>%d g</b>matières grasses</span></div><div class="corpo"><div><h4>Ingrédients</h4><ul class="ing">%s</ul></div><div><h4>Préparation</h4><ol class="passos">%s</ol></div></div><div class="dica"><b>CONSEIL DE CUISINE :</b> %s</div><div class="troca"><b>↺ REMPLACEMENT INTELLIGENT :</b> %s</div></section>'%(rid,num,H.escape(name),num,H.escape(name),prep,total,H.escape(str(servings)),kcal,carbs,protein,fat,ing,pas,H.escape(tip),H.escape(swap))

def toc_html(pmap=None):
 out=['<section class="frente"><h2>Sommaire</h2><div class="filete"></div><div class="sum"><table>'];idx=0
 for cat,intro,names in SELECTION:
  out.append('<tr><td class="cat" colspan="4">%s</td></tr>'%H.escape(cat))
  for name in names:
   idx+=1;pg=str(pmap[idx]) if pmap else '';out.append('<tr><td class="num">%02d</td><td><a href="#r%02d">%s</a></td><td class="dots"></td><td class="pg">%s</td></tr>'%(idx,idx,H.escape(name),pg))
 out.append('</table></div></section>');return ''.join(out)

def body_html():
 out=[]
 for chapter,(cat,intro,names) in enumerate(SELECTION,1):
  out.append('<section class="abre"><img class="capfoto" src="imagens/capitulo-%02d.jpg" alt="Image du chapitre %s"><div class="tag">Chapitre %02d</div><h2>%s</h2><div class="filete"></div><p>%s</p></section>'%(chapter,H.escape(cat),chapter,H.escape(cat),H.escape(intro)))
  for r in RECIPES:
   if r["cat"]==cat:out.append(recipe_html(r))
 return ''.join(out)

def render(pmap=None):return "<!DOCTYPE html><html lang='fr'><head><meta charset='utf-8'><style>%s</style></head><body>%s%s%s%s%s%s</body></html>"%(CSS,COVER,FRONT,toc_html(pmap),body_html(),BONUS,BACK)

def build():
 from weasyprint import HTML
 import fitz
 open('ebook_fr_probe.html','w').write(render(None));HTML(filename='ebook_fr_probe.html').write_pdf('ebook_fr_probe.pdf')
 d=fitz.open('ebook_fr_probe.pdf');pmap={}
 for i in range(d.page_count):
  text=d[i].get_text();norm=text.replace(' ','')
  if 'INGRÉDIENTS' in norm and 'PRÉPARATION' in norm:
   m=re.search(r'(?m)^(\d{2})\n',text)
   if m and 1<=int(m.group(1))<=50:pmap[int(m.group(1))]=i+1
 assert len(pmap)==50,(len(pmap),sorted(set(range(1,51))-set(pmap)))
 open('50-recettes-low-carb-fr.html','w').write(render(pmap));HTML(filename='50-recettes-low-carb-fr.html').write_pdf('50-recettes-low-carb-fr.pdf')
 print('PDF français généré :',len(pmap),'recettes avec pagination')

if __name__=='__main__':build()
