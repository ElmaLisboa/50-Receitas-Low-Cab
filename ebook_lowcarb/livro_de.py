# -*- coding: utf-8 -*-
"""Deutsche Ausgabe von 50 Low-Carb-Rezepte für den Alltag."""
import html as H
import re
import livro as pt
import livro_en as layout

NAMES = [
 "Ofenomelett mit Spinat und Käse", "Low-Carb-Mikrowellenbrot in 2 Minuten", "Bananen-Hafer-Pfannkuchen ohne Mehl",
 "Herzhafte Ei-, Gemüse- und Speck-Muffins", "Tapioka-Crepe aus der Pfanne mit Käse und Tomate", "Käsebrot aus der Pfanne",
 "Cremiger Hähnchen-Wrap mit Blattkohl", "Cremiges Rührei mit Avocado und Samen", "Protein-Joghurt mit Nuss-Granola",
 "Einfacher Blumenkohlreis", "Zucchini-Nudeln mit hausgemachter Tomatensoße", "Palmherzen-Nudeln mit Knoblauch und Öl",
 "Kompletter Hähnchensalat mit Joghurt-Dressing", "Thunfischsalat mit Ei und Zitronen-Mayonnaise", "Scharfer Hackfleisch-Salat-Wrap",
 "Blumenkohlauflauf mit gezupftem Trockenfleisch", "Auberginen-Lasagne Bolognese", "Gefüllte Aubergine mit Hackfleisch",
 "Low-Carb-Grünkohlsuppe ohne Kartoffeln", "Kürbissuppe mit Kokosmilch und Ingwer", "Gemüsesuppe mit gezupftem Hähnchen",
 "Cremige Zucchinisuppe mit Frischkäse", "Gegrilltes Hähnchen mit Senf-Sahne-Soße", "Ofen-Hähnchenschenkel mit Zitrone und Rosmarin",
 "Low-Carb-Hähnchenpfanne", "Steak mit Pilzsoße", "Hackfleisch mit Zucchini und Tomate",
 "Steak mit Zwiebeln und Knoblauchbutter", "Käsegefüllte Hackbällchen in Tomatensoße", "Gezupfte Schweinerippchen",
 "Ofenlachs mit Zitronenbutter", "Tilapia mit Mandelkruste", "Knoblauchgarnelen", "Kabeljau mit Blumenkohl und Oliven",
 "Fisch-Moqueca mit Kokosmilch und Palmherzen", "Gegrillter Tintenfisch mit Zitrone und Kräutern",
 "Blumenkohl-Pizza mit Mozzarella und Basilikum", "Aubergine alla Parmigiana ohne Panade", "Low-Carb-Feijoada ohne Bohnen",
 "Käsebrot aus der Heißluftfritteuse", "Mit Thunfisch und Frischkäse gefüllte Zucchini", "Low-Carb-Sushi mit Gurkenrollen",
 "Kohlrouladen mit Hackfleisch", "Schokoladen-Avocado-Mousse", "Kokosflan mit Erythrit",
 "Low-Carb-Schokoladencreme zum Löffeln", "Low-Carb-Cheesecake mit Beeren", "Low-Carb-Nuss-Schokoladen-Cookies",
 "Schokoladentrüffel mit Kokosöl", "Low-Carb-Erdnuss-Konfekt nach Paçoca-Art"
]

