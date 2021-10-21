select cod_ibge,
        instituicao,
        valor
from rreo
where conta = 'Mínimo Anual de <18% / 25%> das Receitas de Impostos na Manutenção e Desenvolvimento do Ensino'
and cod_conta = 'MinimoAnualDasReceitasDeImpostosNaManutencaoEDesenvolvimentoDoEnsinoDemonstrativoSimplificado'
and coluna = '% Aplicado Até o Bimestre'
;