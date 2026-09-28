# -*- coding: utf-8 -*-
"""Receitas 51-70 (números 41-50 do livro): jantares rápidos e sobremesas."""

# Formato: (nome, preparo_min, total_min, porcoes, kcal, carb_g, prot_g, gord_g, [ingredientes], [passos], dica, troca)

JANTARES = [
("Pizza de couve-flor com muçarela e manjericão", 25, 50, 2, 330, 12, 22, 22,
 ["1 couve-flor média processada em grãos", "1 ovo", "80 g de muçarela ralada", "4 col. sopa de farinha de amêndoas", "1/2 xíc. de molho de tomate caseiro", "150 g de muçarela para cobertura", "orégano, manjericão e sal"],
 ["Cozinhe a couve-flor processada no vapor por 5 minutos, deixe amornar e esprema em um pano de prato até sair toda a água.", "Misture a couve-flor seca com o ovo, os 80 g de muçarela, a farinha de amêndoas e o sal.", "Abra a massa em disco fino sobre papel-manteiga untado e asse a 200 °C por 15 minutos.", "Cubra com molho, muçarela e orégano e volte ao forno por 10-12 minutos. Finalize com manjericão."],
 "Espremer a couve-flor é inegociável: massa úmida não firma e a pizza desmancha ao cortar.",
 "Congele os discos pré-assados separados por papel-manteiga e monte a pizza em 12 minutos."),

("Lasanha de abobrinha com presunto e queijo", 25, 60, 6, 335, 10, 28, 21,
 ["3 abobrinhas grandes em fatias finas longitudinais", "400 g de carne moída refogada (ou molho à bolonhesa)", "200 g de presunto fatiado", "250 g de muçarela fatiada", "2 col. sopa de parmesão ralado", "orégano, sal e pimenta"],
 ["Salgue as fatias de abobrinha, aguarde 15 minutos, enxágue e seque uma a uma com papel-toalha.", "Sele as fatias rapidamente em frigideira quente, 1 minuto de cada lado.", "Monte em camadas: molho, abobrinha, presunto, muçarela — repetindo até acabar.", "Finalize com parmesão e orégano e asse a 190 °C por 30 minutos. Descanse 10 minutos antes de cortar."],
 "O descanso de 10 minutos depois do forno é o que faz a lasanha cortar em pedaços firmes.",
 "Troque o presunto por peito de peru ou frango desfiado."),

("Berinjela à parmegiana (sem empanar)", 20, 50, 4, 300, 14, 18, 20,
 ["2 berinjelas em fatias de 1 cm", "1 lata de tomate pelado", "2 dentes de alho e 1/2 cebola", "200 g de muçarela ralada", "1/2 xíc. de parmesão ralado", "3 col. sopa de azeite, manjericão, sal e pimenta"],
 ["Salgue as fatias de berinjela por 20 minutos, enxágue e seque.", "Grelhe as fatias em frigideira quente com um fio de azeite, 2 minutos de cada lado.", "Prepare o molho refogando cebola e alho e cozinhando o tomate por 15 minutos.", "Monte em camadas com os queijos e asse a 190 °C por 25 minutos, até gratinar."],
 "Grelhar antes de montar evita a berinjela esponjosa que absorve todo o molho.",
 "Adicione uma camada de carne moída entre as berinjelas para virar prato único completo."),

("Shimeji na manteiga com shoyu", 8, 15, 2, 165, 8, 8, 12,
 ["300 g de shimeji desfiado", "2 col. sopa de manteiga", "1 col. sopa de shoyu", "1 dente de alho picado", "1 col. sopa de cebolinha picada", "pimenta-do-reino"],
 ["Aqueça a manteiga em fogo alto até espumar.", "Junte o shimeji e refogue sem mexer por 2 minutos, deixando dourar.", "Mexa, acrescente o alho e refogue mais 2 minutos.", "Regue com o shoyu, cozinhe 1 minuto até secar e finalize com cebolinha."],
 "Panela quente e sem mexer no começo: é assim que o cogumelo doura em vez de soltar água e cozinhar.",
 "Serve como acompanhamento ou vira recheio de omelete e de wrap de couve."),

("Feijoada low carb (sem feijão)", 30, 90, 6, 420, 8, 34, 28,
 ["500 g de carnes variadas (costela, paio, linguiça, carne seca)", "1 couve-flor grande processada", "200 g de bacon em cubos", "1 cebola, 4 dentes de alho e 2 folhas de louro", "1 col. sopa de páprica defumada", "azeite, sal e pimenta", "couve refogada e laranja para acompanhar"],
 ["Dessalgue as carnes salgadas por 12 horas, trocando a água.", "Cozinhe as carnes em água com louro por 40 minutos (ou 25 na pressão) e corte em pedaços.", "Frite o bacon, refogue a cebola, o alho e a páprica, junte as carnes e 2 xíc. do caldo e cozinhe 20 minutos.", "Sirva sobre a couve-flor processada refogada na manteiga, com couve e laranja."],
 "A couve-flor refogada na gordura do bacon é o que substitui a textura do feijão no prato.",
 "Versão expressa: use só paio, linguiça e bacon — pronto em 40 minutos."),

("Pão de queijo de airfryer", 10, 25, 12, 130, 3, 8, 9,
 ["200 g de muçarela ralada", "1 ovo", "3 col. sopa de polvilho azedo", "2 col. sopa de requeijão", "1/2 col. chá de fermento em pó", "sal a gosto"],
 ["Derreta a muçarela no micro-ondas por 40 segundos e misture até virar massa.", "Junte o requeijão, o ovo, o polvilho, o fermento e o sal e sove com as mãos untadas.", "Modele 12 bolinhas e acomode na cesta da airfryer sem encostar uma na outra.", "Asse a 180 °C por 12-15 minutos, até dourar."],
 "Polvilho azedo, não doce — é o azedo que dá a casca crocante e o interior elástico.",
 "Congele as bolinhas cruas e asse direto do congelador, somando 3 minutos."),

("Abobrinha recheada com atum e requeijão", 15, 35, 3, 275, 8, 24, 17,
 ["3 abobrinhas médias", "2 latas de atum escorridas", "4 col. sopa de requeijão", "1/4 de cebola picada", "1 tomate sem sementes picado", "1/2 xíc. de muçarela ralada", "salsinha, azeite, sal e pimenta"],
 ["Corte as abobrinhas ao meio e retire o miolo com uma colher, deixando 0,5 cm de parede.", "Misture o atum, o requeijão, a cebola, o tomate, a salsinha, sal e pimenta.", "Recheie as canoas, regue com um fio de azeite e polvilhe a muçarela.", "Asse a 190 °C por 22-25 minutos."],
 "Tire as sementes do tomate: é de lá que vem a água que deixa o recheio ralo.",
 "Sem atum? Use frango desfiado ou carne moída já cozida."),

("Sushi low carb (rolinho de pepino)", 20, 25, 2, 235, 7, 22, 13,
 ["1 pepino japonês grande", "200 g de salmão cru ou atum em tiras", "3 col. sopa de cream cheese", "1/2 abacate em tiras", "1 col. sopa de gergelim", "shoyu, wasabi e cebolinha"],
 ["Fatie o pepino em lâminas finas e longas com descascador ou mandolina.", "Seque as lâminas com papel-toalha e tempere com uma pitada de sal.", "Espalhe o cream cheese, coloque o peixe e o abacate e enrole como um charuto.", "Finalize com gergelim e sirva com shoyu e wasabi."],
 "Salgue as lâminas de pepino e seque: pepino com água solta no rolinho e desmancha.",
 "Versão cozida: troque o peixe cru por camarão ou kani desfiado."),

("Charuto de repolho com carne moída", 25, 60, 4, 320, 12, 26, 19,
 ["1 repolho médio", "500 g de carne moída", "1/2 xíc. de arroz de couve-flor cru", "1 cebola e 3 dentes de alho", "1 ovo", "1 lata de tomate pelado", "hortelã, cominho, sal e pimenta"],
 ["Cozinhe o repolho inteiro em água fervente por 5 minutos e separe as folhas com cuidado.", "Misture a carne com o arroz de couve-flor, a cebola picada, o alho, o ovo e os temperos.", "Coloque 1 col. sopa de recheio em cada folha, dobre as laterais e enrole firme.", "Acomode na panela, cubra com o tomate pelado batido e cozinhe tampado por 35 minutos em fogo baixo."],
 "Retire o talo grosso da folha de repolho com uma faca antes de enrolar: o charuto fecha sem rasgar.",
 "Congele os charutos crus separados por papel e cozinhe direto do congelador por 50 minutos."),

("Arroz de brócolis com alho", 8, 15, 4, 95, 7, 6, 5,
 ["1 maço de brócolis ninja", "2 dentes de alho picados", "1 col. sopa de azeite", "1/4 de cebola picada", "sal e pimenta-do-reino"],
 ["Processe apenas os floretes do brócolis em pulsos curtos até virar grãos.", "Refogue o alho e a cebola no azeite por 2 minutos.", "Junte o brócolis e refogue em fogo alto por 4-5 minutos, mexendo sempre.", "Tempere com sal e pimenta e sirva imediatamente."],
 "Use só os floretes: o talo tem fibra dura e deixa o arroz com pedacinhos fibrosos.",
 "Acrescente 1 ovo mexido e shoyu para virar um arroz frito low carb completo."),
]

