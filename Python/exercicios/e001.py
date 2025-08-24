"""
Crie um programa que receba dois números inteiros e imprima a soma deles.
"""

def soma(lista:list) -> None:
    print(f'Resultado: {lista[0]} + {lista[1]} = {sum(lista)}')
    
if __name__ == "__main__":
    print("\n=== SOMA DE INTEIROS ===")
    numeros = [int(input(f'Digite o {i+1}º número: ')) for i in range(2)] 
    soma(numeros)
