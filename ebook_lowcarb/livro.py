# -*- coding: utf-8 -*-
"""Monta o ebook '50 Receitas Low Carb para o Dia a Dia' em HTML + PDF (WeasyPrint)."""
import html as H
from dados_receitas_1 import CAFE, ALMOCO, SOPAS
from dados_receitas_2 import CARNES, PEIXES
from dados_receitas_3 import JANTARES, SOBREMESAS

TODAS = {r[0]: r for r in CAFE + ALMOCO + SOPAS + CARNES + PEIXES + JANTARES + SOBREMESAS}

# Seleção final: 50 receitas na ordem do livro
SELECAO = [
 ("Café da manhã e lanches rápidos",
  "Comece o dia com receitas práticas e saciantes, sem depender do pão francês. Este capítulo reúne ovos, queijos, farinhas de amêndoas ou coco e frutas em porções equilibradas. A maioria das opções exige até 15 minutos de preparo ativo.",
  ["Omelete de forno com espinafre e queijo",
   "Pão low carb de micro-ondas (2 minutos)",
   "Panqueca de banana com aveia (sem farinha)",
   "Muffin salgado de ovo, legumes e bacon",
   "Crepioca de frigideira com queijo e tomate",
   "Pão de queijo de frigideira",
   "Wrap de couve com frango cremoso",
   "Ovos mexidos cremosos com abacate e sementes",
   "Iogurte proteico com granola de castanhas"]),
 ("Almoços completos",
  "Pratos de panela única, saladas que seguram a tarde e os substitutos oficiais do arroz e do macarrão — sem cara de dieta.",
  ["Arroz de couve-flor simples",
   "Macarrão de abobrinha ao molho de tomate caseiro",
   "Espaguete de palmito ao alho e óleo",
   "Salada completa de frango com molho de iogurte",
   "Salada de atum com ovo e maionese de limão",
   "Wrap de alface com carne moída picante",
   "Escondidinho low carb de couve-flor com carne seca",
   "Lasanha de berinjela à bolonhesa",
   "Berinjela recheada com carne moída"]),
 ("Sopas e caldos",
  "Para a noite fria e para a marmita: cremosidade sem batata e sem farinha de trigo.",
  ["Caldo verde low carb (sem batata)",
   "Sopa de abóbora com leite de coco e gengibre",
   "Sopa de legumes com frango desfiado",
   "Creme de abobrinha com cream cheese"]),
 ("Carnes e aves",
  "Proteína é o alicerce do low carb bem feito: aqui ela vem dourada, molhada e com molho de verdade — nada de frango seco de marmita.",
  ["Frango grelhado ao molho de mostarda e creme",
   "Sobrecoxa assada com limão e alecrim",
   "Frango xadrez low carb",
   "Filé ao molho de cogumelos",
   "Carne moída com abobrinha e tomate",
   "Bife acebolado com manteiga de alho",
   "Almôndegas recheadas com queijo ao sugo",
   "Costelinha de porco desfiada"]),
 ("Peixes e frutos do mar",
  "Do salmão de domingo à sardinha de segunda: gordura boa, preparo rápido e sabor de restaurante.",
  ["Salmão ao forno com manteiga de limão",
   "Tilápia empanada na farinha de amêndoas",
   "Camarão ao alho e óleo",
   "Bacalhau com couve-flor e azeitonas",
   "Moqueca de peixe com leite de coco e palmito",
   "Lula grelhada com limão e ervas"]),
 ("Jantares em até 30 minutos de bancada",
  "A regra da noite: o jantar fica pronto antes de a série terminar o episódio. Receitas de uma panela, uma assadeira ou uma airfryer.",
  ["Pizza de couve-flor com muçarela e manjericão",
   "Berinjela à parmegiana (sem empanar)",
   "Feijoada low carb (sem feijão)",
   "Pão de queijo de airfryer",
   "Abobrinha recheada com atum e requeijão",
   "Sushi low carb (rolinho de pepino)",
   "Charuto de repolho com carne moída"]),
 ("Sobremesas sem açúcar",
  "Doce de verdade não precisa de açúcar refinado: cacau, coco, castanhas e adoçantes que não enganam o paladar.",
  ["Mousse de chocolate com abacate",
   "Pudim de coco com eritritol",
   "Brigadeiro low carb de colher",
   "Cheesecake low carb de frutas vermelhas",
   "Cookie low carb de castanhas e chocolate",
   "Trufas de chocolate com óleo de coco",
   "Paçoca low carb de amendoim"]),
]

