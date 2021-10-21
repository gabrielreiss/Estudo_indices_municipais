select 
    cod_ibge,
    instituicao,
    valor

from rreo
where cod_conta == 'RREO6ResultadoPrimarioEstadosMunicipios'
and coluna LIKE '%VALOR%'
;