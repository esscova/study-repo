"""
Crie um programa que leia o nome de 3 alunos e suas respectivas notas, depois mostre o nome do aluno com a maior nota.
"""

def aluno_com_maior_nota(alunos: list) -> dict:
    return max(alunos, key=lambda aluno: aluno['nota'])

if __name__ == "__main__":
    try:
        print(f'\n{"=" * 5} ENCONTRAR MELHOR ALUNO {"=" * 5}')

        alunos = [
            {'nome': input(f"Digite o nome do aluno {i+1}: "),
             'nota': float(input(f"Digite a nota do aluno {i+1}: ").replace(',', '.'))}
            for i in range(3)
        ]

        aluno = aluno_com_maior_nota(alunos)
        print(f"O aluno com a maior nota é: {aluno['nome']} com nota {aluno['nota']}")

        print(f'{"=" * 15} FIM {"=" * 15}\n')
    except ValueError as e:
        print(f"Erro inesperado: {e}")

