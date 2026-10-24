#!/usr/bin/env python3
"""Renderiza um manuscrito de bônus culinário em PDF A4 ilustrado.

O locale é inferido pelo nome do arquivo (por exemplo, ``pt-BR.md``). As fotos
são associadas pelo prefixo numérico (01_*.jpg, 02_*.jpg, ...). Para Hindi e
japonês/chinês, informe também as fontes Noto com --script-fonts-dir.
"""
from __future__ import annotations

import argparse
import html
import re
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

from PIL import Image, ImageOps
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

PAGE_W, PAGE_H = A4
MARGIN = 42
CONTENT_W = PAGE_W - 2 * MARGIN
DARK = HexColor("#233E34")
GREEN = HexColor("#55735F")
SAGE = HexColor("#EAF0E9")
CREAM = HexColor("#F7F4ED")
GOLD = HexColor("#B7834B")
TEXT = HexColor("#29332E")
MUTED = HexColor("#65716A")
LINE = HexColor("#DDE3DC")


# Copy follows the field labels used in each localized Markdown manuscript.
LOCALES: Dict[str, Dict[str, str]] = {
    "pt-BR": {
        "bonus": "BÔNUS 1", "edition": "Português do Brasil",
        "exclusive": "EDIÇÃO EXCLUSIVA", "recipes_word": "RECEITAS",
        "guide": "GUIA COMPLEMENTAR", "intro_title": "Sobre este caderno",
        "before": "Antes de começar", "contents": "SUMÁRIO",
        "contents_title": "Receitas neste caderno",
        "contents_note": "Os números à direita indicam a página da receita no PDF.",
        "yield": "Rendimento:", "time": "Tempo de preparo:",
        "pairing": "Combina com:", "storage": "Conservação:",
        "ingredients": "Ingredientes", "steps": "Modo de preparo",
    },
    "pt-PT": {
        "bonus": "BÓNUS 1", "edition": "Português de Portugal",
        "exclusive": "EDIÇÃO EXCLUSIVA", "recipes_word": "RECEITAS",
        "guide": "GUIA COMPLEMENTAR", "intro_title": "Sobre este caderno",
        "before": "Antes de começar", "contents": "ÍNDICE",
        "contents_title": "Receitas deste caderno",
        "contents_note": "Os números à direita indicam a página da receita no PDF.",
        "yield": "Rendimento:", "time": "Tempo de preparação:",
        "pairing": "Combina com:", "storage": "Conservação:",
        "ingredients": "Ingredientes", "steps": "Preparação",
    },
    "es": {
        "bonus": "BONO 1", "edition": "Español",
        "exclusive": "EDICIÓN EXCLUSIVA", "recipes_word": "RECETAS",
        "guide": "GUÍA COMPLEMENTARIA", "intro_title": "Sobre este cuaderno",
        "before": "Antes de empezar", "contents": "ÍNDICE",
        "contents_title": "Recetas de este cuaderno",
        "contents_note": "Los números de la derecha indican la página de la receta en el PDF.",
        "yield": "Rendimiento:", "time": "Tiempo de preparación:",
        "pairing": "Combina con:", "storage": "Conservación:",
        "ingredients": "Ingredientes", "steps": "Preparación",
    },
    "nl-NL": {
        "bonus": "BONUS 1", "edition": "Nederlands",
        "exclusive": "EXCLUSIEVE EDITIE", "recipes_word": "RECEPTEN",
        "guide": "EXTRA GIDS", "intro_title": "Over dit boekje",
        "before": "Voordat je begint", "contents": "INHOUD",
        "contents_title": "Recepten in dit boekje",
        "contents_note": "De getallen rechts geven de paginanummers van de recepten in de PDF aan.",
        "yield": "Opbrengst:", "time": "Bereidingstijd:",
        "pairing": "Lekker bij:", "storage": "Bewaren:",
        "ingredients": "Ingrediënten", "steps": "Bereiding",
    },
    "en-GB": {
        "bonus": "BONUS 1", "edition": "English (UK)",
        "exclusive": "EXCLUSIVE EDITION", "recipes_word": "RECIPES",
        "guide": "BONUS GUIDE", "intro_title": "About this booklet",
        "before": "Before you begin", "contents": "CONTENTS",
        "contents_title": "Recipes in this booklet",
        "contents_note": "The numbers on the right show each recipe’s page in the PDF.",
        "yield": "Makes:", "time": "Preparation time:",
        "pairing": "Pairs with:", "storage": "Storage:",
        "ingredients": "Ingredients", "steps": "Method",
    },
    "en-US": {
        "bonus": "BONUS 1", "edition": "English (US)",
        "exclusive": "EXCLUSIVE EDITION", "recipes_word": "RECIPES",
        "guide": "BONUS GUIDE", "intro_title": "About this booklet",
        "before": "Before you begin", "contents": "CONTENTS",
        "contents_title": "Recipes in this booklet",
        "contents_note": "The numbers on the right show each recipe’s page in the PDF.",
        "yield": "Makes:", "time": "Preparation time:",
        "pairing": "Pairs with:", "storage": "Storage:",
        "ingredients": "Ingredients", "steps": "Method",
    },
    "it-IT": {
        "bonus": "BONUS 1", "edition": "Italiano",
        "exclusive": "EDIZIONE ESCLUSIVA", "recipes_word": "RICETTE",
        "guide": "GUIDA DEL BONUS", "intro_title": "Questo quaderno",
        "before": "Prima di iniziare", "contents": "INDICE",
        "contents_title": "Ricette in questo quaderno",
        "contents_note": "I numeri a destra indicano la pagina della ricetta nel PDF.",
        "yield": "Porzioni:", "time": "Tempo di preparazione:",
        "pairing": "Si abbina a:", "storage": "Conservazione:",
        "ingredients": "Ingredienti", "steps": "Preparazione",
    },
    "ja-JP": {
        "bonus": "ボーナス 1", "edition": "日本語",
        "exclusive": "特別版", "recipes_word": "レシピ",
        "guide": "ボーナス小冊子", "intro_title": "この冊子について",
        "before": "作り始める前に", "contents": "目次",
        "contents_title": "掲載レシピ",
        "contents_note": "右側の数字はPDF内のレシピページを示します。",
        "yield": "分量:", "time": "調理時間:",
        "pairing": "合う料理:", "storage": "保存:",
        "ingredients": "材料", "steps": "作り方",
    },
    "de-DE": {
        "bonus": "BONUS 1", "edition": "Deutsch",
        "exclusive": "EXKLUSIVE AUSGABE", "recipes_word": "REZEPTE",
        "guide": "BONUS-HEFT", "intro_title": "Über dieses Heft",
        "before": "Bevor du anfängst", "contents": "INHALT",
        "contents_title": "Rezepte in diesem Heft",
        "contents_note": "Die Zahlen rechts zeigen die Rezeptseite im PDF.",
        "yield": "Ergibt:", "time": "Zubereitungszeit:",
        "pairing": "Passt zu:", "storage": "Aufbewahrung:",
        "ingredients": "Zutaten", "steps": "Zubereitung",
    },
    "hi-IN": {
        "bonus": "बोनस 1", "edition": "हिन्दी",
        "exclusive": "विशेष संस्करण", "recipes_word": "रेसिपी",
        "guide": "पूरक पुस्तिका", "intro_title": "इस पुस्तिका के बारे में",
        "before": "शुरू करने से पहले", "contents": "विषय-सूची",
        "contents_title": "इस पुस्तिका की रेसिपी",
        "contents_note": "दाईं ओर की संख्याएँ PDF में रेसिपी का पृष्ठ बताती हैं।",
        "yield": "मात्रा:", "time": "तैयारी का समय:",
        "pairing": "इसके साथ परोसें:", "storage": "भंडारण:",
        "ingredients": "सामग्री", "steps": "विधि",
    },
    "fr-FR": {
        "bonus": "BONUS 1", "edition": "Français",
        "exclusive": "ÉDITION EXCLUSIVE", "recipes_word": "RECETTES",
        "guide": "GUIDE COMPLÉMENTAIRE", "intro_title": "À propos de ce carnet",
        "before": "Avant de commencer", "contents": "SOMMAIRE",
        "contents_title": "Recettes de ce carnet",
        "contents_note": "Les numéros à droite indiquent la page de la recette dans le PDF.",
        "yield": "Pour :", "time": "Temps de préparation :",
        "pairing": "À servir avec :", "storage": "Conservation :",
        "ingredients": "Ingrédients", "steps": "Préparation",
    },
    "zh-TW": {
        "bonus": "加贈 1", "edition": "繁體中文・台灣",
        "exclusive": "特別版", "recipes_word": "道食譜",
        "guide": "加贈小冊", "intro_title": "關於本食譜小冊",
        "before": "開始前", "contents": "目錄",
        "contents_title": "本冊食譜",
        "contents_note": "右側數字表示該食譜在 PDF 中的頁碼。",
        "yield": "份量：", "time": "準備時間：",
        "pairing": "適合搭配：", "storage": "保存方式：",
        "ingredients": "食材", "steps": "作法",
    },
    "zh-CN": {
        "bonus": "附赠 1", "edition": "简体中文・中国大陆",
        "exclusive": "特别版", "recipes_word": "道食谱",
        "guide": "附赠小册", "intro_title": "关于本小册",
        "before": "开始前", "contents": "目录",
        "contents_title": "本册食谱",
        "contents_note": "右侧数字表示该食谱在 PDF 中的页码。",
        "yield": "份量：", "time": "准备时间：",
        "pairing": "搭配建议：", "storage": "保存：",
        "ingredients": "食材", "steps": "做法",
    },
}