CAT = {
 "Café da manhã e lanches rápidos": ("Frühstück und schnelle Snacks", "Starte mit praktischen, sättigenden Rezepten in den Tag, ganz ohne klassisches Brot. Dieses Kapitel vereint Eier, Käse, Mandel- oder Kokosmehl und Obst in ausgewogenen Portionen. Die meisten Optionen brauchen höchstens 15 Minuten aktive Zubereitungszeit."),
 "Almoços completos": ("Komplette Mittagessen", "Einfache Gerichte aus einem Topf, Salate, die bis zum Nachmittag satt halten, und clevere Alternativen zu Reis und Pasta — ohne nach Diät zu schmecken."),
 "Sopas e caldos": ("Suppen und Brühen", "Für kalte Abende und zum Mitnehmen: cremiger Genuss ohne Kartoffeln und Weizenmehl."),
 "Carnes e aves": ("Fleisch und Geflügel", "Protein ist die Grundlage einer guten Low-Carb-Ernährung: goldbraun, saftig und mit echten Soßen — niemals trockenes Meal-Prep-Hähnchen."),
 "Peixes e frutos do mar": ("Fisch und Meeresfrüchte", "Vom Sonntagslachs bis zur schnellen Mahlzeit unter der Woche: gute Fette, kurze Zubereitung und Restaurantgeschmack."),
 "Jantares em até 30 minutos de bancada": ("Abendessen in 30 Minuten", "Die Regel für den Abend: Das Essen ist fertig, bevor die Folge endet. Rezepte aus einer Pfanne, einem Blech oder der Heißluftfritteuse."),
 "Sobremesas sem açúcar": ("Zuckerfreie Desserts", "Ein echtes Dessert braucht keinen raffinierten Zucker: Kakao, Kokos, Nüsse und Süßungsmittel, die deinen Gaumen nicht täuschen."),
}

# Deutsch wird NICHT durch lexikalische Substitution erzeugt. Das alte
# translate_text() ließ Portugiesisch in den Zutaten stehen ("600 g von Fisch
# firme in postas", "1 vidro von Palmherzen in Scheiben") und erzeugte in den
# Schritten unlesbaren Mischtext ("Rühre nicht die moqueca danach von colocar
# der Fisch: balançar die Pfanne desmancha die postas"). Deutsch verlangt
# Kasus, Zusammensetzungen und Wortstellung, die kein Regex-Verfahren liefert.
# Alles kommt aus zwei endlichen, von Hand geprüften Tabellen in de_overrides:
#   INGREDIENTS : exakte Entsprechung der 258 Zutatenzeilen des Korpus;
#   OVERRIDES   : Zubereitung, Küchentipp und intelligenter Tausch der 50
#                 Rezepte (Imperativ du, konsistent mit dem FRONT).
# Eine fehlende Zeile lässt den Build scheitern statt Portugiesisch
# durchzulassen.
from de_overrides import INGREDIENTS, OVERRIDES

def ingredient(line):
    s = str(line)
    if s not in INGREDIENTS:
        raise KeyError("Zutatenzeile ohne deutsche Übersetzung: %r" % s)
    return INGREDIENTS[s]

def override(num):
    if num not in OVERRIDES:
        raise KeyError("Rezept %d ohne deutschen Text (de_overrides.OVERRIDES)" % num)
    return OVERRIDES[num]

PT_TO_DE = {r["d"][0]: NAMES[r["num"] - 1] for r in pt.RECEITAS}
RECIPES = []
for r in pt.RECEITAS:
    d = r["d"]; name, prep, total, servings, kcal, carbs, protein, fat, ingredients, steps, tip, swap = d
    passos, dica, troca = override(r["num"])
    assert len(passos) == len(steps), "receita %d: %d passos em alemão para %d em português" % (r["num"], len(passos), len(steps))
    RECIPES.append({"num": r["num"], "id": r["id"], "cat": CAT[r["cat"]][0], "d": (PT_TO_DE[name], prep, total, servings, kcal, carbs, protein, fat, [ingredient(x) for x in ingredients], passos, dica, troca)})
SELECTION = []
for cat_pt, intro_pt, names in pt.SELECAO:
    cat_de, intro_de = CAT[cat_pt]; SELECTION.append((cat_de, intro_de, [PT_TO_DE[n] for n in names]))

