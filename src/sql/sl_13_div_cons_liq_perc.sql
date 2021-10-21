select cod_ibge,
        instituicao,
        valor
from rgf
where conta = '% da DCL sobre a RCL AJUSTADA (III/VI)'
and cod_conta = 'PercentualDaDCLSobreARCL'
and coluna = 'Até o 3º Quadrimestre'
;