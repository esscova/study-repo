"""
Desenvolva um programa que calcule o fatorial de um número informado pelo usuário.
"""

def calcula_fatorial(num:int) -> int:
    fatorial = 1
    for i in range(1, num+1):
        fatorial *= i
    return fatorial
    
if __name__ == "__main__":
    try:
        print("\n=== CALCULO DE FATORIAL ===")
        numero = int(input("Digite um número inteiro para calcular seu fatorial: "))
        print("=== Resultado: {}\n".format(calcula_fatorial(numero)))
    except Exception as e:
        print("Erro inesperado: {}".format(e)) 
