#!/usr/bin/env python3
"""Renderiza um manuscrito Markdown de bônus culinário em PDF A4 ilustrado.

Dependências: ReportLab e Pillow. As receitas são lidas do Markdown; as imagens
são associadas pelo prefixo numérico (01_*.jpg, 02_*.jpg, ...).
"""
from __future__ import annotations

import argparse
import html
import re
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import List

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
    title: str
    subtitle: str
    intro: List[str]
    notes: List[str]
    recipes: List[Recipe]


def clean_inline(text: str) -> str:
    """Escape manuscript text and preserve the small subset of Markdown used."""
    text = html.escape(text, quote=False)
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)


def parse_manuscript(path: Path) -> Manuscript:
    lines = path.read_text(encoding="utf-8").splitlines()
    title = ""
    subtitle = ""
    title_index = -1
    subtitle_index = -1
    recipe_start = None
    for i, line in enumerate(lines):
        if line.startswith("# ") and not title:
            title = line[2:].strip()
            title_index = i
        elif line.startswith("## ") and not re.match(r"## \d+\.", line) and not subtitle:
            subtitle = line[3:].strip()
            subtitle_index = i
        elif re.match(r"## \d+\.", line):
            recipe_start = i
            break
    if not title or not subtitle or recipe_start is None:
        raise ValueError(f"Estrutura Markdown não reconhecida: {path}")

    intro_lines = lines[subtitle_index + 1 :]
    intro: List[str] = []
    notes: List[str] = []
    mode = "intro"
    for line in intro_lines:
        if re.match(r"## \d+\.", line):
            break
        if line.strip() == "### Antes de começar":
            mode = "notes"
            continue
        if line.strip() == "---":
            continue
        if line.startswith("<!--") or line.startswith("### "):
            continue
        if mode == "intro" and line.strip():
            intro.append(line.strip())
        elif mode == "notes" and line.startswith("- "):
            notes.append(line[2:].strip())

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
        for line in block[1:]:
            line = line.strip()
            if not line:
                continue
            if line == "### Ingredientes":
                section = "ingredients"
                continue
            if line in ("### Modo de preparo", "### Preparação"):
                section = "steps"
                continue
            if line.startswith("**Rendimento:**"):
                yield_text = re.sub(r"^\*\*Rendimento:\*\*\s*", "", line).strip()
                continue
            if line.startswith("**Tempo de preparo:**"):
                time_text = re.sub(r"^\*\*Tempo de preparo:\*\*\s*", "", line).strip()
                continue
            if line.startswith("**Combina com:**"):
                pieces = re.split(r"\s{2,}\*\*Conservação:\*\*\s*", line, maxsplit=1)
                pairing = re.sub(r"^\*\*Combina com:\*\*\s*", "", pieces[0]).strip()
                if len(pieces) > 1:
                    storage = pieces[1].strip()
                continue
            if line.startswith("**Conservação:**"):
                storage = re.sub(r"^\*\*Conservação:\*\*\s*", "", line).strip()
                continue
            if section == "ingredients" and line.startswith("- "):
                ingredients.append(line[2:].strip())
            elif section == "steps" and re.match(r"\d+\.\s", line):
                steps.append(re.sub(r"^\d+\.\s*", "", line).strip())
        if not all((yield_text, time_text, ingredients, steps, pairing, storage)):
            raise ValueError(f"Receita {number} incompleta no manuscrito: {recipe_title}")
        recipes.append(Recipe(number, recipe_title, yield_text, time_text,
                              ingredients, steps, pairing, storage))

    if not recipes:
        raise ValueError("Nenhuma receita encontrada no manuscrito.")
    return Manuscript(title, subtitle, intro, notes, recipes)


def register_fonts(font_dir: Path) -> None:
    regular = font_dir / "DejaVuSans.ttf"
    bold = font_dir / "DejaVuSans-Bold.ttf"
    serif = font_dir / "DejaVuSerif.ttf"
    serif_bold = font_dir / "DejaVuSerif-Bold.ttf"
    required = (regular, bold, serif, serif_bold)
    if not all(path.exists() for path in required):
        raise FileNotFoundError("Não encontrei as fontes DejaVu Sans e DejaVu Serif. "
                                "Use --font-dir para indicar a pasta das fontes.")
    pdfmetrics.registerFont(TTFont("DejaVu", str(regular)))
    pdfmetrics.registerFont(TTFont("DejaVu-Bold", str(bold)))
    pdfmetrics.registerFont(TTFont("DejaVuSerif", str(serif)))
    pdfmetrics.registerFont(TTFont("DejaVuSerif-Bold", str(serif_bold)))
    pdfmetrics.registerFontFamily("DejaVu", normal="DejaVu", bold="DejaVu-Bold",
                                  italic="DejaVu", boldItalic="DejaVu-Bold")
    pdfmetrics.registerFontFamily("DejaVuSerif", normal="DejaVuSerif",
                                  bold="DejaVuSerif-Bold", italic="DejaVuSerif",
                                  boldItalic="DejaVuSerif-Bold")


