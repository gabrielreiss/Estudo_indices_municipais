/*
fundeb sobre receita total
*/

select t1.cod_ibge,
        t1.instituicao,
        t1.valor / t2.valor as valor
from (
    select cod_ibge,
            instituicao,
            valor
    from rreo
    where conta = 'Transferências do FUNDEB'
    and cod_conta = 'TransferenciasDoFUNDEB'
    and coluna = 'RECEITAS REALIZADAS (a)'
) as t1

left join (
    select cod_ibge,
            valor
    from rreo
    where conta = 'RECEITAS (EXCETO INTRA-ORÇAMENTÁRIAS) (I)'
    and coluna = 'Até o Bimestre (c)'
) as t2
on t1.cod_ibge = t2.cod_ibge
;