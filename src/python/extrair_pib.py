import pandas as pd
import requests
import sqlalchemy
import os
import time
from tqdm import tqdm

BASE_DIR = os.path.abspath('.')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, 'data')
TABELAS_DIR = os.path.join(BASE_DIR, 'tabelas')

str_banco = 'sqlite:///' + os.path.join(DATA_DIR, 'banco.db')
engine = sqlalchemy.create_engine(str_banco)
conn = engine.connect()

link = 'https://apidatalake.tesouro.gov.br/ords/siconfi/tt/entes'
r = requests.get(link)
x = r.json()
entes = pd.DataFrame(x['items'])
municipios = entes.query('populacao > 100000 & populacao <300000').cod_ibge
time.sleep(1)

pib = pd.read_excel(
    os.path.join(DATA_DIR,'PIB dos Municípios - base de dados 2010-2018.xls')
    )

pib_faixa = pib[pib['Código do Município'].isin(municipios)]
pib_faixa.to_sql('pib',
                conn,
                if_exists='replace')

pib_2018 = pib_faixa.query('Ano == 2018')
#pib_2018[['Código do Município','Produto Interno Bruto per capita, \na preços correntes\n(R$ 1,00)']]
amostra = pib_2018[['Código do Município','Produto Interno Bruto per capita, \na preços correntes\n(R$ 1,00)']]
amostra.columns = ['cod_ibge', 'pib_per_capita']
amostra.to_csv(os.path.join(TABELAS_DIR,'pib_per_capita.csv'))
amostra = amostra.sort_values('pib_per_capita', ascending=False)
amostra = amostra.reset_index()
amostra.query("cod_ibge == 4300604")

#Descobrir posição do ranking
teste = pib.query('Ano == 2018')
teste = teste.sort_values('Produto Interno Bruto per capita, \na preços correntes\n(R$ 1,00)', ascending= False)
teste = teste.reset_index()
teste = teste.rename(columns={'Código do Município':'cod_ibge'})
teste.query("cod_ibge == 4300604")

teste = teste.rename(columns={'Sigla da Unidade da Federação':'sigla'})
teste = teste.query('sigla == "RS"')
teste = teste.reset_index()
teste = teste.query("cod_ibge == 4300604")

teste['Atividade com terceiro maior valor adicionado bruto']

#percentual de contribuição do setor de serviços para o pib municipal
teste = pib_2018
df = pd.DataFrame()
a = teste['Código do Município']
b = teste['Valor adicionado bruto dos Serviços,\na preços correntes \n- exceto Administração, defesa, educação e saúde públicas e seguridade social\n(R$ 1.000)']/teste['Produto Interno Bruto, \na preços correntes\n(R$ 1.000)']
df['cod_ibge']= a
df['valor'] = b
df.to_csv(os.path.join(TABELAS_DIR,'pib_servico.csv'))

#Evolução PIB per capita municipal
base = pib[[
    'Ano',
    'Código do Município',
    'Produto Interno Bruto per capita, \na preços correntes\n(R$ 1,00)'
]]
base = base.rename(columns={
    'Código do Município':'cod_ibge',
    'Produto Interno Bruto per capita, \na preços correntes\n(R$ 1,00)': 'valor'
})
base = base[base['cod_ibge'].isin(municipios)]
base.to_csv(os.path.join(TABELAS_DIR,'pib_evolucao.csv'))