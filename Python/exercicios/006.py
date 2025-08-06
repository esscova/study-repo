"""
Implemente um programa que leia 10 números e conte quantos são positivos.
"""

def contador_de_numeros_positivos(numeros: list) -> int:
    positivo = 0
    for numero in numeros:
        if numero > 0:
            positivo += 1
    return positivo

if __name__ == "__main__":
    try:
        print(f'\n{"=" * 5} CONTADOR DE POSITIVOS {"=" * 5}')
        numeros = [int(input(f"Digite o {i+1}º número: ")) for i in range(3)]
        print("Resultado: {}".format(contador_de_numeros_positivos(numeros)))
        print(f'{"=" * 15} FIM {"=" * 15}')
    except Exception as e:
        print("Erro inesperado: {}".format(e))

