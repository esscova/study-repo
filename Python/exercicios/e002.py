"""
Faça um programa que leia um número e diga se ele é par ou ímpar.
"""

def impar_par(num: int) -> str:
    return f"O número {num} é Par." if (num % 2 == 0) else f"O número {num} é ímpar."

if __name__ == "__main__":
    print("\n=== ÍMPAR OU PAR ===")
    numero = int(float(input("Digite um número: ").replace(",", ".")))
    print(f'Resultado: {impar_par(numero)}\n')
