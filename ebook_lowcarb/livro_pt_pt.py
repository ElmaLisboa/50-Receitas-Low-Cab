# -*- coding: utf-8 -*-
"""
50 Receitas Low Carb — português de Portugal (pt-PT).

Derivado do corpus pt-BR (livro.py + dados_receitas_*.py): seleção de 7
capítulos, intros, valores e linhas de ingrediente passam direto (texto
europeu só onde difere, via pt_pt_overrides.INGREDIENTS_PT — pass-through).
Passos, dicas e trocas das 50 receitas = OVERRIDES_PT escrito à mão
(registro TU: Refoga, Bate, Mistura — nunca o "você" brasileiro).

Labels pt-PT: Preparação / Total / Rende / Dificuldade fácil / kcal / porção /
hidratos de carbono / proteínas / gorduras boas / Ingredientes / Método /
DICA DE QUEM COZINHA / ↺ TROCA INTELIGENTE / Sumário. Lang = pt-PT.
Saídas: 50-receitas-low-carb-pt-PT.{html,pdf} — probe INGREDIENTES + MÉTODO.
Markup e classes espelham livro.py (CSS compartilhado).
"""
from html import escape as H_escape
import re

import livro as pt
import pt_pt_overrides as ov

CSS = pt.CSS

# ---------------------------------------------------------------------------
# Nomes das 50 receitas em pt-PT, na ordem do livro (índice = num-1).
NOMES_PT = [
 "Omelete de forno com espinafre e queijo",
 "Pão low carb de micro-ondas (2 minutos)",
 "Panqueca de banana com aveia (sem farinha)",
 "Muffin salgado de ovo, legumes e bacon",
 "Crepe de tapioca de frigideira com queijo e tomate",
 "Pão de queijo de frigideira",
 "Wrap de couve com frango cremoso",
 "Ovos mexidos cremosos com abacate e sementes",
 "Iogurte proteico com granola de castanhas",
 "Arroz de couve-flor simples",
 "Macarrão de abobrinha ao molho de tomate caseiro",
 "Esparguete de palmito ao alho e óleo",
 "Salada completa de frango com molho de iogurte",
 "Salada de atum com ovo e maionese de limão",
 "Wrap de alface com carne picante",
 "Escondidinho low carb de couve-flor com carne seca",
 "Lasanha de beringela à bolonhesa",
 "Beringela recheada com carne picada",
 "Caldo verde low carb (sem batata)",
 "Sopa de abóbora com leite de coco e gengibre",
 "Sopa de legumes com frango desfiado",
 "Creme de abobrinha com queijo creme",
 "Frango grelhado ao molho de mostarda e creme",
 "Sobrecoxa assada com limão e alecrim",
 "Frango xadrez low carb",
 "Filé ao molho de cogumelos",
 "Carne picada com abobrinha e tomate",
 "Bife acebolado com manteiga de alho",
 "Almôndegas recheadas com queijo em molho de tomate",
 "Costelinha de porco desfiada",
 "Salmão ao forno com manteiga de limão",
 "Tilápia empanada na farinha de amêndoas",
 "Camarão ao alho e óleo",
 "Bacalhau com couve-flor e azeitonas",
 "Moqueca de peixe com leite de coco e palmito",
 "Lula grelhada com limão e ervas",
 "Pizza de couve-flor com mozzarella e manjericão",
 "Beringela à parmegiana (sem empanar)",
 "Feijoada low carb (sem feijão)",
 "Pão de queijo de airfryer",
 "Abobrinha recheada com atum e queijo creme",
 "Sushi low carb (rolinho de pepino)",
 "Charuto de repolho com carne picada",
 "Mousse de chocolate com abacate",
 "Pudim de coco com eritritol",
 "Brigadeiro low carb de colher",
 "Cheesecake low carb de frutas vermelhas",
 "Biscoito low carb de castanhas e chocolate",
 "Trufas de chocolate com óleo de coco",
 "Paçoca low carb de amendoim",
]
assert len(NOMES_PT) == 50

PT_TO_PTPT = {r["d"][0]: NOMES_PT[i] for i, r in enumerate(pt.RECEITAS)}

