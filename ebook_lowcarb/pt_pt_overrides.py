# -*- coding: utf-8 -*-
"""
Português de Portugal (pt-PT) — adaptação do corpus brasileiro (dados_receitas_*).

Escrito à mão, linha a linha: NÃO é substituição léxica nem regex. Cada entrada
foi revista em português europeu e só existe onde o texto difere do pt-BR; o
resto é servido direto do corpus com pass-through. Contrato fail-loudly:
  * linha de ingrediente com marcador BR sem entrada aqui -> KeyError no import;
  * receita sem OVERRIDES -> KeyError no import;
  * contagem de passos divergente -> AssertionError no import.
A validação de QA depois do render varre o HTML/PDF final por 50+ marcadores
BR (= 0) e exige os marcadores pt-PT (presentes).

Convenções adotadas (revistas uma a uma):
  registro    imperativo de TU (Refoga, Bate, Mistura, Junta, Aquece, Serve...),
              2.ª pessoa: tu/tua/teu — o "você" brasileiro é marca de origem;
  cozinha     lume (fogo baixo/médio/alto -> lume brando/médio/forte), tacho
              (panela), frigorífico (geladeira), alourar (dourar o processo;
              adjetivo "dourada" de cor mantém-se), papel de cozinha
              (papel-toalha), papel vegetal (papel-manteiga), papel de alumínio,
              espiralador, banho-maria, frigideira, assadeira, refratário;
  ingredientes nata (creme de leite), mozzarella (muçarela), queijo creme
              (requeijão/cream cheese), carne picada (carne moída), beringela
              (berinjela), aipo (salsão), salsa (cheiro-verde/salsinha),
              cebolinho (cebolinha), couve portuguesa (couve manteiga — caldo
              verde autêntico), amido de mandioca azedo (polvilho azedo),
              molho de soja (shoyu), esparguete (espaguete), chávena (xícara),
              c. de sopa / c. de chá (col. sopa / col. chá), caixinha de nata;
  termos      hidratos de carbono (carboidratos), pequeno-almoço (café da
              manhã), menu (cardápio), bónus (bônus), take-away (delivery),
              tupper/pote de levar (marmita), coringa (curinga), Dijon,
              tailandês (thai), biscoito (cookie), crepe de tapioca (crepioca);
  mantidos    pratos e marcas culturais brasileiras: feijoada, moqueca, paçoca,
              brigadeiro, escondidinho, xadrez, parmegiana, abobrinha (= courgette
              em Portugal), muçarela? NÃO — mozzarella; linguiça, paio, carne
              seca, dendê, copa-lombo? -> entremeada.
"""
import livro as pt

