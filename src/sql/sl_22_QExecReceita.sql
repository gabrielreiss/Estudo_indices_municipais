select t1.cod_ibge,
        t1.instituicao,
        CASE WHEN t1.valor IS NULL THEN 0 ELSE t1.valor END /
        CASE WHEN t2.valor IS NULL THEN 0 ELSE t2.valor END as 'valor'
from (
    select *
    from rreo
    where conta = 'RECEITAS (EXCETO INTRA-ORÇAMENTÁRIAS) (I)'
    and coluna = 'Até o Bimestre (c)'
) as t1

left join (
    select cod_ibge,
            valor
    from rreo
    where conta = 'RECEITAS (EXCETO INTRA-ORÇAMENTÁRIAS) (I)'
    and coluna = 'PREVISÃO INICIAL'
) as t2
on t1.cod_ibge = t2.cod_ibge
;