# Capítulos: (título, intro) em português europeu, na ordem de pt.SELECAO.
CAPS_PT = [
 ("Pequeno-almoço e lanches rápidos",
  "Começa o dia com receitas práticas e saciantes, sem depender do pão de todos os dias. "
  "Este capítulo junta ovos, queijos, farinhas de amêndoas ou coco e frutas em porções "
  "equilibradas. A maioria das opções exige no máximo 15 minutos de preparação."),
 ("Almoços completos",
  "Pratos de tacho único, saladas que seguram a tarde e os substitutos oficiais do arroz e do "
  "macarrão — sem cara de dieta."),
 ("Sopas e caldos",
  "Para a noite fria e para o pote de levar: cremosidade sem batata e sem farinha de trigo."),
 ("Carnes e aves",
  "A carne entra sem medo, desde que o molho faça o trabalho: gordura boa, lume bem usado e "
  "tempero que não pede desculpa. Aqui ela vem dourada, suculenta e com molho bem feito — "
  "nada de frango seco de tupper."),
 ("Peixes e frutos do mar",
  "Do salmão de domingo ao bacalhau de segunda: gordura boa, preparação rápida e sabor de "
  "restaurante."),
 ("Jantares em até 30 minutos de bancada",
  "A regra da noite: o jantar fica pronto antes de a série terminar o episódio. Receitas de um "
  "tacho, uma assadeira ou uma airfryer."),
 ("Sobremesas sem açúcar",
  "Doce de verdade não precisa de açúcar refinado: cacau, coco, castanhas e adoçantes que não "
  "enganam o paladar. A regra é simples — o doce entra em quantidade certa, a proteína e a "
  "gordura boa seguram o apetite."),
]
assert len(CAPS_PT) == 7

CAPA = """
<section class="capa">
  <div class="txt">
    <div class="kicker">Série Cozinha Prática · vol. 1 · versão de Portugal</div>
    <h1>50 RECEITAS<br><span class="hl">LOW CARB</span></h1>
    <div class="sub">para o dia a dia — sem farinha, sem açúcar e sem miséria</div>
  </div>
  <div class="faixa"><span class="marca">COZINHA PRÁTICA</span><span>menos hidratos, mais vida real</span></div>
</section>"""

