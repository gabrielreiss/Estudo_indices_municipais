select  t1.cod_ibge,
        Impostos,
        ReceitaTotal,
        Impostos/ReceitaTotal as 'imp_perc'

from (
    select  *,
            valor as 'Impostos'
    from rreo
    where conta = 'IMPOSTOS, TAXAS E CONTRIBUIÇÕES DE MELHORIA'
    and coluna = 'Até o Bimestre (c)'
) as t1

left join
(
    select  cod_ibge,
            valor as 'ReceitaTotal'
    from rreo
    where conta = 'RECEITAS (EXCETO INTRA-ORÇAMENTÁRIAS) (I)'
    and coluna = 'Até o Bimestre (c)'
) as t2
on t1.cod_ibge = t2.cod_ibge
;