# Numeração sequencial 01-50 + ids
RECEITAS = []  # dicts com num, id, cat, dados
n = 0
for cat_nome, cat_intro, nomes in SELECAO:
    for nome in nomes:
        n += 1
        RECEITAS.append({"num": n, "id": "r%02d" % n, "cat": cat_nome, "d": TODAS[nome]})
assert len(RECEITAS) == 50, len(RECEITAS)
POR_NUM = {r["num"]: r for r in RECEITAS}

CSS = """
@page { size: 165mm 240mm; margin: 15mm 13mm 10mm 15mm;
  @bottom-right { content: counter(page); font: 7.5pt 'DejaVu Sans'; color: #8a8a8a; }
  @bottom-left  { content: "50 Receitas Low Carb para o Dia a Dia"; font: 7.5pt 'DejaVu Sans'; color: #8a8a8a; } }
@page capa { margin: 0; @bottom-right { content: none; } @bottom-left { content: none; }
  background: linear-gradient(rgba(12,17,15,0.78), rgba(12,17,15,0.2) 40%, rgba(12,17,15,0) 52%, rgba(12,17,15,0.45) 90%), url('capa_fundo.jpg') center/cover no-repeat; }
@page contra { margin: 0; @bottom-right { content: none; } @bottom-left { content: none; } background: #16261e; }

* { box-sizing: border-box; }
body { font-family: 'DejaVu Sans'; font-size: 8.6pt; line-height: 1.55; color: #26221c; }
h1, h2, h3 { font-family: 'DejaVu Serif'; color: #1e3d2f; }

/* ---- CAPA ---- */
.capa { page: capa; }
.capa .txt { position: absolute; top: 26mm; left: 12mm; right: 12mm; color: #fff; }
.capa .kicker { font: 700 9pt 'DejaVu Sans'; letter-spacing: 3pt; color: #d9b64a; text-transform: uppercase; }
.capa h1 { color: #fff; font-size: 30pt; line-height: 1.08; margin: 4mm 0 2mm; font-weight: 700; }
.capa h1 .hl { color: #d9b64a; }
.capa .sub { font: 12pt 'DejaVu Serif'; font-style: italic; color: #f2ede2; }
.capa .faixa { position: absolute; bottom: 22mm; left: 12mm; right: 12mm; border-top: 1px solid rgba(255,255,255,.5); padding-top: 3mm;
  color: #f2ede2; font: 8.5pt 'DejaVu Sans'; display: flex; justify-content: space-between; }
.capa .marca { letter-spacing: 2pt; font-weight: 700; }

/* ---- contracapa ---- */
.contra { page: contra; color: #efe9dc; }
.contra .in { position: absolute; top: 20mm; left: 15mm; right: 15mm; bottom: 16mm; }
.contra h2 { color: #d9b64a; font-size: 15pt; margin: 0 0 5mm; }
.contra p, .contra li { font-size: 9pt; }
.contra ul { padding-left: 5mm; }
.contra .marca { margin-top: 8mm; font-weight: 700; letter-spacing: 2pt; font-size: 9pt; color:#d9b64a }

/* ---- frentes de texto ---- */
.frente { break-before: page; }
.frente h2 { font-size: 15pt; margin: 0 0 4mm; }
.frente .filete { width: 22mm; height: 1mm; background: #c9a227; margin: 0 0 5mm; }
p { margin: 0 0 3mm; }
.quadro { background: #f4efe3; border-left: 3px solid #c9a227; padding: 4mm 5mm; margin: 4mm 0; }
.quadro b { color: #1e3d2f; }
.legal { font-size: 7.6pt; color: #6b675f; }
table { width: 100%; border-collapse: collapse; font-size: 8.2pt; margin: 3mm 0; }
th { font-family: 'DejaVu Serif'; color: #1e3d2f; text-align: left; border-bottom: 1.2px solid #1e3d2f; padding: 1.5mm 1mm; }
td { border-bottom: 0.4px solid #cfc9bb; padding: 1.6mm 1mm; vertical-align: top; }
td b { color: #1e3d2f; }

/* ---- sumário ---- */
.sum { margin-top: 3mm; }
.sum table { width: 100%; border-collapse: collapse; }
.sum td { border: none; padding: 0 0 1.8mm 0; font-size: 8.3pt; vertical-align: bottom; }
.sum td.num { color: #c9a227; font-weight: 700; width: 8mm; }
.sum td.dots { border-bottom: 1px dotted #9a9484; }
.sum td.pg { text-align: right; font-weight: 700; color: #1e3d2f; width: 9mm; padding-left: 2mm; }
.sum td.cat { font: 700 10pt 'DejaVu Serif'; color: #1e3d2f; padding: 4mm 0 1.5mm 0; }
.sum a { text-decoration: none; color: #26221c; }
.marcador { font-size: 1pt; color: rgba(0,0,0,0); }

/* ---- abertura de categoria ---- */
.abre { break-before: page; padding-top: 18mm; }
.abre .capfoto { display: block; width: 125mm; height: 78mm; object-fit: cover; margin: 0 auto 8mm; border-radius: 2mm; border: 0.5px solid #ded8ca; }
.abre .tag { font: 700 8pt 'DejaVu Sans'; letter-spacing: 2.5pt; color: #c9a227; text-transform: uppercase; }
.abre h2 { font-size: 21pt; line-height: 1.12; margin: 3mm 0 4mm; }
.abre .filete { width: 26mm; height: 1.2px; background: #c9a227; margin-bottom: 5mm; }
.abre p { font-size: 9.5pt; max-width: 118mm; }

/* ---- receita ---- */
.receita { break-before: page; }
.receita header { display: flex; align-items: baseline; gap: 4mm; padding: 0; margin: 0 0 3mm; min-height: 0; }
.receita .num { font: 700 24pt 'DejaVu Serif'; color: #c9a227; line-height: 1; }
.receita .titulo { flex: 1; min-width: 0; overflow: visible; }
.receita h3 { font-size: 12.5pt; line-height: 1.2; margin: 0; overflow: visible; word-break: normal; overflow-wrap: normal; }
.receita .foto { display: block; width: 110mm; height: 66mm; object-fit: cover; margin: 2mm auto 2mm; border-radius: 1.5mm; border: 0.5px solid #ded8ca; }
.receita .meta { display: flex; justify-content: center; align-items: baseline; gap: 5mm; border-bottom: 1.2px solid #1e3d2f; padding: 0 0 3.5mm; margin: 0 0 4mm; font-size: 8pt; line-height: 1.2; color: #6b675f; text-align: center; }
.receita .meta span { white-space: nowrap; }
.receita .meta b { color: #1e3d2f; }
.receita .corpo { display: grid; grid-template-columns: 52mm 1fr; gap: 6mm; }
.receita h4 { font: 700 8.2pt 'DejaVu Sans'; letter-spacing: 1.5pt; text-transform: uppercase; color: #1e3d2f; margin: 0 0 2mm; }
.receita ul.ing { list-style: none; margin: 0; padding: 0; font-size: 8.2pt; }
.receita ul.ing li { padding: 0 0 1.6mm 4mm; position: relative; }
.receita ul.ing li::before { content: ""; position: absolute; left: 0; top: 1.9mm; width: 2mm; height: 2mm; background: #c9a227; }
.receita ol.passos { margin: 0; padding: 0; list-style: none; counter-reset: p; font-size: 8.4pt; }
.receita ol.passos li { counter-increment: p; padding: 0 0 2.4mm 8mm; position: relative; }
.receita ol.passos li::before { content: counter(p); position: absolute; left: 0; top: 0.2mm; width: 5.6mm; height: 5.6mm; border-radius: 50%;
  background: #1e3d2f; color: #fff; font-size: 7.4pt; font-weight: 700; display: flex; align-items: center; justify-content: center; }
.nutris { display: flex; gap: 2mm; margin: 3.5mm 0; }
.nutris span { flex: 1; text-align: center; background: #f4efe3; padding: 1.6mm 0; font-size: 7.6pt; }
.nutris b { display: block; font-size: 9.5pt; color: #1e3d2f; }
.dica { background: #f4efe3; border-left: 3px solid #c9a227; padding: 2.8mm 3.5mm; font-size: 8pt; margin-top: 2.5mm; }
.dica b { color: #1e3d2f; }
.troca { border: 1px dashed #7d947f; border-radius: 2mm; padding: 1.5mm 3.2mm; font-size: 7.7pt; line-height: 1.35; margin-top: 1.5mm; color: #33473a; }

/* ---- bônus ---- */
.menu td.dia { font-weight: 700; color: #1e3d2f; white-space: nowrap; }
.lista2 { columns: 2; column-gap: 7mm; font-size: 8.2pt; }
.lista2 li { margin-bottom: 1.2mm; }
.check li::marker { color: #c9a227; }
"""