FRENTE = """
<section class="frente legal">
  <h2>Créditos e aviso legal</h2><div class="filete"></div>
  <p><b>50 Receitas Low Carb para o Dia a Dia</b> — 1ª edição, 2026, versão portuguesa de Portugal.<br>
  Série Cozinha Prática · volume 1.</p>
  <p>Todos os direitos reservados. É proibida a reprodução total ou parcial deste material por qualquer meio, sem autorização por escrito. Este ebook é um produto digital destinado ao comprador: partilhe apenas o link oficial de venda.</p>
  <div class="quadro"><b>AVISO IMPORTANTE:</b> as informações nutricionais (kcal, hidratos de carbono, proteínas e gorduras) são <b>estimativas por porção</b>, calculadas a partir da lista de ingredientes e de tabelas de composição de alimentos. Elas variam conforme marca, tamanho dos alimentos e utensílios. Este livro tem caráter educativo e <b>não substitui</b> orientação de médico ou nutricionista. Pessoas com diabetes, doença renal, gestantes, lactantes ou em uso contínuo de medicamentos devem consultar um profissional antes de adotar dieta com restrição de hidratos de carbono. Adoçantes como eritritol e xilitol são seguros para a maioria das pessoas em doses moderadas; em excesso podem causar desconforto digestivo. Xilitol é tóxico para cães — mantenha sobremesas fora do alcance de animais domésticos.</div>
  <p><b>Medidas usadas neste livro:</b> 1 chávena = 240 ml · 1 c. de sopa = 15 ml · 1 c. de chá = 5 ml · 1 c. de sopa rasa = sem montanha no topo · forno sempre pré-aquecido, salvo indicação contrária.</p>
  <p class="legal">Diagramação e fotos ilustrativas geradas para fins editoriais.</p>
</section>

<section class="frente">
  <h2>Bem-vindo à sua cozinha low carb</h2><div class="filete"></div>
  <p>Não compraste um livro de dieta. Compraste <b>50 respostas prontas</b> para a pergunta que derruba qualquer reeducação alimentar: <i>“o que vou comer hoje?”</i>.</p>
  <p>Low carb não é comer salada triste. É comer omelete cremoso, lasanha que corta em fatia, feijoada de domingo e até cheesecake — trocando farinha e açúcar por ingredientes que sustentam, sem passar fome e sem cozinhar duas vezes (uma para ti, outra para a família).</p>
  <p>As receitas daqui foram escolhidas por três critérios: <b>ingredientes da mercearia do bairro</b> (nada que só exista em loja de importados), <b>tempo real de quem trabalha</b> (a maioria sai em 30 minutos de bancada) e <b>sobra que resolve o dia seguinte</b>.</p>
  <div class="quadro"><b>A regra de ouro deste livro:</b> hidrato de carbono é tempero, não fundação. Ele entra para dar sabor e cor — tomate, cenoura, fruta — nunca para virar a base do prato. A base é sempre proteína + gordura boa + legume.</div>
  <p>Cozinha uma receita nova por dia durante sete semanas e, no fim, terás um repertório que nenhuma segunda-feira consegue sabotar. Bom apetite.</p>
</section>

<section class="frente">
  <h2>Como usar este livro na prática</h2><div class="filete"></div>
  <p><b>1. Começa pelo fim.</b> Abre o bónus “Menu de 7 dias” e confere a lista de compras da semana antes de ir ao supermercado. Cozinhar sem plano é o caminho mais rápido para pedir take-away à quinta-feira.</p>
  <p><b>2. Dobra a receita certa.</b> Quase toda receita de almoço e jantar rende 2 porções: a segunda é o almoço de amanhã. Low carb funciona muito melhor quando o almoço já existe.</p>
  <p><b>3. Usa as caixas.</b> Cada receita tem uma <b>Dica de quem cozinha</b> (o erro que estraga o prato) e uma <b>Troca inteligente</b> (como adaptar sem sair do low carb). Elas valem mais que a lista de ingredientes.</p>
  <p><b>4. Não corras atrás de zero hidratos de carbono.</b> O alvo realista é 60–120 g por dia, conforme o teu objetivo. Os macros de cada receita estão ali para somar, não para prender.</p>
  <p><b>5. Congela sem medo.</b> As receitas marcadas com dica de congelamento foram testadas para isso: porções individuais, pote fechado, etiqueta com data.</p>
</section>

<section class="frente">
  <h2>Substituições que salvam qualquer despensa</h2><div class="filete"></div>
  <p>Low carb é, antes de tudo, um jogo de trocas. Memoriza esta tabela e nunca mais ficas refém da farinha e do açúcar:</p>
  <table>
    <tr><th>Tira da receita</th><th>Coloca no lugar</th><th>Proporção / observação</th></tr>
    <tr><td>Açúcar refinado</td><td><b>Eritritol ou xilitol</b></td><td>1:1; xilitol adoça um pouco mais — usa 20% menos</td></tr>
    <tr><td>Farinha de trigo</td><td><b>Farinha de amêndoas + 1 ovo</b></td><td>metade da quantidade; o ovo dá a liga</td></tr>
    <tr><td>Arroz branco</td><td><b>Couve-flor processada</b></td><td>refoga crua, em lume forte, 5–6 min (receita 10)</td></tr>
    <tr><td>Macarrão</td><td><b>Abobrinha, palmito ou konjac</b></td><td>refogo de 90 s a 3 min; nunca cozinhar demais</td></tr>
    <tr><td>Batata</td><td><b>Couve-flor, nabo ou rabanete assado</b></td><td>para purês e caldos; abóbora entra com moderação</td></tr>
    <tr><td>Leite condensado</td><td><b>Leite de coco reduzido + xilitol</b></td><td>ferva 200 ml até reduzir à metade com 3 colheres de xilitol</td></tr>
    <tr><td>Ketchup / molho pronto</td><td><b>Tomate pelado + temperos</b></td><td>20 min de lume brando; o açúcar do pronto some</td></tr>
    <tr><td>Molho de soja comum</td><td><b>Molho de soja com menos sódio ou tamari</b></td><td>conta 1 g de hidratos por colher de sopa</td></tr>
  </table>
  <h2 style="margin-top:6mm">Despensa coringa: compra uma vez, usa a semana toda</h2>
  <div class="lista2"><ul>
    <li>Farinha de amêndoas e coco ralado sem açúcar</li><li>Eritritol / xilitol e cacau 100%</li>
    <li>Leite e creme de coco sem açúcar</li><li>Azeite, óleo de coco e manteiga</li>
    <li>Ovos (mínimo 1 dúzia/semana) e queijos: mozzarella, parmesão, queijo creme</li>
    <li>Nata fresca e queijo creme</li>
    <li>Couve-flor, abobrinha, beringela, repolho e couve</li>
    <li>Tomate pelado em lata e azeitonas</li>
    <li>Frango, carne picada, ovos, peixe e atum em lata</li><li>Castanhas: pará, caju, amêndoa e amendoim</li>
    <li>Alho, cebola, limão, ervas frescas e páprica defumada</li><li>Sementes de chia e linhaça dourada</li>
  </ul></div>
</section>
"""