SOBREMESAS = [
("Mousse de chocolate com abacate", 10, 40, 4, 265, 12, 6, 22,
 ["1 abacate grande maduro", "3 col. sopa de cacau em pó 100%", "200 ml de creme de leite fresco", "3 col. sopa de adoçante em pó (eritritol ou xilitol)", "1 col. chá de essência de baunilha", "1 pitada de sal"],
 ["Bata o abacate com o cacau, o adoçante, a baunilha e o sal até ficar completamente liso, sem grumos.", "Bata o creme de leite em ponto de chantilly firme.", "Incorpore o chantilly à mistura de chocolate em três etapas, mexendo de baixo para cima.", "Leve à geladeira por no mínimo 30 minutos antes de servir."],
 "O abacate precisa estar bem maduro — o verde firme deixa gosto vegetal e grumos.",
 "Sem abacate? Use 1 xíc. de creme de leite batido com o cacau e o adoçante, sem a fruta."),

("Pudim de coco com eritritol", 12, 55, 8, 190, 6, 8, 15,
 ["4 ovos", "200 ml de leite de coco sem açúcar", "100 ml de creme de leite", "4 col. sopa de eritritol", "1/2 xíc. de coco ralado sem açúcar", "1 col. chá de essência de baunilha", "1 pitada de sal"],
 ["Bata todos os ingredientes no liquidificador por 1 minuto.", "Despeje em forma untada com óleo de coco.", "Cubra com papel-alumínio e asse em banho-maria a 180 °C por 45-50 minutos.", "Deixe esfriar completamente e leve à geladeira por 4 horas antes de desenformar."],
 "O banho-maria é obrigatório: sem ele, o pudim forma bolhas e fica com textura de ovo mexido.",
 "Caramelize o fundo da forma com 2 col. sopa de xilitol derretido para imitar o caramelo tradicional."),

("Brigadeiro low carb de colher", 8, 25, 6, 145, 6, 4, 12,
 ["1 lata de creme de leite", "3 col. sopa de cacau em pó 100%", "3 col. sopa de eritritol ou xilitol", "1 col. sopa de manteiga", "1 pitada de sal", "chocolate 70% picado para finalizar (opcional)"],
 ["Misture o creme de leite, o cacau, o adoçante e a manteiga em panela de fundo grosso.", "Cozinhe em fogo baixo, mexendo sem parar, por 12-15 minutos.", "O ponto é quando a mistura desgruda do fundo da panela ao inclinar.", "Desligue, junte o sal, transfira para um pote e deixe esfriar."],
 "Adoçantes com eritritol não dão o mesmo brilho do açúcar: acrescente 1 col. de chá de óleo de coco no final.",
 "Para enrolar, leve à geladeira por 4 horas e passe em cacau em pó ou castanha triturada."),

("Cheesecake low carb de frutas vermelhas", 25, 70, 10, 285, 8, 9, 25,
 ["1 1/2 xíc. de farinha de amêndoas", "3 col. sopa de manteiga derretida", "500 g de cream cheese em temperatura ambiente", "3 ovos", "1/2 xíc. de eritritol", "200 g de iogurte natural", "1 xíc. de frutas vermelhas congeladas", "suco de 1/2 limão e essência de baunilha"],
 ["Misture a farinha de amêndoas com a manteiga e forre o fundo de uma forma de aro removível. Asse 8 minutos a 180 °C.", "Bata o cream cheese com o eritritol até ficar liso, junte os ovos um a um, depois o iogurte, o limão e a baunilha.", "Despeje sobre a base e asse em banho-maria a 160 °C por 50 minutos, até as bordas firmarem e o centro tremer levemente.", "Desligue o forno e deixe o cheesecake esfriar lá dentro por 1 hora. Cubra com as frutas aquecidas com 1 col. de adoçante."],
 "Esfriar dentro do forno desligado evita a rachadura no centro — choque térmico é o vilão.",
 "Sem forma de aro? Use forma comum forrada com papel-manteiga cruzado para puxar o cheesecake."),

("Cookie low carb de castanhas e chocolate", 12, 30, 12, 130, 4, 4, 11,
 ["1 xíc. de farinha de amêndoas", "1 ovo", "2 col. sopa de manteiga derretida", "2 col. sopa de eritritol", "1/2 col. chá de fermento em pó", "1/2 xíc. de chocolate 70% picado", "1 pitada de sal e baunilha"],
 ["Misture a farinha, o eritritol, o fermento e o sal.", "Junte o ovo, a manteiga e a baunilha e misture até formar uma massa úmida.", "Incorpore o chocolate picado e modele 12 bolinhas achatadas em assadeira forrada.", "Asse a 170 °C por 12-14 minutos, até as bordas dourarem."],
 "Eles saem moles do forno e endurecem ao esfriar — não deixe mais tempo achando que estão crus.",
 "Guarde em pote fechado por até 5 dias ou congele a massa modelada por 2 meses."),

("Trufas de chocolate com óleo de coco", 10, 40, 12, 110, 4, 2, 10,
 ["100 g de chocolate 85% picado", "3 col. sopa de óleo de coco", "2 col. sopa de creme de leite", "1 col. sopa de eritritol em pó", "2 col. sopa de cacau em pó para enrolar", "1 pitada de sal e gotas de baunilha"],
 ["Derreta o chocolate com o óleo de coco em banho-maria ou no micro-ondas em pulsos de 20 segundos.", "Junte o creme de leite, o eritritol, o sal e a baunilha e misture até ficar brilhante.", "Leve à geladeira por 30 minutos, até firmar o suficiente para modelar.", "Modele bolinhas com as mãos e passe no cacau em pó."],
 "Derreta o chocolate em pulsos curtos, mexendo a cada 20 segundos: em fogo direto ele queima e fica arenoso.",
 "Guarde na geladeira — em temperatura ambiente o óleo de coco derrete e a trufa perde a forma."),

("Morangos assados com creme e canela", 8, 25, 4, 175, 10, 4, 14,
 ["500 g de morangos inteiros", "1 col. sopa de eritritol", "1 col. chá de canela em pó", "suco de 1/2 limão", "200 ml de creme de leite fresco batido em chantilly", "folhas de hortelã"],
 ["Misture os morangos com o eritritol, a canela e o limão em um refratário.", "Asse a 180 °C por 18-20 minutos, até soltarem uma calda espessa.", "Deixe amornar por 10 minutos.", "Sirva com o chantilly por cima e hortelã."],
 "Assar concentra o açúcar natural do morango: sobremesa doce sem adoçante em excesso.",
 "Funciona igual com framboesa, amora ou mirtilo — reduza o tempo para 12 minutos."),

("Flan de baunilha sem açúcar", 10, 60, 6, 155, 4, 7, 12,
 ["3 ovos", "300 ml de creme de leite", "200 ml de leite de coco", "3 col. sopa de eritritol", "1 col. chá de essência de baunilha", "1 pitada de sal"],
 ["Bata todos os ingredientes com um fouet, sem incorporar ar.", "Passe pela peneira para remover a película dos ovos.", "Despeje em forminhas individuais untadas e cubra com papel-alumínio.", "Asse em banho-maria a 160 °C por 40-45 minutos. Deixe esfriar e gele por 4 horas."],
 "Peneirar a mistura é o que deixa o flan liso: sem isso, ficam fios de clara cozida na textura.",
 "Sirva com 1 col. de chá de cacau em pó peneirado por cima."),

("Pudim de chia com coco e frutas", 5, 245, 2, 220, 12, 8, 15,
 ["3 col. sopa de sementes de chia", "250 ml de leite de coco sem açúcar", "1 col. sopa de eritritol", "1/2 col. chá de baunilha", "1/2 xíc. de frutas vermelhas", "coco em flocos para finalizar"],
 ["Misture a chia, o leite de coco, o eritritol e a baunilha em um pote com tampa.", "Mexa bem, aguarde 5 minutos e mexa de novo — isso impede que a chia empelote no fundo.", "Leve à geladeira por no mínimo 4 horas, ou de um dia para o outro.", "Cubra com as frutas e o coco em flocos antes de servir."],
 "A segunda mexida aos 5 minutos é o truque: sem ela, metade das sementes fica grudada no fundo.",
 "Faça 5 potes no domingo e tenha café da manhã pronto até sexta."),

("Bombom gelado de pasta de amendoim", 10, 50, 10, 125, 4, 5, 11,
 ["1/2 xíc. de pasta de amendoim integral sem açúcar", "100 g de chocolate 85% picado", "2 col. sopa de óleo de coco", "1 col. sopa de eritritol em pó", "1 pitada de sal"],
 ["Misture a pasta de amendoim com o eritritol e o sal até ficar homogênea.", "Modele 10 bolinhas achatadas e leve ao congelador por 20 minutos.", "Derreta o chocolate com o óleo de coco em banho-maria.", "Banhe as bolinhas no chocolate, apoie em papel-manteiga e volte ao congelador por 20 minutos."],
 "Congelar o recheio antes de banhar impede que ele se misture ao chocolate e vaze.",
 "Guarde em pote fechado na geladeira por até 10 dias."),

("Sorvete de coco com raspas de limão", 10, 300, 6, 185, 5, 3, 18,
 ["400 ml de leite de coco sem açúcar", "200 ml de creme de leite fresco", "3 col. sopa de eritritol", "raspas de 1 limão", "1 col. chá de baunilha", "1 pitada de sal"],
 ["Bata o creme de leite até formar picos moles.", "Misture o leite de coco, o eritritol, as raspas, a baunilha e o sal.", "Incorpore o creme batido delicadamente e despeje em um pote largo.", "Congele por 5 horas, batendo com um garfo a cada hora para quebrar os cristais de gelo."],
 "As batidas com garfo durante o congelamento são o que separa sorvete cremoso de bloco de gelo.",
 "Versão de chocolate: troque as raspas por 2 col. sopa de cacau em pó peneirado."),

("Paçoca low carb de amendoim", 8, 20, 12, 115, 4, 5, 10,
 ["1 1/2 xíc. de amendoim torrado sem pele e sem sal", "2 col. sopa de farinha de amêndoas", "2 col. sopa de eritritol em pó", "1 pitada de sal", "1 col. chá de óleo de coco (opcional)"],
 ["Processe o amendoim em pulsos até virar uma farofa úmida — cuidado para não virar pasta.", "Junte a farinha de amêndoas, o eritritol e o sal e pulse mais 3 vezes.", "Se estiver muito seco, acrescente o óleo de coco e misture.", "Aperte a mistura em forminhas ou em um pote forrado, corte em quadrados e deixe firmar por 15 minutos."],
 "Processe em pulsos curtos e pare antes: amendoim processado demais vira manteiga e a paçoca não firma.",
 "Guarde em pote fechado por até 10 dias em local fresco."),
]

RECEITAS_3 = JANTARES + SOBREMESAS
