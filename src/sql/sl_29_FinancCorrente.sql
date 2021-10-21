select t1.cod_ibge,
        t1.instituicao,
        CASE WHEN t1.valor IS NULL THEN 0 ELSE t1.valor END /
        CASE WHEN t2.valor IS NULL THEN 0 ELSE t2.valor END as 'valor'
from (
    select *
    from rreo
    where conta = 'IMPOSTOS, TAXAS E CONTRIBUIÇÕES DE MELHORIA'
    and coluna = 'Até o Bimestre (c)'
    and cod_conta = 'ReceitaTributaria'
) as t1

left join (
    select cod_ibge,
            valor
    from rreo
    where conta = 'DESPESAS CORRENTES'
    and coluna = 'DESPESAS LIQUIDADAS ATÉ O BIMESTRE (h)'
    and cod_conta = 'DespesasCorrentes'
) as t2
on t1.cod_ibge = t2.cod_ibge
;