CSS = layout.CSS.replace("50 Low-Carb Recipes for Everyday Life", "50 Low-Carb-Rezepte für den Alltag") + "\n@page { margin-bottom: 6mm; } .dica { padding: 2mm 3mm; margin-top: 1.5mm; font-size: 7.7pt; } .troca { padding: 0.8mm 3mm; margin-top: 0.8mm; font-size: 7.3pt; line-height: 1.3; }"
FRONT = """
<section class="frente legal"><h2>Impressum und rechtliche Hinweise</h2><div class="filete"></div><p><b>50 Low-Carb-Rezepte für den Alltag</b> — 1. Ausgabe, 2026.<br>Serie Praktische Küche · Band 1.</p><p>Alle Rechte vorbehalten. Die vollständige oder teilweise Vervielfältigung dieses Materials ist ohne schriftliche Genehmigung untersagt. Dieses Ebook ist ein digitales Produkt für den Käufer.</p><div class="quadro"><b>WICHTIGER HINWEIS:</b> Die Nährwertangaben (Kalorien, Kohlenhydrate, Eiweiß und Fett) sind <b>Schätzwerte pro Portion</b>. Sie können je nach Marke, Größe der Zutaten und Küchengeräten abweichen. Dieses Buch dient der Information und <b>ersetzt keine</b> Beratung durch Arzt oder Ernährungsfachkraft. Menschen mit Diabetes, Nierenerkrankungen, Schwangere, Stillende und Personen, die dauerhaft Medikamente einnehmen, sollten vor einer kohlenhydratreduzierten Ernährung fachlichen Rat einholen. Xylit ist für Hunde giftig — Desserts mit Xylit von Haustieren fernhalten.</div><p><b>Maße in diesem Buch:</b> 1 Tasse = 240 ml · 1 EL = 15 ml · 1 TL = 5 ml · Esslöffel nicht gehäuft · Ofen immer vorheizen, sofern nicht anders angegeben.</p></section>
<section class="frente"><h2>Willkommen in deiner Low-Carb-Küche</h2><div class="filete"></div><p>Du hast kein Diätbuch gekauft. Du hast <b>50 fertige Antworten</b> auf die Frage gekauft, die jede Ernährungsumstellung ins Wanken bringen kann: <i>„Was koche ich heute?“</i>.</p><p>Low Carb bedeutet nicht traurige Salate. Es bedeutet cremiges Omelett, schnittfeste Lasagne, Feijoada am Sonntag und sogar Cheesecake — mit Zutaten, die satt machen, ohne zwei verschiedene Gerichte kochen zu müssen.</p><div class="quadro"><b>Die goldene Regel dieses Buches:</b> Kohlenhydrate sind Akzente, nicht die Grundlage. Die Grundlage sind immer Eiweiß, gute Fette und Gemüse.</div><p>Eine neue Rezeptidee pro Tag für sieben Wochen — und du hast ein Repertoire, das jeden Montag retten kann. Guten Appetit.</p></section>
<section class="frente"><h2>So verwendest du dieses Buch</h2><div class="filete"></div><p><b>1. Beginne am Ende.</b> Prüfe den Bonus „7-Tage-Menü“ und die Einkaufsliste, bevor du einkaufst.</p><p><b>2. Koche die richtige Menge.</b> Die meisten Mittag- und Abendessen ergeben zwei Portionen: Die zweite ist das Mittagessen für morgen.</p><p><b>3. Nutze die Kästen.</b> Jedes Rezept enthält einen <b>Küchentipp</b> und einen <b>Intelligenten Tausch</b>.</p><p><b>4. Suche nicht nach null Kohlenhydraten.</b> Die Nährwerte helfen bei der Auswahl, sie sollen Essen nicht zur Belastung machen.</p><p><b>5. Friere ohne Bedenken ein.</b> Die Hinweise zum Einfrieren sind für Einzelportionen und geschlossene Behälter gedacht.</p></section>
<section class="frente"><h2>Clevere Zutaten-Tausche</h2><div class="filete"></div><p>Low Carb bedeutet auch, Zutaten geschickt zu ersetzen:</p><table><tr><th>Weglassen</th><th>Stattdessen</th><th>Hinweis</th></tr><tr><td>Raffinierter Zucker</td><td><b>Erythrit oder Xylit</b></td><td>1:1; Xylit ist etwas süßer</td></tr><tr><td>Weizenmehl</td><td><b>Mandelmehl + 1 Ei</b></td><td>die Hälfte verwenden; Ei bindet</td></tr><tr><td>Weißer Reis</td><td><b>Blumenkohlreis</b></td><td>roh bei hoher Hitze 5–6 Minuten braten</td></tr><tr><td>Pasta</td><td><b>Zucchini, Palmherzen oder Konjak</b></td><td>90 Sekunden bis 3 Minuten braten</td></tr><tr><td>Kartoffel</td><td><b>Blumenkohl, Rübe oder Radieschen</b></td><td>für Püree und Brühen</td></tr></table><h2 style="margin-top:6mm">Grundausstattung</h2><div class="lista2"><ul><li>Mandelmehl und ungesüßte Kokosraspeln</li><li>Erythrit oder Xylit und 100% Kakao</li><li>Ungesüßte Kokosmilch und Sahne</li><li>Olivenöl, Kokosöl und Butter</li><li>Eier, Mozzarella, Parmesan und Frischkäse</li><li>Blumenkohl, Zucchini, Aubergine, Kohl und Grünkohl</li><li>Geschälte Tomaten aus der Dose und Oliven</li><li>Hähnchen, Hackfleisch, Fisch und Thunfisch</li><li>Nüsse, Zitronen, frische Kräuter und geräuchertes Paprikapulver</li></ul></div></section>
"""
BONUS = """
<section class="frente"><h2>Bonus 1 — 7-Tage-Menü</h2><div class="filete"></div><p>Ein realistischer Plan für die erste Woche: sättigendes Frühstück, Mittagessen als Abendessen und ein Dessert zur passenden Zeit.</p><table><tr><th>Tag</th><th>Frühstück</th><th>Mittagessen</th><th>Snack</th><th>Abendessen</th></tr><tr><td class="dia">Mo</td><td>01 · Ofenomelett</td><td>10 + 23 · Blumenkohlreis mit Hähnchen</td><td>09 · Joghurt-Granola</td><td>37 · Blumenkohl-Pizza</td></tr><tr><td class="dia">Di</td><td>05 · Tapioka-Crepe</td><td>17 · Auberginen-Lasagne</td><td>06 · Käsebrot</td><td>31 · Lachs + 44 · Mousse</td></tr><tr><td class="dia">Mi</td><td>02 · Mikrowellenbrot</td><td>11 · Zucchini-Nudeln</td><td>45 · Kokosflan</td><td>35 · Fisch-Moqueca</td></tr><tr><td class="dia">Do</td><td>07 · Blattkohl-Wrap</td><td>13 · Hähnchensalat</td><td>08 · Avocado-Eier</td><td>26 · Steak mit Pilzen</td></tr><tr><td class="dia">Fr</td><td>03 · Bananenpfannkuchen</td><td>16 · Blumenkohlauflauf</td><td>09 · Joghurt-Granola</td><td>33 · Knoblauchgarnelen</td></tr><tr><td class="dia">Sa</td><td>04 · Herzhafte Muffins</td><td>18 · Gefüllte Aubergine</td><td>46 · Schokoladencreme</td><td>42 · Low-Carb-Sushi</td></tr><tr><td class="dia">So</td><td>06 · Käsebrot</td><td>30 · Schweinerippchen</td><td>47 · Cheesecake</td><td>19 · Grünkohlsuppe + 28 · Steak</td></tr></table><p class="legal">Portionen an die eigenen Bedürfnisse anpassen. Dieser Plan ist keine medizinische Verordnung.</p></section>
<section class="frente"><h2>Bonus 2 — Einkaufsliste für die erste Woche</h2><div class="filete"></div><p>Ausdrucken und mit zum Einkauf nehmen. Für zwei Personen:</p><div class="lista2"><ul class="check"><li>2 Dutzend Eier</li><li>1 kg Hähnchenbrust + 8 Schenkel</li><li>1 kg Hackfleisch + 500 g Steak</li><li>600 g Lachs oder fester Fisch + 400 g Garnelen</li><li>2 Dosen Thunfisch</li><li>500 g Mozzarella + Parmesan + Frischkäse</li><li>Sahne</li><li>2 Packungen ungesüßte Kokosmilch</li><li>Blumenkohl, Zucchini, Aubergine, Kohl und Grünkohl</li><li>Tomaten + 2 Dosen geschälte Tomaten</li><li>Avocado, Bananen, Erdbeeren und Zitronen</li><li>Zwiebeln, Knoblauch, Ingwer, Kräuter und Paprikapulver</li><li>Oliven, Palmherzen, Nüsse und Erdnüsse</li><li>Mandelmehl, Kokosraspeln und Chiasamen</li><li>Erythrit oder Xylit, Kakao und 85% Schokolade</li><li>Olivenöl, Butter und Kokosöl</li><li>Sojasoße und Senf</li></ul></div></section>
<section class="frente"><h2>Bevor du die Küche schließt</h2><div class="filete"></div><p>Du hast jetzt 50 Rezepte für den Alltag: leicht erhältliche Zutaten, einfache Zubereitung und geplante Reste. Der Unterschied zwischen diesem Ebook und einer besser organisierten Woche ist eine kleine Entscheidung: <b>deine nächste Mahlzeit</b>.</p><p>Wähle ein Rezept für heute Abend, bereite es zu und teile es mit jemandem. Gemeinsam essen macht Wiederholen leichter.</p><div class="quadro"><b>WEITERE BÄNDE VON PRAKTISCHE KÜCHE:</b> Band 2 — <i>Low-Carb-Mahlzeiten für die Woche</i> · Band 3 — <i>Zuckerfreie Party-Desserts</i>.</div></section>
"""
COVER = """<section class="capa"><div class="txt"><div class="kicker">Serie Praktische Küche · Band 1</div><h1>50 REZEPTE<br><span class="hl">LOW CARB</span></h1><div class="sub">für den Alltag — ohne Mehl, ohne Zucker, ohne Verzicht</div></div><div class="faixa"><span class="marca">PRAKTISCHE KÜCHE</span><span>weniger Kohlenhydrate, mehr echtes Leben</span></div></section>"""
BACK = """<section class="contra"><div class="in"><h2>Hör auf, jeden Montag neu anzufangen.</h2><p>Dieses Buch vereint 50 Rezepte für eine Low-Carb-Routine ohne doppelt zu kochen: Frühstück, das satt macht, Mittagessen als Abendessen, Suppen für kalte Abende und Desserts ohne schlechtes Gewissen.</p><ul><li><b>50 vollständige Rezepte</b> mit Zeit, Menge und geschätzten Nährwerten pro Portion;</li><li><b>Küchentipp</b> zu jedem Rezept;</li><li><b>Intelligenter Tausch</b> für flexible Zutaten;</li><li><b>7-Tage-Menü</b> und druckbare Einkaufsliste;</li><li><b>Tabelle für Zutaten-Tausche</b> bei Mehl, Zucker, Reis und Pasta.</li></ul><p>Einfache Zutaten. Realistische Zeit. Geschmack für Menschen, die sich nicht wie auf Diät fühlen wollen.</p><div class="marca">PRAKTISCHE KÜCHE</div></div></section>"""