def receita_html(r, markers=True):
    num, rid, d = r["num"], r["id"], r["d"]
    nome, prep, tot, porc, kcal, carb, prot, gord, ings, passos, dica, troca = d
    marc = '<span class="marcador">@@%s@@</span>' % rid if markers else ""
    ing = "".join("<li>%s</li>" % H.escape(i) for i in ings)
    pas = "".join("<li>%s</li>" % H.escape(p) for p in passos)
    return """
<section class="receita" id="%s">%s
  <header><div class="num">%02d</div>
    <div class="titulo"><h3>%s</h3></div></header>
  <img class="foto" src="imagens/receita-%02d.jpg" alt="%s">
  <div class="meta"><span><b>Preparo</b> %d min</span><span><b>Total</b> %d min</span><span><b>Rende</b> %s</span><span><b>Dificuldade</b> fácil</span></div>
  <div class="nutris">
    <span><b>%d</b>kcal / porção</span><span><b>%d g</b>carboidratos</span>
    <span><b>%d g</b>proteínas</span><span><b>%d g</b>gorduras boas</span></div>
  <div class="corpo">
    <div><h4>Ingredientes</h4><ul class="ing">%s</ul></div>
    <div><h4>Modo de preparo</h4><ol class="passos">%s</ol></div>
  </div>
  <div class="dica"><b>DICA DE QUEM COZINHA:</b> %s</div>
  <div class="troca"><b>↺ TROCA INTELIGENTE:</b> %s</div>
</section>""" % (rid, marc, num, H.escape(nome), num, H.escape(nome), prep, tot, H.escape(str(porc)),
                 kcal, carb, prot, gord, ing, pas, H.escape(dica), H.escape(troca))

