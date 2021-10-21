select t1.cod_ibge,
        t1.instituicao,
        (CASE WHEN t1.valor IS NULL THEN 0 ELSE t1.valor END +
        CASE WHEN t2.valor IS NULL THEN 0 ELSE t2.valor END ) /
        CASE WHEN t3.valor IS NULL THEN 0 ELSE t3.valor END as 'valor'
from (
    select *
    from rreo
    where conta = 'JUROS E ENCARGOS DA DÍVIDA'
    and coluna = 'DESPESAS EMPENHADAS ATÉ O BIMESTRE (f)'
    and cod_conta = 'JurosEEncargosDaDivida'
) as t1

left join (
    select *
    from rreo
    where conta = 'AMORTIZAÇÃO DA DÍVIDA'
    and coluna = 'DESPESAS EMPENHADAS ATÉ O BIMESTRE (f)'
    and cod_conta = 'AmortizacaoDaDivida'
) as t2
on t1.cod_ibge = t2.cod_ibge

left join (
    select *
    from rreo
    where conta = 'RECEITAS CORRENTES'
    and coluna = 'Até o Bimestre (c)'
    and cod_conta = 'ReceitasCorrentes'
) as t3
on t1.cod_ibge = t3.cod_ibge
;