def styles():
    return {
        "body": ParagraphStyle("body", fontName="DejaVu", fontSize=9.2,
                                leading=12.3, textColor=TEXT, spaceAfter=0),
        "small": ParagraphStyle("small", fontName="DejaVu", fontSize=8.5,
                                 leading=11.2, textColor=TEXT),
        "intro": ParagraphStyle("intro", fontName="DejaVu", fontSize=10.3,
                                 leading=15.2, textColor=TEXT),
        "title": ParagraphStyle("title", fontName="DejaVu-Bold", fontSize=21,
                                leading=25, textColor=DARK),
        "page_title": ParagraphStyle("page_title", fontName="DejaVu-Bold", fontSize=24,
                                      leading=29, textColor=DARK),
        "subtitle": ParagraphStyle("subtitle", fontName="DejaVu", fontSize=11,
                                    leading=15, textColor=MUTED),
    }


def draw_paragraph(c, text: str, x: float, top: float, width: float,
                   style: ParagraphStyle) -> float:
    p = Paragraph(text, style)
    _, h = p.wrap(width, max(1, top))
    p.drawOn(c, x, top - h)
    return top - h


def draw_section_label(c, text: str, x: float, top: float, width: float) -> float:
    c.setFillColor(GREEN)
    c.setFont("DejaVu-Bold", 8.2)
    c.drawString(x, top - 9, text.upper())
    c.setStrokeColor(LINE)
    c.setLineWidth(0.7)
    c.line(x, top - 14, x + width, top - 14)
    return top - 23


def draw_footer(c, page_num: int, label: str) -> None:
    c.setStrokeColor(LINE)
    c.setLineWidth(0.6)
    c.line(MARGIN, 31, PAGE_W - MARGIN, 31)
    c.setFillColor(MUTED)
    c.setFont("DejaVu", 7.5)
    c.drawString(MARGIN, 19, label)
    c.drawRightString(PAGE_W - MARGIN, 19, f"{page_num}")


def prepare_crop(source: Path, destination: Path, size: tuple[int, int], quality: int = 88) -> None:
    with Image.open(source) as original:
        image = ImageOps.fit(original.convert("RGB"), size, method=Image.Resampling.LANCZOS,
                             centering=(0.5, 0.5))
        image.save(destination, "JPEG", quality=quality, optimize=True, progressive=True)


def draw_cover(c, cover_path: Path, manuscript: Manuscript,
               bonus_label: str, edition_label: str, temp_dir: Path) -> None:
    crop = temp_dir / "cover_a4.jpg"
    prepare_crop(cover_path, crop, (1240, 1754), 92)
    c.drawImage(str(crop), 0, 0, width=PAGE_W, height=PAGE_H)

    ivory = HexColor("#F5EBDD")
    antique_gold = HexColor("#D1AE73")
    c.setFillColor(antique_gold)
    c.setFont("DejaVu-Bold", 8)
    c.drawString(52, PAGE_H - 62, f"{bonus_label}  ·  EDIÇÃO EXCLUSIVA")
    c.setStrokeColor(antique_gold)
    c.setLineWidth(1.2)
    c.line(52, PAGE_H - 82, 112, PAGE_H - 82)

    c.setFillColor(ivory)
    c.setFont("DejaVuSerif", 13)
    c.drawString(52, PAGE_H - 128, "CADERNO DE")
    c.setFont("DejaVuSerif-Bold", 29)
    c.drawString(52, PAGE_H - 171, "MOLHOS &")
    c.drawString(52, PAGE_H - 207, "VINAGRETAS")

    c.setFillColor(antique_gold)
    c.setFont("DejaVu-Bold", 8)
    c.drawString(53, PAGE_H - 235, "LOW CARB  ·  15 RECEITAS")
    c.setFillColor(ivory)
    c.setFont("DejaVu", 7.5)
    c.drawString(53, PAGE_H - 257, edition_label.upper())
    c.setFont("DejaVu", 9)
    c.drawString(52, PAGE_H - 280,
                  "Receitas caseiras para dar mais sabor às suas refeições")
    c.showPage()


