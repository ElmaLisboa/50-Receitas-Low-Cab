# -*- coding: utf-8 -*-
"""Receitas 01-16: café da manhã, almoços e sopas."""

# Formato: (nome, preparo_min, total_min, porcoes, kcal, carb_g, prot_g, gord_g, [ingredientes], [passos], dica, troca)

CAFE = [
("Omelete de forno com espinafre e queijo", 10, 30, 2, 385, 6, 27, 28,
 ["4 ovos", "1 xíc. de espinafre picado (fresco ou congelado, espremido)", "50 g de queijo muçarela ralado", "2 col. sopa de creme de leite", "1/2 cebola picada", "1 col. sopa de azeite", "sal, pimenta-do-reino e noz-moscada a gosto"],
 ["Refogue a cebola no azeite por 3 minutos, junte o espinafre e cozinhe até secar a água.", "Bata os ovos com o creme de leite, sal, pimenta e noz-moscada.", "Misture o refogado e o queijo aos ovos.", "Despeje em refratário pequeno untado e asse a 180 °C por 20-25 minutos, até o centro firmar."],
 "Faça dois de uma vez: o segundo dura 3 dias na geladeira e vira café da manhã de amanhã.",
 "Troque o espinafre por abobrinha ralada e espremida — mesma técnica, sabor mais neutro."),

("Crepioca de frigideira com queijo e tomate", 5, 10, 1, 290, 14, 18, 16,
 ["1 ovo", "1 col. sopa rasa de goma de tapioca", "1 col. sopa de requeijão ou creme de leite", "2 fatias de queijo muçarela", "3 rodelas finas de tomate", "orégano e sal a gosto"],
 ["Bata o ovo com a tapioca, o requeijão e o sal até ficar homogêneo.", "Aqueça uma frigideira antiaderente em fogo baixo e despeje a mistura.", "Cozinhe 2 minutos, vire, cubra com queijo e tomate e dobre ao meio.", "Deixe mais 1 minuto com a tampa fechada para o queijo derreter."],
 "Fogo baixo é o segredo: em fogo alto a crepioca resseca e racha na hora de dobrar.",
 "Versão doce: recheie com 1 col. de chá de pasta de amendoim e canela."),

("Pão low carb de micro-ondas (2 minutos)", 5, 7, 1, 245, 4, 14, 18,
 ["1 ovo", "2 col. sopa de farinha de amêndoas", "1 col. sopa de creme de leite", "1/2 col. chá de fermento em pó", "1 pitada de sal", "1/2 col. chá de manteiga para untar"],
 ["Misture tudo em uma caneca ou pote quadrado untado, com um garfo, até sumirem as bolinhas de farinha.", "Leve ao micro-ondas por 90 segundos em potência alta.", "Desenforme, corte ao meio e doure na frigideira ou torradeira por 1 minuto de cada lado."],
 "Só fica bom se você dourar depois — o micro-ondas assa, mas não dá cor nem textura de pão.",
 "Sem farinha de amêndoas? Use 1 col. sopa de farinha de linhaça dourada + 1 de coco."),

("Panqueca de banana com aveia (sem farinha)", 8, 15, 2, 260, 22, 15, 12,
 ["1 banana bem madura", "2 ovos", "3 col. sopa de farelo de aveia", "1/2 col. chá de canela", "1/2 col. chá de fermento", "1 col. chá de manteiga ou óleo de coco"],
 ["Amasse a banana com um garfo até virar purê.", "Junte os ovos, a aveia, a canela e o fermento e misture bem.", "Aqueça a manteiga em fogo baixo e despeje conchas pequenas.", "Doure 2 minutos de cada lado, virando quando aparecerem bolhas na superfície."],
 "A banana precisa estar com a casca pintada de marrom: é o que adoça sem açúcar.",
 "Troque a banana por 1/2 maçã ralada + 1 col. chá de adoçante para reduzir ainda mais o carbo."),

("Muffin salgado de ovo, legumes e bacon", 15, 35, 6, 180, 3, 12, 13,
 ["6 ovos", "1/2 xíc. de bacon em cubos", "1/2 abobrinha ralada e espremida", "1/2 xíc. de queijo ralado", "2 col. sopa de cebolinha picada", "sal e pimenta a gosto"],
 ["Frite o bacon até dourar e escorra em papel-toalha.", "Rale a abobrinha, salgue, espere 5 minutos e esprema bem com as mãos.", "Bata os ovos, misture todos os ingredientes e distribua em forminhas de muffin.", "Asse a 180 °C por 20-25 minutos, até o centro ficar firme."],
 "Congele em saco zip e reaqueça 30 segundos no micro-ondas: café pronto em meio minuto.",
 "Troque o bacon por frango desfiado para uma versão com menos gordura saturada."),

("Pão de queijo de frigideira", 5, 10, 1, 275, 6, 16, 21,
 ["1 ovo", "2 col. sopa de polvilho azedo", "2 col. sopa de queijo parmesão ou muçarela ralada", "1 col. sopa de creme de leite", "1 pitada de sal"],
 ["Misture tudo com um garfo até virar uma massa cremosa.", "Despeje em frigideira pequena antiaderente untada, em fogo baixo.", "Tampe e deixe 4 minutos, vire e deixe mais 3 minutos.", "Corte ao meio e recheie ainda quente."],
 "O polvilho azedo (não o doce) é o que dá o puxa-puxa característico.",
 "Recheio curinga: requeijão com orégano ou frango desfiado com catupiry."),

("Wrap de couve com frango cremoso", 12, 20, 2, 310, 9, 26, 19,
 ["4 folhas grandes de couve manteiga", "1 xíc. de frango cozido desfiado", "3 col. sopa de requeijão ou iogurte natural", "1/2 cenoura ralada", "1/2 xíc. de alface picada", "suco de 1/4 de limão, sal e pimenta"],
 ["Passe as folhas de couve por água fervente por 20 segundos e depois em água gelada — isso amacia sem cozinhar.", "Misture o frango com o requeijão, o limão, sal e pimenta.", "Monte sobre a folha seca: alface, cenoura e o frango cremoso.", "Enrole firme como um charuto, dobrando as laterais, e corte ao meio."],
 "Seque bem a couve com papel-toalha: folha molhada faz o wrap desmontar na mão.",
 "Troque a couve por folha de acelga crua, que é mais crocante e não precisa de choque térmico."),

("Ovos mexidos cremosos com abacate e sementes", 8, 10, 1, 405, 8, 20, 33,
 ["2 ovos", "1 col. sopa de manteiga", "1/2 abacate pequeno em fatias", "1 col. sopa de sementes de girassol ou abóbora", "cebolinha picada, sal e pimenta"],
 ["Bata os ovos com sal e pimenta sem fazer espuma.", "Derreta a manteiga em fogo baixo, despeje os ovos e espere 20 segundos sem mexer.", "Arraste com uma espátula do centro para as bordas, repetindo até ficar cremoso e ainda úmido.", "Sirva imediatamente com o abacate por cima, as sementes e a cebolinha."],
 "Tire do fogo quando ainda parecer cru demais: o calor da panela termina o cozimento.",
 "Sem abacate? Use 2 col. sopa de creme de leite azedo com limão."),

("Smoothie de morango com coco (sem açúcar)", 5, 5, 1, 240, 12, 14, 16,
 ["1 xíc. de morangos congelados", "200 ml de leite de coco sem açúcar", "1 col. sopa de whey protein sabor baunilha (opcional)", "1 col. sopa de pasta de amendoim", "gelo e adoçante a gosto"],
 ["Bata o leite de coco com a pasta de amendoim até dissolver.", "Acrescente os morangos congelados e o whey.", "Bata por 40 segundos, parando para raspar as laterais.", "Ajuste a doçura com adoçante e sirva na hora."],
 "Use fruta congelada em vez de gelo: dilui menos e fica cremoso como milk-shake.",
 "Sem whey? Troque por 2 col. sopa de iogurte grego natural integral."),

("Torrada de pão low carb com pasta de atum", 8, 10, 1, 295, 5, 24, 20,
 ["1 fatia do pão low carb de micro-ondas (receita 03)", "1 lata pequena de atum em água, escorrido", "2 col. sopa de maionese caseira ou requeijão", "1 col. chá de mostarda", "1/4 de cebola roxa picada bem fina", "salsinha, sal e pimenta"],
 ["Toste a fatia de pão na frigideira até dourar dos dois lados.", "Misture o atum com a maionese, a mostarda, a cebola e a salsinha.", "Tempere com sal e pimenta e espalhe sobre a torrada.", "Finalize com mais salsinha e um fio de azeite."],
 "Escorra o atum apertando com as costas de uma colher — pasta aguada escorre pelo pão.",
 "Troque o atum por frango desfiado ou ovo cozido picado."),

("Iogurte proteico com granola de castanhas", 5, 5, 1, 320, 10, 22, 22,
 ["170 g de iogurte natural integral", "1/3 xíc. de mix de castanhas picadas (pará, caju, amêndoa)", "1 col. sopa de coco em flocos sem açúcar", "1/2 col. chá de canela", "1 col. chá de adoçante ou mel (opcional)", "5 morangos picados"],
 ["Toste as castanhas com o coco em flocos em frigideira seca por 2 minutos, mexendo sempre.", "Monte o iogurte em uma tigela, cubra com os morangos.", "Espalhe a granola morna por cima e polvilhe a canela.", "Adoce só se necessário — a canela já engana o paladar."],
 "Nunca toste a granola perto do telefone: castanha queima em 30 segundos e amarga tudo.",
 "Granola em lote: triplique a receita e guarde 15 dias em pote fechado."),

("Pão de muçarela com 3 ingredientes", 10, 30, 8, 165, 2, 12, 12,
 ["200 g de muçarela ralada", "1 ovo", "2 col. sopa de farinha de amêndoas", "1/2 col. chá de fermento em pó", "sal e orégano a gosto"],
 ["Derreta a muçarela no micro-ondas por 40 segundos e misture até virar uma massa elástica.", "Junte o ovo, a farinha de amêndoas, o fermento, o sal e o orégano e sove rápido com as mãos untadas.", "Modele 8 pãezinhos e acomode em assadeira forrada.", "Asse a 180 °C por 18-20 minutos, até dourar."],
 "Se a massa grudar demais, unte as mãos com azeite em vez de acrescentar mais farinha.",
 "Sirva aberto com requeijão e orégano: substitui o pão francês do lanche da tarde."),

("Ovos benedict low carb (base de abobrinha)", 15, 25, 2, 420, 8, 24, 33,
 ["1 abobrinha grande em 4 rodelas grossas", "4 ovos", "4 fatias de presunto cru ou bacon", "2 col. sopa de manteiga", "1 gema", "suco de 1/2 limão", "sal, páprica e cebolinha"],
 ["Sele as rodelas de abobrinha em frigideira quente com azeite, 3 minutos de cada lado, e tempere com sal.", "Frite o presunto ou bacon até ficar crocante.", "Faça o molho: derreta a manteiga, bata com a gema e o limão em fogo baixíssimo até engrossar sem ferver.", "Poche os ovos em água com vinagre por 3 minutos, monte sobre a abobrinha e cubra com molho e presunto."],
 "O molho talha se a panela esquentar demais — cozinhe em banho-maria se o fogão for muito forte.",
 "Troque a abobrinha por fatia grossa de berinjela grelhada."),
]