def sumario_html(pmap=None):
    out = ['<section class="frente"><h2>Sumário</h2><div class="filete"></div><div class="sum"><table>']
    idx = 0
    for cat_nome, cat_intro, nomes in SELECAO:
        out.append('<tr><td class="cat" colspan="4">%s</td></tr>' % H.escape(cat_nome))
        for nome in nomes:
            idx += 1
            pg = "%d" % pmap[idx] if pmap else ""
            out.append('<tr><td class="num">%02d</td><td><a href="#r%02d">%s</a></td><td class="dots"></td><td class="pg">%s</td></tr>'
                       % (idx, idx, H.escape(nome), pg))
    out.append("</table></div></section>")
    return "".join(out)

def corpo_html(markers=True):
    out = []
    for cap_num, (cat_nome, cat_intro, nomes) in enumerate(SELECAO, 1):
        out.append('<section class="abre"><img class="capfoto" src="imagens/capitulo-%02d.jpg" alt="Imagem do capítulo %s"><div class="tag">Capítulo %02d</div><h2>%s</h2><div class="filete"></div><p>%s</p></section>'
                   % (cap_num, H.escape(cat_nome), cap_num, H.escape(cat_nome), H.escape(cat_intro)))
        for r in RECEITAS:
            if r["cat"] == cat_nome:
                out.append(receita_html(r, markers=markers))
    return "".join(out)

