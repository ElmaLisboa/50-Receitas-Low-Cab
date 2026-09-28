# -*- coding: utf-8 -*-
"""Receitas 31-50: carnes e aves, peixes e frutos do mar."""

# Formato: (nome, preparo_min, total_min, porcoes, kcal, carb_g, prot_g, gord_g, [ingredientes], [passos], dica, troca)

CARNES = [
("Frango grelhado ao molho de mostarda e creme", 12, 25, 2, 385, 5, 38, 24,
 ["2 filés de peito de frango (150 g cada)", "2 col. sopa de mostarda dijon", "100 ml de creme de leite fresco", "1 dente de alho picado", "1 col. sopa de manteiga", "1 col. chá de tomilho", "sal e pimenta-do-reino"],
 ["Tempere os filés com sal e pimenta e sele em frigideira bem quente, 4 minutos de cada lado. Reserve.", "Na mesma frigideira, derreta a manteiga e refogue o alho por 30 segundos.", "Junte a mostarda, o creme de leite e o tomilho e reduza por 3 minutos até engrossar.", "Volte o frango à panela, banhe com o molho e sirva com legumes salteados."],
 "Não lave a frigideira entre o frango e o molho: o fundo dourado é o que dá sabor à base do creme.",
 "Sem dijon? Use mostarda amarela + 1/2 col. chá de mel ou adoçante para equilibrar a acidez."),

("Sobrecoxa assada com limão e alecrim", 10, 50, 4, 410, 3, 36, 28,
 ["8 sobrecoxas de frango com pele", "suco e raspas de 1 limão", "4 ramos de alecrim", "4 dentes de alho amassados", "3 col. sopa de azeite", "sal grosso e pimenta-do-reino"],
 ["Misture o azeite, o suco e as raspas de limão, o alho, o alecrim, o sal e a pimenta.", "Envolva as sobrecoxas na marinada e deixe descansar 20 minutos (ou de um dia para o outro).", "Disponha em assadeira com a pele para cima, sem sobrepor.", "Asse a 200 °C por 40-45 minutos, até a pele ficar crocante e o suco sair transparente."],
 "Pele para cima e sem sobrepor: é assim que ela fica crocante em vez de cozida no próprio vapor.",
 "Acrescente cebola e abobrinha na assadeira nos últimos 25 minutos para fazer o acompanhamento junto."),

("Frango xadrez low carb", 15, 25, 3, 320, 10, 30, 18,
 ["400 g de peito de frango em cubos", "1 pimentão vermelho e 1 verde em cubos", "1 abobrinha em cubos", "1/2 xíc. de castanha-de-caju torrada", "3 col. sopa de shoyu (ou 2 de shoyu + água)", "1 dente de alho e 1 pedaço pequeno de gengibre ralado", "1 col. sopa de amido de milho diluído em 3 de água (opcional)"],
 ["Sele o frango em fogo alto com um fio de óleo, em duas levas, até dourar. Reserve.", "Refogue o alho e o gengibre por 30 segundos, junte os pimentões e a abobrinha por 4 minutos.", "Volte o frango, acrescente o shoyu e o amido diluído e mexa até o molho envolver tudo.", "Finalize com a castanha-de-caju fora do fogo, para continuar crocante."],
 "O shoyu tem sódio e um pouco de carbo: use a versão com menos sódio e conte 1 g de carbo por colher.",
 "Sem castanha-de-caju? Use amendoim torrado sem pele — mais barato e igualmente crocante."),

("Filé ao molho de cogumelos", 12, 30, 2, 430, 7, 38, 28,
 ["2 bifes altos de filé-mignon ou alcatra", "200 g de cogumelos paris ou shimeji", "150 ml de creme de leite fresco", "1/4 de xíc. de caldo de carne", "1 col. sopa de manteiga", "1 dente de alho e tomilho fresco", "sal e pimenta-do-reino"],
 ["Tempere a carne com sal e pimenta e sele em frigideira muito quente, 3 minutos de cada lado. Reserve.", "Na mesma panela, derreta a manteiga e refogue os cogumelos até dourar e secar a água.", "Junte o alho, o caldo e o creme de leite e reduza por 5 minutos.", "Volte a carne, aqueça por 1 minuto e sirva com o molho por cima."],
 "Não amontoe os cogumelos na panela: em excesso, eles soltam água e cozinham em vez de dourar.",
 "Versão sem creme: use 2 col. sopa de requeijão diluído no caldo quente."),

("Carne moída com abobrinha e tomate", 15, 30, 4, 310, 9, 27, 19,
 ["500 g de carne moída (patinho ou acém)", "2 abobrinhas em cubos", "1 lata de tomate pelado", "1 cebola e 3 dentes de alho", "1 col. sopa de azeite", "orégano, cominho, sal e pimenta", "cheiro-verde e queijo ralado"],
 ["Refogue a cebola e o alho no azeite até amaciar.", "Junte a carne moída e doure bem, sem mexer nos primeiros 2 minutos para formar crosta.", "Acrescente o tomate pelado, os temperos e cozinhe 10 minutos.", "Junte a abobrinha e cozinhe mais 8 minutos, até ficar macia mas firme. Finalize com cheiro-verde."],
 "Dourar a carne sem mexer no começo é o que cria o fundo escuro e o sabor de panela.",
 "Sirva sobre arroz de couve-flor ou recheando pimentões e abobrinhas."),

("Bife acebolado com manteiga de alho", 10, 20, 2, 415, 5, 36, 27,
 ["2 bifes de alcatra ou contrafilé", "1 cebola grande em rodelas", "3 dentes de alho picados", "2 col. sopa de manteiga", "1 col. sopa de azeite", "sal, pimenta e salsa picada"],
 ["Tempere os bifes com sal e pimenta e sele em frigideira quente com azeite, 3 minutos de cada lado. Reserve.", "Na mesma frigideira, doure a cebola em fogo médio por 8 minutos, até caramelizar.", "Junte a manteiga e o alho e cozinhe 1 minuto, sem queimar o alho.", "Volte os bifes, envolva na cebola, finalize com salsa e sirva."],
 "Tire a carne da geladeira 20 minutos antes: bife gelado solta água e cozinha em vez de selar.",
 "Acrescente 1 col. sopa de shoyu na cebola para um fundo mais escuro e salgado."),

("Carne de panela com legumes", 20, 90, 6, 375, 12, 32, 22,
 ["800 g de músculo, acém ou paleta em cubos", "1 cenoura, 1 abobrinha e 1 xíc. de vagem", "1 cebola, 3 dentes de alho e 1 tomate", "2 col. sopa de extrato de tomate", "1 L de água quente", "2 folhas de louro, azeite, sal, pimenta e cheiro-verde"],
 ["Sele a carne em óleo quente, em levas, até dourar de todos os lados.", "Refogue a cebola, o alho e o tomate, junte o extrato e mexa por 1 minuto.", "Volte a carne, cubra com a água quente, junte o louro e cozinhe tampado por 60 minutos (ou 35 na pressão).", "Acrescente os legumes e cozinhe mais 15 minutos. Ajuste o sal e finalize com cheiro-verde."],
 "Água quente, sempre: água fria fecha as fibras da carne e ela demora o dobro do tempo para amaciar.",
 "Congele o caldo separado da carne e use como base de sopa durante a semana."),

("Almôndegas recheadas com queijo ao sugo", 25, 50, 4, 365, 8, 30, 24,
 ["500 g de carne moída", "1 ovo", "3 col. sopa de farinha de amêndoas", "1 dente de alho ralado, salsa, sal e pimenta", "100 g de muçarela em cubos para rechear", "1 lata de tomate pelado", "2 col. sopa de azeite e manjericão"],
 ["Misture a carne com o ovo, a farinha de amêndoas, o alho, a salsa, o sal e a pimenta. Deixe descansar 10 minutos.", "Abra porções na palma da mão, coloque um cubo de queijo e feche bem, sem deixar frestas.", "Sele as almôndegas em frigideira com azeite até dourar de todos os lados.", "Cubra com o molho de tomate quente e cozinhe tampado por 20 minutos em fogo baixo."],
 "Feche a almôndega apertando bem: fresta aberta é queijo vazando para o molho.",
 "A farinha de amêndoas pode ser substituída por 2 col. sopa de farelo de aveia (some 2 g de carbo por porção)."),

("Costelinha de porco desfiada", 20, 180, 6, 445, 6, 34, 32,
 ["1,2 kg de costelinha ou copa-lombo de porco", "1 col. sopa de páprica defumada", "1 col. chá de cominho, alho em pó, cebola em pó", "1 col. sopa de vinagre de maçã", "2 col. sopa de mostarda", "sal, pimenta e 2 col. sopa de azeite"],
 ["Misture as especiarias com o sal e a pimenta e esfregue em toda a carne, junto com a mostarda.", "Deixe marinar por no mínimo 30 minutos (ideal: 12 horas na geladeira).", "Sele a carne em panela quente com azeite para dourar todos os lados.", "Cubra com papel-alumínio e asse a 150 °C por 2h30, ou cozinhe na pressão por 45 minutos. Desfie com dois garfos."],
 "Temperatura baixa e tempo longo: é isso que desfia. Fogo alto só resseca a superfície.",
 "Misture o desfiado com 2 col. sopa de requeijão e sirva em wrap de alface."),

("Bife de chorizo com chimichurri caseiro", 10, 25, 2, 460, 4, 36, 33,
 ["2 bifes de chorizo ou contrafilé", "1/2 xíc. de salsa picada", "2 col. sopa de orégano seco", "3 dentes de alho picados", "1/2 xíc. de azeite", "2 col. sopa de vinagre de vinho tinto", "pimenta calabresa, sal e pimenta-do-reino"],
 ["Misture todos os ingredientes do chimichurri e deixe descansar 15 minutos para os sabores se soltarem.", "Tempere a carne com sal grosso e pimenta-do-reino.", "Sele em frigideira ou grelha bem quente, 4 minutos de cada lado para ponto médio.", "Deixe a carne descansar 5 minutos antes de cortar e sirva com o chimichurri por cima."],
 "Descansar a carne depois de grelhar mantém o suco dentro — cortar na hora faz tudo escorrer na tábua.",
 "O chimichurri dura 10 dias na geladeira e serve para frango, peixe e legumes assados."),
]