def draw_intro(c, manuscript: Manuscript, s, label: str, page_num: int) -> None:
    c.setFillColor(CREAM)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    c.setFillColor(GREEN)
    c.rect(0, PAGE_H - 7, PAGE_W, 7, fill=1, stroke=0)
    c.setFillColor(GOLD)
    c.setFont("DejaVu-Bold", 8)
    c.drawString(MARGIN, PAGE_H - 55, f"{label}  ·  GUIA COMPLEMENTAR")
    y = PAGE_H - 91
    y = draw_paragraph(c, "Sobre este caderno", MARGIN, y, CONTENT_W, s["page_title"]) - 17
    for paragraph in manuscript.intro:
        y = draw_paragraph(c, clean_inline(paragraph), MARGIN, y, CONTENT_W, s["intro"]) - 12
    y -= 6
    y = draw_section_label(c, "Antes de começar", MARGIN, y, CONTENT_W)
    bullet_style = ParagraphStyle("bullet", parent=s["intro"], fontSize=9.4, leading=13.2,
                                  leftIndent=12, firstLineIndent=-10, spaceAfter=7)
    for item in manuscript.notes:
        bullet = f'<font color="{GREEN.hexval()}">•</font>  {clean_inline(item)}'
        y = draw_paragraph(c, bullet, MARGIN + 4, y, CONTENT_W - 8, bullet_style) - 3
    draw_footer(c, page_num, "CADERNO DE MOLHOS E VINAGRETAS  ·  PT-BR")
    c.showPage()


def draw_contents(c, recipes: List[Recipe], page_num: int) -> None:
    c.setFillColor(colors.white)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    c.setFillColor(GREEN)
    c.rect(0, PAGE_H - 7, PAGE_W, 7, fill=1, stroke=0)
    c.setFillColor(GOLD)
    c.setFont("DejaVu-Bold", 8)
    c.drawString(MARGIN, PAGE_H - 55, "BÔNUS 1  ·  SUMÁRIO")
    s = styles()
    y = draw_paragraph(c, "Receitas neste caderno", MARGIN, PAGE_H - 91,
                       CONTENT_W, s["page_title"]) - 24
    gap = 26
    col_w = (CONTENT_W - gap) / 2
    columns = [recipes[:8], recipes[8:]]
    for col_index, items in enumerate(columns):
        x = MARGIN + col_index * (col_w + gap)
        cy = y
        for recipe in items:
            c.setFillColor(GREEN)
            c.setFont("DejaVu-Bold", 9)
            c.drawString(x, cy - 10, f"{recipe.number:02d}")
            title_style = ParagraphStyle("toc", fontName="DejaVu", fontSize=9.4,
                                         leading=12.5, textColor=TEXT)
            title_bottom = draw_paragraph(c, clean_inline(recipe.title), x + 25,
                                          cy, col_w - 57, title_style)
            c.setFillColor(MUTED)
            c.setFont("DejaVu", 8)
            c.drawRightString(x + col_w, cy - 10, str(recipe.number + 3))
            cy = min(cy - 36, title_bottom - 17)
    c.setFillColor(MUTED)
    c.setFont("DejaVu", 7.5)
    c.drawString(MARGIN, 54, "Os números à direita indicam a página da receita no PDF.")
    draw_footer(c, page_num, "CADERNO DE MOLHOS E VINAGRETAS  ·  PT-BR")
    c.showPage()


def bullet_html(items: List[str]) -> str:
    return "<br/>".join(
        f'<font color="{GREEN.hexval()}">•</font>  {clean_inline(item)}' for item in items
    )


def numbered_html(items: List[str]) -> str:
    return "<br/><br/>".join(
        f'<font color="{GREEN.hexval()}"><b>{i}.</b></font>  {clean_inline(item)}'
        for i, item in enumerate(items, 1)
    )