RECIPE_WORDS = {
    "pt-BR": "RECEITA", "pt-PT": "RECEITA", "es": "RECETA",
    "nl-NL": "RECEPT", "en-GB": "RECIPE", "en-US": "RECIPE",
    "it-IT": "RICETTA", "ja-JP": "レシピ", "de-DE": "REZEPT",
    "hi-IN": "रेसिपी", "fr-FR": "RECETTE", "zh-TW": "食譜", "zh-CN": "食谱",
}
for _locale, _word in RECIPE_WORDS.items():
    LOCALES[_locale]["recipe"] = _word

SCRIPT_LOCALES = {"hi-IN", "ja-JP", "zh-TW", "zh-CN"}
CJK_LOCALES = {"ja-JP", "zh-TW", "zh-CN"}


@dataclass
class Recipe:
    number: int
    title: str
    yield_text: str
    time_text: str
    ingredients: List[str]
    steps: List[str]
    pairing: str
    storage: str


@dataclass
class Manuscript:
    locale: str
    title: str
    subtitle: str
    intro: List[str]
    notes: List[str]
    recipes: List[Recipe]


@dataclass(frozen=True)
class FontSet:
    regular: str
    bold: str
    title: str
    shaping: bool = False
    cjk_wrap: bool = False


def clean_inline(text: str) -> str:
    """Escape manuscript text and preserve the small subset of Markdown used."""
    text = html.escape(text, quote=False)
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)