BONUS = """
<section class="frente">
  <h2>Bónus 1 — Menu de 7 dias (com números das receitas)</h2><div class="filete"></div>
  <p>Um plano realista de primeira semana: pequeno-almoço reforçado, almoço que vira jantar e doce no lugar certo. Os números referem-se às receitas deste livro.</p>
  <table>
    <tr><th>Dia</th><th>Pequeno-almoço</th><th>Almoço</th><th>Lanche</th><th>Jantar</th></tr>
    <tr><td class="dia">Seg</td><td>01 · Omelete de forno</td><td>10 + 23 · arroz de couve-flor com frango com mostarda</td><td>09 · iogurte com granola</td><td>37 · pizza de couve-flor</td></tr>
    <tr><td class="dia">Ter</td><td>05 · crepe de tapioca</td><td>17 · lasanha de beringela</td><td>06 · pão de queijo</td><td>31 · salmão + 44 · mousse</td></tr>
    <tr><td class="dia">Qua</td><td>02 · pão de micro-ondas</td><td>11 · macarrão de abobrinha</td><td>45 · pudim de coco</td><td>35 · moqueca</td></tr>
    <tr><td class="dia">Qui</td><td>07 · wrap de couve</td><td>13 · salada completa de frango</td><td>08 · ovos com abacate</td><td>26 · filé ao molho de cogumelos</td></tr>
    <tr><td class="dia">Sex</td><td>03 · panqueca de banana</td><td>16 · escondidinho</td><td>09 · iogurte com granola</td><td>33 · camarão ao alho e óleo</td></tr>
    <tr><td class="dia">Sáb</td><td>04 · muffins salgados</td><td>18 · beringela recheada</td><td>46 · brigadeiro</td><td>42 · sushi low carb</td></tr>
    <tr><td class="dia">Dom</td><td>06 · pão de queijo</td><td>30 · costelinha desfiada</td><td>47 · cheesecake</td><td>19 · caldo verde + 28 · bife acebolado</td></tr>
  </table>
  <p class="legal">As porções devem ser ajustadas ao teu gasto calórico. Este menu é sugestão educativa, não prescrição.</p>
</section>

<section class="frente">
  <h2>Bónus 2 — Lista de compras da primeira semana</h2><div class="filete"></div>
  <p>Imprime e leva ao supermercado. Cobre os menus de segunda a domingo, para 2 pessoas:</p>
  <div class="lista2"><ul class="check">
    <li>2 dúzias de ovos</li><li>1 kg de peito de frango + 8 sobrecoxas</li>
    <li>1 kg de carne picada + 500 g de filé (alcatra/mignon)</li><li>600 g de salmão ou peixe firme + 400 g de camarão</li>
    <li>2 latas de atum</li>
    <li>500 g de mozzarella + 200 g de parmesão + queijo creme</li>
    <li>1 nata fresca (500 ml) + 1 caixinha de nata</li><li>2 vidros de leite de coco sem açúcar</li>
    <li>2 couve-flores grandes + 6 abobrinhas + 3 beringelas</li><li>1 repolho, 2 alfaces, couve portuguesa, espinafre</li>
    <li>Tomates maduros + 2 latas de tomate pelado</li>
    <li>Abacate, bananas maduras, morangos, limões</li>
    <li>Cebola, alho, gengibre, salsa, manjericão, alecrim</li><li>Azeitonas, palmito, castanhas e amendoim</li>
    <li>Farinha de amêndoas, coco ralado sem açúcar, chia</li>
    <li>Eritritol/xilitol, cacau 100%, chocolate 85%</li>
    <li>Azeite, manteiga, óleo de coco</li>
    <li>Molho de soja com menos sódio, mostarda, páprica defumada</li>
  </ul></div>
  <div class="quadro"><b>Regra da feira:</b> anda primeiro no corredor do hortifrúti e do açougue; os industrializados ficam por último e só entram se o rótulo tiver menos de 5 g de hidratos de carbono por porção.</div>
</section>

<section class="frente">
  <h2>Antes de fechar a cozinha</h2><div class="filete"></div>
  <p>Agora tens 50 receitas testadas na lógica do dia a dia: ingredientes da mercearia do bairro, um tacho só e sobra planejada. O que separa este PDF de uma vida mais leve é uma decisão pequena — <b>a próxima refeição</b>.</p>
  <p>Escolhe UMA receita desta noite, cozina-a e conta para alguém. Comida boa contada é comida repetida.</p>
  <div class="quadro"><b>PRÓXIMOS PASSOS DA SÉRIE COZINHA PRÁTICA:</b> Volume 2 — <i>Refeições Low Carb da Semana</i> (congelamento por lote) · Volume 3 — <i>Doces de Festa sem Açúcar</i>. Quem compra este ebook tem desconto de lançamento: usa o código <b>LOWCARB10</b> na página oficial.</div>
  <p>Fez uma receita? Marque <b>#50LowCarb</b> — as melhores fotos entram na próxima edição com crédito.</p>
</section>
"""

