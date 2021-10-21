import pandas as pd
import requests
import sqlalchemy
import os
import time
from tqdm import tqdm

BASE_DIR = os.path.abspath('.')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, 'data')
SQL_DIR = os.path.join(BASE_DIR, 'src', 'sql')

str_banco = 'sqlite:///' + os.path.join(DATA_DIR, 'banco.db')
engine = sqlalchemy.create_engine(str_banco)
conn = engine.connect()

with open(os.path.join(SQL_DIR, 'municipios.sql'), 'r') as sql_file:
    query = sql_file.read()

df = pd.read_sql(query, conn)
df

link = 'https://apidatalake.tesouro.gov.br/ords/siconfi/tt/entes'
r = requests.get(link)
x = r.json()
entes = pd.DataFrame(x['items'])
#entes.to_sql('entes', conn, if_exists='replace')
municipios = entes.query('populacao > 100000 & populacao <300000').cod_ibge
time.sleep(1)

municipios = list(set(municipios) - set(df.cod_ibge))

def link_rreo(id_ente,an_exercicio,nr_periodo):
    co_tipo_demonstrativo='RREO'
    link = f'https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rreo?an_exercicio={an_exercicio}&id_ente={id_ente}&nr_periodo={nr_periodo}&co_tipo_demonstrativo={co_tipo_demonstrativo}&co_esfera=M'
    return link

def extrair(link):
    r = requests.get(link)
    x = r.json()
    df = pd.DataFrame(x['items'])
    df.to_sql('rreo',
              conn,
              if_exists='append')

for id_ente in tqdm(municipios):
    for an_exercicio in list(range(2015,2022)):
        for nr_periodo in list(range(1,7)):
            link = link_rreo(id_ente,an_exercicio,nr_periodo)
            extrair(link)
            time.sleep(0.5)