FRENTE = """
<section class="frente legal">
  <h2>Créditos e aviso legal</h2><div class="filete"></div>
  <p><b>50 Receitas Low Carb para o Dia a Dia</b> — 1ª edição, 2026.<br>
  Série Cozinha Prática · volume 1.</p>
  <p>Todos os direitos reservados. É proibida a reprodução total ou parcial deste material por qualquer meio, sem autorização por escrito. Este ebook é um produto digital destinado ao comprador: compartilhe apenas o link oficial de venda.</p>
  <div class="quadro"><b>AVISO IMPORTANTE:</b> as informações nutricionais (kcal, carboidratos, proteínas e gorduras) são <b>estimativas por porção</b>, calculadas a partir da lista de ingredientes e de tabelas de composição de alimentos. Elas variam conforme marca, tamanho dos alimentos e utensílios. Este livro tem caráter educativo e <b>não substitui</b> orientação de médico ou nutricionista. Pessoas com diabetes, doença renal, gestantes, lactantes ou em uso contínuo de medicamentos devem consultar um profissional antes de adotar dieta com restrição de carboidratos. Adoçantes como eritritol e xilitol são seguros para a maioria das pessoas em doses moderadas; em excesso podem causar desconforto digestivo. Xilitol é tóxico para cães — mantenha sobremesas fora do alcance de pets.</div>
  <p><b>Medidas usadas neste livro:</b> 1 xíc. = 240 ml · 1 col. sopa = 15 ml · 1 col. chá = 5 ml · 1 col. sopa rasa = sem montanha no topo · forno sempre pré-aquecido, salvo indicação contrária.</p>
  <p class="legal">Diagramação e fotos ilustrativas geradas para fins editoriais.</p>
</section>

<section class="frente">
  <h2>Bem-vindo à sua cozinha low carb</h2><div class="filete"></div>
  <p>Você não comprou um livro de dieta. Comprou <b>50 respostas prontas</b> para a pergunta que derruba qualquer reeducação alimentar: <i>“o que eu faço de comer hoje?”</i>.</p>
  <p>Low carb não é comer salada triste. É comer omelete cremoso, lasanha que corta em fatia, feijoada de domingo e até cheesecake — trocando farinha e açúcar por ingredientes que sustentam, sem passar fome e sem cozinhar duas vezes (uma comida para você, outra para a família).</p>
  <p>As receitas daqui foram escolhidas por três critérios: <b>ingredientes de mercado de bairro</b> (nada que só exista em loja de importados), <b>tempo real de gente que trabalha</b> (a maioria sai em 30 minutos de bancada) e <b>sobra que resolve o dia seguinte</b>.</p>
  <div class="quadro"><b>A regra de ouro deste livro:</b> carboidrato é tempero, não fundação. Ele entra para dar sabor e cor — tomate, cenoura, fruta — nunca para virar a base do prato. A base é sempre proteína + gordura boa + legume.</div>
  <p>Cozinhe uma receita nova por dia durante sete semanas e, no fim, você terá um repertório que nenhuma segunda-feira consegue sabotar. Bom apetite.</p>
</section>

<section class="frente">
  <h2>Como usar este livro na prática</h2><div class="filete"></div>
  <p><b>1. Comece pelo fim.</b> Abra o bônus “Cardápio de 7 dias” e confira a lista de compras da semana antes de ir ao mercado. Cozinhar sem plano é o jeito mais rápido de pedir delivery na quinta-feira.</p>
  <p><b>2. Dobre a receita certa.</b> Quase toda receita de almoço e jantar rende 2 porções: a segunda é o almoço de amanhã. Low carb funciona muito melhor quando o almoço já existe.</p>
  <p><b>3. Use as caixas.</b> Cada receita tem uma <b>Dica de quem cozinha</b> (o erro que estraga o prato) e uma <b>Troca inteligente</b> (como adaptar sem sair do low carb). Elas valem mais que a lista de ingredientes.</p>
  <p><b>4. Não persiga zero carboidrato.</b> O alvo realista é 60–120 g por dia, conforme seu objetivo. As macros de cada receita estão ali para somar, não para aprisionar.</p>
  <p><b>5. Congele sem medo.</b> As receitas marcadas com dica de congelamento foram testadas para isso: porções individuais, pote fechado, etiqueta com data.</p>
</section>

<section class="frente">
  <h2>Substituições que salvam qualquer despensa</h2><div class="filete"></div>
  <p>Low carb é, antes de tudo, um jogo de trocas. Memorize esta tabela e você nunca mais fica refém da farinha e do açúcar:</p>
  <table>
    <tr><th>Tira da receita</th><th>Coloca no lugar</th><th>Proporção / observação</th></tr>
    <tr><td>Açúcar refinado</td><td><b>Eritritol ou xilitol</b></td><td>1:1; xilitol adoça um pouco mais — use 20% menos</td></tr>
    <tr><td>Farinha de trigo</td><td><b>Farinha de amêndoas + 1 ovo</b></td><td>metade da quantidade; o ovo dá a liga</td></tr>
    <tr><td>Arroz branco</td><td><b>Couve-flor processada</b></td><td>refogue crua, em fogo alto, 5–6 min (receita 10)</td></tr>
    <tr><td>Macarrão</td><td><b>Abobrinha, palmito ou konjac</b></td><td>refogo de 90 s a 3 min; nunca cozinhar demais</td></tr>
    <tr><td>Batata</td><td><b>Couve-flor, nabo ou rabanete assado</b></td><td>para purês e caldos; abóbora entra com moderação</td></tr>
    <tr><td>Leite condensado</td><td><b>Leite de coco reduzido + xilitol</b></td><td>ferva 200 ml até reduzir à metade com 3 col. de xilitol</td></tr>
    <tr><td>Ketchup / molho pronto</td><td><b>Tomate pelado + temperos</b></td><td>20 min de fogo baixo; o açúcar do pronto some</td></tr>
    <tr><td>Shoyu comum</td><td><b>Shoyu com menos sódio ou tamari</b></td><td>conte 1 g de carbo por colher de sopa</td></tr>
  </table>
  <h2 style="margin-top:6mm">Despensa curinga: compre uma vez, use a semana toda</h2>
  <div class="lista2"><ul>
    <li>Farinha de amêndoas e coco ralado sem açúcar</li><li>Eritritol / xilitol e cacau 100%</li>
    <li>Leite e creme de coco sem açúcar</li><li>Azeite, óleo de coco e manteiga</li>
    <li>Ovos (mínimo 1 dúzia/semana) e queijos: muçarela, parmesão, requeijão</li>
    <li>Creme de leite fresco e cream cheese</li>
    <li>Couve-flor, abobrinha, berinjela, repolho e couve</li>
    <li>Tomate pelado em lata e azeitonas</li>
    <li>Frango, carne moída, ovos, peixe e atum em lata</li><li>Castanhas: pará, caju, amêndoa e amendoim</li>
    <li>Alho, cebola, limão, ervas frescas e páprica defumada</li><li>Sementes de chia e linhaça dourada</li>
  </ul></div>
</section>
"""

