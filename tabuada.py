print('Tabuada inteligente. Pressione 0 para encerrar.')

while True:
    # Solicita ao usuário para digitar um número entre 1 e 10
    numero = int(input('Digite um número de 1 a 10: '))

    # Verifica se o número fornecido é menor que 0
    if numero < 0:
        # Informa ao usuário que o número precisa ser maior que 0
        print('Precisa ser um número maior que 0!')

    # Verifica se o número fornecido é igual a 0
    elif numero == 0:
        # Encerra o loop e o programa
        break

    else:
        # Imprime uma linha de separação para melhorar a visualização
        print('-=' * 25)

        # Gera e imprime a tabuada do número fornecido
        # O loop vai de 1 a 10 (inclusive)
        for c in range(1, 11):
            # Calcula e imprime a multiplicação do número com o valor atual de c
            print(f'{numero} x {c} = {numero * c}')

        # Imprime outra linha de separação após a tabuada para organizar a saída
        print('-=' * 25)

# Imprime uma mensagem de encerramento quando o programa termina
print('FIM')