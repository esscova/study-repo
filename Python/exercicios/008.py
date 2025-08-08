"""
Crie um programa que receba uma frase e conte quantas vogais ela possui.
"""

def contador_de_vogais(frase: str) -> int:
    vogais = 'aeiou'
    quantidade_de_vogais = sum(1 for vogal in frase if vogal in vogais)
    return quantidade_de_vogais

if __name__ == "__main__":
    try:
        print(f'\n{"=" * 5} CONTADOR DE VOGAIS EM FRASES {"=" * 5}')
        frase = input(f"Escreva sua frase: ")
        print("Resultado: A frase '{}' contém {} vogais".format(frase,contador_de_vogais(frase.lower())))
        print(f'{"=" * 15} FIM {"=" * 15}')
    except Exception as e:
        print("Erro inesperado: {}".format(e))

