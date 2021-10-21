select cod_ibge,
        instituicao,
        valor
from rreo
where conta = 'RECEITA CORRENTE LÍQUIDA (III) = (I - II)'
and cod_conta='RREO3ReceitaCorrenteLiquida'
and coluna='TOTAL (ÚLTIMOS 12 MESES)'
;