#!/usr/bin/env bash
# Mockup do ebook pt-PT (ImageMagick puro):
#   tools/mockup.sh <capa.png> <pagina.png> <fundo.jpg> <saida.png>
# Capa grande à esquerda com bloco de páginas creme, página interna à direita,
# sombras suaves, rodapé dourado com identidade do volume.
set -euo pipefail

CAPA="${1:?capa.png}"
PAG="${2:?pagina.png}"
FUNDO="${3:?fundo.jpg}"
SAIDA="${4:?saida.png}"
T=/tmp/mockup_work
rm -rf "$T"; mkdir -p "$T"
FONT_B=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf
FONT_R=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf

FW=$(identify -format %w "$FUNDO")
FH=$(identify -format %h "$FUNDO")

# ---------- capa: altura 78% do fundo + aresta creme de 16px + rotação -4° ----------
TH=$(python3 -c "print(int($FH*0.78))")
convert "$CAPA" -resize x"$TH" \
  -gravity east -background '#e8e2d4' -splice 16x0 \
  -rotate -4 "$T/capa_rot.png"
convert "$T/capa_rot.png" -alpha set -background black \
  -shadow 50x30+18+22 "$T/capa_sh.png"
convert "$T/capa_sh.png" "$T/capa_rot.png" -gravity center \
  -compose over -composite "$T/capa_final.png"

# ---------- página interna: altura 70% + rotação +5° ----------
PH=$(python3 -c "print(int($FH*0.70))")
convert "$PAG" -resize x"$PH" -rotate 5 "$T/pag_rot.png"
convert "$T/pag_rot.png" -alpha set -background black \
  -shadow 45x26+14+18 "$T/pag_sh.png"
convert "$T/pag_sh.png" "$T/pag_rot.png" -gravity center \
  -compose over -composite "$T/pag_final.png"

# ---------- composição ----------
convert "$FUNDO" \
  \( "$T/pag_final.png" \) -geometry +980+110 -compose over -composite \
  \( "$T/capa_final.png" \) -geometry +300+60 -compose over -composite \
  -fill 'rgba(8,12,10,0.55)' -draw "rectangle 0,$((FH-118)) $FW,$FH" \
  -font "$FONT_B" -pointsize 40 -fill '#d9b64a' \
  -gravity southwest -annotate +48+60 "50 RECEITAS LOW CARB  ·  VERSÃO DE PORTUGAL" \
  -font "$FONT_R" -pointsize 23 -fill '#efe9dc' \
  -gravity southwest -annotate +50+24 "PDF + HTML · 69 páginas · português de Portugal (pt-PT) · Série Cozinha Prática" \
  "$SAIDA"

identify "$SAIDA"