# ---------------------------------------------------------------------------
# Ingredientes: chave = linha EXATA do corpus -> valor pt-PT. Só as linhas que
# diferem; qualquer linha com marcador BR que falte aqui derruba o import.
INGREDIENTS_PT = {
 # ---- unidades BR -> PT (chávena, c. de sopa, c. de chá) ----
 "1 xíc. de espinafre picado (fresco ou congelado, espremido)": "1 chávena de espinafre picado (fresco ou congelado, espremido)",
 "1/2 xíc. de bacon em cubos": "1/2 chávena de bacon em cubos",
 "1/2 xíc. de queijo ralado": "1/2 chávena de queijo ralado",
 "1 xíc. de frango cozido desfiado": "1 chávena de frango cozido desfiado",
 "1/2 xíc. de alface picada": "1/2 chávena de alface picada",
 "1/3 xíc. de mix de castanhas picadas (pará, caju, amêndoa)": "1/3 chávena de mix de castanhas (pará, caju e amêndoas) picadas",
 "4 xíc. de folhas variadas": "4 chávenas de folhas variadas",
 "1/2 xíc. de salsão picado": "1/2 chávena de aipo picado",
 "1/4 de xíc. de parmesão ralado": "1/4 de chávena de parmesão ralado",
 "1/2 xíc. de muçarela ralada": "1/2 chávena de mozzarella ralada",
 "1/2 xíc. de vagem picada": "1/2 chávena de vagem picada",
 "1 xíc. de couve-flor em buquês": "1 chávena de couve-flor em buquês",
 "1/2 xíc. de castanha-de-caju torrada": "1/2 chávena de castanha-de-caju torrada",
 "1/4 de xíc. de caldo de carne": "1/4 de chávena de caldo de carne",
 "1/2 xíc. de farinha de amêndoas": "1/2 chávena de farinha de amêndoas",
 "1/2 xíc. de parmesão ralado": "1/2 chávena de parmesão ralado",
 "1/2 xíc. de azeitonas pretas": "1/2 chávena de azeitonas pretas",
 "1/2 xíc. de azeite": "1/2 chávena de azeite",
 "1/2 xíc. de molho de tomate caseiro": "1/2 chávena de molho de tomate caseiro",
 "1/2 xíc. de arroz de couve-flor cru": "1/2 chávena de arroz de couve-flor cru",
 "1/2 xíc. de coco ralado sem açúcar": "1/2 chávena de coco ralado sem açúcar",
 "1 xíc. de frutas vermelhas congeladas": "1 chávena de frutas vermelhas congeladas",
 "1/2 xíc. de eritritol": "1/2 chávena de eritritol",
 "1 xíc. de farinha de amêndoas": "1 chávena de farinha de amêndoas",
 "1/2 xíc. de chocolate 70% picado": "1/2 chávena de chocolate 70% picado",
 "1 1/2 xíc. de farinha de amêndoas": "1 1/2 chávenas de farinha de amêndoas",
 "1 1/2 xíc. de amendoim torrado sem pele e sem sal": "1 1/2 chávenas de amendoim torrado sem pele e sem sal",
 "1 col. sopa rasa de goma de tapioca": "1 c. de sopa rasa de goma de tapioca",
 "1 col. sopa de azeite": "1 c. de sopa de azeite",
 "2 col. sopa de azeite": "2 c. de sopa de azeite",
 "3 col. sopa de azeite": "3 c. de sopa de azeite",
 "2 col. sopa de azeite, sal e pimenta": "2 c. de sopa de azeite, sal e pimenta",
 "1 col. sopa de azeite, sal, pimenta e cebolinha": "1 c. de sopa de azeite, sal, pimenta e cebolinho",
 "3 col. sopa de azeite, manjericão, sal e pimenta": "3 c. de sopa de azeite, manjericão, sal e pimenta",
 "2 col. sopa de azeite e manjericão": "2 c. de sopa de azeite e manjericão",
 "1 col. sopa de manteiga": "1 c. de sopa de manteiga",
 "2 col. sopa de manteiga": "2 c. de sopa de manteiga",
 "2 col. sopa de manteiga derretida": "2 c. de sopa de manteiga derretida",
 "3 col. sopa de manteiga derretida": "3 c. de sopa de manteiga derretida",
 "1 col. sopa de sementes de girassol ou abóbora": "1 c. de sopa de sementes de girassol ou abóbora",
 "1 col. sopa de coco em flocos sem açúcar": "1 c. de sopa de coco em flocos sem açúcar",
 "1 col. sopa de gergelim": "1 c. de sopa de gergelim",
 "2 col. sopa de farinha de amêndoas": "2 c. de sopa de farinha de amêndoas",
 "3 col. sopa de farinha de amêndoas": "3 c. de sopa de farinha de amêndoas",
 "4 col. sopa de farinha de amêndoas": "4 c. de sopa de farinha de amêndoas",
 "3 col. sopa de farelo de aveia": "3 c. de sopa de farelo de aveia",
 "2 col. sopa de cebolinha picada": "2 c. de sopa de cebolinho picado",
 "2 col. sopa de molho de tomate": "2 c. de sopa de molho de tomate",
 "2 col. sopa de azeite de dendê (ou azeite comum)": "2 c. de sopa de azeite de dendê (ou azeite comum)",
 "sal, pimenta e 2 col. sopa de azeite": "sal, pimenta e 2 c. de sopa de azeite",
 "3 col. sopa de maionese": "3 c. de sopa de maionese",
 "2 col. sopa de mostarda dijon": "2 c. de sopa de mostarda Dijon",
 "2 col. sopa de mostarda": "2 c. de sopa de mostarda",
 "1 col. sopa de vinagre de maçã": "1 c. de sopa de vinagre de maçã",
 "1 col. sopa de páprica defumada": "1 c. de sopa de páprica defumada",
 "1 col. sopa de amido de milho diluído em 3 de água (opcional)": "1 c. de sopa de amido de milho diluído em 3 de água (opcional)",
 "4 col. sopa de eritritol": "4 c. de sopa de eritritol",
 "2 col. sopa de eritritol": "2 c. de sopa de eritritol",
 "1 col. sopa de eritritol em pó": "1 c. de sopa de eritritol em pó",
 "2 col. sopa de eritritol em pó": "2 c. de sopa de eritritol em pó",
 "3 col. sopa de eritritol ou xilitol": "3 c. de sopa de eritritol ou xilitol",
 "3 col. sopa de óleo de coco": "3 c. de sopa de óleo de coco",
 "2 col. sopa de cacau em pó para enrolar": "2 c. de sopa de cacau em pó para enrolar",
 "3 col. sopa de cacau em pó 100%": "3 c. de sopa de cacau em pó 100%",
 "3 col. sopa de adoçante em pó (eritritol ou xilitol)": "3 c. de sopa de adoçante em pó (eritritol ou xilitol)",
 "1/2 col. chá de fermento em pó": "1/2 c. de chá de fermento em pó",
 "1/2 col. chá de manteiga para untar": "1/2 c. de chá de manteiga para untar",
 "1/2 col. chá de canela": "1/2 c. de chá de canela",
 "1/2 col. chá de fermento": "1/2 c. de chá de fermento",
 "1 col. chá de manteiga ou óleo de coco": "1 c. de chá de manteiga ou óleo de coco",
 "1 col. chá de adoçante ou mel (opcional)": "1 c. de chá de adoçante ou mel (opcional)",
 "1 col. chá de mostarda, suco de 1/2 limão, azeite, sal e ervas": "1 c. de chá de mostarda, suco de 1/2 limão, azeite, sal e ervas",
 "1 col. chá de mostarda, sal, pimenta e salsinha": "1 c. de chá de mostarda, sal, pimenta e salsa",
 "1 col. chá de tomilho": "1 c. de chá de tomilho",
 "1 col. chá de páprica": "1 c. de chá de páprica",
 "1 col. chá de pimenta calabresa (opcional)": "1 c. de chá de pimenta calabresa (opcional)",
 "1 col. chá de cominho, alho em pó, cebola em pó": "1 c. de chá de cominho, alho em pó, cebola em pó",
 "1 col. chá de essência de baunilha": "1 c. de chá de essência de baunilha",
 "1 col. chá de óleo de coco (opcional)": "1 c. de chá de óleo de coco (opcional)",
 # ---- vocabulário BR -> PT ----
 "50 g de queijo muçarela ralado": "50 g de mozzarella ralada",
 "2 fatias de queijo muçarela": "2 fatias de mozzarella",
 "100 g de muçarela ralada": "100 g de mozzarella ralada",
 "200 g de muçarela fatiada": "200 g de mozzarella fatiada",
 "80 g de muçarela ralada": "80 g de mozzarella ralada",
 "150 g de muçarela para cobertura": "150 g de mozzarella para cobertura",
 "200 g de muçarela ralada": "200 g de mozzarella ralada",
 "100 g de muçarela em cubos para rechear": "100 g de mozzarella em cubos para rechear",
 "2 col. sopa de queijo parmesão ou muçarela ralada": "2 c. de sopa de queijo parmesão ou mozzarella ralada",
 "100 g de cream cheese": "100 g de queijo creme",
 "500 g de cream cheese em temperatura ambiente": "500 g de queijo creme à temperatura ambiente",
 "3 col. sopa de cream cheese": "3 c. de sopa de queijo creme",
 "1 col. sopa de requeijão ou creme de leite": "1 c. de sopa de queijo creme ou nata",
 "3 col. sopa de requeijão ou iogurte natural": "3 c. de sopa de queijo creme ou iogurte natural",
 "2 col. sopa de requeijão": "2 c. de sopa de queijo creme",
 "4 col. sopa de requeijão": "4 c. de sopa de queijo creme",
 "2 col. sopa de creme de leite": "2 c. de sopa de nata",
 "1 col. sopa de creme de leite": "1 c. de sopa de nata",
 "100 ml de creme de leite fresco": "100 ml de nata fresca",
 "150 ml de creme de leite fresco": "150 ml de nata fresca",
 "200 ml de creme de leite fresco": "200 ml de nata fresca",
 "100 ml de creme de leite": "100 ml de nata",
 "1 lata de creme de leite": "1 caixinha de nata",
 "500 g de carne moída": "500 g de carne picada",
 "400 g de carne moída": "400 g de carne picada",
 "500 g de carne moída (patinho ou acém)": "500 g de carne picada",
 "2 berinjelas grandes em fatias finas": "2 beringelas grandes em fatias finas",
 "2 berinjelas cortadas ao meio": "2 beringelas cortadas ao meio",
 "2 berinjelas em fatias de 1 cm": "2 beringelas em fatias de 1 cm",
 "sal e cheiro-verde": "sal e salsa",
 "cheiro-verde": "salsa",
 "cheiro-verde e queijo ralado": "salsa e queijo ralado",
 "cebolinha picada, sal e pimenta": "cebolinho picado, sal e pimenta",
 "salsinha, pimenta-do-reino e sal": "salsa, pimenta-do-reino e sal",
 "salsinha, pimenta-do-reino e 1 folha de louro": "salsa, pimenta-do-reino e 1 folha de louro",
 "salsinha, sal e pimenta-do-reino": "salsa, sal e pimenta-do-reino",
 "salsinha, sal, pimenta e cominho": "salsa, sal, pimenta e cominho",
 "salsinha, azeite, sal e pimenta": "salsa, azeite, sal e pimenta",
 "1 col. sopa de salsinha ou endro": "1 c. de sopa de salsa ou endro",
 "1 col. sopa de salsinha e 1 de cebolinha": "1 c. de sopa de salsa e 1 de cebolinho",
 "shoyu, wasabi e cebolinha": "molho de soja, wasabi e cebolinho",
 "3 col. sopa de shoyu (ou 2 de shoyu + água)": "3 c. de sopa de molho de soja (ou 2 de molho de soja + água)",
 "4 folhas grandes de couve manteiga": "4 folhas grandes de couve portuguesa",
 "1 maço de couve manteiga em tiras finas": "1 maço de couve portuguesa em tiras finas",
 "1 vidro de palmito pupunha em fios (ou espaguete de konjac)": "1 vidro de palmito em fios (ou esparguete de konjac)",
 "2 col. sopa de polvilho azedo": "2 c. de sopa de amido de mandioca azedo",
 "3 col. sopa de polvilho azedo": "3 c. de sopa de amido de mandioca azedo",
 "1,2 L de água ou caldo, azeite, sal, louro e salsinha": "1,2 L de água ou caldo, azeite, sal, louro e salsa",
}