CONTRA = """
<section class="contra"><div class="in">
  <h2>Chega de começar a dieta na segunda-feira.</h2>
  <p>Este livro reúne as 50 receitas que mantêm uma família inteira no low carb sem cozinhar duas vezes: pequeno-almoço que segura a manhã, almoço que vira jantar, sopa para a noite fria e doce que não pede desculpa.</p>
  <ul>
    <li><b>50 receitas completas</b> com tempo, rendimento e macros estimados por porção;</li>
    <li><b>Dica de quem cozinha</b> em cada receita — o erro que estraga o prato e como evitar;</li>
    <li><b>Troca inteligente</b> para adaptar sem sair da dieta;</li>
    <li><b>Menu de 7 dias</b> + lista de compras pronta para imprimir;</li>
    <li><b>Tabela de substituições</b> de farinha, açúcar, arroz e macarrão.</li>
  </ul>
  <p>Ingredientes da mercearia do bairro. Tempo de quem trabalha. Sabor de quem não está “de regime”.</p>
  <div class="marca">COZINHA PRÁTICA</div>
</div></section>"""

# ---------------------------------------------------------------------------
# Receita (labels pt-PT; probe detecta INGREDIENTES + MÉTODO).
def receita_html(r):
    num, rid, d = r["num"], r["id"], r["d"]
    nome, prep, tot, porc, kcal, carb, prot, gord, ings, _passos, _dica, _troca = d
    nome = PT_TO_PTPT[nome]
    steps, dica, troca = ov.override(num)
    ing = "".join("<li>%s</li>" % H_escape(ov.ingredient(i)) for i in ings)
    pas = "".join("<li>%s</li>" % H_escape(p) for p in steps)
    return """
<section class="receita" id="%s">
  <header><div class="num">%02d</div>
    <div class="titulo"><h3>%s</h3></div></header>
  <img class="foto" src="imagens/receita-%02d.jpg" alt="%s">
  <div class="meta"><span><b>Preparação</b> %d min</span><span><b>Total</b> %d min</span><span><b>Rende</b> %s</span><span><b>Dificuldade</b> fácil</span></div>
  <div class="nutris">
    <span><b>%d</b>kcal / porção</span><span><b>%d g</b>hidratos de carbono</span>
    <span><b>%d g</b>proteínas</span><span><b>%d g</b>gorduras boas</span></div>
  <div class="corpo">
    <div><h4>Ingredientes</h4><ul class="ing">%s</ul></div>
    <div><h4>Método</h4><ol class="passos">%s</ol></div>
  </div>
  <div class="dica"><b>DICA DE QUEM COZINHA:</b> %s</div>
  <div class="troca"><b>↺ TROCA INTELIGENTE:</b> %s</div>
</section>""" % (rid, num, H_escape(nome), num, H_escape(nome), prep, tot, H_escape(str(porc)),
                 kcal, carb, prot, gord, ing, pas, H_escape(dica), H_escape(troca))


