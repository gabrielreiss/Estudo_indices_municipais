select t1.cod_ibge,
        t1.instituicao,
        t1.ResultadoPrimario,
        t2.ReceitaPrimariaTotal,
        t1.ResultadoPrimario/t2.ReceitaPrimariaTotal as valor
from (
    select 
        cod_ibge,
        instituicao,
        valor as 'ResultadoPrimario'
    from rreo
    where cod_conta == 'RREO6ResultadoPrimarioEstadosMunicipios'
    and coluna LIKE '%VALOR%'
) as t1

left join (
    select cod_ibge,
            valor as 'ReceitaPrimariaTotal'
    from rreo
    where conta = 'RECEITA PRIMÁRIA TOTAL  (XII) = (IV + XI)'
    and cod_conta = 'RREO6TotalReceitaPrimaria'
    and coluna = 'RECEITAS REALIZADAS (a)'
) as t2
on t1.cod_ibge = t2.cod_ibge
;