select cod_ibge,
        instituicao,
        valor
from rgf
where conta = 'DESPESA TOTAL COM PESSOAL - DTP (VIII) = (IIIa + IIIb)'
and cod_conta = 'DespesaComPessoalTotal'
and coluna = '% sobre a RCL Ajustada'