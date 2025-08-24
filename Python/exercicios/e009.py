"""
Faça um programa que gere e imprima a sequência de Fibonacci até o n-ésimo termo informado pelo usuário.
"""
# sequencia: 0 1 1 2 3 5 ...
# os dois primeiros sao fixos 0 e 1, do terceiro em diante soma dois anteriores

def imprimir_fibonacci(n:int ) -> None:
    primeiro_termo = 0
    segundo_termo = 1

    if n <= 0:print("Inserir inteiro positivo.")
    elif n == 1 : print(f'Sequencia de fibonacci: {primeiro_termo}')
    else:
        print('Sequencia de fibonacci:', primeiro_termo, segundo_termo, end=' ')
        for _ in range(2,n): # pula os 2 primeiros
            termo_atual = primeiro_termo + segundo_termo
            print(termo_atual, end=' ')
            primeiro_termo = segundo_termo
            segundo_termo = termo_atual 

if __name__ == "__main__":
    try:
        print(f'\n{"=" * 5} SEQUENCIA DE FIBONACCI {"=" * 5}')
        num = int(input(f"Digite o termo da sequência: "))
        imprimir_fibonacci(num)
        print(f'\n{"=" * 15} FIM {"=" * 15}')
    except Exception as e:
        print("Erro inesperado: {}".format(e))

