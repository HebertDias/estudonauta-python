from random import randint
from time import sleep
import emoji

# Define cores para destacar o texto
cores = {
    'verde': '\033[0;32m',
    'vermelho': '\033[0;31m',
    'reset': '\033[0m'
}

# Imprime a borda e opções do jogo
print('+-'*24)
print('[1]'+emoji.emojize('🪨'), 'Pedra\n''[2]' + emoji.emojize('📃'), 'Papel\n''[3]' + emoji.emojize('✂️'), 'Tesoura')
print('+-'*24)

# Solicita ao usuário para escolher uma opção
choice = int(input('Escolha um número: '))
machine = randint(1, 3)  # A máquina escolhe uma opção aleatória
print()

# Atribui o emoji correspondente à escolha do usuário
if choice == 1:
    user = emoji.emojize('🪨')
elif choice == 2:
    user = emoji.emojize('📃')
else:
    user = emoji.emojize('✂️')

print('Você escolheu: {}!' .format(user))
print()
sleep(0.8)

# Simula o tempo de espera do jogo
print('Jo... ', end='')
sleep(0.8)
print('Ken...', end='')
sleep(0.8)
print(' Po!')
sleep(0.9)
print()

# Atribui o emoji correspondente à escolha da máquina
if machine == 1:
    pc = emoji.emojize('🪨')
elif machine == 2:
    pc = emoji.emojize('📃')
else:
    pc = emoji.emojize('✂️')

print()
print(' ' * 14, '{} vs {}' .format(user, pc))
print()

sleep(0.9)

# Imprime a borda inferior
print('+-'*24)

# Verifica o resultado do jogo e imprime o resultado
if user == pc:
    print(' ' * 14, 'Empate!')
else:
    # Verifica se o usuário venceu
    if user == emoji.emojize('🪨') and pc == emoji.emojize('✂️') or \
       user == emoji.emojize('✂️') and pc == emoji.emojize('📃') or \
       user == emoji.emojize('📃') and pc == emoji.emojize('🪨'):
        print(' ' * 14, '{}Você venceu!{}'.format(cores['verde'], cores['reset']))
    else:
        print(' ' * 10, '{}A Máquina venceu!{}'.format(cores['vermelho'], cores['reset']))

# Imprime a borda inferior novamente
print('+-'*24)