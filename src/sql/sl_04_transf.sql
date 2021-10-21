select t1.cod_ibge,
        t1.instituicao,
        (t1.TransfCorrente + 
        CASE WHEN t2.TransfCapital IS NULL THEN 0 ELSE t2.TransfCapital END
        ) / t3.ReceitaTotal as 'valor'

from (
    select  cod_ibge,
            instituicao,
            valor as 'TransfCorrente'
    from rreo
    where conta = 'TRANSFERÊNCIAS CORRENTES'
    and coluna = 'Até o Bimestre (c)'
) as t1

left join(
    select  cod_ibge,
            valor as 'TransfCapital'
    from rreo
    where conta = 'TRANSFERÊNCIAS DE CAPITAL'
    and coluna = 'Até o Bimestre (c)'
) as t2
on t1.cod_ibge = t2.cod_ibge

left JOIN(
    select  cod_ibge,
            valor as 'ReceitaTotal'
    from rreo
    where conta = 'RECEITAS (EXCETO INTRA-ORÇAMENTÁRIAS) (I)'
    and coluna = 'Até o Bimestre (c)'
) as t3
on t1.cod_ibge = t3.cod_ibge
;