def recipe_html(r):
    num, rid, d = r["num"], r["id"], r["d"]; name, prep, total, servings, kcal, carbs, protein, fat, ingredients, steps, tip, swap = d
    ing = ''.join('<li>%s</li>' % H.escape(x) for x in ingredients); pas = ''.join('<li>%s</li>' % H.escape(x) for x in steps)
    return '<section class="receita" id="%s"><header><div class="num">%02d</div><div class="titulo"><h3>%s</h3></div></header><img class="foto" src="imagens/receita-%02d.jpg" alt="%s"><div class="meta"><span><b>Zubereitung</b> %d Min.</span><span><b>Gesamt</b> %d Min.</span><span><b>Ergibt</b> %s</span><span><b>Schwierigkeit</b> einfach</span></div><div class="nutris"><span><b>%d</b>kcal / Portion</span><span><b>%d g</b>Kohlenhydrate</span><span><b>%d g</b>Eiweiß</span><span><b>%d g</b>Fett</span></div><div class="corpo"><div><h4>Zutaten</h4><ul class="ing">%s</ul></div><div><h4>Zubereitung</h4><ol class="passos">%s</ol></div></div><div class="dica"><b>KÜCHENTIPP:</b> %s</div><div class="troca"><b>↺ INTELLIGENTER TAUSCH:</b> %s</div></section>' % (rid, num, H.escape(name), num, H.escape(name), prep, total, H.escape(str(servings)), kcal, carbs, protein, fat, ing, pas, H.escape(tip), H.escape(swap))