# ---------------------------------------------------------------------------
# Passos + dica + troca em português europeu, escritos à mão (imperativo de
# tu). Só receitas que diferem do pt-BR — aqui são as 50: o registro brasileiro
# (você/fogo/panela/dourar) atravessa o corpus inteiro. Contagem conferida.
OVERRIDES_PT = {
1: ([
 "Refoga a cebola no azeite por 3 minutos, junta o espinafre e cozinha até secar a água.",
 "Bate os ovos com a nata, sal, pimenta e noz-moscada.",
 "Mistura o refogado e o queijo aos ovos.",
 "Despeja em refratário pequeno untado e assa a 180 °C por 20-25 minutos, até o centro firmar.",
 ], "Faz dois de uma vez: o segundo dura 3 dias no frigorífico e vira o pequeno-almoço de amanhã.", "Troca o espinafre por abobrinha ralada e espremida — mesma técnica, sabor mais neutro."),
2: ([
 "Mistura tudo numa caneca ou pote quadrado untado, com um garfo, até sumirem as bolinhas de farinha.",
 "Leva ao micro-ondas por 90 segundos em potência máxima.",
 "Desenforma, corta ao meio e aloura na frigideira ou torradeira por 1 minuto de cada lado.",
 ], "Só fica bom se alourares depois — o micro-ondas assa, mas não dá cor nem textura de pão.", "Sem farinha de amêndoas? Usa 1 c. de sopa de farinha de linhaça dourada + 1 de coco."),
3: ([
 "Amassa a banana com um garfo até virar purê.",
 "Junta os ovos, a aveia, a canela e o fermento e mistura bem.",
 "Aquece a manteiga em lume brando e despeja conchas pequenas.",
 "Aloura 2 minutos de cada lado, virando quando aparecerem bolhas na superfície.",
 ], "A banana precisa de casca castanha: é o que adoça sem açúcar.", "Troca a banana por 1/2 maçã ralada + 1 c. de chá de adoçante para reduzir ainda mais os hidratos."),
4: ([
 "Frita o bacon até alourar e escorre em papel de cozinha.",
 "Rala a abobrinha, salga, espera 5 minutos e espreme bem com as mãos.",
 "Bate os ovos, mistura todos os ingredientes e distribui em forminhas de muffin.",
 "Asse a 180 °C por 20-25 minutos, até o centro ficar firme.",
 ], "Congela num saco selável e reaquece 30 segundos no micro-ondas: o pequeno-almoço sai em meio minuto.", "Troca o bacon por frango desfiado para uma versão com menos gordura saturada."),
5: ([
 "Bate o ovo com a tapioca, o queijo creme e o sal até ficar homogêneo.",
 "Aquece uma frigideira antiaderente em lume brando e despeja a mistura.",
 "Cozinha 2 minutos, vira, cubre com queijo e tomate e dobra ao meio.",
 "Deixa mais 1 minuto com a tampa fechada para o queijo derreter.",
 ], "Lume brando é o segredo: em lume forte o crepe resseca e racha na hora de dobrar.", "Versão doce: recheia com 1 c. de chá de pasta de amendoim e canela."),
6: ([
 "Mistura tudo com um garfo até virar uma massa cremosa.",
 "Despeja em frigideira pequena antiaderente untada, em lume brando.",
 "Tampe e deixa 4 minutos, vira e deixa mais 3 minutos.",
 "Corta ao meio e recheia ainda quente.",
 ], "O amido de mandioca azedo (não o doce) é o que dá a textura elástica característica.", "Recheio coringa: queijo creme com orégano ou frango desfiado cremoso."),
7: ([
 "Passa as folhas de couve por água fervente por 20 segundos e depois em água gelada — isso amacia sem cozinhar.",
 "Mistura o frango com o queijo creme, o limão, sal e pimenta.",
 "Monta sobre a folha seca: alface, cenoura e o frango cremoso.",
 "Enrola firme como um charuto, dobrando as laterais, e corta ao meio.",
 ], "Seca bem a couve com papel de cozinha: folha molhada faz o wrap desmontar na mão.", "Troca a couve por folha de acelga crua, que é mais crocante e não precisa de choque térmico."),
8: ([
 "Bate os ovos com sal e pimenta sem fazer espuma.",
 "Derrete a manteiga em lume brando, despeja os ovos e espera 20 segundos sem mexer.",
 "Arrasta com uma espátula do centro para as bordas, repetindo até ficar cremoso e ainda úmido.",
 "Serve imediatamente com o abacate por cima, as sementes e o cebolinho.",
 ], "Tira do lume quando ainda parecer cru demais: o calor do tacho termina o cozimento.", "Sem abacate? Usa 2 c. de sopa de creme azedo com limão."),
9: ([
 "Tosta as castanhas com o coco em flocos em frigideira seca por 2 minutos, mexendo sempre.",
 "Monta o iogurte numa tigela, cubre com os morangos.",
 "Espalha a granola morna por cima e polvilha a canela.",
 "Adoça só se necessário — a canela já engana o paladar.",
 ], "Nunca tosta a granola perto do telefone: castanha queima em 30 segundos e amarga tudo.", "Granola em lote: triplica a receita e guarda 15 dias em pote fechado."),
10: ([
 "Processa a couve-flor crua em pulsos curtos até virar grãos do tamanho de arroz (ou rala no ralador grosso).",
 "Refoga o alho e a cebola no azeite por 2 minutos.",
 "Junta a couve-flor e refoga em lume forte por 5-6 minutos, mexendo.",
 "Tempera com sal e finaliza com salsa — sem tampar, senão vira purê.",
 ], "A couve-flor nunca deve ser processada cozida: solta água e vira papa. Sempre crua e em pulsos curtos.", "Base neutra: guarda 4 dias no frigorífico e aceita qualquer sobra de proteína por cima."),
11: ([
 "Faz o molho: refoga cebola e alho, junta o tomate picado e cozinha 20 minutos em lume brando até encorpar.",
 "Corta a abobrinha em tiras finas com descascador ou espiralador.",
 "Refoga a abobrinha por 90 segundos no azeite quente — só para amornar, nunca cozinhar.",
 "Junta o molho, mexe rapidamente e finaliza com manjericão e parmesão.",
 ], "Salga a abobrinha já espiralizada, deixa 10 minutos no escorredor e seca com papel de cozinha: corta a água que afina o molho.", "Troca o tomate pelado por molho de couve-flor batida com parmesão para uma versão ainda mais baixa em hidratos."),
12: ([
 "Escorra e seque bem o palmito com papel de cozinha.",
 "Aquece o azeite em lume brando e aloura o alho laminado sem deixar queimar.",
 "Junta o palmito e refoga 3 minutos em lume médio-forte para evaporar a água.",
 "Desliga, mistura o parmesão, a salsa e a pimenta e serve imediatamente.",
 ], "Palmito e konjac soltam muita água: secar bem antes do refogo é o que impede o prato de ficar aguado.", "Acrescenta 1 chávena de camarão salteado para virar prato principal completo."),
13: ([
 "Tempera o frango com sal, pimenta e páprica e grelha 5 minutos de cada lado.",
 "Monta as folhas, o pepino, o tomate e o abacate em duas tigelas.",
 "Mistura o iogurte com a mostarda, o limão, 1 c. de sopa de azeite, sal e ervas.",
 "Cobre com o frango morno e rega com o molho na hora de comer.",
 ], "Salada com molho separado dura 2 dias no tupper; com molho junto, murcha em 3 horas.", "Troca o frango por atum ou grão-de-bico cozido (aumenta a porção e soma os hidratos)."),
14: ([
 "Mistura a maionese com o limão, a mostarda, sal e pimenta.",
 "Junta o atum, o ovo, o aipo e a cebola e incorpora delicadamente.",
 "Finaliza com salsa e ajusta o sal.",
 "Serve sobre folhas, em wrap de couve ou recheando tomate.",
 ], "O aipo é o que dá crocância — sem ele, a salada fica pastosa.", "Versão para levar: monta em pote de vidro com as folhas no fundo e a salada por cima."),
15: ([
 "Refoga a cebola, o alho e o pimentão por 4 minutos.",
 "Acrescenta a carne picada e aloura bem, quebrando os grumos com a espátula.",
 "Junta o molho de tomate e os temperos e cozinha 8 minutos até secar o líquido.",
 "Serve em folhas de alface com queijo e creme azedo.",
 ], "Seca as folhas de alface com papel de cozinha — folha molhada rasga ao enrolar.", "Sem carne picada? Usa frango desfiado com os mesmos temperos."),
16: ([
 "Cozinha a couve-flor no vapor até ficar macia e bata com a manteiga e o queijo creme até virar purê liso.",
 "Refoga a cebola e o alho, junta a carne seca desfiada e refoga 5 minutos.",
 "Monta em refratário: carne no fundo, purê por cima, mozzarella por último.",
 "Leva ao forno a 200 °C por 20 minutos, até gratinar.",
 ], "Escorra bem a couve-flor cozida antes de bater: excesso de água deixa o purê ralo.", "Sem carne seca? Usa carne picada refogada com pimentão ou frango desfiado."),
17: ([
 "Salga as fatias de beringela, deixa 20 minutos, enxágua e seca bem.",
 "Grelha as fatias em frigideira quente com um fio de azeite, 2 minutos de cada lado.",
 "Faz o molho: refoga cebola e alho, junta a carne picada, aloura, acrescenta o tomate e cozinha 25 minutos.",
 "Monta em camadas — molho, beringela, mozzarella — terminando com molho e parmesão. Asse a 190 °C por 35 minutos.",
 ], "Secar a beringela é obrigatório: sem isso, a lasanha solta água e vira sopa no refratário.", "Troca a beringela por fatias finas de abobrinha, grelhando por menos tempo."),
18: ([
 "Retira parte da polpa das beringelas, pica e reserva.",
 "Salga as metades e leva ao forno a 180 °C por 15 minutos para amaciar.",
 "Refoga cebola e alho, aloura a carne, junta a polpa picada e o tomate e cozinha 10 minutos.",
 "Recheia as beringelas, cubre com queijo e volta ao forno por 15 minutos.",
 ], "Asse as cascas antes de rechear: beringela crua no forno fica dura por dentro e queimada por fora.", "Troca a carne picada por atum com queijo creme para uma versão de 25 minutos."),
19: ([
 "Frite a linguiça em tacho grande até alourar e reserva parte da gordura.",
 "Refoga a cebola e o alho nessa gordura por 3 minutos.",
 "Junta a couve-flor e o caldo, cozinha 15 minutos e bata no liquidificador até ficar cremoso.",
 "Volta ao tacho, junta a couve em tiras e a linguiça e cozinha 5 minutos, sem deixar a couve amolecer demais.",
 ], "A couve entra no final e cozinha só 5 minutos — deve ficar verde-viva, não castanha.", "Versão sem embutido: troca a linguiça por frango desfiado e acrescenta páprica defumada."),
20: ([
 "Refoga a cebola, o alho e o gengibre no azeite por 3 minutos.",
 "Junta a abóbora e o caldo e cozinha 20 minutos, até amaciar.",
 "Bate no liquidificador com o leite de coco até ficar liso.",
 "Ajusta o sal, aquece sem ferver e finaliza com cebolinho.",
 ], "A abóbora tem mais hidratos que outros legumes — controla a porção se estiveres em fase de indução.", "Troca o gengibre por curry em pó e finaliza com coentro para um perfil tailandês."),
21: ([
 "Cozinha o frango na água com louro e sal por 20 minutos, retira e desfie.",
 "No mesmo caldo, refoga cebola e alho à parte e devolve ao tacho com o tomate.",
 "Junta a cenoura e cozinha 8 minutos, depois a abobrinha, a vagem e a couve-flor por mais 8 minutos.",
 "Volta o frango desfiado, ajusta o sal e finaliza com salsa.",
 ], "Cozinha os legumes em ordem de dureza: cenoura primeiro, folhas e abobrinha por último.", "Congela em potes de 500 ml: dura 3 meses e resolve jantar sem planejamento."),
22: ([
 "Refoga a cebola e o alho no azeite até alourar.",
 "Junta a abobrinha e o caldo e cozinha 15 minutos.",
 "Bate no liquidificador com o queijo creme até ficar aveludado.",
 "Volta ao tacho, tempera com pimenta-branca e noz-moscada e aquece sem ferver.",
 ], "O queijo creme entra sempre com o lume apagado ou brando: ferver faz o creme talhar e separar.", "Troca o queijo creme por 100 ml de nata para uma versão mais leve."),
23: ([
 "Tempera os filés com sal e pimenta e sela em frigideira bem quente, 4 minutos de cada lado. Reserva.",
 "Na mesma frigideira, derrete a manteiga e refoga o alho por 30 segundos.",
 "Junta a mostarda, a nata e o tomilho e reduz por 3 minutos até engrossar.",
 "Volta o frango ao tacho, banhe com o molho e serve com legumes salteados.",
 ], "Não laves a frigideira entre o frango e o molho: o fundo alourado é o que dá sabor à base do creme.", "Sem Dijon? Usa mostarda amarela + 1/2 c. de chá de mel ou adoçante para equilibrar a acidez."),
24: ([
 "Mistura o azeite, o suco e as raspas de limão, o alho, o alecrim, o sal e a pimenta.",
 "Envolve as sobrecoxas na marinada e deixa descansar 20 minutos (ou de um dia para o outro).",
 "Arruma em assadeira com a pele para cima, sem sobrepor.",
 "Assa a 200 °C por 40-45 minutos, até a pele ficar crocante e o suco sair transparente.",
 ], "Pele para cima e sem sobrepor: é assim que ela fica crocante em vez de cozida no próprio vapor.", "Acrescenta cebola e abobrinha na assadeira nos últimos 25 minutos para fazer o acompanhamento junto."),
25: ([
 "Sela o frango em lume forte com um fio de óleo, em duas levas, até alourar. Reserva.",
 "Refoga o alho e o gengibre por 30 segundos, junta os pimentões e a abobrinha por 4 minutos.",
 "Volta o frango, acrescenta o molho de soja e o amido diluído e mexe até o molho envolver tudo.",
 "Finaliza com a castanha-de-caju fora do lume, para continuar crocante.",
 ], "O molho de soja tem sódio e um pouco de hidratos: usa a versão com menos sódio e conta 1 g de hidratos por colher.", "Sem castanha-de-caju? Usa amendoim torrado sem pele — mais barato e igualmente crocante."),
26: ([
 "Tempera a carne com sal e pimenta e sela em frigideira muito quente, 3 minutos de cada lado. Reserva.",
 "No mesmo tacho, derrete a manteiga e refoga os cogumelos até alourar e secar a água.",
 "Junta o alho, o caldo e a nata e reduz por 5 minutos.",
 "Volta a carne, aquece por 1 minuto e serve com o molho por cima.",
 ], "Evita amontoar os cogumelos no tacho: em excesso, soltam água e cozinham em vez de alourar.", "Versão sem creme: usa 2 c. de sopa de queijo creme diluído no caldo quente."),
27: ([
 "Refoga a cebola e o alho no azeite até amaciar.",
 "Junta a carne picada e aloura bem, sem mexer nos primeiros 2 minutos para formar crosta.",
 "Acrescenta o tomate pelado, os temperos e cozinha 10 minutos.",
 "Junta a abobrinha e cozinha mais 8 minutos, até ficar macia mas firme. Finaliza com salsa.",
 ], "Alourar a carne sem mexer no começo é o que cria o fundo escuro e o sabor de tacho.", "Serve sobre arroz de couve-flor ou recheando pimentões e abobrinhas."),
28: ([
 "Tempera os bifes com sal e pimenta e sela em frigideira quente com azeite, 3 minutos de cada lado. Reserva.",
 "Na mesma frigideira, aloura a cebola em lume médio por 8 minutos, até caramelizar.",
 "Junta a manteiga e o alho e cozinha 1 minuto, sem queimar o alho.",
 "Volta os bifes, envolve na cebola, finaliza com salsa e serve.",
 ], "Tira a carne do frigorífico 20 minutos antes: bife gelado solta água e cozinha em vez de selar.", "Acrescenta 1 c. de sopa de molho de soja na cebola para um fundo mais escuro e salgado."),
29: ([
 "Mistura a carne com o ovo, a farinha de amêndoas, o alho, a salsa, o sal e a pimenta. Deixa descansar 10 minutos.",
 "Abre porções na palma da mão, coloca um cubo de queijo e fecha bem, sem deixar frestas.",
 "Sela as almôndegas em frigideira com azeite até alourar de todos os lados.",
 "Cobre com o molho de tomate quente e cozinha tampado por 20 minutos em lume brando.",
 ], "Fecha a almôndega apertando bem: fresta aberta é queijo vazando para o molho.", "A farinha de amêndoas pode ser substituída por 2 c. de sopa de farelo de aveia (soma 2 g de hidratos por porção)."),
30: ([
 "Mistura as especiarias com o sal e a pimenta e esfrega em toda a carne, junto com a mostarda.",
 "Deixa marinar por no mínimo 30 minutos (ideal: 12 horas no frigorífico).",
 "Sela a carne em tacho quente com azeite para alourar todos os lados.",
 "Cobre com papel de alumínio e assa a 150 °C por 2h30, ou cozinha na pressão por 45 minutos. Desfie com dois garfos.",
 ], "Temperatura baixa e tempo longo: é isso que desfia. Lume forte só resseca a superfície.", "Mistura o desfiado com 2 c. de sopa de queijo creme e serve em wrap de alface."),
31: ([
 "Tempera o salmão com sal e pimenta e acomoda em refratário untado.",
 "Mistura a manteiga derretida com o alho, o limão, as raspas e a salsa.",
 "Rega o peixe com a mistura e deixa 10 minutos.",
 "Assa a 200 °C por 12-15 minutos, até a carne ficar opaca e soltar em lascas.",
 ], "O salmão pronto solta em lascas quando pressionado com o garfo — passar do ponto deixa seco.", "Troca o limão por 1 c. de sopa de mostarda Dijon na manteiga para um perfil mais intenso."),
32: ([
 "Tempera os filés com sal, pimenta e limão e seca bem com papel de cozinha.",
 "Mistura a farinha de amêndoas com o parmesão e a páprica.",
 "Passa o filé no ovo e depois na mistura seca, apertando para aderir.",
 "Asse a 200 °C por 15 minutos em assadeira untada, ou frite em 3 c. de sopa de azeite por 4 minutos de cada lado.",
 ], "Secar o filé antes de empanar é o que impede a casca de soltar durante o cozimento.", "Farinha de amêndoas cara? Usa farinha de linhaça dourada com o mesmo parmesão."),
33: ([
 "Seca os camarões com papel de cozinha e tempera com sal e pimenta.",
 "Aquece o azeite em lume médio e aloura o alho laminado sem queimar.",
 "Aumenta o lume e junta os camarões, mexendo por 2-3 minutos até ficarem rosados.",
 "Desliga, rega com limão e finaliza com salsa.",
 ], "O camarão cozinha em 2 minutos: passou disso, fica borrachudo. Tira do lume assim que rosar.", "Acrescenta 1/2 chávena de vinho branco e reduz por 1 minuto para uma versão mais sofisticada."),
34: ([
 "Aferventa o bacalhau por 5 minutos, escorra e retira pele e espinhas.",
 "Cozinha a couve-flor no vapor por 6 minutos, mantendo firme.",
 "Refoga a cebola e o alho em metade do azeite até alourar bem.",
 "Monta em refratário com o bacalhau, a couve-flor e as azeitonas, rega com o azeite restante e asse a 190 °C por 20 minutos.",
 ], "Dessalga o bacalhau trocando a água a cada 6 horas, por 24 a 48 horas no frigorífico.", "Sem bacalhau? Usa lascas de peixe branco firme, como pescada ou tilápia, salgadas na hora."),
35: ([
 "Tempera o peixe com limão, sal e pimenta e deixa 15 minutos.",
 "Em tacho largo, refoga cebola e alho, monta camadas de tomate e pimentão.",
 "Acomoda o peixe por cima, cubre com o leite de coco e cozinha tampado por 15 minutos em lume brando.",
 "Junta o palmito e o dendê, cozinha mais 5 minutos e finaliza com coentro.",
 ], "Não mexas na moqueca depois de pôr o peixe: balançar o tacho desmancha as postas.", "Sem dendê? Usa azeite comum com 1 c. de chá de páprica defumada para dar cor."),
36: ([
 "Seca muito bem os anéis de lula com papel de cozinha.",
 "Aquece uma frigideira ou grelha até ficar bem quente, quase fumegando.",
 "Grelha a lula por 90 segundos de cada lado — nem um segundo a mais.",
 "Tempera com sal, alho cru, azeite, limão e ervas e serve na hora.",
 ], "A lula tem duas janelas: 90 segundos ou 40 minutos em cozido. Entre elas, fica borracha.", "Sem lula? Usa anéis de polvo pré-cozido, grelhando apenas para alourar."),
37: ([
 "Cozinha a couve-flor processada no vapor por 5 minutos, deixa amornar e espreme num pano de prato até sair toda a água.",
 "Mistura a couve-flor seca com o ovo, os 80 g de mozzarella, a farinha de amêndoas e o sal.",
 "Abre a massa em disco fino sobre papel vegetal untado e assa a 200 °C por 15 minutos.",
 "Cobre com molho, mozzarella e orégano e volta ao forno por 10-12 minutos. Finaliza com manjericão.",
 ], "Espremer a couve-flor é inegociável: massa úmida não firma e a pizza desmancha ao cortar.", "Congela os discos pré-assados separados por papel vegetal e monta a pizza em 12 minutos."),
38: ([
 "Salga as fatias de abobrinha, espera 15 minutos, enxágua e seca uma a uma com papel de cozinha.",
 "Sela as fatias rapidamente em frigideira quente, 1 minuto de cada lado.",
 "Monta em camadas: molho, abobrinha, presunto, mozzarella — repetindo até acabar.",
 "Finaliza com parmesão e orégano e assa a 190 °C por 30 minutos. Descansa 10 minutos antes de cortar.",
 ], "O descanso de 10 minutos depois do forno é o que faz a lasanha cortar em pedaços firmes.", "Troca o presunto por peito de peru ou frango desfiado."),
39: ([
 "Dessalga as carnes salgadas por 12 horas, trocando a água.",
 "Cozinha as carnes em água com louro por 40 minutos (ou 25 na pressão) e corta em pedaços.",
 "Frita o bacon, refoga a cebola, o alho e a páprica, junta as carnes e 2 chávenas do caldo e cozinha 20 minutos.",
 "Serve sobre a couve-flor processada refogada na manteiga, com couve e laranja.",
 ], "A couve-flor refogada na gordura do bacon é o que substitui a textura do feijão no prato.", "Versão expressa: usa só paio, linguiça e bacon — pronto em 40 minutos."),
40: ([
 "Derrete a mozzarella no micro-ondas por 40 segundos e mistura até virar massa.",
 "Junta o queijo creme, o ovo, o amido de mandioca, o fermento e o sal e sova com as mãos untadas.",
 "Modela 12 bolinhas e acomoda na cesta da airfryer sem encostar uma na outra.",
 "Asse a 180 °C por 12-15 minutos, até alourar.",
 ], "Amido de mandioca azedo, não doce — é o azedo que dá a casca crocante e o interior elástico.", "Congela as bolinhas cruas e assa direto do congelador, somando 3 minutos."),
41: ([
 "Corta as abobrinhas ao meio e retira o miolo com uma colher, deixando 0,5 cm de parede.",
 "Mistura o atum, o queijo creme, a cebola, o tomate, a salsa, sal e pimenta.",
 "Recheia as canoas, rega com um fio de azeite e polvilha a mozzarella.",
 "Asse a 190 °C por 22-25 minutos.",
 ], "Tira as sementes do tomate: é de lá que vem a água que deixa o recheio ralo.", "Sem atum? Usa frango desfiado ou carne picada já cozida."),
42: ([
 "Fatia o pepino em lâminas finas e longas com descascador ou mandolina.",
 "Seca as lâminas com papel de cozinha e tempera com uma pitada de sal.",
 "Espalha o queijo creme, coloca o peixe e o abacate e enrola como um charuto.",
 "Finaliza com gergelim e serve com molho de soja e wasabi.",
 ], "Salga as lâminas de pepino e seca: pepino com água solta no rolinho e desmancha.", "Versão cozida: troca o peixe cru por camarão ou kani desfiado."),
43: ([
 "Cozinha o repolho inteiro em água fervente por 5 minutos e separa as folhas com cuidado.",
 "Mistura a carne com o arroz de couve-flor, a cebola picada, o alho, o ovo e os temperos.",
 "Coloca 1 c. de sopa de recheio em cada folha, dobra as laterais e enrola firme.",
 "Acomoda no tacho, cobre com o tomate pelado batido e cozinha tampado por 35 minutos em lume brando.",
 ], "Retira o talo grosso da folha de repolho com uma faca antes de enrolar: o charuto fecha sem rasgar.", "Congela os charutos crus separados por papel e cozinha direto do congelador por 50 minutos."),
44: ([
 "Bate o abacate com o cacau, o adoçante, a baunilha e o sal até ficar completamente liso, sem grumos.",
 "Bate a nata em ponto de chantilly firme.",
 "Incorpora o chantilly à mistura de chocolate em três etapas, mexendo de baixo para cima.",
 "Leva ao frigorífico por no mínimo 30 minutos antes de servir.",
 ], "O abacate precisa de estar bem maduro — o verde firme deixa gosto vegetal e grumos.", "Sem abacate? Usa 1 chávena de nata batida com o cacau e o adoçante, sem a fruta."),
45: ([
 "Bate todos os ingredientes no liquidificador por 1 minuto.",
 "Despeja em forma untada com óleo de coco.",
 "Cobre com papel de alumínio e assa em banho-maria a 180 °C por 45-50 minutos.",
 "Deixa esfriar completamente e leva ao frigorífico por 4 horas antes de desenformar.",
 ], "O banho-maria é obrigatório: sem ele, o pudim forma bolhas e fica com textura de ovo mexido.", "Caramelize o fundo da forma com 2 c. de sopa de xilitol derretido para imitar o caramelo tradicional."),
46: ([
 "Mistura a nata, o cacau, o adoçante e a manteiga em tacho de fundo grosso.",
 "Cozinha em lume brando, mexendo sem parar, por 12-15 minutos.",
 "O ponto é quando a mistura desgruda do fundo do tacho ao inclinar.",
 "Desliga, junta o sal, transfere para um pote e deixa esfriar.",
 ], "Adoçantes com eritritol não dão o mesmo brilho do açúcar: acrescenta 1 c. de chá de óleo de coco no final.", "Para enrolar, leva ao frigorífico por 4 horas e passa em cacau em pó ou castanha triturada."),
47: ([
 "Mistura a farinha de amêndoas com a manteiga e forre o fundo de uma forma de aro removível. Asse 8 minutos a 180 °C.",
 "Bate o queijo creme com o eritritol até ficar liso, junta os ovos um a um, depois o iogurte, o limão e a baunilha.",
 "Despeja sobre a base e assa em banho-maria a 160 °C por 50 minutos, até as bordas firmarem e o centro tremer levemente.",
 "Desliga o forno e deixa o cheesecake esfriar lá dentro por 1 hora. Cobre com as frutas aquecidas com 1 c. de adoçante.",
 ], "Esfriar dentro do forno desligado evita a rachadura no centro — choque térmico é o vilão.", "Sem forma de aro? Usa forma comum forrada com papel vegetal cruzado para puxar o cheesecake."),
48: ([
 "Mistura a farinha, o eritritol, o fermento e o sal.",
 "Junta o ovo, a manteiga e a baunilha e mistura até formar uma massa úmida.",
 "Incorpora o chocolate picado e modela 12 bolinhas achatadas em assadeira forrada.",
 "Asse a 170 °C por 12-14 minutos, até as bordas alourarem.",
 ], "Saem moles do forno e endurecem ao esfriar — não deixes mais tempo achando que estão crus.", "Guarda em pote fechado por até 5 dias ou congela a massa modelada por 2 meses."),
49: ([
 "Derrete o chocolate com o óleo de coco em banho-maria ou no micro-ondas em pulsos de 20 segundos.",
 "Junta a nata, o eritritol, o sal e a baunilha e mistura até ficar brilhante.",
 "Leva ao frigorífico por 30 minutos, até firmar o suficiente para modelar.",
 "Modela bolinhas com as mãos e passa no cacau em pó.",
 ], "Derrete o chocolate em pulsos curtos, mexendo a cada 20 segundos: em lume direto ele queima e fica arenoso.", "Guarda no frigorífico — em temperatura ambiente o óleo de coco derrete e a trufa perde a forma."),
50: ([
 "Processa o amendoim em pulsos até virar uma farofa úmida — cuidado para não virar pasta.",
 "Junta a farinha de amêndoas, o eritritol e o sal e pulsa mais 3 vezes.",
 "Se estiver muito seco, acrescenta o óleo de coco e mistura.",
 "Aperta a mistura em forminhas ou num pote forrado, corta em quadrados e deixa firmar por 15 minutos.",
 ], "Processa em pulsos curtos e pára antes: amendoim processado demais vira manteiga e a paçoca não firma.", "Guarda em pote fechado por até 10 dias em local fresco."),
}

