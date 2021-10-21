select cod_ibge,
        instituicao,
        valor
from rreo
where conta = 'Cota-Parte do FPM'
and cod_conta = 'RREO3CotaParteDoFPM'
and coluna = 'TOTAL (ÚLTIMOS 12 MESES)'
;