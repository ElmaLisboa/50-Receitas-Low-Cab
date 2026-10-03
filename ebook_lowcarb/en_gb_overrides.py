# -*- coding: utf-8 -*-
"""
British English (en-GB) port of the International English text.

Escrito à mão, linha a linha, a partir de en_overrides (modelo EN): NÃO é
substituição léxica nem regex. Cada entrada abaixo foi revista em inglês
britânico e só existe onde o texto difere do en-US; o restante é herdado do
dicionário EN com update() explícito — qualquer linha nova do corpus PT sem
cobertura derruba o build com KeyError (contrato fail-loudly idêntico ao EN).

Convenções adotadas (revistas uma a uma):
  grafia      flavour, colour, centre, caramelise, organise, savoury, yoghurt,
              omelette, lasagne, mould/moulds, non-stick, spiralise, biscuits;
  vocabulário courgette (zucchini), aubergine (eggplant), prawns (shrimp),
              beef mince (ground beef), coriander (cilantro), pepper (bell
              pepper), chilli flakes (red pepper flakes), cornflour
              (cornstarch), double cream (heavy cream), stock (broth), tins
              (cans), kitchen paper (paper towels), baking tray (baking
              sheet), baking paper (parchment), resealable bag (zip-top),
              fridge (refrigerator), pork scratchings (cracklings),
              natural yoghurt (plain yogurt), fillet steak (fillet mignon),
              takeaway (takeout), salting (reduced-sodium kept, é UK válido);
  método      "grill" em frigideira vira pan-fry/fry; grelha vira griddle;
              water bath vira bain-marie; Yield vira Serves (no template);
  mantidos    pot (panela é UK), sour cream, cream cheese, cup/tbsp/tsp (a
              caixa de medidas do front explica 1 cup = 240 ml), °C, nomes de
              pratos brasileiros (feijoada, moqueca, paçoca, dendê, paio).
Validação: QA varre o HTML/PDF final atrás de 40+ marcadores US (= 0) e de
resíduo PT (= 0), além de exigir a presença dos marcadores britânicos.
"""
from en_overrides import INGREDIENTS as _EN_INGREDIENTS, OVERRIDES as _EN_OVERRIDES

