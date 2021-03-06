import pandas as pd
import requests
import sqlalchemy
import os
import time
from tqdm import tqdm

#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_columns', 5)

#link = 'https://apidatalake.tesouro.gov.br/ords/siconfi/tt/entes'
#link = 'https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rreo?an_exercicio=2020&id_ente=4300604&nr_periodo=1&co_tipo_demonstrativo=RREO'
#link = 'https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rreo?an_exercicio=2020&id_ente=4300604&nr_periodo=1&co_tipo_demonstrativo=RREO&no_anexo=RREO-Anexo 14&co_esfera=M'

BASE_DIR = os.path.abspath('.')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, 'data')

str_banco = 'sqlite:///' + os.path.join(DATA_DIR, 'banco.db')
engine = sqlalchemy.create_engine(str_banco)
conn = engine.connect()

def extrair_rgf(id_ente,an_exercicio):
    link = f'https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca?an_exercicio={an_exercicio}&id_ente={id_ente}'
    r = requests.get(link)
    x = r.json()
    df = pd.DataFrame(x['items'])
    df.to_sql('dca',
              conn,
              if_exists='append')

#extrair código dos entes
#talvez uma boa estratégia seria pegar só municípios com 
#uma faixa populacional específica exemplo 100 mil a 300 mil hab.

link = 'https://apidatalake.tesouro.gov.br/ords/siconfi/tt/entes'
r = requests.get(link)
x = r.json()
entes = pd.DataFrame(x['items'])
entes.to_sql('entes', conn, if_exists='replace')
municipios = entes.query('populacao > 100000 & populacao <300000').cod_ibge
time.sleep(1)

#fazer um loop que pegue todos os municipios
#nos diferentes exercicios e periodos
#cuidar o tempo de 1 segundo entre requisições
#alvorada id_ente='4300604'

#for id_ente in '4300604':
for id_ente in tqdm(municipios):
    for an_exercicio in list(range(2020,2021)):
        try:
            extrair_rgf(id_ente,an_exercicio)
            time.sleep(0.5)
        except:
            break