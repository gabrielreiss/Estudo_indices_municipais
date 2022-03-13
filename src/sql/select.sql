    select 
            t7.'Código do Município',
            t7.'PIBperCapita'

    from (
        select *
        from pib
        WHERE Ano = '2018'
    ) as t7