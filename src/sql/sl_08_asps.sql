select cod_ibge,
    instituicao,
    valor
from rreo
where conta = 'Despesas com Ações e Serviços Públicos de Saúde Executadas com Recursos de Impostos'
and cod_conta = 'AplicacaoTotalDasDespesasComAcoesEServicosPublicosDeSaude'
and coluna = '% Aplicado Até o Bimestre'
;