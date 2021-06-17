# Passo 1: Define variáveis e importa libs
from random import choice
from time import sleep
ints = range(1,10)
pc = choice(ints)
tot = 1
print('\033[33m','-=-' * 16)
print('   ADVINHE O NÚMERO QUE O COMPUTADOR ESCOLHEU!!')
print('_=_' * 17, '\033[m')

chute = int(input('\033[1;34m''\nDe 1 a 10, escolha um número para '
                  'saber se é o mesmo escolhido pelo computador: ''\033[m'))


# Passo 2: Adiciona emoção hahhha uma pequena espera
print ('\033[1;32m''\nPROCESSANDO.')
sleep(0.5)
print ('PROCESSANDO..')
sleep(1)
print ('PROCESSANDO...''\033[m')
sleep(1.25)

# Passo 3: Estabelece o  loop com as condicionais para o game.

while chute != pc:
    if chute > pc:
        print('\033[1;31m')
        chute = int(input(f'O computador escolheu um número menor que {chute}. \nTente outro número abaixo de {chute}.'
                          f'\nDe 1 a {chute-1}: '))
        tot += 1
        print('\033[1;32m''\nPROCESSANDO.')
        sleep(0.5)
        print('PROCESSANDO..')
        sleep(1)
        print('PROCESSANDO...''\033[m')
        sleep(1.25)

    else:
        print('\033[1;35m')
        chute = int(input(f'O computador escolheu um número maior que {chute}. \nTente outro número acima de {chute}.'
                          f'\nDe {chute+1} a 10: '))
        tot += 1
        print('\033[1;32m''\nPROCESSANDO.')
        sleep(0.5)
        print('PROCESSANDO..')
        sleep(1)
        print('PROCESSANDO...''\033[m')
        sleep(1.25)

# Passo 4: Fim do jogo. nova tentativa

print('\033[1;32m''\nParabéns!! Você acertou!!'
    f'\nO número escolhido pelo computador foi {pc}!!\n'
    f'Você precisou de {tot} tentativas nessa rodada!!' '\033[m')

