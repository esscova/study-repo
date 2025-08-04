"""
Faça um programa que leia uma lista de 5 números, armazene-os em uma lista e, em seguida, mostre-os em ordem inversa.
"""

def lista_reversa(lista:list) -> list:
    return lista[::-1]
    
if __name__ == "__main__":
    try:
        print("\n=== ORDEM INVERSA DE LISTA ===")
        lista_de_numeros = [
            float(input("Digite o º{} número: ".format(i+1) ).replace(",","."))
            for i in range(5)
        ]
        print("=== Resultado: {} ===\n".format(lista_reversa(lista_de_numeros)))
    except Exception as e:
        print("Erro inesperado: {}".format(e))
