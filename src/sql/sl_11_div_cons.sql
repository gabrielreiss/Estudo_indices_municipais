select cod_ibge,
        instituicao,
        valor
from rgf
where conta = 'DÍVIDA CONSOLIDADA - DC (I)'
and cod_conta = 'DividaConsolidada'
and coluna = 'Até o 3º Quadrimestre'
;