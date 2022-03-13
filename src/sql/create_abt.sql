SELECT 
        t1.cod_ibge,
        t1.instituicao,
        t2.t2.IDH,
        t2.'IDH-renda',
        t2.'IDH-longevidade',
        t2.'IDH-educacao',
        t3.'RCL' / t4.populacao as 'RCL/Pop',
        t5.'imp_perc',
        t6.'transf_perc',
        t8.'PIBperCapita'


        /* t4.populacao */
FROM(
    select distinct cod_ibge,
                    instituicao
    from rreo
) as T1

left join(
    SELECT  
            cod_ibge,
            instituicao,
            valor as 'IDH',
            renda as 'IDH-renda',
            longevidade as 'IDH-longevidade',
            educacao as 'IDH-educacao'
    from tb_idh2
) as T2
ON T1.cod_ibge = T2.cod_ibge

left join(
    SELECT  
            cod_ibge,
            instituicao,
            valor as 'RCL'
    from tb_rcl
) as T3
ON T1.cod_ibge = T3.cod_ibge

left join(
    SELECT  
            cod_ibge,
            populacao
    from tb_pop
) as T4
ON T1.cod_ibge = T4.cod_ibge

left join(
    SELECT  
            cod_ibge,
            imp_perc
    from tb_imp_perc
) as T5
ON T1.cod_ibge = T5.cod_ibge

left join(
    SELECT  
            cod_ibge,
            valor as 'transf_perc'
    from tb_transf_perc
) as T6
ON T1.cod_ibge = T6.cod_ibge

left join(
    select 
            t7.'Código do Município',
            t7.'PIBperCapita'

    from (
        select *
        from pib
        WHERE Ano = '2018'
    ) as t7
) as T8
ON t1.cod_ibge = t8.'Código do Município'

;