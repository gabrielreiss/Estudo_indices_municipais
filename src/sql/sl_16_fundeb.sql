select cod_ibge,
        instituicao,
        valor
from rreo
where conta = 'TransferĂȘncias do FUNDEB'
and cod_conta = 'TransferenciasDoFUNDEB'
and coluna = 'RECEITAS REALIZADAS (a)'
;