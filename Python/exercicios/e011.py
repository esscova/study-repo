#
# OBJETIVO: Prática de estrutura de dados em Python
# DESCRICAO: Análise de temporada de vendas por mes retornando metricas após manipular estruturas de dados;
#

# imports
import random
import logging

# configs
logging.basicConfig(
  level=logging.INFO,
  format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# helper functions
logger.info("Gerando Dados")
def gerar_dados(valor_min:int=9000, valor_max=30000) -> list[dict]:
  m = "Janeiro Fevereiro Março Abril Maio Junho Julho Agosto Setembro Outubro Novembro Dezembro".split()
  v = [round(random.uniform(valor_min, valor_max),2) for _ in range(12)]
  return [{"mes": mes, "vendas": vendas} for mes, vendas in zip(m, v)]

# execucao
if __name__ == '__main__':
  vendas_mensais = gerar_dados()

  # total de vendas
  logger.info("Calculando Total em Vendas.")
  total_vendas = sum(item['vendas'] for item in vendas_mensais)

  # media anual
  logger.info("Calculando Venda Anual.")
  media = total_vendas/len(vendas_mensais)

  # meses acima da media
  logger.info("Filtrando Meses que venderam acima da média anual.")
  meses_acima_media = [i['mes'] for i in vendas_mensais if i['vendas']>media]

  # tupla com resultados
  logger.info("Filtrando Resultados para Relatório.")
  resultado = [
    (item['mes'], item['vendas'])
    for item in vendas_mensais
    if item['vendas']>media
  ]
  resultado = sorted(resultado, key=lambda x:x[1], reverse=True)

  # relatorio
  print(f"""
  RELATÓRIO
  {'-'*50}
  TOTAL EM VENDAS ($): {round(total_vendas,2):>10}
  MÉDIA DE VENDAS ($): {round(media,2):>10}

  MESES QUE REPORTARAM VENDAS ACIMA DA MÉDIA ANUAL
  {'-'*50}
  {meses_acima_media}

  MÉTRICAS DE VENDAS 
  {'-'*50}
  {resultado}

  """)




