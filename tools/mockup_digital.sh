#!/usr/bin/env bash
# Mockup DIGITAL do ebook pt-PT (ImageMagick puro):
#   tools/mockup_digital.sh <capa.png> <pagina.png> <fundo.jpg> <saida.png>
# Tablet (ecrã = capa real do PDF) + telemóvel (ecrã = topo da receita 01),
# molduras desenhadas em código (geometria conhecida), sombras e rodapé dourado.
set -euo pipefail

CAPA="${1:?capa.png}"
PAG="${2:?pagina.png}"
FUNDO="${3:?fundo.jpg}"
SAIDA="${4:?saida.png}"
T=/tmp/mockup_digital_work
rm -rf "$T"; mkdir -p "$T"
FONT_B=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf
FONT_R=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf

FW=$(identify -format %w "$FUNDO")
FH=$(identify -format %h "$FUNDO")

# ================= TABLET (retrato, ecrã = capa) =================
SCR_W=486; SCR_H=707; BEZ=18
TBL_W=$((SCR_W + 2*BEZ)); TBL_H=$((SCR_H + 2*BEZ))
convert "$CAPA" -resize "${SCR_W}x${SCR_H}!" "$T/tbl_screen.png"
convert -size ${TBL_W}x${TBL_H} xc:none -fill '#14161a' \
  -draw "roundrectangle 0,0,$((TBL_W-1)),$((TBL_H-1)),30,30" \
  "$T/tbl_frame.png"
convert "$T/tbl_frame.png" "$T/tbl_screen.png" -gravity center -compose over -composite \
  -fill none -stroke '#3d434a' -strokewidth 2 \
  -draw "roundrectangle 1,1,$((TBL_W-2)),$((TBL_H-2)),30,30" \
  -stroke none -fill '#2b3138' -draw "circle $((TBL_W/2)),9 $((TBL_W/2)),15" \
  "$T/tablet.png"
convert "$T/tablet.png" -alpha set -background black -shadow 60x34+10+26 "$T/tbl_sh.png"
convert "$T/tbl_sh.png" "$T/tablet.png" -gravity center -compose over -composite \
  "$T/tablet_final.png"

# ================= TELEMÓVEL (ecrã = topo da receita) =================
PSW=250; PSH=540; PBEZ=12
PHN_W=$((PSW + 2*PBEZ)); PHN_H=$((PSH + 2*PBEZ))
convert "$PAG" -resize x${PSH} \
  -gravity north -crop ${PSW}x${PSH}+0+0 +repage "$T/phn_screen.png"
convert -size ${PHN_W}x${PHN_H} xc:none -fill '#14161a' \
  -draw "roundrectangle 0,0,$((PHN_W-1)),$((PHN_H-1)),34,34" "$T/phn_frame.png"
convert "$T/phn_frame.png" "$T/phn_screen.png" -gravity center -compose over -composite \
  -fill none -stroke '#3d434a' -strokewidth 2 \
  -draw "roundrectangle 1,1,$((PHN_W-2)),$((PHN_H-2)),34,34" \
  -stroke none -fill '#2b3138' -draw "circle $((PHN_W/2)),$((PHN_H-16)),$((PHN_W/2)),$((PHN_H-22))" \
  "$T/phone.png"
convert "$T/phone.png" -alpha set -background black -shadow 50x30+8+22 "$T/phn_sh.png"
convert "$T/phn_sh.png" "$T/phone.png" -gravity center -compose over -composite \
  "$T/phone_final.png"

# ================= COMPOSIÇÃO =================
convert "$FUNDO" \
  \( "$T/tablet_final.png" \) -geometry +430+52 -compose over -composite \
  \( "$T/phone_final.png" \) -geometry +1080+170 -compose over -composite \
  -fill 'rgba(8,12,10,0.55)' -draw "rectangle 0,$((FH-118)) $FW,$FH" \
  -font "$FONT_B" -pointsize 40 -fill '#d9b64a' \
  -gravity southwest -annotate +48+60 "EBOOK DIGITAL  ·  50 RECEITAS LOW CARB  ·  VERSÃO DE PORTUGAL" \
  -font "$FONT_R" -pointsize 23 -fill '#efe9dc' \
  -gravity southwest -annotate +50+24 "PDF + HTML · 69 páginas · português de Portugal (pt-PT) · Série Cozinha Prática" \
  "$SAIDA"

identify "$SAIDA"
