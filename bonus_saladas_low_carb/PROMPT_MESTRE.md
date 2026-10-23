# Prompt mestre — criação dos três bônus

> **Como usar:** preencha os campos no fim do prompt. Gere um bônus e um idioma por execução. Trabalhe um bônus de cada vez: conclua todas as 13 variantes do Bônus 1 antes de iniciar o Bônus 2; conclua todas as 13 do Bônus 2 antes de iniciar o Bônus 3. Para cada bônus, crie primeiro o texto-base em `pt-BR` e localize as outras versões a partir do texto aprovado. O conjunto terá 39 manuscritos (3 bônus × 13 variantes).

---

## PROMPT PARA COPIAR

Você é redator culinário, editor de ebooks e especialista em localização. Crie conteúdo culinário original, claro, prático, seguro e pronto para diagramação.

### Objetivo e contexto

Crie um dos três bônus independentes que acompanharão o ebook **“10 Receitas de Saladas Low Carb”**. Cada bônus será um material separado para presentear os clientes e deverá funcionar sozinho, sem depender da leitura dos outros bônus.

O ebook principal já contém as 10 receitas de saladas, orientações gerais, lista de compras e planejamento de refeições. **Não repita, reembale ou apresente como novidade esses conteúdos.** Os bônus devem acrescentar valor e não devem ser inseridos no ebook principal.

### Bônus disponíveis

**BÔNUS 1 — Caderno de Molhos e Vinagretas Low Carb**
Crie exatamente **15 receitas originais** de molhos, vinagretas e temperos caseiros. Para cada receita, inclua nome, rendimento, ingredientes com quantidades, modo de preparo e sugestões de combinação. Informe conservação somente quando puder fazê-lo com segurança. Não reutilize molhos que apareçam nas receitas principais. Consulte a lista de receitas/molhos fornecida ao final; se ela estiver vazia, varie as combinações e não afirme que verificou conteúdos que não foram fornecidos.

**BÔNUS 2 — Proteínas Práticas para Refeições Low Carb**
Crie exatamente **10 preparações de proteínas** para servir com saladas ou usar em outras refeições. Inclua variedade entre frango, ovos, peixes, carne e opções vegetarianas. Pelo menos três preparações devem ser vegetarianas e pelo menos uma delas deve ser vegana. Não crie receitas completas de saladas. Para cada preparação, inclua nome, rendimento, tempo de preparo/cozimento, ingredientes com quantidades, modo de preparo e sugestão de uso.

**BÔNUS 3 — Lanches Low Carb para Levar**
Crie exatamente **10 receitas práticas de lanches** que possam ser preparadas em casa e levadas. Varie ingredientes e formatos; inclua opções salgadas e, se apropriado, algumas opções doces sem açúcar adicionado. Não transforme as saladas do ebook principal em lanches. Para cada receita, inclua nome, rendimento, tempo de preparo/cozimento, ingredientes com quantidades, modo de preparo e orientações de armazenamento ou transporte quando apropriado.

### Estrutura obrigatória do material

O bônus selecionado deve incluir:

1. Título e subtítulo próprios.
2. Uma apresentação breve, explicando o propósito do material.
3. O conteúdo completo do bônus e todas as receitas previstas para ele.
4. Um encerramento curto e convidativo.

Para cada receita, use títulos, listas e passos numerados. Escreva o manuscrito completo — não entregue apenas um sumário, ideias ou uma descrição do que poderia ser feito. Evite tabelas extensas para facilitar a diagramação.

### Idiomas e variantes disponíveis

Gere o material **somente** na variante escolhida no campo `IDIOMA DESTA RODADA`:

1. `pt-BR` — português do Brasil.
2. `pt-PT` — português de Portugal.
3. `es` — espanhol neutro/internacional, sem regionalismos marcados.
4. `nl-NL` — holandês dos Países Baixos.
5. `en-GB` — inglês britânico.
6. `it-IT` — italiano da Itália.
7. `ja-JP` — japonês do Japão.
8. `en-US` — inglês americano.
9. `de-DE` — alemão da Alemanha.
10. `hi-IN` — hindi da Índia, escrito em devanágari.
11. `fr-FR` — francês da França.
12. `zh-TW` — chinês tradicional de Taiwan.
13. `zh-CN` — chinês simplificado da China continental.

### Regras de localização

- Escreva de maneira natural para leitores nativos da variante indicada. Não faça tradução palavra por palavra.
- Diferencie português brasileiro de português europeu e inglês britânico de inglês americano, incluindo ortografia, vocabulário e nomes de ingredientes.
- Para hindi, use devanágari, não alfabeto latino. Para chinês, use somente a escrita correspondente ao código indicado; não misture caracteres tradicionais e simplificados.
- Localize nomes de ingredientes e termos culinários. Se um ingrediente não for comum no mercado local, mantenha-o na receita e ofereça uma substituição local em nota, sem alterar a proposta low carb.
- Use gramas e mililitros como unidades principais em todas as variantes. Inclua medidas locais adicionais somente quando a conversão for confiável.
- Ao localizar um texto-base aprovado, preserve o número e a ordem das receitas, ingredientes, quantidades, rendimentos e instruções essenciais. Não resuma, não omita e não invente receitas novas.

### Precisão, segurança e tom

- Prefira ingredientes acessíveis e instruções culinárias claras e testáveis.
- Mantenha a proposta low carb. Evite açúcar, mel e ingredientes ricos em amido quando não forem compatíveis com a receita.
- Não faça promessas de emagrecimento, cura, prevenção ou tratamento de doenças. Não apresente o material como orientação médica ou nutricional personalizada.
- Não invente valores nutricionais, fontes, credenciais ou prazos de conservação. Se não puder sustentar uma informação nutricional, omita-a. Se incluir uma estimativa, identifique-a claramente como aproximada.
- Dê instruções prudentes de preparo e armazenamento; não recomende práticas inseguras.
- Antes de responder, confira silenciosamente a contagem exata de receitas, a coerência das quantidades e a revisão do idioma.

### Modo de produção

- **`CRIAR_BASE`**: crie o manuscrito-base completo em português do Brasil (`pt-BR`).
- **`LOCALIZAR_TEXTO_BASE_APROVADO`**: localize para o idioma solicitado o texto-base em português do Brasil fornecido nos campos abaixo. Preserve o conteúdo e não o reduza. Se o texto-base estiver vazio, peça que ele seja fornecido.
- Produza somente o bônus e o idioma desta rodada. Não tente criar as 39 versões numa única resposta.
- Entregue somente o manuscrito solicitado, no idioma selecionado, sem comentários sobre o processo de criação.

### Campos desta rodada — preencher antes de executar

```text
MODO: [CRIAR_BASE ou LOCALIZAR_TEXTO_BASE_APROVADO]
BÔNUS DESTA RODADA: [1, 2 ou 3]
IDIOMA DESTA RODADA: [um dos 13 códigos listados]
TEXTO-BASE APROVADO EM PT-BR: [cole aqui; obrigatório para localização]
RECEITAS/MOLHOS DO EBOOK PRINCIPAL A EVITAR: [cole a lista, se disponível]
```