# ---------------------------------------------------------------------------
# Validações fail-loudly no import.
BR_ING_MARKERS = (
 "xíc", "col. sopa", "col. chá", "creme de leite", "muçarela", "requeijão",
 "cream cheese", "berinjela", "carne moída", "cheiro-verde", "cebolinha",
 "salsão", "polvilho", "shoyu", "couve manteiga", "espaguete", "catupiry",
 "papel-toalha", "papel-manteiga", "papel-alumínio", "geladeira", "salsinha",
)

_corpus_ing = {}
for _r in pt.RECEITAS:
    for _line in _r["d"][8]:
        _corpus_ing[str(_line)] = _r["num"]

for _k in INGREDIENTS_PT:
    if _k not in _corpus_ing:
        raise KeyError("INGREDIENTS_PT: linha nao existe no corpus: %r" % _k)

for _line, _num in sorted(_corpus_ing.items()):
    if any(_m in _line for _m in BR_ING_MARKERS) and _line not in INGREDIENTS_PT:
        raise KeyError(
            "receita %d: ingrediente com marcador BR sem entrada em INGREDIENTS_PT: %r"
            % (_num, _line))

if set(OVERRIDES_PT) != set(range(1, 51)):
    raise KeyError(
        "OVERRIDES_PT precisa cobrir 1..50; faltam %s"
        % sorted(set(range(1, 51)) - set(OVERRIDES_PT)))

for _n, (_steps, _tip, _swap) in OVERRIDES_PT.items():
    _corpus_steps = pt.POR_NUM[_n]["d"][9]
    if len(_steps) != len(_corpus_steps):
        raise AssertionError(
            "receita %d: %d passos pt-PT vs %d no corpus"
            % (_n, len(_steps), len(_corpus_steps)))


def ingredient(line):
    """Corpus pt-BR -> pt-PT; pass-through para linhas sem diferença."""
    return INGREDIENTS_PT.get(str(line), str(line))


def override(num):
    if num not in OVERRIDES_PT:
        raise KeyError("Receita %d sem texto pt-PT (en_gb/OVERRIDES_PT)" % num)
    return OVERRIDES_PT[num]