ALMOCO = [
("Arroz de couve-flor simples", 10, 15, 4, 65, 5, 4, 3,
 ["1 couve-flor média em buquês", "1 col. sopa de azeite", "2 dentes de alho picados", "1/4 de cebola picada", "sal e cheiro-verde"],
 ["Processe a couve-flor crua em pulsos curtos até virar grãos do tamanho de arroz (ou rale no ralador grosso).", "Refogue o alho e a cebola no azeite por 2 minutos.", "Junte a couve-flor e refogue em fogo alto por 5-6 minutos, mexendo.", "Tempere com sal e finalize com cheiro-verde — não tampe, senão vira purê."],
 "Nunca processe a couve-flor cozida: ela solta água e vira papa. Sempre crua e em pulsos curtos.",
 "Base neutra: guarda 4 dias na geladeira e aceita qualquer sobra de proteína por cima."),

("Arroz de couve-flor à grega", 15, 25, 4, 145, 11, 6, 9,
 ["1 receita de arroz de couve-flor (receita 13)", "1/2 cenoura em cubinhos", "1/2 xíc. de vagem picada", "1/4 de xíc. de pimentão vermelho picado", "1/3 xíc. de uvas-passas (opcional)", "1/4 xíc. de amêndoas laminadas", "2 col. sopa de azeite e sal"],
 ["Refogue a cenoura e a vagem no azeite por 4 minutos, mantendo crocantes.", "Acrescente o pimentão e refogue mais 2 minutos.", "Junte o arroz de couve-flor pronto e aqueça por 3 minutos.", "Finalize com as amêndoas tostadas e as passas, se usar."],
 "As amêndoas entram só no final: tostadas no refogo desde o início, elas amolecem.",
 "Sem passas, use 2 col. sopa de damasco picado — mesma doçura com menos carbo."),

("Salada completa de frango com molho de iogurte", 15, 25, 2, 340, 12, 32, 18,
 ["1 peito de frango grelhado em tiras", "4 xíc. de folhas variadas", "1/2 pepino em rodelas", "1 tomate em gomos", "1/4 de abacate", "170 g de iogurte natural", "1 col. chá de mostarda, suco de 1/2 limão, azeite, sal e ervas"],
 ["Tempere o frango com sal, pimenta e páprica e grelhe 5 minutos de cada lado.", "Monte as folhas, o pepino, o tomate e o abacate em duas tigelas.", "Misture o iogurte com a mostarda, o limão, 1 col. sopa de azeite, sal e ervas.", "Cubra com o frango morno e regue com o molho na hora de comer."],
 "Salada com molho separado dura 2 dias na marmita; com molho junto, murcha em 3 horas.",
 "Troque o frango por atum ou grão-de-bico cozido (aumente a porção e some os carbos)."),

("Salada de atum com ovo e maionese de limão", 12, 20, 2, 375, 6, 28, 27,
 ["2 latas de atum em água escorrido", "2 ovos cozidos picados", "1/2 xíc. de salsão picado", "1/4 de cebola roxa picada", "3 col. sopa de maionese", "suco de 1/2 limão", "1 col. chá de mostarda, sal, pimenta e salsinha"],
 ["Misture a maionese com o limão, a mostarda, sal e pimenta.", "Junte o atum, o ovo, o salsão e a cebola e incorpore delicadamente.", "Finalize com salsinha e ajuste o sal.", "Sirva sobre folhas, em wrap de couve ou recheando tomate."],
 "O salsão é o que dá crocância — sem ele, a salada fica pastosa.",
 "Versão de marmita: monte em pote de vidro com as folhas no fundo e a salada por cima."),

("Macarrão de abobrinha ao molho de tomate caseiro", 12, 30, 2, 265, 14, 12, 18,
 ["2 abobrinhas grandes", "6 tomates maduros (ou 1 lata de tomate pelado)", "2 dentes de alho", "1/2 cebola", "1 col. sopa de azeite", "manjericão, sal e pimenta", "parmesão ralado para finalizar"],
 ["Faça o molho: refogue cebola e alho, junte o tomate picado e cozinhe 20 minutos em fogo baixo até encorpar.", "Corte a abobrinha em tiras finas com descascador ou espiralizador.", "Refogue a abobrinha por 90 segundos no azeite quente — só para amornar, nunca cozinhar.", "Junte o molho, mexa rapidamente e finalize com manjericão e parmesão."],
 "Salgue a abobrinha já espiralizada, deixe 10 minutos no escorredor e seque com papel: corta a água que afina o molho.",
 "Troque o tomate pelado por molho de couve-flor batida com parmesão para uma versão ainda mais baixa em carbo."),

("Escondidinho low carb de couve-flor com carne seca", 25, 60, 6, 390, 13, 28, 25,
 ["1 couve-flor grande", "400 g de carne seca dessalgada e desfiada", "2 col. sopa de requeijão", "2 col. sopa de manteiga", "1 cebola picada", "3 dentes de alho", "100 g de muçarela ralada", "cheiro-verde"],
 ["Cozinhe a couve-flor no vapor até ficar macia e bata com a manteiga e o requeijão até virar purê liso.", "Refogue a cebola e o alho, junte a carne seca desfiada e refogue 5 minutos.", "Monte em refratário: carne no fundo, purê por cima, muçarela por último.", "Leve ao forno a 200 °C por 20 minutos, até gratinar."],
 "Escorra bem a couve-flor cozida antes de bater: excesso de água deixa o purê ralo.",
 "Sem carne seca? Use carne moída refogada com pimentão ou frango desfiado."),

("Lasanha de berinjela à bolonhesa", 30, 75, 6, 355, 12, 30, 22,
 ["2 berinjelas grandes em fatias finas", "500 g de carne moída", "1 lata de tomate pelado", "1 cebola e 3 dentes de alho", "200 g de muçarela fatiada", "100 g de parmesão ralado", "azeite, orégano, sal e pimenta"],
 ["Salgue as fatias de berinjela, deixe 20 minutos, enxágue e seque bem.", "Grelhe as fatias em frigideira quente com um fio de azeite, 2 minutos de cada lado.", "Faça o molho: refogue cebola e alho, junte a carne moída, doure, acrescente o tomate e cozinhe 25 minutos.", "Monte em camadas — molho, berinjela, muçarela — terminando com molho e parmesão. Asse a 190 °C por 35 minutos."],
 "Secar a berinjela é obrigatório: sem isso, a lasanha solta água e vira sopa no refratário.",
 "Troque a berinjela por fatias finas de abobrinha, grelhando por menos tempo."),

("Berinjela recheada com carne moída", 20, 50, 4, 330, 11, 26, 20,
 ["2 berinjelas cortadas ao meio", "400 g de carne moída", "1 cebola e 2 dentes de alho picados", "1 tomate picado", "1/2 xíc. de muçarela ralada", "2 col. sopa de azeite", "salsinha, sal, pimenta e cominho"],
 ["Retire parte da polpa das berinjelas, pique e reserve.", "Salgue as metades e leve ao forno a 180 °C por 15 minutos para amaciar.", "Refogue cebola e alho, doure a carne, junte a polpa picada e o tomate e cozinhe 10 minutos.", "Recheie as berinjelas, cubra com queijo e volte ao forno por 15 minutos."],
 "Asse as cascas antes de rechear: berinjela crua no forno fica dura por dentro e queimada por fora.",
 "Troque a carne moída por atum com requeijão para uma versão de 25 minutos."),

("Abobrinha recheada com frango e requeijão", 20, 45, 4, 305, 9, 28, 18,
 ["4 abobrinhas médias", "300 g de frango cozido desfiado", "4 col. sopa de requeijão", "1/2 cebola picada", "2 dentes de alho", "1/2 xíc. de muçarela ralada", "milho-verde sem açúcar (opcional), sal, páprica e salsinha"],
 ["Corte as abobrinhas ao meio no sentido do comprimento e retire o miolo com uma colher.", "Refogue a cebola e o alho, junte o miolo picado, o frango, o requeijão e os temperos.", "Recheie as canoas de abobrinha e polvilhe a muçarela.", "Asse a 190 °C por 25 minutos, até a abobrinha ficar macia e o queijo dourado."],
 "Deixe 0,5 cm de parede na abobrinha: fina demais, ela desaba quando sai do forno.",
 "Versão vegetariana: troque o frango por shimeji refogado com cream cheese."),

("Wrap de alface com carne moída picante", 15, 25, 3, 320, 8, 26, 21,
 ["1 alface americana (folhas inteiras)", "500 g de carne moída", "1 cebola picada", "2 dentes de alho", "1 pimentão pequeno picado", "2 col. sopa de molho de tomate", "páprica defumada, cominho, pimenta e sal", "queijo ralado e creme azedo para servir"],
 ["Refogue a cebola, o alho e o pimentão por 4 minutos.", "Acrescente a carne moída e doure bem, quebrando os grumos com a espátula.", "Junte o molho de tomate e os temperos e cozinhe 8 minutos até secar o líquido.", "Sirva em folhas de alface com queijo e creme azedo."],
 "Seque as folhas de alface com papel-toalha — folha molhada rasga ao enrolar.",
 "Sem carne moída? Use frango desfiado com os mesmos temperos."),

("Espaguete de palmito ao alho e óleo", 10, 20, 2, 210, 7, 8, 17,
 ["1 vidro de palmito pupunha em fios (ou espaguete de konjac)", "4 dentes de alho laminados", "3 col. sopa de azeite", "1/4 de xíc. de parmesão ralado", "salsinha, pimenta-do-reino e sal"],
 ["Escorra e seque bem o palmito com papel-toalha.", "Aqueça o azeite em fogo baixo e doure o alho laminado sem deixar queimar.", "Junte o palmito e refogue 3 minutos em fogo médio-alto para evaporar a água.", "Desligue, misture o parmesão, a salsinha e a pimenta e sirva imediatamente."],
 "Palmito e konjac soltam muita água: secar bem antes do refogo é o que impede o prato de ficar aguado.",
 "Acrescente 1 xíc. de camarão salteado para virar prato principal completo."),
]