# ---------------------------------------------------------------------------
# Ingredientes: chave = linha PT do corpus (idêntica ao EN) -> valor en-GB.
# Só as linhas que diferem do en-US; todas revistas aqui.
INGREDIENTS_GB = {
 "2 col. sopa de creme de leite": "2 tbsp double cream",
 "1 col. sopa de creme de leite": "1 tbsp double cream",
 "1 col. sopa de requeijão ou creme de leite": "1 tbsp cream cheese or double cream",
 "1/2 abobrinha ralada e espremida": "1/2 courgette, grated and squeezed dry",
 "3 col. sopa de requeijão ou iogurte natural": "3 tbsp cream cheese or natural yoghurt",
 "170 g de iogurte natural integral": "170 g whole-milk natural yoghurt",
 "170 g de iogurte natural": "170 g natural yoghurt",
 "200 g de iogurte natural": "200 g natural yoghurt",
 "1/3 xíc. de mix de castanhas picadas (pará, caju, amêndoa)": "1/3 cup chopped mixed nuts (Brazil nuts, cashews and almonds)",
 "2 abobrinhas grandes": "2 large courgettes",
 "1 abobrinha em cubos": "1 courgette, diced",
 "2 abobrinhas em cubos": "2 courgettes, diced",
 "3 abobrinhas grandes em rodelas": "3 large courgettes, sliced into rounds",
 "3 abobrinhas médias": "3 medium courgettes",
 "1,2 L de água ou caldo, azeite, sal, louro e salsinha": "1.2 L water or stock, olive oil, salt, bay leaf and parsley",
 "6 tomates maduros (ou 1 lata de tomate pelado)": "6 ripe tomatoes (or 1 tin peeled whole tomatoes)",
 "1 lata de tomate pelado": "1 tin peeled whole tomatoes",
 "4 xíc. de folhas variadas": "4 cups mixed salad leaves",
 "2 latas de atum em água escorrido": "2 tins tuna in water, drained",
 "2 latas de atum escorridas": "2 tins tuna, drained",
 "1 pimentão pequeno picado": "1 small pepper, chopped",
 "1 pimentão vermelho e 1 verde em cubos": "1 red and 1 green pepper, diced",
 "2 tomates e 1 pimentão em rodelas": "2 tomatoes and 1 pepper, sliced into rounds",
 "500 g de carne moída": "500 g beef mince",
 "400 g de carne moída": "400 g beef mince",
 "500 g de carne moída (patinho ou acém)": "500 g beef mince (knuckle or chuck)",
 "2 berinjelas grandes em fatias finas": "2 large aubergines, in thin slices",
 "2 berinjelas cortadas ao meio": "2 aubergines, halved",
 "2 berinjelas em fatias de 1 cm": "2 aubergines, in 1 cm slices",
 "1 L de caldo de galinha ou água": "1 L chicken stock or water",
 "700 ml de caldo de legumes": "700 ml vegetable stock",
 "600 ml de caldo de legumes": "600 ml vegetable stock",
 "1/4 de xíc. de caldo de carne": "1/4 cup beef stock",
 "torresmo ou crouton low carb para servir": "pork scratchings or low-carb croutons to serve",
 "1 col. sopa de amido de milho diluído em 3 de água (opcional)": "1 tbsp cornflour diluted in 3 tbsp water (optional)",
 "2 bifes altos de filé-mignon ou alcatra": "2 thick-cut fillet or rump steaks",
 "400 g de camarão limpo": "400 g prawns, peeled and deveined",
 "1 col. chá de pimenta calabresa (opcional)": "1 tsp chilli flakes (optional)",
 "pimenta calabresa, sal e pimenta-do-reino": "chilli flakes, salt and black pepper",
 "coentro, limão, sal e pimenta": "coriander, lemon, salt and pepper",
 "150 ml de creme de leite fresco": "150 ml double cream",
 "100 ml de creme de leite fresco": "100 ml double cream",
 "200 ml de creme de leite fresco": "200 ml double cream",
 "100 ml de creme de leite": "100 ml double cream",
 "1 lata de creme de leite": "1 small carton of double cream",
 "1 pepino japonês grande": "1 large cucumber",
}

