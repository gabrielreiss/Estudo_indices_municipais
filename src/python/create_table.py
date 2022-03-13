import os
import pandas as pd
import sqlalchemy

BASE_DIR = os.path.abspath(".")
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
DATA_DIR = os.path.join(BASE_DIR,'data')
SQL_DIR = os.path.join(BASE_DIR, 'src', 'sql')
PYTHON_DIR = os.path.join(BASE_DIR, 'src', 'python')
TABELAS_DIR = os.path.join(BASE_DIR,'tabelas')

str_conn = 'sqlite:///' + os.path.join(DATA_DIR, 'banco.db') + '?check_same_thread=False'
engine = sqlalchemy.create_engine(str_conn)
conn = engine.connect()

def cria_tabela(nome_query, nome_tabela):
    print(f'Criando tabela {nome_tabela}...')
    with open( os.path.join(SQL_DIR, f'{nome_query}.sql'), 'rb') as query_file:
        query = query_file.read().decode("UTF-8")

    data = pd.read_sql_query(query, conn)

    data.to_sql(f'tb_{nome_tabela}',conn, if_exists="replace")

cria_tabela('sl_00_idh','idh2')
cria_tabela('sl_03_pop','pop')
cria_tabela('sl_01_RCL', 'rcl')
cria_tabela('sl_02_impostos', 'imp_perc')
cria_tabela('sl_04_transf', 'transf_perc')
cria_tabela('sl_07_res_prim', 'res_prim')
cria_tabela('sl_09_res_prim_perc', 'res_prim_perc')
cria_tabela('sl_08_asps', 'asps')
cria_tabela('sl_06_educacao', 'educacao')
cria_tabela('sl_16_fundeb', 'fundeb')
cria_tabela('sl_17_fundeb_rt', 'fundeb_rt')
cria_tabela('sl_10_desp_pessoal', 'desp_pessoal')
cria_tabela('sl_11_div_cons', 'div_cons')
cria_tabela('sl_12_div_cons_liq', 'div_cons_liq')
cria_tabela('sl_13_div_cons_liq_perc', 'div_cons_liq_perc')
cria_tabela('sl_14_op_credito', 'op_credito')
cria_tabela('sl_15_op_credito_perc', 'op_credito_perc')
cria_tabela('sl_18_liq_geral', 'liq_geral')
cria_tabela('sl_19_liq_corrente', 'liq_corrente')
cria_tabela('sl_20_endividamento', 'endividamento')
cria_tabela('sl_21_imobilizado', 'imobilizado')
cria_tabela('sl_22_QExecReceita', 'QExecReceita')
cria_tabela('sl_23_QExecDespesa', 'QExecDespesa')
cria_tabela('sl_24_QResOrc', 'QResOrc')
cria_tabela('sl_25_QCorrente', 'QCorrente')
cria_tabela('sl_26_QCapital', 'QCapital')
cria_tabela('sl_27_QFinanceiro', 'QFinanceiro')
cria_tabela('sl_28_QPermanente', 'QPermanente')
cria_tabela('sl_29_FinancCorrente', 'FinancCorrente')
cria_tabela('sl_30_DividaCorrente', 'DividaCorrente')