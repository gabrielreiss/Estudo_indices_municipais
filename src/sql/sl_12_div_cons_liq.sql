select cod_ibge,
        instituicao,
        valor
from rgf
where conta = 'DÍVIDA CONSOLIDADA LÍQUIDA (DCL) (III) = (I - II)'
and cod_conta = 'DividaConsolidadaLiquida'
and coluna = 'Até o 3º Quadrimestre'
;