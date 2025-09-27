# DIO-AzureTranslatorOpenAI


## Funcionalidades

Este projeto permite:

* **Extração de texto de páginas web** : Utiliza `requests` e `BeautifulSoup` para acessar uma URL e extrair o texto limpo da página, removendo scripts e estilos.
* **Tradução automática de textos** : Integração com a API do Azure Translator e OpenAI (via LangChain) para traduzir textos extraídos para o idioma desejado, com resposta em formato Markdown.
* **Automação de tradução de artigos** : Função que recebe uma URL, extrai o texto e retorna a tradução completa do artigo para português.
* **Exemplo de uso em notebook** : O notebook demonstra como instalar dependências, extrair texto de uma URL e traduzir automaticamente usando a API do Azure/OpenAI.

## Como usar

1. Instale as dependências:

   ```
   pip install requests beautifulsoup4 openai langchain-openai python-docx
   ```
2. Configure sua chave de API do Azure Translator e OpenAI.
3. Utilize as funções do notebook ou do script para extrair e traduzir textos de páginas web.

## Exemplo de código

```
from langchain_openai import AzureChatOpenAI

client = AzureChatOpenAI(
    azure_endpoint="<SEU ENDPOINT>",
    api_key="<SUA API KEY>",
    api_version="2024-10-21",
    deployment_name="gpt-4o-mini"
)

def extract_text_from_url(url):
    # ... função conforme notebook ...
    pass

def translate_article(txt, lang):
    # ... função conforme notebook ...
    pass

def tradutor_de_url(url):
    text = extract_text_from_url(url)
    return translate_article(text, "pt-br")
```