# ---------------------------------------------------------------------------
# Passos + cooking tip + smart swap em inglês britânico, escritos à mão.
# Só as receitas que diferem do en-US (3, 14, 29, 40 e 44 são idênticas e
# seguem vindo de _EN_OVERRIDES); contagem de passos conferida por assert.
OVERRIDES_GB = {
1: ([
 "Sauté the onion in olive oil for 3 minutes, add the spinach and cook until the water evaporates.",
 "Whisk the eggs with the cream, salt, pepper and nutmeg.",
 "Fold the sautéed mixture and the cheese into the eggs.",
 "Pour into a small greased baking dish and bake at 180 °C for 20–25 minutes, until the centre is set.",
 ], "Make two at once: the second one keeps 3 days in the fridge and becomes tomorrow's breakfast.", "Swap the spinach for grated courgette squeezed dry — same technique, milder flavour."),
2: ([
 "Mix everything in a mug or small greased square dish with a fork until no lumps of flour remain.",
 "Microwave on high for 90 seconds.",
 "Turn out, cut in half and toast in a pan or toaster for 1 minute on each side.",
 ], "It is only good if you toast it: the microwave cooks the bread but gives it no colour and no crumb.", "No almond flour? Use 1 tbsp golden flaxseed meal and 1 tbsp coconut flour."),
4: ([
 "Brown the bacon and drain on kitchen paper.",
 "Grate the courgette, salt it, wait 5 minutes and squeeze it firmly in your hands.",
 "Whisk the eggs, fold everything together and divide among the cups of a muffin tin.",
 "Bake at 180 °C for 20–25 minutes, until firm in the centre.",
 ], "Freeze in a resealable bag and microwave 30 seconds: breakfast is ready in half a minute.", "Swap the bacon for shredded chicken for a version lower in saturated fat."),
5: ([
 "Whisk the egg with the tapioca, cream cheese and salt until smooth.",
 "Heat a non-stick pan over low heat and pour in the batter.",
 "Cook 2 minutes, flip, top with cheese and tomato and fold in half.",
 "Leave 1 more minute covered so the cheese melts.",
 ], "Low heat is the secret: on high heat the crepe dries out and cracks when you fold it.", "Sweet version: fill with 1 tsp peanut butter and cinnamon."),
6: ([
 "Mix everything with a fork until you have a creamy batter.",
 "Pour into a small greased non-stick pan over low heat.",
 "Cover and cook 4 minutes, flip and cook 3 minutes more.",
 "Cut in half and fill while hot.",
 ], "Use sour (fermented) cassava starch, not the sweet kind: the sour one gives the characteristic chew.", "Go-to filling: cream cheese and oregano, or shredded chicken with cream cheese."),
7: ([
 "Blanch the collard leaves 20 seconds in boiling water, then in ice water: they soften without cooking.",
 "Mix the chicken with the cream cheese, lemon, salt and pepper.",
 "Assemble on the dried leaf: lettuce, carrot and creamy chicken.",
 "Roll tightly like a cigar, folding in the ends, and cut in half.",
 ], "Pat the collard dry with kitchen paper: a wet leaf makes the wrap fall apart in your hand.", "Use raw chard leaves instead — crunchier and no blanching needed."),
8: ([
 "Beat the eggs with salt and pepper without whipping them foamy.",
 "Melt the butter over low heat, add the eggs and wait 20 seconds without stirring.",
 "Pull a spatula from the centre to the edges, repeating until creamy and still wet.",
 "Serve immediately topped with avocado, seeds and chives.",
 ], "Take them off the heat while they still look underdone: the pan's residual heat finishes them.", "No avocado? Use 2 tbsp sour cream with lemon."),
9: ([
 "Toast the nuts and coconut flakes in a dry pan for 2 minutes, stirring constantly.",
 "Spoon the yoghurt into a bowl and top with the strawberries.",
 "Scatter the warm granola over and dust with cinnamon.",
 "Sweeten only if needed: the cinnamon already fools the palate.",
 ], "Never toast granola with your phone in reach: nuts burn in 30 seconds and turn bitter.", "Batch it: triple the granola and keep it 15 days in a sealed jar."),
10: ([
 "Pulse the raw cauliflower until rice-sized, or grate it on the largest holes.",
 "Sauté the garlic and onion in olive oil for 2 minutes.",
 "Add the cauliflower and stir-fry over high heat for 5–6 minutes.",
 "Salt and finish with fresh herbs — do not cover, or it turns to mash.",
 ], "Never process cooked cauliflower: it releases water and turns to paste. Always raw, and pulse.", "A neutral base: it keeps 4 days in the fridge and takes any leftover protein on top."),
11: ([
 "Make the sauce: sauté onion and garlic, add chopped tomato and simmer 20 minutes until thick.",
 "Slice the courgette into thin ribbons with a peeler or spiraliser.",
 "Sauté the courgette 90 seconds in hot oil — just to warm it, never to cook it.",
 "Add the sauce, toss briefly and finish with basil and parmesan.",
 ], "Salt the spiralised courgette, drain 10 minutes in a colander and pat dry: that removes the water that dilutes the sauce.", "Swap the peeled tomatoes for a sauce of blended cauliflower with parmesan — lower in carbs still."),
12: ([
 "Drain the hearts of palm and pat them very dry with kitchen paper.",
 "Warm the olive oil over low heat and golden the sliced garlic without burning it.",
 "Add the hearts of palm and sauté 3 minutes over medium-high heat to drive off water.",
 "Turn off the heat, toss with parmesan, parsley and pepper and serve at once.",
 ], "Hearts of palm and konjac release a lot of water: drying them well before sautéing is what keeps the dish from turning soggy.", "Add 1 cup sautéed prawns to make it a complete main."),
13: ([
 "Season the chicken with salt, pepper and paprika and pan-fry 5 minutes on each side.",
 "Divide the greens, cucumber, tomato and avocado between two bowls.",
 "Whisk the yoghurt with mustard, lemon, 1 tbsp olive oil, salt and herbs.",
 "Top with the warm chicken and dress right before eating.",
 ], "Dressing on the side keeps a salad 2 days in a container; dressed ahead, it wilts in 3 hours.", "Swap the chicken for tuna or cooked chickpeas (increase the portion and count the carbs)."),
15: ([
 "Sauté the onion, garlic and pepper for 4 minutes.",
 "Add the beef mince and brown well, breaking it up with a spatula.",
 "Stir in the tomato sauce and spices and cook 8 minutes until the liquid is gone.",
 "Serve in lettuce leaves with cheese and sour cream.",
 ], "Pat the lettuce leaves dry: a wet leaf tears when you roll it.", "No beef mince? Use shredded chicken with the same spices."),
16: ([
 "Steam the cauliflower until tender and blend with butter and cream cheese until smooth.",
 "Sauté the onion and garlic, add the shredded dried beef and cook 5 minutes.",
 "Layer in a baking dish: meat on the bottom, mash on top, mozzarella last.",
 "Bake at 200 °C for 20 minutes until golden.",
 ], "Drain the cooked cauliflower well before blending: excess water makes the mash runny.", "No dried beef? Use beef mince sautéed with pepper, or shredded chicken."),
17: ([
 "Salt the aubergine slices, rest 20 minutes, rinse and pat dry.",
 "Fry them in a hot pan with a little olive oil, 2 minutes on each side.",
 "Make the sauce: sauté onion and garlic, brown the beef, add tomato and simmer 25 minutes.",
 "Layer sauce, aubergine and mozzarella, ending with sauce and parmesan. Bake at 190 °C for 35 minutes.",
 ], "Drying the aubergine is mandatory: skip it and the lasagne releases water and turns to soup in the dish.", "Swap the aubergine for thin courgette slices and fry them for less time."),
18: ([
 "Scoop out some of the aubergine flesh, chop it and set aside.",
 "Salt the shells and bake at 180 °C for 15 minutes to soften.",
 "Sauté onion and garlic, brown the meat, add the chopped flesh and tomato and cook 10 minutes.",
 "Fill the shells, top with cheese and return to the oven 15 minutes.",
 ], "Bake the shells before filling: raw aubergine in the oven stays hard inside and burnt outside.", "Swap the beef mince for tuna and cream cheese for a 25-minute version."),
19: ([
 "Brown the sausage in a large pot and reserve some of the fat.",
 "Sauté the onion and garlic in that fat for 3 minutes.",
 "Add the cauliflower and stock, cook 15 minutes and blend until creamy.",
 "Return to the pot, add the sliced collard and sausage and cook 5 minutes without letting the greens turn limp.",
 ], "Collard goes in last and cooks only 5 minutes: it should stay bright green, not brown.", "Cured-meat-free version: swap the sausage for shredded chicken and add smoked paprika."),
20: ([
 "Sauté the onion, garlic and ginger in olive oil for 3 minutes.",
 "Add the squash and stock and cook 20 minutes until tender.",
 "Blend with the coconut milk until smooth.",
 "Adjust the salt, rewarm without boiling and finish with chives.",
 ], "Kabocha has more carbs than other vegetables: mind your portion if you are in the induction phase.", "Swap the ginger for curry powder and finish with coriander for a Thai profile."),
21: ([
 "Simmer the chicken in water with bay leaf and salt 20 minutes, remove and shred.",
 "Sauté the onion and garlic separately and return them to the pot with the tomato.",
 "Add the carrot and cook 8 minutes; then the courgette, green beans and cauliflower for 8 more.",
 "Stir in the shredded chicken, adjust the salt and finish with parsley.",
 ], "Cook the vegetables in order of firmness: carrot first, leafy greens and courgette last.", "Freeze in 500 ml jars: it keeps 3 months and rescues an unplanned dinner."),
22: ([
 "Sauté the onion and garlic in olive oil until golden.",
 "Add the courgette and stock and cook 15 minutes.",
 "Blend with the cream cheese until velvety.",
 "Return to the pot, season with white pepper and nutmeg and rewarm without boiling.",
 ], "Always add cream cheese off the heat or on low: boiling makes it split and separate.", "Swap the cream cheese for 100 ml double cream for a lighter version."),
23: ([
 "Season the fillets with salt and pepper and sear in a very hot pan, 4 minutes on each side. Set aside.",
 "In the same pan, melt the butter and sauté the garlic 30 seconds.",
 "Add the mustard, cream and thyme and reduce 3 minutes until thickened.",
 "Return the chicken to the pan, coat in the sauce and serve with sautéed vegetables.",
 ], "Do not wash the pan between chicken and sauce: the browned bits are what flavour the cream base.", "No Dijon? Use mild mustard with 1/2 tsp honey or sweetener to balance the acidity."),
24: ([
 "Mix the olive oil, lemon juice and zest, garlic, rosemary, salt and pepper.",
 "Coat the thighs in the marinade and rest 20 minutes, or overnight.",
 "Arrange skin-side up on a baking tray without overlapping.",
 "Bake at 200 °C for 40–45 minutes until the skin is crisp and the juices run clear.",
 ], "Skin up and not overlapping: that is how skin turns crisp instead of steaming.", "Add onion and courgette to the tray for the last 25 minutes to cook a side at the same time."),
25: ([
 "Sear the chicken over high heat with a little oil, in two batches, until browned. Set aside.",
 "Sauté the garlic and ginger 30 seconds, add the peppers and courgette for 4 minutes.",
 "Return the chicken, add the soy sauce and diluted cornflour and toss until coated.",
 "Finish with the cashews off the heat so they stay crunchy.",
 ], "Soy sauce carries sodium and some carbs: choose a reduced-sodium version and count 1 g carb per tablespoon.", "No cashews? Use roasted skinless peanuts — cheaper and just as crunchy."),
26: ([
 "Season the meat with salt and pepper and sear in a very hot pan, 3 minutes on each side. Set aside.",
 "In the same pan, melt the butter and sauté the mushrooms until browned and dry.",
 "Add the garlic, stock and cream and reduce 5 minutes.",
 "Return the meat, warm 1 minute and serve with the sauce poured over.",
 ], "Do not crowd the mushrooms: in a full pan they release water and steam instead of browning.", "Cream-free version: use 2 tbsp cream cheese thinned with hot stock."),
27: ([
 "Sauté the onion and garlic in olive oil until soft.",
 "Add the beef mince and brown well, leaving it undisturbed for 2 minutes to build a crust.",
 "Stir in the peeled tomatoes and spices and cook 10 minutes.",
 "Add the courgette and cook 8 minutes more until tender but firm. Finish with fresh herbs.",
 ], "Letting the meat brown undisturbed at first is what creates the dark fond and the stewed flavour.", "Serve over cauliflower rice, or use it to stuff peppers and courgette."),
28: ([
 "Season the steaks with salt and pepper and sear in a hot pan with olive oil, 3 minutes on each side. Set aside.",
 "In the same pan, brown the onion over medium heat 8 minutes until caramelised.",
 "Add the butter and garlic and cook 1 minute without burning the garlic.",
 "Return the steaks, coat in the onion, finish with parsley and serve.",
 ], "Take the meat out of the fridge 20 minutes ahead: a cold steak releases water and steams instead of searing.", "Add 1 tbsp soy sauce to the onions for a darker, richer pan sauce."),
30: ([
 "Mix the spices with salt and pepper and rub all over the meat along with the mustard.",
 "Marinate at least 30 minutes, ideally 12 hours in the fridge.",
 "Sear the meat in a hot pot with olive oil to brown all sides.",
 "Cover with foil and bake at 150 °C for 2 h 30, or pressure-cook 45 minutes. Shred with two forks.",
 ], "Low and slow is what shreds: high heat only dries out the surface.", "Toss the shredded meat with 2 tbsp cream cheese and serve in lettuce wraps."),
31: ([
 "Season the salmon with salt and pepper and place in a greased baking dish.",
 "Mix the melted butter with garlic, lemon juice and zest and parsley.",
 "Pour over the fish and rest 10 minutes.",
 "Bake at 200 °C for 12–15 minutes until opaque and flaking.",
 ], "Salmon is done when it flakes under fork pressure: past that it dries out.", "Replace the lemon with 1 tbsp Dijon in the butter for a sharper flavour."),
32: ([
 "Season the fillets with salt, pepper and lemon and pat them very dry with kitchen paper.",
 "Mix the almond flour with parmesan and paprika.",
 "Dip the fillets in egg, then in the dry mix, pressing to adhere.",
 "Bake at 200 °C for 15 minutes on a greased baking tray, or fry in 3 tbsp olive oil, 4 minutes on each side.",
 ], "Drying the fillet before coating is what stops the crust from sliding off in the pan.", "Almond flour pricey? Use golden flaxseed meal with the same parmesan."),
33: ([
 "Pat the prawns dry with kitchen paper and season with salt and pepper.",
 "Warm the olive oil over medium heat and golden the sliced garlic without burning it.",
 "Raise the heat, add the prawns and toss 2–3 minutes until pink.",
 "Turn off the heat and finish with lemon and parsley.",
 ], "Prawns cook in 2 minutes; beyond that they turn rubbery. Off the heat as soon as they are pink.", "Add 1/2 cup white wine and reduce 1 minute for a fancier version."),
34: ([
 "Poach the cod 5 minutes, drain and remove skin and bones.",
 "Steam the cauliflower 6 minutes, keeping it firm.",
 "Sauté the onion and garlic in half the olive oil until golden.",
 "Layer in a baking dish with the cod, cauliflower and olives, drizzle with the remaining oil and bake at 190 °C for 20 minutes.",
 ], "Desalt the cod by changing the water every 6 hours for 24–48 hours in the fridge.", "No cod? Use flakes of firm white fish such as hake or tilapia, salted at the time."),
35: ([
 "Season the fish with lemon, salt and pepper and rest 15 minutes.",
 "In a wide pot, sauté the onion and garlic, then layer the tomato and pepper.",
 "Lay the fish on top, cover with coconut milk and simmer covered 15 minutes on low heat.",
 "Add the hearts of palm and dendê oil, cook 5 minutes more and finish with coriander.",
 ], "Do not stir the moqueca after adding the fish: shaking the pot breaks the steaks.", "No dendê oil? Use regular olive oil with 1 tsp smoked paprika for colour."),
36: ([
 "Pat the squid rings very dry with kitchen paper.",
 "Heat a griddle pan or barbecue until very hot, almost smoking.",
 "Griddle the squid 90 seconds on each side, not one second longer.",
 "Dress with salt, raw garlic, olive oil, lemon and herbs and serve immediately.",
 ], "Squid has two windows: 90 seconds, or 40 minutes in a stew. In between, it is rubbery.", "No squid? Use pre-cooked octopus rings, grilled just to brown."),
37: ([
 "Steam the riced cauliflower 5 minutes, cool and squeeze in a towel until all the water is out.",
 "Mix the dry cauliflower with egg, 80 g mozzarella, almond flour and salt.",
 "Press into a thin round on greased baking paper and bake at 200 °C for 15 minutes.",
 "Top with sauce, mozzarella and oregano and bake 10–12 minutes more. Finish with basil.",
 ], "Squeezing the cauliflower is non-negotiable: a wet crust will not hold and the pizza falls apart when sliced.", "Freeze par-baked rounds between baking paper and assemble a pizza in 12 minutes."),
38: ([
 "Salt the aubergine slices 20 minutes, rinse and pat dry.",
 "Fry in a hot pan with a little olive oil, 2 minutes on each side.",
 "Make the sauce by sautéing onion and garlic and simmering the tomato 15 minutes.",
 "Layer with the cheeses and bake at 190 °C for 25 minutes until golden.",
 ], "Frying before assembling prevents spongy aubergine that soaks up all the sauce.", "Add a layer of beef mince between the aubergine for a complete one-dish meal."),
39: ([
 "Desalt the cured meats for 12 hours, changing the water.",
 "Simmer the meats in water with bay leaf 40 minutes, or 25 in a pressure cooker, and cut into pieces.",
 "Fry the bacon, sauté the onion, garlic and smoked paprika, add the meats and 2 cups stock and cook 20 minutes.",
 "Serve over riced cauliflower sautéed in butter, with collard greens and orange.",
 ], "Cauliflower sautéed in bacon fat is what replaces the texture of beans in the dish.", "Express version: use only paio, sausage and bacon — ready in 40 minutes."),
41: ([
 "Halve the courgette and scoop the core with a spoon, leaving a 0.5 cm wall.",
 "Mix the tuna, cream cheese, onion, tomato, parsley, salt and pepper.",
 "Fill the shells, drizzle with olive oil and top with mozzarella.",
 "Bake at 190 °C for 22–25 minutes.",
 ], "Seed the tomato: that is where the water comes from that floods the filling.", "No tuna? Use shredded chicken or already-cooked beef mince."),
42: ([
 "Slice the cucumber into long thin ribbons with a peeler or mandoline.",
 "Pat the ribbons dry and season with a pinch of salt.",
 "Spread the cream cheese, lay the fish and avocado and roll like a cigar.",
 "Finish with sesame seeds and serve with soy sauce and wasabi.",
 ], "Salt and dry the cucumber ribbons: waterlogged cucumber loosens inside the roll and it falls apart.", "Cooked version: swap the raw fish for prawns or shredded surimi."),
43: ([
 "Boil the whole cabbage 5 minutes and carefully peel off the leaves.",
 "Mix the meat with the riced cauliflower, chopped onion, garlic, egg and spices.",
 "Place 1 tbsp filling on each leaf, fold in the sides and roll tightly.",
 "Arrange in a pot, cover with blended peeled tomatoes and simmer covered 35 minutes on low heat.",
 ], "Trim the thick leaf rib with a knife before rolling: the cabbage closes without tearing.", "Freeze raw between baking paper and cook straight from frozen for 50 minutes."),
45: ([
 "Blend all the ingredients for 1 minute.",
 "Pour into a mould greased with coconut oil.",
 "Cover with foil and bake in a bain-marie at 180 °C for 45–50 minutes.",
 "Cool completely and chill for 4 hours before unmoulding.",
 ], "The bain-marie is mandatory: without it the flan bubbles and turns out like scrambled eggs.", "Caramelise the mould with 2 tbsp melted xylitol to mimic traditional caramel."),
46: ([
 "Mix the cream, cocoa, sweetener and butter in a heavy-based pan.",
 "Cook over low heat, stirring constantly, for 12–15 minutes.",
 "It is done when the mixture pulls away from the bottom of the pan as you tilt it.",
 "Turn off the heat, add the salt, transfer to a jar and cool.",
 ], "Erythritol-based sweeteners will not give the same shine as sugar: add 1 tsp coconut oil at the end.", "To make truffles, chill 4 hours, then roll in cocoa powder or chopped nuts."),
47: ([
 "Mix the almond flour with the butter and press into the base of a springform tin. Bake 8 minutes at 180 °C.",
 "Beat the cream cheese with the erythritol until smooth, add the eggs one at a time, then the yoghurt, lemon and vanilla.",
 "Pour over the base and bake in a bain-marie at 160 °C for 50 minutes, until the edges are set and the centre still jiggles.",
 "Turn off the oven and cool the cheesecake inside for 1 hour. Top with the berries warmed with 1 tbsp sweetener.",
 ], "Cooling inside the turned-off oven prevents the centre from cracking: thermal shock is the culprit.", "No springform tin? Line a regular tin with crossing strips of baking paper so you can lift the cheesecake out."),
48: ([
 "Mix the flour, erythritol, baking powder and salt.",
 "Add the egg, butter and vanilla and mix until a moist dough forms.",
 "Fold in the chopped chocolate and shape 12 flattened balls on a baking-paper-lined tray.",
 "Bake at 170 °C for 12–14 minutes until the edges are golden.",
 ], "They come out soft and firm up as they cool — do not bake longer thinking they are raw.", "Keeps 5 days in a sealed jar, or freeze the shaped dough for 2 months."),
49: ([
 "Melt the chocolate with the coconut oil in a bain-marie or microwave in 20-second bursts.",
 "Add the cream, erythritol, salt and vanilla and mix until glossy.",
 "Chill 30 minutes until firm enough to shape.",
 "Roll into balls with your hands and coat in cocoa powder.",
 ], "Melt in short bursts, stirring every 20 seconds: direct heat scorches the chocolate and makes it grainy.", "Keep in the fridge: at room temperature the coconut oil melts and the truffles lose their shape."),
50: ([
 "Pulse the peanuts until sandy and moist — careful not to turn them into butter.",
 "Add the almond flour, erythritol and salt and pulse 3 more times.",
 "If the mix is too dry, add the coconut oil and mix.",
 "Press into small moulds or a baking-paper-lined jar, cut into squares and set 15 minutes.",
 ], "Pulse and stop early: over-processed peanuts turn to butter and the sweet will not set.", "Keeps 10 days in a sealed jar in a cool place."),
}

