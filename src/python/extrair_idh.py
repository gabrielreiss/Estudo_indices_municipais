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

idh = pd.read_excel(
    os.path.join(DATA_DIR,'idh.xlsx')
    )
idh.to_sql('idh',conn)