def toc_html(pmap=None):
    out=['<section class="frente"><h2>Inhalt</h2><div class="filete"></div><div class="sum"><table>']; idx=0
    for cat,intro,names in SELECTION:
        out.append('<tr><td class="cat" colspan="4">%s</td></tr>' % H.escape(cat))
        for name in names:
            idx+=1; pg=str(pmap[idx]) if pmap else ''; out.append('<tr><td class="num">%02d</td><td><a href="#r%02d">%s</a></td><td class="dots"></td><td class="pg">%s</td></tr>'%(idx,idx,H.escape(name),pg))
    out.append('</table></div></section>'); return ''.join(out)

def body_html():
    out=[]
    for chapter,(cat,intro,names) in enumerate(SELECTION,1):
        out.append('<section class="abre"><img class="capfoto" src="imagens/capitulo-%02d.jpg" alt="Bild für %s"><div class="tag">Kapitel %02d</div><h2>%s</h2><div class="filete"></div><p>%s</p></section>'%(chapter,H.escape(cat),chapter,H.escape(cat),H.escape(intro)))
        for r in RECIPES:
            if r["cat"]==cat: out.append(recipe_html(r))
    return ''.join(out)

def render(pmap=None): return "<!DOCTYPE html><html lang='de'><head><meta charset='utf-8'><style>%s</style></head><body>%s%s%s%s%s%s</body></html>"%(CSS,COVER,FRONT,toc_html(pmap),body_html(),BONUS,BACK)

def build():
    from weasyprint import HTML
    import fitz
    open('ebook_de_probe.html','w').write(render(None)); HTML(filename='ebook_de_probe.html').write_pdf('ebook_de_probe.pdf')
    d=fitz.open('ebook_de_probe.pdf'); pmap={}
    for i in range(d.page_count):
        text=d[i].get_text(); norm=text.replace(' ','')
        if 'ZUTATEN' in norm and 'ZUBEREITUNG' in norm:
            m=re.search(r'(?m)^(\d{2})\n',text)
            if m and 1<=int(m.group(1))<=50: pmap[int(m.group(1))]=i+1
    assert len(pmap)==50,(len(pmap),sorted(set(range(1,51))-set(pmap)))
    open('50-low-carb-rezepte-de.html','w').write(render(pmap)); HTML(filename='50-low-carb-rezepte-de.html').write_pdf('50-low-carb-rezepte-de.pdf')
    print('Deutsche PDF erstellt:',len(pmap),'Rezepte mit Seitenzuordnung')

if __name__=='__main__': build()
