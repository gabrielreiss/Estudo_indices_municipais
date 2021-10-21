select cod_ibge,
        instituicao,
        valor
from rgf
where conta = 'Operações de Crédito Internas e Externas'
and coluna = '% SOBRE A RCL AJUSTADA'
;