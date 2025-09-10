#
# OBJETIVO: Analisar dados
# DESCRICAO: Criar um programa que calcule métricas
#


# 0.0 imports
import random
import logging

## 0.1 configuracoes
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

## 0.2 constantes
DIAS = 30
VALOR_MINIMO = 10
VALOR_MAXIMO = 1000

## 0.3 funcoes auxiliares
def gerar_dados_de_vendas(dias: int, valor_minimo: int, valor_maximo: int) -> list[float] | None:
    try:
        if valor_minimo >= valor_maximo:
            logger.error("valor_minimo deve ser menor que valor_maximo.")
            return None
        if dias <= 0:
            logger.error("dias deve ser maior que zero.")
            return None
        lista = [round(random.uniform(valor_minimo, valor_maximo), 2) for _ in range(dias)]
        logger.info("Dados gerados com sucesso!")
        return lista
    except Exception as e:
        logger.error(f"Erro ao gerar dados: {e}")
        return None

def calcular_metricas(vendas: list[float]) -> dict[str, float] | None:
    try:
        if not vendas:
            logger.error("Lista de vendas está vazia.")
            return None
        logger.info("Calculando total de vendas")
        total = round(sum(vendas), 2)
        logger.info("Calculando média de vendas diárias")
        media = round(total / len(vendas), 2)
        logger.info("Calculando menor venda")
        menor = round(min(vendas), 2)
        logger.info("Calculando maior venda")
        maior = round(max(vendas), 2)
        logger.info("Métricas calculadas")
        return {
            "Total de vendas": total,
            "Média de vendas": media,
            "Menor venda": menor,
            "Maior venda": maior,
        }
    except Exception as e:
        logger.error(f"Erro ao calcular métricas: {e}")
        return None

# 1.0 funcao principal
def main(dias: int, minimo: int, maximo: int) -> dict[str, float] | None:
    registro_de_vendas = gerar_dados_de_vendas(dias, minimo, maximo)
    if registro_de_vendas is None:
        logger.error("Falha ao gerar dados de vendas.")
        return None
    metricas = calcular_metricas(registro_de_vendas)
    return metricas

# 2.0 Execucao
if __name__ == "__main__":
    dados = main(DIAS, VALOR_MINIMO, VALOR_MAXIMO)
    if dados:
        print(f"""
            Relatório
            {'-'*36}
            Total de vendas:        R${dados['Total de vendas']:>10}
            Média diária de vendas: R${dados['Média de vendas']:>10}
            Menor venda:            R${dados['Menor venda']:>10}
            Maior venda:            R${dados['Maior venda']:>10}
        """)
    else:
        print("Erro ao obter Relatório")
