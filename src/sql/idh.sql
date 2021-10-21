select distinct t1.cod_ibge,
                t1.instituicao,
                t2.Territorialidades,
                t2.`IDHM 2010` as 'valor',
                t2.`IDHM Renda 2010` as 'renda',
                t2.`IDHM Longevidade 2010` as 'longevidade',
                t2.`IDHM Educação 2010` as 'educacao'
from(
    select cod_ibge,
            instituicao
    from rreo
) as t1

left join (
    select *
    from idh
) as t2
on t1.instituicao = t2.instituicao
;