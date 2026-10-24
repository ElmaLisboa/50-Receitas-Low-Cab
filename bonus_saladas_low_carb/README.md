# Bônus adicionais — 10 Receitas de Saladas Low Carb

Esta pasta organiza a criação de **três bônus independentes** para presentear os clientes do ebook principal. O ebook principal já contém as 10 receitas de saladas, orientações gerais, lista de compras e planejamento de refeições; os bônus novos devem complementar o material sem repetir esses conteúdos.

## Bônus planejados

1. **Caderno de Molhos e Vinagretas Low Carb** — 15 receitas originais.
2. **Proteínas Práticas para Refeições Low Carb** — 10 preparações, incluindo opções vegetarianas e veganas.
3. **Lanches Low Carb para Levar** — 10 receitas práticas.

Cada bônus terá uma versão própria em cada uma das 13 variantes abaixo — **39 manuscritos ao todo**:

| Código | Idioma/variante |
|---|---|
| `pt-BR` | Português do Brasil |
| `pt-PT` | Português de Portugal |
| `es` | Espanhol neutro/internacional |
| `nl-NL` | Holandês dos Países Baixos |
| `en-GB` | Inglês britânico |
| `it-IT` | Italiano da Itália |
| `ja-JP` | Japonês do Japão |
| `en-US` | Inglês americano |
| `de-DE` | Alemão da Alemanha |
| `hi-IN` | Hindi da Índia, em devanágari |
| `fr-FR` | Francês da França |
| `zh-TW` | Chinês tradicional de Taiwan |
| `zh-CN` | Chinês simplificado da China continental |

## Estrutura dos manuscritos

Cada pasta de bônus contém um arquivo Markdown por variante linguística:

```text
manuscritos/
├── 01_molhos_vinagretas/<locale>.md
├── 02_proteinas_praticas/<locale>.md
└── 03_lanches_para_levar/<locale>.md
```

Os manuscritos ainda não produzidos são modelos vazios. Status atual:

- **Bônus 1 — Molhos e Vinagretas:** rascunhos em `pt-BR`, `pt-PT`, `es` e `nl-NL`; manuscritos em `manuscritos/01_molhos_vinagretas/`. Capa premium e 15 imagens em `imagens/01_molhos_vinagretas/`. PDF de revisão `pt-BR` atualizado em `pdfs/01_molhos_vinagretas/pt-BR.pdf`.
- **Bônus 1 — idiomas pendentes:** `en-GB`, `it-IT`, `ja-JP`, `en-US`, `de-DE`, `hi-IN`, `fr-FR`, `zh-TW` e `zh-CN`.
- **Bônus 2 — Proteínas Práticas (`pt-BR`):** rascunho completo em `manuscritos/02_proteinas_praticas/pt-BR.md`; traduções pendentes.
- **Bônus 3 — Lanches (`pt-BR`):** rascunho completo em `manuscritos/03_lanches_para_levar/pt-BR.md`; traduções pendentes.

## Fluxo de trabalho recomendado

1. Concluir o **Bônus 1 em todas as 13 variantes**, começando pelo texto-base `pt-BR` e localizando cada idioma restante a partir do conteúdo aprovado.
2. Revisar e aprovar o conjunto completo do Bônus 1 antes de iniciar outro bônus.
3. Só depois de concluir o Bônus 1, repetir o processo para o **Bônus 2** e, em seguida, para o **Bônus 3**.
4. Produzir um bônus e um idioma por execução, preservar quantidades e conteúdo e salvar cada versão no arquivo correspondente.

O prompt reutilizável está em [`PROMPT_MESTRE.md`](PROMPT_MESTRE.md). Para evitar respostas truncadas e divergências entre versões, use-o para gerar **um bônus em um idioma por execução**.

## Renderização de PDF

O gerador está em `tools/render_pdf.py`. Instale as dependências listadas em `requirements-pdf.txt` e execute-o com os caminhos do manuscrito, das imagens e do PDF de saída. Exemplo para a versão brasileira do Bônus 1:

```bash
python -m pip install -r bonus_saladas_low_carb/requirements-pdf.txt
python bonus_saladas_low_carb/tools/render_pdf.py \
  --manuscript bonus_saladas_low_carb/manuscritos/01_molhos_vinagretas/pt-BR.md \
  --images bonus_saladas_low_carb/imagens/01_molhos_vinagretas \
  --output bonus_saladas_low_carb/pdfs/01_molhos_vinagretas/pt-BR.pdf \
  --bonus-label "BÔNUS 1" \
  --edition-label "Português do Brasil"
```