def _plain_text_from_markup(text: str) -> str:
    text = re.sub(r"<br\s*/?>", "\\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    return html.unescape(text)


def _begin_actual_text(c, text: str) -> bool:
    """Preserve the source Unicode string for shaped Devanagari text extraction."""
    plain = _plain_text_from_markup(text)
    if not plain:
        return False
    utf16 = "FEFF" + plain.encode("utf-16-be").hex().upper()
    c._code.append(f"/Span << /ActualText <{utf16}> >> BDC")
    return True


def _read_label(line: str, label: str) -> Optional[str]:
    marker = f"**{label}**"
    if line.startswith(marker):
        return line[len(marker):].strip()
    return None


def parse_manuscript(path: Path) -> Manuscript:
    locale = path.stem
    if locale not in LOCALES:
        raise ValueError(f"Locale não reconhecido no nome do arquivo: {locale}")
    labels = LOCALES[locale]
    lines = path.read_text(encoding="utf-8").splitlines()
    title = ""
    subtitle = ""
    subtitle_index = -1
    recipe_start = None
    for i, line in enumerate(lines):
        if line.startswith("# ") and not title:
            title = line[2:].strip()
        elif line.startswith("## ") and not re.match(r"## \d+\.", line) and not subtitle:
            subtitle = line[3:].strip()
            subtitle_index = i
        elif re.match(r"## \d+\.", line):
            recipe_start = i
            break
    if not title or not subtitle or recipe_start is None:
        raise ValueError(f"Estrutura Markdown não reconhecida: {path}")

    intro: List[str] = []
    notes: List[str] = []
    mode = "intro"
    for line in lines[subtitle_index + 1:recipe_start]:
        stripped = line.strip()
        if stripped == f"### {labels['before']}":
            mode = "notes"
            continue
        if stripped == "---" or line.startswith("<!--") or line.startswith("### "):
            continue
        if mode == "intro" and stripped:
            intro.append(stripped)
        elif mode == "notes" and stripped.startswith("- "):
            notes.append(stripped[2:].strip())

    ingredient_heading = f"### {labels['ingredients']}"
    steps_heading = f"### {labels['steps']}"
    yield_label = labels["yield"]
    time_label = labels["time"]
    pairing_label = labels["pairing"]
    storage_label = labels["storage"]
    storage_marker = f"**{storage_label}**"
    recipe_headers = [i for i, line in enumerate(lines) if re.match(r"## \d+\.", line)]
    recipes: List[Recipe] = []
    for idx, start in enumerate(recipe_headers):
        end = recipe_headers[idx + 1] if idx + 1 < len(recipe_headers) else len(lines)
        block = lines[start:end]
        match = re.match(r"## (\d+)\.\s*(.+)", block[0])
        if not match:
            continue
        number, recipe_title = int(match.group(1)), match.group(2).strip()
        yield_text = ""
        time_text = ""
        ingredients: List[str] = []
        steps: List[str] = []
        pairing = ""
        storage = ""
        section = ""
        for raw_line in block[1:]:
            line = raw_line.strip()
            if not line:
                continue
            if line == ingredient_heading:
                section = "ingredients"
                continue
            if line == steps_heading:
                section = "steps"
                continue
            value = _read_label(line, yield_label)
            if value is not None:
                yield_text = value
                continue
            value = _read_label(line, time_label)
            if value is not None:
                time_text = value
                continue
            value = _read_label(line, pairing_label)
            if value is not None:
                if storage_marker in value:
                    pairing, storage = value.split(storage_marker, 1)
                    pairing, storage = pairing.strip(), storage.strip()
                else:
                    pairing = value
                continue
            value = _read_label(line, storage_label)
            if value is not None:
                storage = value
                continue
            if section == "ingredients" and line.startswith("- "):
                ingredients.append(line[2:].strip())
            elif section == "steps" and re.match(r"\d+\.\s", line):
                steps.append(re.sub(r"^\d+\.\s*", "", line).strip())
        if not all((yield_text, time_text, ingredients, steps, pairing, storage)):
            raise ValueError(f"Receita {number} incompleta em {path}: {recipe_title}")
        recipes.append(Recipe(number, recipe_title, yield_text, time_text,
                              ingredients, steps, pairing, storage))

    if len(recipes) != 15:
        raise ValueError(f"Esperadas 15 receitas em {path}; encontradas {len(recipes)}.")
    return Manuscript(locale, title, subtitle, intro, notes, recipes)


def register_fonts(font_dir: Path, script_fonts_dir: Optional[Path], locale: str) -> FontSet:
    if locale in SCRIPT_LOCALES:
        if script_fonts_dir is None:
            raise FileNotFoundError(
                f"A variante {locale} requer fontes Noto. Use --script-fonts-dir "
                "com pastas hi-IN, ja-JP, zh-TW e zh-CN."
            )
        script_dir = script_fonts_dir / locale
        regular = script_dir / "NotoSans-Regular.ttf"
        bold = script_dir / "NotoSans-Bold.ttf"
        if not regular.is_file() or not bold.is_file():
            raise FileNotFoundError(
                f"Fontes Noto não encontradas em {script_dir}: "
                "NotoSans-Regular.ttf e NotoSans-Bold.ttf são necessários."
            )
        regular_name = f"Noto-{locale}"
        bold_name = f"Noto-{locale}-Bold"
        pdfmetrics.registerFont(TTFont(regular_name, str(regular)))
        pdfmetrics.registerFont(TTFont(bold_name, str(bold)))
        pdfmetrics.registerFontFamily(regular_name, normal=regular_name, bold=bold_name,
                                      italic=regular_name, boldItalic=bold_name)
        return FontSet(regular_name, bold_name, bold_name,
                       shaping=(locale == "hi-IN"), cjk_wrap=(locale in CJK_LOCALES))

    regular = font_dir / "DejaVuSans.ttf"
    bold = font_dir / "DejaVuSans-Bold.ttf"
    serif = font_dir / "DejaVuSerif.ttf"
    serif_bold = font_dir / "DejaVuSerif-Bold.ttf"
    required = (regular, bold, serif, serif_bold)
    if not all(path.is_file() for path in required):
        raise FileNotFoundError(
            "Não encontrei as fontes DejaVu Sans e DejaVu Serif. "
            "Use --font-dir para indicar a pasta das fontes."
        )
    pdfmetrics.registerFont(TTFont("DejaVu", str(regular)))
    pdfmetrics.registerFont(TTFont("DejaVu-Bold", str(bold)))
    pdfmetrics.registerFont(TTFont("DejaVuSerif", str(serif)))
    pdfmetrics.registerFont(TTFont("DejaVuSerif-Bold", str(serif_bold)))
    pdfmetrics.registerFontFamily("DejaVu", normal="DejaVu", bold="DejaVu-Bold",
                                  italic="DejaVu", boldItalic="DejaVu-Bold")
    pdfmetrics.registerFontFamily("DejaVuSerif", normal="DejaVuSerif",
                                  bold="DejaVuSerif-Bold", italic="DejaVuSerif",
                                  boldItalic="DejaVuSerif-Bold")
    return FontSet("DejaVu", "DejaVu-Bold", "DejaVuSerif-Bold")


def _style_options(fonts: FontSet) -> dict:
    options = {}
    if fonts.shaping:
        options["shaping"] = True
    if fonts.cjk_wrap:
        options["wordWrap"] = "CJK"
    return options


def styles(locale: str, fonts: FontSet) -> Dict[str, ParagraphStyle]:
    common = _style_options(fonts)
    body_size = 8.2 if locale == "hi-IN" else (8.4 if fonts.cjk_wrap else 9.2)
    body_leading = 10.7 if locale == "hi-IN" else (11.0 if fonts.cjk_wrap else 12.3)
    return {
        "body": ParagraphStyle("body", fontName=fonts.regular, fontSize=body_size,
                                leading=body_leading, textColor=TEXT, spaceAfter=0, **common),
        "small": ParagraphStyle("small", fontName=fonts.regular, fontSize=body_size - 0.4,
                                 leading=body_leading - 1.0, textColor=TEXT, **common),
        "intro": ParagraphStyle("intro", fontName=fonts.regular,
                                 fontSize=9.0 if locale == "hi-IN" else (9.4 if fonts.cjk_wrap else 10.3),
                                 leading=13.0 if locale == "hi-IN" else (13.2 if fonts.cjk_wrap else 15.2),
                                 textColor=TEXT, **common),
        "title": ParagraphStyle("title", fontName=fonts.title,
                                fontSize=20 if fonts.cjk_wrap or fonts.shaping else 21,
                                leading=25 if fonts.cjk_wrap or fonts.shaping else 25,
                                textColor=DARK, **common),
        "page_title": ParagraphStyle("page_title", fontName=fonts.title,
                                      fontSize=20 if fonts.cjk_wrap or fonts.shaping else 24,
                                      leading=25 if fonts.cjk_wrap or fonts.shaping else 29,
                                      textColor=DARK, **common),
        "subtitle": ParagraphStyle("subtitle", fontName=fonts.regular, fontSize=10,
                                    leading=14, textColor=MUTED, **common),
    }


def draw_paragraph(c, text: str, x: float, top: float, width: float,
                   style: ParagraphStyle) -> float:
    p = Paragraph(text, style)
    _, h = p.wrap(width, max(1, top))
    marked = bool(getattr(style, "shaping", False)) and _begin_actual_text(c, text)
    try:
        p.drawOn(c, x, top - h)
    finally:
        if marked:
            c._code.append("EMC")
    return top - h


def draw_string(c, x: float, y: float, text: str, font_name: str,
                font_size: float, fonts: FontSet) -> None:
    marked = fonts.shaping and _begin_actual_text(c, text)
    try:
        c.setFont(font_name, font_size)
        c.drawString(x, y, text, shaping=fonts.shaping)
    finally:
        if marked:
            c._code.append("EMC")


def draw_section_label(c, text: str, x: float, top: float, width: float,
                       fonts: FontSet) -> float:
    draw_string(c, x, top - 9, text.upper(), fonts.bold, 8.0, fonts)
    c.setFillColor(GREEN)
    c.setStrokeColor(LINE)
    c.setLineWidth(0.7)
    c.line(x, top - 14, x + width, top - 14)
    return top - 23


def draw_footer(c, page_num: int, label: str, fonts: FontSet) -> None:
    c.setStrokeColor(LINE)
    c.setLineWidth(0.6)
    c.line(MARGIN, 31, PAGE_W - MARGIN, 31)
    c.setFillColor(MUTED)
    draw_string(c, MARGIN, 19, label, fonts.regular, 7.0, fonts)
    c.setFont(fonts.regular, 7.5)
    c.drawRightString(PAGE_W - MARGIN, 19, f"{page_num}")


def prepare_crop(source: Path, destination: Path, size: tuple[int, int], quality: int = 88) -> None:
    with Image.open(source) as original:
        image = ImageOps.fit(original.convert("RGB"), size, method=Image.Resampling.LANCZOS,
                             centering=(0.5, 0.5))
        image.save(destination, "JPEG", quality=quality, optimize=True, progressive=True)


def draw_cover(c, cover_path: Path, manuscript: Manuscript, labels: Dict[str, str],
               bonus_label: str, edition_label: str, fonts: FontSet, temp_dir: Path) -> None:
    crop = temp_dir / "cover_a4.jpg"
    prepare_crop(cover_path, crop, (1240, 1754), 92)
    c.drawImage(str(crop), 0, 0, width=PAGE_W, height=PAGE_H)

    ivory = HexColor("#F5EBDD")
    antique_gold = HexColor("#D1AE73")
    if manuscript.locale == "pt-BR":
        c.setFillColor(antique_gold)
        draw_string(c, 52, PAGE_H - 62, "BÔNUS 1  ·  EDIÇÃO EXCLUSIVA",
                    fonts.bold, 8, fonts)
        c.setStrokeColor(antique_gold)
        c.setLineWidth(1.2)
        c.line(52, PAGE_H - 82, 112, PAGE_H - 82)
        c.setFillColor(ivory)
        draw_string(c, 52, PAGE_H - 128, "CADERNO DE", "DejaVuSerif", 13, fonts)
        draw_string(c, 52, PAGE_H - 171, "MOLHOS &", "DejaVuSerif-Bold", 29, fonts)
        draw_string(c, 52, PAGE_H - 207, "VINAGRETAS", "DejaVuSerif-Bold", 29, fonts)
        c.setFillColor(antique_gold)
        draw_string(c, 53, PAGE_H - 235, "LOW CARB  ·  15 RECEITAS",
                    fonts.bold, 8, fonts)
        c.setFillColor(ivory)
        draw_string(c, 53, PAGE_H - 257, edition_label.upper(),
                    fonts.regular, 7.5, fonts)
        draw_string(c, 52, PAGE_H - 280,
                    "Receitas caseiras para dar mais sabor às suas refeições",
                    fonts.regular, 9, fonts)
        c.showPage()
        return

    c.setFillColor(antique_gold)
    draw_string(c, 52, PAGE_H - 62,
                f"{bonus_label}  ·  {labels['exclusive']}", fonts.bold, 7.5, fonts)
    c.setStrokeColor(antique_gold)
    c.setLineWidth(1.2)
    c.line(52, PAGE_H - 82, 112, PAGE_H - 82)

    title_size = 24 if fonts.cjk_wrap or fonts.shaping else 27
    title_style = ParagraphStyle(
        "cover_title", fontName=fonts.title, fontSize=title_size,
        leading=title_size + 5, textColor=ivory, alignment=0,
        spaceAfter=0, **_style_options(fonts)
    )
    title_bottom = draw_paragraph(c, clean_inline(manuscript.title), 52,
                                  PAGE_H - 119, PAGE_W - 104, title_style)

    c.setFillColor(antique_gold)
    draw_string(c, 53, title_bottom - 21,
                f"15 {labels['recipes_word']}", fonts.bold, 7.8, fonts)
    c.setFillColor(ivory)
    draw_string(c, 53, title_bottom - 42, edition_label.upper(),
                fonts.regular, 7.2, fonts)
    subtitle_style = ParagraphStyle(
        "cover_subtitle", fontName=fonts.regular, fontSize=8.5,
        leading=11.2, textColor=ivory, spaceAfter=0, **_style_options(fonts)
    )
    draw_paragraph(c, clean_inline(manuscript.subtitle), 52,
                   title_bottom - 54, PAGE_W - 104, subtitle_style)
    c.showPage()


def draw_intro(c, manuscript: Manuscript, labels: Dict[str, str], s,
               bonus_label: str, edition_label: str, fonts: FontSet,
               page_num: int) -> None:
    c.setFillColor(CREAM)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    c.setFillColor(GREEN)
    c.rect(0, PAGE_H - 7, PAGE_W, 7, fill=1, stroke=0)
    c.setFillColor(GOLD)
    draw_string(c, MARGIN, PAGE_H - 55,
                f"{bonus_label}  ·  {labels['guide']}", fonts.bold, 7.5, fonts)
    y = PAGE_H - 91
    y = draw_paragraph(c, clean_inline(labels["intro_title"]), MARGIN, y,
                       CONTENT_W, s["page_title"]) - 17
    for paragraph in manuscript.intro:
        y = draw_paragraph(c, clean_inline(paragraph), MARGIN, y,
                           CONTENT_W, s["intro"]) - 12
    y -= 6
    y = draw_section_label(c, labels["before"], MARGIN, y, CONTENT_W, fonts)
    bullet_style = ParagraphStyle(
        "bullet", parent=s["intro"], fontSize=8.8 if fonts.shaping else 9.2,
        leading=12.2 if fonts.shaping else 13.0,
        leftIndent=12, firstLineIndent=-10, spaceAfter=6, **_style_options(fonts)
    )
    for item in manuscript.notes:
        bullet = f'<font color="{GREEN.hexval()}">•</font>  {clean_inline(item)}'
        y = draw_paragraph(c, bullet, MARGIN + 4, y, CONTENT_W - 8, bullet_style) - 3
    draw_footer(c, page_num, f"{bonus_label}  ·  {edition_label.upper()}", fonts)
    c.showPage()


def draw_contents(c, recipes: List[Recipe], labels: Dict[str, str],
                  bonus_label: str, edition_label: str, fonts: FontSet,
                  page_num: int) -> None:
    """Render a premium, locale-aware table of contents."""
    header_bottom = PAGE_H - 164
    c.setFillColor(CREAM)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    # Deep-green masthead with a restrained gold edge to echo the premium cover.
    c.setFillColor(GOLD)
    c.rect(0, PAGE_H - 6, PAGE_W, 6, fill=1, stroke=0)
    c.setFillColor(DARK)
    c.rect(0, header_bottom, PAGE_W, PAGE_H - 6 - header_bottom, fill=1, stroke=0)
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.8)
    c.line(MARGIN, header_bottom, PAGE_W - MARGIN, header_bottom)

    c.setFillColor(GOLD)
    draw_string(c, MARGIN, PAGE_H - 49,
                f"{bonus_label}  ·  {labels['contents']}", fonts.bold, 7.5, fonts)
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.2)
    c.line(MARGIN, PAGE_H - 62, MARGIN + 36, PAGE_H - 62)

    title_style = ParagraphStyle(
        "toc_header", fontName=fonts.title,
        fontSize=22 if fonts.cjk_wrap or fonts.shaping else 24,
        leading=27 if fonts.cjk_wrap or fonts.shaping else 29,
        textColor=colors.white, spaceAfter=0, **_style_options(fonts)
    )
    draw_paragraph(c, clean_inline(labels["contents_title"]), MARGIN,
                   PAGE_H - 77, CONTENT_W - 82, title_style)

    # A small edition medallion adds an editorial touch without introducing
    # untranslated copy or changing the page numbering.
    medallion_x = PAGE_W - MARGIN - 30
    medallion_y = PAGE_H - 111
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.1)
    c.circle(medallion_x, medallion_y, 28, stroke=1, fill=0)
    c.setFillColor(GOLD)
    c.setFont(fonts.title, 21)
    c.drawCentredString(medallion_x, medallion_y - 7, "15")
    # One full-width row per recipe makes the titles easier to scan and uses
    # the available page height without splitting the list into columns.
    list_top = header_bottom - 14
    row_gap = 4
    title_size = 9.0 if fonts.shaping else (9.2 if fonts.cjk_wrap else 10.0)
    title_leading = 11.0 if fonts.shaping else (11.4 if fonts.cjk_wrap else 12.2)
    title_style = ParagraphStyle(
        "toc_card_title", fontName=fonts.bold, fontSize=title_size,
        leading=title_leading, textColor=TEXT, spaceAfter=0,
        **_style_options(fonts)
    )
    x = MARGIN
    row_w = CONTENT_W
    badge_x = x + 23
    title_x = x + 47
    page_w = 26
    page_x = x + row_w - 8 - page_w
    title_w = page_x - title_x - 10
    cy = list_top
    note_y = 54
    note_h = 30
    for recipe in recipes:
        title = clean_inline(recipe.title)
        paragraph = Paragraph(title, title_style)
        _, title_h = paragraph.wrap(title_w, PAGE_H)
        card_h = max(32, title_h + 16)
        card_bottom = cy - card_h
        if card_bottom < note_y + note_h + 8:
            raise ValueError("O sumário em lista única não cabe na página.")

        c.setFillColor(colors.white)
        c.setStrokeColor(LINE)
        c.setLineWidth(0.55)
        c.roundRect(x, card_bottom, row_w, card_h, 7, stroke=1, fill=1)
        c.setFillColor(GOLD)
        c.roundRect(x + 1, card_bottom + 6, 2.2, card_h - 12,
                    1.1, stroke=0, fill=1)

        badge_y = card_bottom + card_h / 2
        c.setFillColor(DARK)
        c.circle(badge_x, badge_y, 11.5, stroke=0, fill=1)
        c.setFillColor(colors.white)
        c.setFont(fonts.bold, 7.2)
        c.drawCentredString(badge_x, badge_y - 2.5,
                            f"{recipe.number:02d}")

        c.setFillColor(SAGE)
        c.roundRect(page_x, badge_y - 11, page_w, 22, 7,
                    stroke=0, fill=1)
        c.setFillColor(DARK)
        c.setFont(fonts.bold, 7.2)
        c.drawCentredString(page_x + page_w / 2, badge_y - 2.5,
                            str(recipe.number + 3))

        title_top = card_bottom + (card_h + title_h) / 2
        draw_paragraph(c, title, title_x, title_top, title_w, title_style)
        cy = card_bottom - row_gap

    # A quiet legend anchors the page while leaving generous breathing room.
    c.setFillColor(SAGE)
    c.roundRect(MARGIN, note_y, CONTENT_W, note_h, 8, stroke=0, fill=1)
    c.setFillColor(GOLD)
    c.circle(MARGIN + 14, note_y + note_h / 2, 2.1, stroke=0, fill=1)
    note_style = ParagraphStyle(
        "toc_note", fontName=fonts.regular, fontSize=6.9,
        leading=8.5, textColor=MUTED, spaceAfter=0,
        **_style_options(fonts)
    )
    draw_paragraph(c, clean_inline(labels["contents_note"]), MARGIN + 24,
                   note_y + note_h - 7, CONTENT_W - 34, note_style)
    draw_footer(c, page_num, f"{bonus_label}  ·  {edition_label.upper()}", fonts)
    c.showPage()