def draw_recipe(c, recipe: Recipe, image_path: Path, page_num: int,
                label: str, edition_label: str, temp_dir: Path) -> None:
    c.setFillColor(colors.white)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    c.setFillColor(GREEN)
    c.rect(0, PAGE_H - 7, PAGE_W, 7, fill=1, stroke=0)
    c.setFillColor(GOLD)
    c.setFont("DejaVu-Bold", 8)
    c.drawString(MARGIN, PAGE_H - 48, f"{label}  ·  RECEITA {recipe.number:02d}/15")

    s = styles()
    title_style = ParagraphStyle("recipe_title", parent=s["title"], fontSize=20,
                                 leading=24, spaceAfter=0)
    title_bottom = draw_paragraph(c, clean_inline(recipe.title), MARGIN,
                                  PAGE_H - 65, CONTENT_W, title_style)

    meta_y = title_bottom - 12
    meta_h = 28
    box_gap = 10
    box_w = (CONTENT_W - box_gap) / 2
    for x, title, value in [
        (MARGIN, "RENDIMENTO", recipe.yield_text),
        (MARGIN + box_w + box_gap, "TEMPO", recipe.time_text),
    ]:
        c.setFillColor(SAGE)
        c.roundRect(x, meta_y - meta_h, box_w, meta_h, 6, fill=1, stroke=0)
        c.setFillColor(GREEN)
        c.setFont("DejaVu-Bold", 6.6)
        c.drawString(x + 10, meta_y - 10, title)
        c.setFillColor(DARK)
        c.setFont("DejaVu", 8.2)
        c.drawString(x + 10, meta_y - 21, value)

    image_w, image_h = CONTENT_W, 288
    image_x = MARGIN
    image_y = meta_y - meta_h - 10 - image_h
    cache_path = temp_dir / f"recipe_{recipe.number:02d}.jpg"
    prepare_crop(image_path, cache_path, (1400, 780), 88)
    c.drawImage(str(cache_path), image_x, image_y, width=image_w, height=image_h,
                preserveAspectRatio=False, mask="auto")

    body_top = image_y - 20
    col_gap = 20
    col_w = (CONTENT_W - col_gap) / 2
    left_x = MARGIN
    right_x = MARGIN + col_w + col_gap

    left_y = draw_section_label(c, "Ingredientes", left_x, body_top, col_w)
    ingredient_style = ParagraphStyle("ingredients", parent=s["body"], fontSize=8.5,
                                      leading=11.2, spaceAfter=0)
    left_y = draw_paragraph(c, bullet_html(recipe.ingredients), left_x, left_y,
                            col_w, ingredient_style) - 13
    left_y = draw_section_label(c, "Combina com", left_x, left_y, col_w)
    pairing_style = ParagraphStyle("pairing", parent=s["small"], fontSize=8.2,
                                   leading=10.8)
    left_y = draw_paragraph(c, clean_inline(recipe.pairing), left_x, left_y,
                            col_w, pairing_style)

    right_y = draw_section_label(c, "Modo de preparo", right_x, body_top, col_w)
    step_style = ParagraphStyle("steps", parent=s["body"], fontSize=8.5,
                                leading=11.2, spaceAfter=0)
    right_y = draw_paragraph(c, numbered_html(recipe.steps), right_x, right_y,
                             col_w, step_style) - 13
    right_y = draw_section_label(c, "Conservação", right_x, right_y, col_w)
    storage_style = ParagraphStyle("storage", parent=s["small"], fontSize=8.0,
                                   leading=10.5)
    right_y = draw_paragraph(c, clean_inline(recipe.storage), right_x, right_y,
                             col_w, storage_style)

    lower = min(left_y, right_y)
    if lower < 42:
        raise ValueError(f"Conteúdo da receita {recipe.number} excede a área útil do PDF (y={lower:.1f}).")
    draw_footer(c, page_num, f"{label}  ·  {edition_label.upper()}")
    c.showPage()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manuscript", required=True, type=Path)
    parser.add_argument("--images", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--cover", type=Path, default=None)
    parser.add_argument("--bonus-label", default="BÔNUS 1")
    parser.add_argument("--edition-label", default="Português do Brasil")
    parser.add_argument("--font-dir", type=Path,
                        default=Path("/usr/share/fonts/truetype/dejavu"))
    args = parser.parse_args()

    if not args.manuscript.is_file():
        raise SystemExit(f"Manuscrito não encontrado: {args.manuscript}")
    cover = args.cover or args.images / "capa.jpg"
    if not cover.is_file():
        raise SystemExit(f"Capa não encontrada: {cover}")
    manuscript = parse_manuscript(args.manuscript)
    if len(manuscript.recipes) != 15:
        raise SystemExit(f"Esperadas 15 receitas; encontradas {len(manuscript.recipes)}.")
    image_paths = {}
    for recipe in manuscript.recipes:
        matches = list(args.images.glob(f"{recipe.number:02d}_*.jpg"))
        if len(matches) != 1:
            raise SystemExit(f"Receita {recipe.number}: esperado 1 JPG, encontrados {len(matches)}.")
        image_paths[recipe.number] = matches[0]

    register_fonts(args.font_dir)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="bonus_pdf_") as tmp:
        temp_dir = Path(tmp)
        c = canvas.Canvas(str(args.output), pagesize=A4, pageCompression=1)
        c.setTitle(manuscript.title)
        c.setSubject(manuscript.subtitle)
        c.setCreator("Bônus Low Carb — renderização A4")
        draw_cover(c, cover, manuscript, args.bonus_label, args.edition_label, temp_dir)
        s = styles()
        draw_intro(c, manuscript, s, args.bonus_label, 2)
        draw_contents(c, manuscript.recipes, 3)
        for recipe in manuscript.recipes:
            draw_recipe(c, recipe, image_paths[recipe.number], recipe.number + 3,
                        args.bonus_label, args.edition_label, temp_dir)
        c.save()
    print(f"PDF criado: {args.output} ({len(manuscript.recipes) + 3} páginas)")


if __name__ == "__main__":
    main()
