from random import choice
from time import sleep
ints = [1,2,3,4,5]
pc = choice(ints)
chute = int(input('De 1 a 5, escolha um número para saber se é o mesmo escolhido pelo computador:  '))
print ('PROCESSANDO...')
sleep(4) #O IMPORT TIME COM A FUNÇÃO SLEEP FAZ O PC ESPERAR X SEGUNDOS ANTES DE EXIBIR ALGO
if chute == pc:
    print('\nParabéns!! Você acertou o número escolhido pelo computador!!\n')
else:
    print('\nPois é!! Não foi dessa vez que você acertou. O Número escolhido foi o {}.\n'.format(pc))
print('Para tentar novamente de play no canto inferior esquerdo. Boa sorte =D !!!')
