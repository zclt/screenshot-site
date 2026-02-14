# Screenshot Site

Uma ferramenta simples para capturar screenshots de páginas web usando Selenium e Chrome headless.

## 🚀 Instalação

Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

## 📸 Como Usar

Execute o script passando a URL do site que deseja capturar como argumento:

```bash
python main.py https://www.example.com
```

### Exemplos

```bash
# Capturar screenshot do Google
python main.py https://www.google.com

# Capturar screenshot do GitHub
python main.py https://www.github.com

# Capturar screenshot de qualquer site
python main.py https://seu-site-aqui.com
```

## 📋 Resultado

O script gera um arquivo de imagem PNG com timestamp no formato:
```
screenshot-YYYYMMDD_HHMMSS.png
```

Exemplo: `screenshot-20260211_081349.png`

## ⚙️ Funcionalidades

- ✅ Captura de screenshot de qualquer URL
- ✅ Navegador Chrome headless (sem interface gráfica)
- ✅ Ignora erros de certificado SSL
- ✅ Nome de arquivo único com timestamp
- ✅ Suporte a linha de comando

## 🔧 Dependências

- `selenium` - Automação do navegador
- `webdriver-manager` - Gerenciamento automático do ChromeDriver
- `Pillow` - Processamento de imagens
- `argparse` - Parsing de argumentos de linha de comando
- `datetime` - Geração de timestamp