def bullet_html(items: List[str]) -> str:
    return "<br/>".join(
        f'<font color="{GREEN.hexval()}">•</font>  {clean_inline(item)}' for item in items
    )


def numbered_html(items: List[str], fonts: FontSet) -> str:
    return "<br/><br/>".join(
        f'<font color="{GREEN.hexval()}"><b>{i}.</b></font>  {clean_inline(item)}'
        for i, item in enumerate(items, 1)
    )


def draw_recipe(c, recipe: Recipe, image_path: Path, page_num: int,
                labels: Dict[str, str], bonus_label: str, edition_label: str,
                locale: str, fonts: FontSet, temp_dir: Path) -> None:
    c.setFillColor(colors.white)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    c.setFillColor(GREEN)
    c.rect(0, PAGE_H - 7, PAGE_W, 7, fill=1, stroke=0)
    c.setFillColor(GOLD)
    draw_string(c, MARGIN, PAGE_H - 48,
                f"{bonus_label}  ·  {labels['recipe'].upper()} {recipe.number:02d}/15",
                fonts.bold, 7.5, fonts)

    s = styles(locale, fonts)
    title_style = ParagraphStyle("recipe_title", parent=s["title"],
                                 fontSize=19 if locale == "hi-IN" else (19.5 if fonts.cjk_wrap else 20),
                                 leading=23 if locale == "hi-IN" else 24, spaceAfter=0,
                                 **_style_options(fonts))
    title_bottom = draw_paragraph(c, clean_inline(recipe.title), MARGIN,
                                  PAGE_H - 65, CONTENT_W, title_style)

    meta_y = title_bottom - 12
    meta_h = 28
    box_gap = 10
    box_w = (CONTENT_W - box_gap) / 2
    for x, label, value in [
        (MARGIN, labels["yield"].rstrip(":"), recipe.yield_text),
        (MARGIN + box_w + box_gap, labels["time"].rstrip(":"), recipe.time_text),
    ]:
        c.setFillColor(SAGE)
        c.roundRect(x, meta_y - meta_h, box_w, meta_h, 6, fill=1, stroke=0)
        c.setFillColor(GREEN)
        draw_string(c, x + 10, meta_y - 10, label.upper(), fonts.bold, 6.2, fonts)
        c.setFillColor(DARK)
        draw_string(c, x + 10, meta_y - 21, value, fonts.regular, 7.7, fonts)

    image_h = 240 if locale == "hi-IN" else (258 if fonts.cjk_wrap else 278)
    image_w = CONTENT_W
    image_x = MARGIN
    image_y = meta_y - meta_h - 10 - image_h
    cache_path = temp_dir / f"recipe_{recipe.number:02d}.jpg"
    prepare_crop(image_path, cache_path, (1400, 780), 88)
    c.drawImage(str(cache_path), image_x, image_y, width=image_w, height=image_h,
                preserveAspectRatio=False, mask="auto")

    body_top = image_y - 18
    col_gap = 20
    col_w = (CONTENT_W - col_gap) / 2
    left_x = MARGIN
    right_x = MARGIN + col_w + col_gap

    left_y = draw_section_label(c, labels["ingredients"], left_x, body_top, col_w, fonts)
    ingredient_style = ParagraphStyle(
        "ingredients", parent=s["body"], fontSize=7.9 if locale == "hi-IN" else (8.0 if fonts.cjk_wrap else 8.5),
        leading=10.2 if locale == "hi-IN" else (10.5 if fonts.cjk_wrap else 11.2),
        spaceAfter=0, **_style_options(fonts)
    )
    left_y = draw_paragraph(c, bullet_html(recipe.ingredients), left_x,
                            left_y, col_w, ingredient_style) - 10
    left_y = draw_section_label(c, labels["pairing"], left_x, left_y, col_w, fonts)
    pairing_style = ParagraphStyle(
        "pairing", parent=s["small"], fontSize=7.4 if locale == "hi-IN" else 7.8,
        leading=9.8 if locale == "hi-IN" else 10.4, **_style_options(fonts)
    )
    left_y = draw_paragraph(c, clean_inline(recipe.pairing), left_x,
                            left_y, col_w, pairing_style)

    right_y = draw_section_label(c, labels["steps"], right_x, body_top, col_w, fonts)
    step_style = ParagraphStyle(
        "steps", parent=s["body"], fontSize=7.9 if locale == "hi-IN" else (8.0 if fonts.cjk_wrap else 8.5),
        leading=10.2 if locale == "hi-IN" else (10.5 if fonts.cjk_wrap else 11.2),
        spaceAfter=0, **_style_options(fonts)
    )
    right_y = draw_paragraph(c, numbered_html(recipe.steps, fonts), right_x,
                             right_y, col_w, step_style) - 10
    right_y = draw_section_label(c, labels["storage"], right_x, right_y, col_w, fonts)
    storage_style = ParagraphStyle(
        "storage", parent=s["small"], fontSize=7.4 if locale == "hi-IN" else 7.7,
        leading=9.7 if locale == "hi-IN" else 10.2, **_style_options(fonts)
    )
    right_y = draw_paragraph(c, clean_inline(recipe.storage), right_x,
                             right_y, col_w, storage_style)

    lower = min(left_y, right_y)
    if lower < 38:
        raise ValueError(
            f"Conteúdo da receita {recipe.number} ({locale}) excede a área útil "
            f"do PDF (y={lower:.1f})."
        )
    draw_footer(c, page_num, f"{bonus_label}  ·  {edition_label.upper()}", fonts)
    c.showPage()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manuscript", required=True, type=Path)
    parser.add_argument("--images", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--cover", type=Path, default=None)
    parser.add_argument("--bonus-label", default=None)
    parser.add_argument("--edition-label", default=None)
    parser.add_argument("--font-dir", type=Path,
                        default=Path("/usr/share/fonts/truetype/dejavu"))
    parser.add_argument("--script-fonts-dir", type=Path, default=None,
                        help="Pasta com subpastas hi-IN, ja-JP, zh-TW e zh-CN contendo fontes Noto.")
    args = parser.parse_args()

    if not args.manuscript.is_file():
        raise SystemExit(f"Manuscrito não encontrado: {args.manuscript}")
    locale = args.manuscript.stem
    if locale not in LOCALES:
        raise SystemExit(f"Locale não reconhecido: {locale}. Arquivo deve usar um código da lista do projeto.")
    labels = LOCALES[locale]
    bonus_label = args.bonus_label or labels["bonus"]
    edition_label = args.edition_label or labels["edition"]
    cover = args.cover or args.images / "capa.jpg"
    if not cover.is_file():
        raise SystemExit(f"Capa não encontrada: {cover}")

    manuscript = parse_manuscript(args.manuscript)
    image_paths = {}
    for recipe in manuscript.recipes:
        matches = list(args.images.glob(f"{recipe.number:02d}_*.jpg"))
        if len(matches) != 1:
            raise SystemExit(f"Receita {recipe.number}: esperado 1 JPG, encontrados {len(matches)}.")
        image_paths[recipe.number] = matches[0]

    fonts = register_fonts(args.font_dir, args.script_fonts_dir, locale)
    s = styles(locale, fonts)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="bonus_pdf_") as tmp:
        temp_dir = Path(tmp)
        c = canvas.Canvas(str(args.output), pagesize=A4, pageCompression=1)
        c.setTitle(manuscript.title)
        c.setSubject(manuscript.subtitle)
        c.setCreator("Bônus Low Carb — renderização A4 multilíngue")
        draw_cover(c, cover, manuscript, labels, bonus_label, edition_label, fonts, temp_dir)
        draw_intro(c, manuscript, labels, s, bonus_label, edition_label, fonts, 2)
        draw_contents(c, manuscript.recipes, labels, bonus_label, edition_label, fonts, 3)
        for recipe in manuscript.recipes:
            draw_recipe(c, recipe, image_paths[recipe.number], recipe.number + 3,
                        labels, bonus_label, edition_label, locale, fonts, temp_dir)
        c.save()
    print(f"PDF criado: {args.output} ({len(manuscript.recipes) + 3} páginas; {locale})")


if __name__ == "__main__":
    main()
