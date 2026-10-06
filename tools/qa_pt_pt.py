#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QA do ebook pt-PT: estrutura HTML, resíduo brasileiro (=0), marcadores
europeus (>0), extração de texto (pypdfium2), fontes (fitz), delta vs corpus
e contagem de páginas. Espelha tools/qa_en_gb.py (17 checks)."""
import re, sys, html as H

BASE = '/home/user/50-Receitas-Low-Cab/ebook_lowcarb'
sys.path.insert(0, BASE)
HTML_F = f'{BASE}/50-receitas-low-carb-pt-PT.html'
PDF_F = f'{BASE}/50-receitas-low-carb-pt-PT.pdf'

ok = True
def chk(label, cond, detail=""):
    global ok
    print(("  OK   " if cond else "  FAIL ") + label + (f" :: {detail}" if detail else ""))
    if not cond: ok = False

# Marcadores brasileiros (pt-BR) que NÃO podem sobrar em texto pt-PT.
BR = [
 r'geladeira', r'\bfreezer\b', r'\bpanela\b', r'\bfogo\b', r'\bdourar\b', r'\bdoure\b',
 r'\bdourando\b', r'\bdourarem\b', r'creme de leite', r'x[íi]c\b', r'col\. sopa', r'col\. ch[áa]',
 r'cheiro-verde', r'papel-toalha', r'papel-manteiga', r'papel-alum[íi]nio', r'sals[ãa]o\b',
 r'berinjela', r'mu[çc]arela', r'requeij[ãa]o', r'cream cheese', r'carne mo[íi]da',
 r'card[áa]pio', r'\bb[ôo]nus\b', r'caf[ée] da manh[ãa]', r'voc[êe]', r'\bdelivery\b',
 r'marmita', r'espiralizador', r'\bcuringa\b', r'catupiry', r'shoyu', r'\bmarrom\b',
 r'ao sugo', r'\bcookie', r'crepioca', r'\bzip\b', r'p[ãa]o franc[êe]s', r'polvilho',
 r'espaguete', r'cebolinha', r'salsinha', r'uvas-passas', r'\bwhey\b', r'milho-verde',
 r'\bmanteca\b', r'fub[áa]',
]

PTPT = ['pequeno-almo[çc]o', r'hidratos de carbono', r'frigor[íi]fico', r'\blume\b',
 r'\btacho\b', r'\bnata\b', r'mozzarella', r'beringela', r'queijo creme', r'ch[áa]vena',
 r'c\. de sopa', r'c\. de ch[áa]', r'alourar', r'papel de cozinha', r'papel vegetal',
 r'\bb[óo]nus\b', r'\bmenu\b', r'take-away', r'\bcoringa\b', r'molho de soja', r'\baipo\b',
 r'cebolinho', r'\bsalsa\b', r'couve portuguesa', r'espiralador', r'Prepara[çc][ãa]o',
 r'M[ée]todo', r'Sum[áa]rio', r'\bRefoga\b', r'\bBate\b', r'\bTempera\b', r'\bServe\b']

def scan(txt, pats):
    return {p: len(re.findall(p, txt, flags=re.I)) for p in pats if re.search(p, txt, flags=re.I)}

# ---------------------------------------------------------------- HTML
src = open(HTML_F, encoding='utf-8').read()
txt = re.sub(r'<style[^>]*>.*?</style>', ' ', src, flags=re.S)
txt = re.sub(r'<[^>]+>', ' ', txt); txt = H.unescape(txt)

print("== HTML ==")
chk("50 seções receita", len(re.findall(r'<section class="receita"', src)) == 50)
ids = re.findall(r'<section class="receita" id="r(\d+)"', src)
chk("ids r01..r50", ids == [f"{i:02d}" for i in range(1, 51)])
hits = scan(txt, BR)
chk("zero marcadores BR no HTML", not hits, str(hits))
miss = [p for p in PTPT if not re.search(p, txt, flags=re.I)]
chk("marcadores pt-PT presentes no HTML", not miss, str(miss))
chk("lang pt-PT", "lang='pt-PT'" in src)
chk("labels: Preparação + Método + hidratos", all(
    w in txt for w in ('Preparação', 'Método', 'hidratos de carbono')))
chk("sumário com páginas preenchidas (pmap)",
    len(re.findall(r'<td class="pg">\d+</td>', src)) == 50,
    str(len(re.findall(r'<td class="pg">\d+</td>', src))))

# ---------------------------------------------------------------- PDF
print("== PDF (extração) ==")
import pymupdf
import pypdfium2 as pdfium

d = pymupdf.open(PDF_F)
n = d.page_count
recipe_pages = []
for i in range(n):
    t = d[i].get_text().replace(' ', '')
    if 'INGREDIENTES' in t and 'MÉTODO' in t:
        recipe_pages.append(i + 1)
chk("páginas com Ingredientes+Método = 50", len(recipe_pages) == 50, f"{len(recipe_pages)}")
chk("≥ 60 páginas totais", n >= 60, str(n))

pdf = pdfium.PdfDocument(PDF_F)
all_txt = "".join(pdf[i].get_textpage().get_text_range() for i in range(len(pdf)))
norm = re.sub(r'\s+', ' ', all_txt)
br_pdf = scan(norm, BR)
chk("zero marcadores BR no PDF extraído", not br_pdf, str(br_pdf))
miss_pdf = [p for p in PTPT if not re.search(p, norm, flags=re.I)]
chk("marcadores pt-PT presentes no PDF", not miss_pdf, str(miss_pdf))
chk("↺ TROCA INTELIGENTE x50", all_txt.count('↺') == 50, str(all_txt.count('↺')))
chk("DICA DE QUEM COZINHA x50", all_txt.count('DICA DE QUEM COZINHA') == 50,
    str(all_txt.count('DICA DE QUEM COZINHA')))
chk("Preparação x50 no PDF", all_txt.count('Preparação') == 50, str(all_txt.count('Preparação')))
chk("spot-check passo pt-PT", 'Refoga a cebola no azeite por 3 minutos' in norm)
flat = re.sub(r'\s+', '', norm).lower()  # capa/h4 saem com letter-spacing
chk("capa versão portugal", 'versãodeportugal' in flat and 'menoshidratos' in flat)

print("== Fontes ==")
fonts = set()
for i in range(n):
    for f in d[i].get_fonts():
        fonts.add(f[3])
print("   ", sorted(fonts))
chk("fontes embutidas presentes", len(fonts) >= 1)
chk("DejaVu cobre o template", any('DejaVu' in f for f in fonts), str(sorted(fonts)))

# ---------------------------------------------------------------- delta vs corpus
print("== Delta vs corpus pt-BR ==")
import pt_pt_overrides as ov
import livro as ptl
chk("keys INGREDIENTS_PT ⊆ corpus", all(
    k in {str(l) for r in ptl.RECEITAS for l in r["d"][8]} for k in ov.INGREDIENTS_PT),
    f"{len(ov.INGREDIENTS_PT)} chaves")
chk("OVERRIDES cobre 1..50", set(ov.OVERRIDES_PT) == set(range(1, 51)))
counts_ok = all(len(ov.OVERRIDES_PT[n][0]) == len(ptl.POR_NUM[n]["d"][9]) for n in range(1, 51))
chk("contagem de passos == corpus (50/50)", counts_ok)
diff_ing = sum(1 for k in ov.INGREDIENTS_PT if ov.INGREDIENTS_PT[k] != k)
print(f"    linhas de ingrediente adaptadas: {diff_ing}/{len(ov.INGREDIENTS_PT)} | "
      f"receitas com texto europeu: {len(ov.OVERRIDES_PT)}/50")
chk("delta ingrediente não vazio", diff_ing > 50)

print("\nRESULTADO:", "TUDO OK ✓" if ok else "FALHAS ✗")
sys.exit(0 if ok else 1)
