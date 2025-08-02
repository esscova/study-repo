"""
Crie um algoritmo que leia a idade de uma pessoa e informe se ela é maior de idade (18 anos ou mais).
"""

def eh_maior_de_idade(idade: int) -> str:
    return "É maior de idade" if idade >= 18 else "É menor de idade."

if __name__ == "__main__":
    try:
        idade = int(float(input("Qual sua idade? ").replace(",", ".")))
        if idade <= 0:
            print('A idade informada não é válida... tente novamente.')
        else:
            print(eh_maior_de_idade(idade))
    except ValueError:
        print('Entrada inválida. Por favor, digite um número válido para a idade.')

