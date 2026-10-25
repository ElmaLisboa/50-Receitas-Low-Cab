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

Os manuscritos ainda não finalizados permanecem em rascunho. Status atual:

- **Bônus 1 — Molhos e Vinagretas:** manuscritos e PDFs concluídos nas 13 variantes; o usuário declarou o bônus concluído. Os PDFs (18 páginas cada) estão em `pdfs/01_molhos_vinagretas/`; a capa premium e as 15 imagens estão em `imagens/01_molhos_vinagretas/`. Os registros de aprovação individuais das traduções foram mantidos como estavam.
- **Bônus 2 — Proteínas Práticas:** manuscrito `pt-BR` revisado linguisticamente e aprovado pelo usuário em `manuscritos/02_proteinas_praticas/pt-BR.md`; PDF em `pdfs/02_proteinas_praticas/pt-BR.pdf` (13 páginas, com capa fotográfica). Os outros 12 manuscritos foram traduzidos e revisados linguisticamente, mas continuam pendentes de aprovação; seus PDFs preliminares atualizados (13 páginas cada) estão em `pdfs/02_proteinas_praticas/`. As 10 imagens das receitas e a capa separada estão em `imagens/02_proteinas_praticas/`.
- **Bônus 3 — Lanches (`pt-BR`):** rascunho em `manuscritos/03_lanches_para_levar/pt-BR.md`; ainda não iniciado. As traduções estão pendentes.

## Fluxo de trabalho recomendado

1. **Bônus 1 concluído** nas 13 variantes, com PDFs gerados.
2. Concluir o **Bônus 2** nas 13 variantes, revisar os manuscritos, produzir a capa e os PDFs correspondentes.
3. Iniciar o **Bônus 3** somente depois de concluir todas as 13 variantes do Bônus 2.
4. Produzir um bônus e um idioma por execução, preservar quantidades e conteúdo e salvar cada versão no arquivo correspondente.

O prompt reutilizável está em [`PROMPT_MESTRE.md`](PROMPT_MESTRE.md). Para evitar respostas truncadas e divergências entre versões, use-o para gerar **um bônus em um idioma por execução**.

## Renderização de PDF

O gerador está em `tools/render_pdf.py`. Ele identifica o locale pelo nome do manuscrito e o bônus pelo parâmetro `--bonus-number`; traduz capa, sumário e rótulos internos. Para o Bônus 2, use `--bonus-number 2`. Se ainda não houver `capa.jpg` para o Bônus 2, o PDF usa uma capa gráfica premium provisória. Instale as dependências listadas em `requirements-pdf.txt` e informe os caminhos do manuscrito, das imagens e do PDF de saída. Exemplo para a versão brasileira do Bônus 1:

```bash
python -m pip install -r bonus_saladas_low_carb/requirements-pdf.txt
python bonus_saladas_low_carb/tools/render_pdf.py \
  --manuscript bonus_saladas_low_carb/manuscritos/01_molhos_vinagretas/pt-BR.md \
  --images bonus_saladas_low_carb/imagens/01_molhos_vinagretas \
  --output bonus_saladas_low_carb/pdfs/01_molhos_vinagretas/pt-BR.pdf
```

Exemplo para o PDF brasileiro de revisão do Bônus 2:

```bash
python bonus_saladas_low_carb/tools/render_pdf.py \
  --bonus-number 2 \
  --manuscript bonus_saladas_low_carb/manuscritos/02_proteinas_praticas/pt-BR.md \
  --images bonus_saladas_low_carb/imagens/02_proteinas_praticas \
  --output bonus_saladas_low_carb/pdfs/02_proteinas_praticas/pt-BR.pdf
```

Para `hi-IN`, `ja-JP`, `zh-TW` e `zh-CN`, obtenha as fontes Noto e informe `--script-fonts-dir`; veja as instruções em [`tools/fonts/README.md`](tools/fonts/README.md). A lista de fontes é externa ao repositório, e os PDFs resultantes já incorporam os glifos necessários.
