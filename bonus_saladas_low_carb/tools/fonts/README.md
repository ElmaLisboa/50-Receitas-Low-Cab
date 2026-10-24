# Fontes para PDFs multilíngues

A renderização em latim usa DejaVu Sans/Serif do sistema. Hindi e japonês/chinês precisam dos TTFs Noto abaixo; os arquivos de fonte não são versionados neste repositório. Os PDFs incorporam os glifos usados na edição.

## Pacotes Noto necessários

- `hi-IN`: `@expo-google-fonts/noto-sans-devanagari@0.4.1`
- `ja-JP`: `@expo-google-fonts/noto-sans-jp@0.4.4`
- `zh-TW`: `@expo-google-fonts/noto-sans-tc@0.4.4`
- `zh-CN`: `@expo-google-fonts/noto-sans-sc@0.4.4`

Baixe os pacotes com `npm pack` e extraia apenas os pesos regular e bold para esta estrutura (ou para outra pasta passada a `--script-fonts-dir`):

```bash
mkdir -p /tmp/noto-pkgs
npm pack --pack-destination /tmp/noto-pkgs @expo-google-fonts/noto-sans-devanagari@0.4.1
npm pack --pack-destination /tmp/noto-pkgs @expo-google-fonts/noto-sans-jp@0.4.4
npm pack --pack-destination /tmp/noto-pkgs @expo-google-fonts/noto-sans-tc@0.4.4
npm pack --pack-destination /tmp/noto-pkgs @expo-google-fonts/noto-sans-sc@0.4.4
```

Estrutura de diretórios:

```text
fonts/
├── hi-IN/NotoSans-Regular.ttf
├── hi-IN/NotoSans-Bold.ttf
├── ja-JP/NotoSans-Regular.ttf
├── ja-JP/NotoSans-Bold.ttf
├── zh-TW/NotoSans-Regular.ttf
├── zh-TW/NotoSans-Bold.ttf
├── zh-CN/NotoSans-Regular.ttf
└── zh-CN/NotoSans-Bold.ttf
```

Exemplo de extração, após baixar os quatro `.tgz` para `/tmp/noto-pkgs`:

```bash
mkdir -p /tmp/bonus-fonts/{hi-IN,ja-JP,zh-TW,zh-CN}

tar -xOzf /tmp/noto-pkgs/expo-google-fonts-noto-sans-devanagari-0.4.1.tgz \
  package/400Regular/NotoSansDevanagari_400Regular.ttf > /tmp/bonus-fonts/hi-IN/NotoSans-Regular.ttf
tar -xOzf /tmp/noto-pkgs/expo-google-fonts-noto-sans-devanagari-0.4.1.tgz \
  package/700Bold/NotoSansDevanagari_700Bold.ttf > /tmp/bonus-fonts/hi-IN/NotoSans-Bold.ttf

tar -xOzf /tmp/noto-pkgs/expo-google-fonts-noto-sans-jp-0.4.4.tgz \
  package/400Regular/NotoSansJP_400Regular.ttf > /tmp/bonus-fonts/ja-JP/NotoSans-Regular.ttf
tar -xOzf /tmp/noto-pkgs/expo-google-fonts-noto-sans-jp-0.4.4.tgz \
  package/700Bold/NotoSansJP_700Bold.ttf > /tmp/bonus-fonts/ja-JP/NotoSans-Bold.ttf

tar -xOzf /tmp/noto-pkgs/expo-google-fonts-noto-sans-tc-0.4.4.tgz \
  package/400Regular/NotoSansTC_400Regular.ttf > /tmp/bonus-fonts/zh-TW/NotoSans-Regular.ttf
tar -xOzf /tmp/noto-pkgs/expo-google-fonts-noto-sans-tc-0.4.4.tgz \
  package/700Bold/NotoSansTC_700Bold.ttf > /tmp/bonus-fonts/zh-TW/NotoSans-Bold.ttf

tar -xOzf /tmp/noto-pkgs/expo-google-fonts-noto-sans-sc-0.4.4.tgz \
  package/400Regular/NotoSansSC_400Regular.ttf > /tmp/bonus-fonts/zh-CN/NotoSans-Regular.ttf
tar -xOzf /tmp/noto-pkgs/expo-google-fonts-noto-sans-sc-0.4.4.tgz \
  package/700Bold/NotoSansSC_700Bold.ttf > /tmp/bonus-fonts/zh-CN/NotoSans-Bold.ttf
```

Os pacotes contêm as licenças das fontes; mantenha os avisos de licença ao redistribuir os TTFs. As fontes Noto são distribuídas sob a SIL Open Font License.