PEIXES = [
("Salmão ao forno com manteiga de limão", 8, 25, 2, 425, 3, 34, 30,
 ["2 postas de salmão (180 g cada)", "2 col. sopa de manteiga derretida", "suco e raspas de 1/2 limão", "2 dentes de alho picados", "1 col. sopa de salsinha ou endro", "sal e pimenta-do-reino"],
 ["Tempere o salmão com sal e pimenta e acomode em refratário untado.", "Misture a manteiga derretida com o alho, o limão, as raspas e a salsinha.", "Regue o peixe com a mistura e deixe 10 minutos.", "Asse a 200 °C por 12-15 minutos, até a carne opacar e soltar em lascas."],
 "Salmão pronto solta em lascas quando pressionado com o garfo — passar do ponto deixa seco.",
 "Troque o limão por 1 col. sopa de mostarda dijon na manteiga para um perfil mais intenso."),

("Tilápia empanada na farinha de amêndoas", 12, 25, 2, 390, 5, 34, 26,
 ["2 filés de tilápia", "1/2 xíc. de farinha de amêndoas", "1 ovo batido", "1/2 xíc. de parmesão ralado", "1 col. chá de páprica", "2 col. sopa de azeite", "sal, pimenta e limão"],
 ["Tempere os filés com sal, pimenta e limão e seque bem com papel-toalha.", "Misture a farinha de amêndoas com o parmesão e a páprica.", "Passe o filé no ovo e depois na mistura seca, apertando para aderir.", "Asse a 200 °C por 15 minutos em assadeira untada, ou frite em 3 col. de azeite por 4 minutos de cada lado."],
 "Secar o filé antes de empanar é o que impede a casca de soltar durante o cozimento.",
 "Farinha de amêndoas cara? Use farinha de linhaça dourada com o mesmo parmesão."),

("Camarão ao alho e óleo", 8, 15, 2, 280, 4, 30, 16,
 ["400 g de camarão limpo", "5 dentes de alho laminados", "3 col. sopa de azeite", "suco de 1/2 limão", "1 col. chá de pimenta calabresa (opcional)", "salsinha, sal e pimenta-do-reino"],
 ["Seque os camarões com papel-toalha e tempere com sal e pimenta.", "Aqueça o azeite em fogo médio e doure o alho laminado sem queimar.", "Aumente o fogo e junte os camarões, mexendo por 2-3 minutos até ficarem rosados.", "Desligue, regue com limão e finalize com salsinha."],
 "Camarão cozinha em 2 minutos: passou disso, fica borrachudo. Tire do fogo assim que rosar.",
 "Acrescente 1/2 xíc. de vinho branco e reduza por 1 minuto para uma versão mais sofisticada."),

("Bacalhau com couve-flor e azeitonas", 20, 50, 4, 340, 10, 30, 20,
 ["500 g de bacalhau dessalgado em lascas", "1 couve-flor média em buquês", "1/2 xíc. de azeitonas pretas", "1 cebola em rodelas e 4 dentes de alho", "1/2 xíc. de azeite", "salsinha, pimenta-do-reino e 1 folha de louro"],
 ["Afervente o bacalhau por 5 minutos, escorra e retire pele e espinhas.", "Cozinhe a couve-flor no vapor por 6 minutos, mantendo firme.", "Refogue a cebola e o alho em metade do azeite até dourar bem.", "Monte em refratário com o bacalhau, a couve-flor e as azeitonas, regue com o azeite restante e asse a 190 °C por 20 minutos."],
 "Dessalgue o bacalhau trocando a água a cada 6 horas, por 24 a 48 horas na geladeira.",
 "Sem bacalhau? Use lascas de peixe branco firme, como pescada ou tilápia, salgadas na hora."),

("Salada de atum com ovo e azeitona", 12, 20, 2, 330, 6, 28, 22,
 ["2 latas de atum em água escorridas", "2 ovos cozidos em quartos", "1/2 xíc. de azeitonas verdes", "1 tomate em cubos", "1/4 de cebola roxa em fatias finas", "4 xíc. de folhas verdes", "2 col. sopa de azeite, vinagre, sal, orégano"],
 ["Misture o azeite, o vinagre, o orégano e o sal para fazer o vinagrete.", "Monte as folhas, o tomate, a cebola e as azeitonas na travessa.", "Distribua o atum escorrido e os ovos por cima.", "Regue com o vinagrete apenas na hora de servir."],
 "Azeitona e atum já são salgados: tempere o molho com metade do sal que usaria normalmente.",
 "Adicione 1/2 abacate para aumentar a saciedade sem elevar o carbo."),

("Patê de sardinha para lanche rápido", 8, 15, 4, 195, 3, 16, 13,
 ["1 lata de sardinha em óleo, escorrida", "3 col. sopa de requeijão ou cream cheese", "1/4 de cebola picada bem fina", "1 col. chá de mostarda", "salsinha, cebolinha, pimenta-do-reino e gotas de limão"],
 ["Amasse a sardinha com um garfo, retirando a espinha central.", "Misture com o requeijão, a mostarda, a cebola e as ervas.", "Ajuste com limão e pimenta a gosto.", "Leve à geladeira por 10 minutos antes de servir."],
 "O limão no final equilibra o gosto forte da sardinha e faz o patê parecer mais leve.",
 "Sirva em torradas low carb, em folhas de alface ou recheando ovos cozidos."),

("Moqueca de peixe com leite de coco e palmito", 20, 40, 4, 310, 12, 28, 18,
 ["600 g de peixe firme em postas (badejo, pescada ou robalo)", "200 ml de leite de coco sem açúcar", "1 vidro de palmito em rodelas", "2 tomates e 1 pimentão em rodelas", "1 cebola em rodelas, 3 dentes de alho", "2 col. sopa de azeite de dendê (ou azeite comum)", "coentro, limão, sal e pimenta"],
 ["Tempere o peixe com limão, sal e pimenta e deixe 15 minutos.", "Em panela larga, refogue cebola e alho, monte camadas de tomate e pimentão.", "Acomode o peixe por cima, cubra com o leite de coco e cozinhe tampado por 15 minutos em fogo baixo.", "Junte o palmito e o dendê, cozinhe mais 5 minutos e finalize com coentro."],
 "Não mexa a moqueca depois de colocar o peixe: balançar a panela desmancha as postas.",
 "Sem dendê? Use azeite comum com 1 col. chá de páprica defumada para dar cor."),

("Lula grelhada com limão e ervas", 10, 15, 2, 240, 5, 26, 13,
 ["500 g de anéis de lula", "suco de 1 limão", "3 col. sopa de azeite", "2 dentes de alho picados", "1 col. sopa de salsinha e 1 de cebolinha", "pimenta calabresa, sal e pimenta-do-reino"],
 ["Seque muito bem os anéis de lula com papel-toalha.", "Aqueça uma frigideira ou grelha até ficar bem quente, quase fumegando.", "Grelhe a lula por 90 segundos de cada lado — nem um segundo a mais.", "Tempere com sal, alho cru, azeite, limão e ervas e sirva na hora."],
 "Lula tem duas janelas: 90 segundos ou 40 minutos em cozido. Entre elas, fica borracha.",
 "Sem lula? Use anéis de polvo pré-cozido, grelhando apenas para dourar."),
]

RECEITAS_2 = CARNES + PEIXES
