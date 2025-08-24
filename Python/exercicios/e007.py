"""
Faça um código que receba um número inteiro e diga se ele é primo.
"""

def verificador_de_numeros_primos(num: int) -> bool:
    if num <= 1: return False
    elif num <= 3: return True
    elif num % 2 == 0 or num % 3 == 0 : return False
    i = 5
    while i * i <= num:
        if num %  i == 0 or num % (i+2) == 0: return False
        i+= 6
    return True

if __name__ == "__main__":
    try:
        print(f'\n{"=" * 5} VERIFICADOR DE NÚMEROS PRIMOS {"=" * 5}')
        numero = int(input(f"Digite o número inteiro: "))
        resultado = "O número é primo." if verificador_de_numeros_primos(numero) else "O número não é primo."
        print("Resultado: {}".format(resultado))
        print(f'{"=" * 15} FIM {"=" * 15}')
    except Exception as e:
        print("Erro inesperado: {}".format(e))