BONUS = """
<section class="frente">
  <h2>Bônus 1 — Cardápio de 7 dias (com números das receitas)</h2><div class="filete"></div>
  <p>Um plano realista de primeira semana: café reforçado, almoço que vira janta e doce no lugar certo. Os números referem-se às receitas deste livro.</p>
  <table>
    <tr><th>Dia</th><th>Café da manhã</th><th>Almoço</th><th>Lanche</th><th>Jantar</th></tr>
    <tr><td class="dia">Seg</td><td>01 · Omelete de forno</td><td>10 + 23 · arroz de couve-flor com frango ao mostarda</td><td>09 · iogurte com granola</td><td>37 · pizza de couve-flor</td></tr>
    <tr><td class="dia">Ter</td><td>05 · crepioca</td><td>17 · lasanha de berinjela</td><td>06 · pão de queijo</td><td>31 · salmão + 44 · mousse</td></tr>
    <tr><td class="dia">Qua</td><td>02 · pão de micro-ondas</td><td>11 · macarrão de abobrinha</td><td>46 · pudim de coco</td><td>35 · moqueca</td></tr>
    <tr><td class="dia">Qui</td><td>07 · wrap de couve</td><td>13 · salada completa de frango</td><td>08 · ovos com abacate</td><td>26 · filé ao molho de cogumelos</td></tr>
    <tr><td class="dia">Sex</td><td>03 · panqueca de banana</td><td>16 · escondidinho</td><td>09 · iogurte com granola</td><td>33 · camarão ao alho e óleo</td></tr>
    <tr><td class="dia">Sáb</td><td>04 · muffins salgados</td><td>18 · berinjela recheada</td><td>47 · brigadeiro</td><td>42 · sushi low carb</td></tr>
    <tr><td class="dia">Dom</td><td>06 · pão de queijo</td><td>30 · costelinha desfiada</td><td>48 · cheesecake</td><td>19 · caldo verde + 28 · bife acebolado</td></tr>
  </table>
  <p class="legal">As porções devem ser ajustadas ao seu gasto calórico. Este cardápio é sugestão educativa, não prescrição.</p>
</section>

<section class="frente">
  <h2>Bônus 2 — Lista de compras da primeira semana</h2><div class="filete"></div>
  <p>Imprima e leve ao mercado. Cobre os cardápios de segunda a domingo, para 2 pessoas:</p>
  <div class="lista2"><ul class="check">
    <li>2 dúzias de ovos</li><li>1 kg de peito de frango + 8 sobrecoxas</li>
    <li>1 kg de carne moída + 500 g de filé (alcatra/mignon)</li><li>600 g de salmão ou peixe firme + 400 g de camarão</li>
    <li>2 latas de atum</li><li>500 g de muçarela + 200 g de parmesão + requeijão + cream cheese</li>
    <li>1 creme de leite fresco (500 ml) + 1 lata de creme de leite</li><li>2 vidros de leite de coco sem açúcar</li>
    <li>2 couve-flores grandes + 6 abobrinhas + 3 berinjelas</li><li>1 repolho, 2 alfaces, couve manteiga, espinafre</li>
    <li>Tomates maduros + 2 latas de tomate pelado</li><li>Abacate, bananas maduras, morangos, limões</li>
    <li>Cebola, alho, gengibre, cheiro-verde, manjericão, alecrim</li><li>Azeitonas, palmito, castanhas e amendoim</li>
    <li>Farinha de amêndoas, coco ralado sem açúcar, chia</li><li>Eritritol/xilitol, cacau 100%, chocolate 85%</li>
    <li>Azeite, manteiga, óleo de coco</li><li>Shoyu com menos sódio, mostarda, páprica defumada</li>
  </ul></div>
  <div class="quadro"><b>Regra da feira:</b> ande primeiro o corredor de hortifrúti e açougue; os industrialados ficam por último e só entram se o rótulo tiver menos de 5 g de carboidrato por porção.</div>
</section>

<section class="frente">
  <h2>Antes de fechar a cozinha</h2><div class="filete"></div>
  <p>Você agora tem 50 receitas testadas na lógica do dia a dia: ingredientes de mercado de bairro, uma panela só e sobra planejada. O que separa este PDF de uma vida mais leve é uma decisão pequena — <b>a próxima refeição</b>.</p>
  <p>Escolha UMA receita desta noite, faça e conte para alguém. Comida boa contada é comida repetida.</p>
  <div class="quadro"><b>PRÓXIMOS PASSOS DA SÉRIE COZINHA PRÁTICA:</b> Volume 2 — <i>Marmitas Low Carb da Semana</i> (congelamento por lote) · Volume 3 — <i>Doces de Festa sem Açúcar</i>. Quem compra este ebook tem desconto de lançamento: use o código <b>LOWCARB10</b> na página oficial.</div>
  <p>Fez uma receita? Marque <b>#50LowCarb</b> — as melhores fotos entram na próxima edição com crédito.</p>
</section>
"""