SOPAS = [
("Caldo verde low carb (sem batata)", 15, 35, 4, 195, 9, 14, 12,
 ["1 couve-flor pequena em buquês", "200 g de linguiça portuguesa ou calabresa em rodelas", "1 maço de couve manteiga em tiras finas", "1 cebola e 3 dentes de alho", "1 L de caldo de galinha ou água", "2 col. sopa de azeite, sal e pimenta"],
 ["Frite a linguiça em panela grande até dourar e reserve parte da gordura.", "Refogue a cebola e o alho nessa gordura por 3 minutos.", "Junte a couve-flor e o caldo, cozinhe 15 minutos e bata no liquidificador até ficar cremoso.", "Volte à panela, junte a couve em tiras e a linguiça e cozinhe 5 minutos, sem deixar a couve amolecer demais."],
 "A couve entra no final e cozinha só 5 minutos — ela deve ficar verde-viva, não marrom.",
 "Versão sem embutido: troque a linguiça por frango desfiado e acrescente páprica defumada."),

("Sopa de abóbora com leite de coco e gengibre", 15, 40, 4, 180, 16, 5, 11,
 ["500 g de abóbora cabotiá em cubos", "200 ml de leite de coco sem açúcar", "1 pedaço de 3 cm de gengibre ralado", "1 cebola e 2 dentes de alho", "700 ml de caldo de legumes", "1 col. sopa de azeite, sal, pimenta e cebolinha"],
 ["Refogue a cebola, o alho e o gengibre no azeite por 3 minutos.", "Junte a abóbora e o caldo e cozinhe 20 minutos, até amaciar.", "Bata no liquidificador com o leite de coco até ficar liso.", "Ajuste o sal, aqueça sem ferver e finalize com cebolinha."],
 "Abóbora tem mais carbo que outros legumes — controle a porção se estiver em fase de indução.",
 "Troque o gengibre por curry em pó e finalize com coentro para um perfil thai."),

("Sopa de legumes com frango desfiado", 20, 45, 4, 240, 14, 24, 10,
 ["300 g de peito de frango", "1 abobrinha em cubos", "1 cenoura em cubos", "1/2 xíc. de vagem picada", "1 xíc. de couve-flor em buquês", "1 cebola, 2 dentes de alho e 1 tomate", "1,2 L de água ou caldo, azeite, sal, louro e salsinha"],
 ["Cozinhe o frango na água com louro e sal por 20 minutos, retire e desfie.", "No mesmo caldo, refogue cebola e alho à parte e devolva à panela com o tomate.", "Junte a cenoura e cozinhe 8 minutos, depois a abobrinha, a vagem e a couve-flor por mais 8 minutos.", "Volte o frango desfiado, ajuste o sal e finalize com salsinha."],
 "Cozinhe os legumes em ordem de dureza: cenoura primeiro, folhas e abobrinha por último.",
 "Congele em potes de 500 ml: dura 3 meses e resolve jantar sem planejamento."),

("Creme de abobrinha com cream cheese", 12, 30, 3, 175, 8, 8, 13,
 ["3 abobrinhas grandes em rodelas", "100 g de cream cheese", "1 cebola e 2 dentes de alho", "600 ml de caldo de legumes", "2 col. sopa de azeite", "sal, pimenta-branca e noz-moscada", "torresmo ou crouton low carb para servir"],
 ["Refogue a cebola e o alho no azeite até dourar.", "Junte a abobrinha e o caldo e cozinhe 15 minutos.", "Bata no liquidificador com o cream cheese até ficar aveludado.", "Volte à panela, tempere com pimenta-branca e noz-moscada e aqueça sem ferver."],
 "Cream cheese entra sempre com o fogo desligado ou baixo: ferver faz o creme talhar e separar.",
 "Troque o cream cheese por 100 ml de creme de leite para uma versão mais leve."),

("Sopa de tomate assado com manjericão", 20, 45, 4, 130, 11, 4, 8,
 ["1 kg de tomate maduro cortado ao meio", "1 cebola em gomos", "4 dentes de alho com casca", "3 col. sopa de azeite", "1 xíc. de manjericão fresco", "400 ml de caldo de legumes", "sal e pimenta-do-reino"],
 ["Disponha os tomates, a cebola e o alho em assadeira, regue com azeite e tempere.", "Asse a 200 °C por 30 minutos, até as bordas caramelizarem.", "Esprema os alhos para fora da casca e bata tudo no liquidificador com o caldo.", "Volte à panela, ajuste o sal, aqueça e finalize com manjericão fresco."],
 "Assar antes de bater é o que tira o gosto ácido e metálico do tomate cru.",
 "Finalize com 1 col. de creme de leite no prato para uma versão mais aveludada."),
]

RECEITAS_1 = CAFE + ALMOCO + SOPAS