def sumario_html(pmap=None):
    out = ['<section class="frente"><h2>Sumário</h2><div class="filete"></div><div class="sum"><table>']
    idx = 0
    ci = 0
    for cat_nome, cat_intro, nomes in pt.SELECAO:
        titulo = CAPS_PT[ci][0]
        ci += 1
        out.append('<tr><td class="cat" colspan="4">%s</td></tr>' % H_escape(titulo))
        for nome in nomes:
            idx += 1
            pg = "%d" % pmap[idx] if pmap else ""
            out.append('<tr><td class="num">%02d</td><td><a href="#r%02d">%s</a></td><td class="dots"></td><td class="pg">%s</td></tr>'
                       % (idx, idx, H_escape(PT_TO_PTPT[nome]), pg))
    out.append("</table></div></section>")
    return "".join(out)


def corpo_html():
    out = []
    ci = 0
    for cap_num, (cat_nome, cat_intro, nomes) in enumerate(pt.SELECAO, 1):
        titulo, intro = CAPS_PT[ci]
        ci += 1
        out.append('<section class="abre"><img class="capfoto" src="imagens/capitulo-%02d.jpg" alt="Imagem do capítulo %s"><div class="tag">Capítulo %02d</div><h2>%s</h2><div class="filete"></div><p>%s</p></section>'
                   % (cap_num, H_escape(titulo), cap_num, H_escape(titulo), H_escape(intro)))
        for r in pt.RECEITAS:
            if r["cat"] == cat_nome:
                out.append(receita_html(r))
    return "".join(out)


def render_html(pmap=None):
    return ("<!DOCTYPE html><html lang='pt-PT'><head><meta charset='utf-8'><style>%s</style></head><body>%s%s%s%s%s%s</body></html>"
            % (CSS, CAPA, FRENTE, sumario_html(pmap), corpo_html(), BONUS, CONTRA))


def build():
    from weasyprint import HTML
    import pymupdf as fitz

    # 1) probe -> pmap (páginas das receitas: INGREDIENTES + MÉTODO)
    # filename= dá base_url p/ imagens relativas (mesmo esquema do corpus)
    open("ebook_pt_pt_probe.html", "w", encoding="utf-8").write(render_html(None))
    HTML(filename="ebook_pt_pt_probe.html").write_pdf("ebook_pt_pt_probe.pdf")
    doc = fitz.open("ebook_pt_pt_probe.pdf")
    pmap = {}
    for i in range(doc.page_count):
        txt = doc[i].get_text()
        norm = re.sub(r"\s+", "", txt).upper()  # h4 tem letter-spacing
        if "INGREDIENTES" in norm and "MÉTODO" in norm:
            for ln in txt.splitlines():
                m = re.match(r"^(\d{2})$", ln.strip())
                if m:
                    pmap[int(m.group(1))] = i + 1
                    break
    doc.close()
    print("probe pmap:", len(pmap), "receitas")
    # 2) render final com páginas do sumário
    html = render_html(pmap)
    with open("50-receitas-low-carb-pt-PT.html", "w", encoding="utf-8") as f:
        f.write(html)
    HTML(filename="50-receitas-low-carb-pt-PT.html").write_pdf("50-receitas-low-carb-pt-PT.pdf")
    # 3) conferência
    doc = fitz.open("50-receitas-low-carb-pt-PT.pdf")
    mapeadas = 0
    for i in range(doc.page_count):
        txt = doc[i].get_text()
        norm = re.sub(r"\s+", "", txt).upper()  # h4 tem letter-spacing
        if "INGREDIENTES" in norm and "MÉTODO" in norm:
            for ln in txt.splitlines():
                if re.match(r"^(\d{2})$", ln.strip()):
                    mapeadas += 1
                    break
    doc.close()
    print("PDF em português de Portugal gerado: 50 receitas mapeadas" if mapeadas == 50
          else "AVISO: %d receitas mapeadas" % mapeadas)


if __name__ == "__main__":
    build()