CAPA = """
<section class="capa">
  <div class="txt">
    <div class="kicker">Série Cozinha Prática · vol. 1</div>
    <h1>50 RECEITAS<br><span class="hl">LOW CARB</span></h1>
    <div class="sub">para o dia a dia — sem farinha, sem açúcar e sem miséria</div>
  </div>
  <div class="faixa"><span class="marca">COZINHA PRÁTICA</span><span>menos carboidrato, mais vida real</span></div>
</section>"""

CONTRA = """
<section class="contra"><div class="in">
  <h2>Chega de começar a dieta na segunda-feira.</h2>
  <p>Este livro reúne as 50 receitas que mantêm uma família inteira no low carb sem cozinhar duas vezes: café que segura a manhã, almoço que vira jantar, sopa para a noite fria e doce que não pede desculpa.</p>
  <ul>
    <li><b>50 receitas completas</b> com tempo, rendimento e macros estimadas por porção;</li>
    <li><b>Dica de quem cozinha</b> em cada receita — o erro que estraga o prato e como evitar;</li>
    <li><b>Troca inteligente</b> para adaptar sem sair da dieta;</li>
    <li><b>Cardápio de 7 dias</b> + lista de compras pronta para imprimir;</li>
    <li><b>Tabela de substituições</b> de farinha, açúcar, arroz e macarrão.</li>
  </ul>
  <p>Ingredientes de mercado de bairro. Tempo de gente que trabalha. Sabor de quem não está “de regime”.</p>
  <div class="marca">COZINHA PRÁTICA</div>
</div></section>"""

