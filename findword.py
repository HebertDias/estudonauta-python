# Strip: Remove espaços em branco antes e depois da string, mas não entre palavras
# Upper: Converte todos os caracteres para maiúsculas para padronizar a formatação internamente

frase = str(input('Diga algo: ')).strip().upper()

# Replace: Substitui os espaços internos por uma string vazia, ajustando a string para não ter espaços
frase_novo = frase.replace(' ', '')

# Verifica se há a letra 'A' na variável frase_novo
if 'A' in frase_novo:
    count = frase_novo.count('A')  # Conta o número de letras 'A'
    print('A letra "A" aparece {} vezes.'.format(count))

    find = frase_novo.find('A') + 1  # Encontra a 1ª ocorrência de 'A' (+' ajustando para começar de 1)
    print('Se localiza pela 1ª vez no {}º caractere.'.format(find))

    find_last = frase_novo.rfind('A') + 1  # Encontra a última ocorrência de 'A' (+1 para começar de 1)
    print('Se localiza pela última vez no {}º caractere.'.format(find_last))
else:
    print('Não foi localizada nenhuma letra "A" em "{}".' .format(frase))





