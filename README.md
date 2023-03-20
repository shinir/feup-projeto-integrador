# FEUP-Projeto-Integrador

## Index
- [Índice](#índice)
- [Contexto do Projeto](#contexto-do-projeto)
- [Objetivos](#objetivos)
- [Modo de utilização](#modo-de-utilização)

## Contexto do Projeto

Os resultados das colocações no ensino superior são todos os anos colocados no sítio Web da DGES, em https://dges.gov.pt/coloc/AAAA/, em que AAAA designa o ano. Neste momento existem dados de 2018 a 2022. 
Para cada estabelecimento e curso, é possível consultar a lista de estudantes colocados (com nº de identificação parcial e nome), a lista ordenada de candidatos (com nº de ordem, nº de identificação parcial, nome, nota de candidatura e nº de opção) e a nota do último colocado pelo contingente geral. É possível também extrair estatísticas gerais em Excel.
Estes dados são analisados pelas direções dos cursos e das escolas (para além da própria comunicação social), para compreender a adequação da oferta em relação à procura de cada curso (nº de vagas versus nº candidatos versus nº colocados, nota mínima, etc.), a procura relativa entre cursos similares em diferentes escolas, a procura relativa entre diferentes cursos da mesma instituição, as tendências de evolução da procura ao longo dos anos, etc.
Ora, uma análise simplista baseada apenas nas notas dos últimos colocados pode ser enganadora, devido à dependência do nºs de vagas, entre outros aspetos. 
Assim, vários responsáveis procuram fazer análises mais sofisticadas e esclarecedores (mas muito trabalhosas), como na L.EIC em https://docs.google.com/presentation/d/18pKq8S3ZepN9HG1UeCgFb-gIeE1uZSvjdVWMNUIEAj4/edit?usp=sharing e https://docs.google.com/presentation/d/18pKq8S3ZepN9HG1UeCgFb-gIeE1uZSvjdVWMNUIEAj4/edit?usp=sharing."

## Objetivos

Desenvolver uma aplicação capaz de extrair do site da DGES os dados de candidaturas e colocações no ensino superior e produzir estatísticas e visualizações diversas (como as referidas nos links acima), mediamente parâmetros fornecidos pelo utilizador (cursos,  escolas e anos em análise, etc.), para compreender a adequação da oferta à procura, a procura relativa entre cursos, escolas e anos, etc. A aplicação deve ser capaz de produzir automaticamente os gráficos e tabelas indicados nos links acima. 
A aplicação deve ter uma interface Web, podendo opcionalmente ser também adaptável a dispositivos móveis. Os dados poderão ser extraídos do site da DGES por web scraping para uma base de dados própria, para facilitar a produção de estatísticas e gráficos de uma forma mais expedita e interativa.

## Modo de utilização

### `scrapper.py`

O script encontra-se estruturado de forma a imprimir os dados obtidos num ficheiro `.csv` . 
Na sua utilização é necessário dar um nome ao ficheiro de output.

**Download dos candidatos:**

```sh
python3 scrapper.py candidatos
```

**Download dos colocados:**

```sh
python3 scrapper.py colocados
```