# ---------------------------------------------------------------------------
# Merge determinístico + validação fail-loudly (sem regex, sem fallback cego).
for _k in INGREDIENTS_GB:
    if _k not in _EN_INGREDIENTS:
        raise KeyError("INGREDIENTS_GB key not present in en_overrides: %r" % _k)
for _n, (_steps, _tip, _swap) in OVERRIDES_GB.items():
    if _n not in _EN_OVERRIDES:
        raise KeyError("OVERRIDES_GB recipe %d not present in en_overrides" % _n)
    _en_steps, _en_tip, _en_swap = _EN_OVERRIDES[_n]
    if len(_steps) != len(_en_steps):
        raise AssertionError(
            "recipe %d: %d British steps vs %d English steps"
            % (_n, len(_steps), len(_en_steps)))

INGREDIENTS = dict(_EN_INGREDIENTS)
INGREDIENTS.update(INGREDIENTS_GB)
OVERRIDES = dict(_EN_OVERRIDES)
OVERRIDES.update(OVERRIDES_GB)

assert set(INGREDIENTS) == set(_EN_INGREDIENTS), "ingredient key drift vs EN"
assert set(OVERRIDES) == set(_EN_OVERRIDES), "override recipe drift vs EN"
assert len(INGREDIENTS_GB) == len(INGREDIENTS_GB), "unreachable"
