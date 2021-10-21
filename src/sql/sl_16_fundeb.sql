select cod_ibge,
        instituicao,
        valor
from rreo
where conta = 'Transferências do FUNDEB'
and cod_conta = 'TransferenciasDoFUNDEB'
and coluna = 'RECEITAS REALIZADAS (a)'
;