def render_html(pmap=None, markers=True):
    return ("<!DOCTYPE html><html lang='pt-BR'><head><meta charset='utf-8'><style>%s</style></head><body>%s%s%s%s%s%s</body></html>"
            % (CSS, CAPA, FRENTE, sumario_html(pmap), corpo_html(markers), BONUS, CONTRA))

def build():
    import re
    import fitz as pymupdf
    from weasyprint import HTML
    # passe 1: sonda sem marcadores para descobrir a página real de cada receita.
    # A identificação usa os títulos de seção exclusivos da página da receita;
    # assim, a troca de layout não cria deslocamentos artificiais no sumário.
    open("probe.html", "w").write(render_html(None, False))
    HTML(filename="probe.html").write_pdf("probe.pdf")
    d = pymupdf.open("probe.pdf")
    pmap = {}
    for i in range(d.page_count):
        text = d[i].get_text()
        if "INGREDIENTES" in text.replace(" ", "") and "MODODEPREPARO" in text.replace(" ", ""):
            m = re.search(r"(?m)^(\d{2})\n", text)
            if m and 1 <= int(m.group(1)) <= 50:
                pmap[int(m.group(1))] = i + 1
    assert len(pmap) == 50, (len(pmap), sorted(set(range(1, 51)) - set(pmap)))
    # passe 2: versão final com páginas reais no sumário
    open("ebook.html", "w").write(render_html(pmap, False))
    HTML(filename="ebook.html").write_pdf("50-receitas-low-carb.pdf")
    print("PDF gerado. Páginas no sumário:", {k: pmap[k] for k in sorted(pmap)})

if __name__ == "__main__":
    build()
