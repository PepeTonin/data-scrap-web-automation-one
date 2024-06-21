<h1 text-align="center">Automação Web para Data Scraping</h1>

## Descrição

Este projeto é uma solução de automação web desenvolvida em Python que utiliza o Selenium WebDriver para coletar dados de uma página web e salvar esses dados em um arquivo de texto. Em seguida, um segundo script é usado para filtrar e processar os dados capturados, gerando um arquivo Excel com as informações desejadas.

## Funcionalidades

- Automação da coleta de dados de uma página web usando Selenium WebDriver.
- Parsing dos dados para obter apenas as informações necessárias.
- Geração de um arquivo Excel com os dados capturados.

## Tecnologias utilizadas

<img src="https://img.shields.io/badge/Python-3.11.3-blue.svg?style=flat-square" alt="python version">
<img src="https://img.shields.io/badge/selenium-4.13.0-green.svg?style=flat-square" alt="selenium version">
<img src="https://img.shields.io/badge/webDriver-4.0.1-green.svg?style=flat-square" alt="selenium version">
<img src="https://img.shields.io/badge/Beautiful_Soup-4.12.2-blue.svg?style=flat-square" alt="beautiful soup version">
<img src="https://img.shields.io/badge/pandas-2.0.1-blue.svg?style=flat-square" alt="pandas version">

## Requisitos

Para rodar este projeto, você precisará ter o [Python 3.11](https://www.python.org/) instalado em sua máquina, além das bibliotecas [Selenium](https://selenium-python.readthedocs.io/), [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/#installing-beautiful-soup), [pandas](https://pandas.pydata.org/docs/#) e [tqdm](https://tqdm.github.io). Além disso, será necessário configurar o [WebDriver](https://selenium-python.readthedocs.io/api.html).

## Como utilizar

1. Clone o repositório para sua máquina local.

```bash
git clone https://github.com/PepeTonin/data-scrap-web-automation-one.git
```

2. Navegue até o diretório do projeto.

```bash
cd data-scrap-web-automation-one
```

3. No arquivo ``data_extractor.py``, insira a url da página web que deseja capturar os dados. (Lembrando que esse script só será capaz de capturar os dados da página que ele foi planejado).

4. Execute o código em ``data_extractor.py``.

```bash
python data_extractor.py
```

5. O script automatizará a navegação na página web e salvará os dados coletados em um arquivo chamado ``data.txt``

6. Execute o script ``data_parser.py`` para processar os dados coletados e gerar o arquivo Excel.

```bash
python data_parser.py
```