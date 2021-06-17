import random
from time import sleep

n1 = 'Pedra'
n2 = 'Papel'
n3 = 'Tesoura'
jokempo = (n1,n2,n3)
escolha = input('Escolha entre {}: '.format(jokempo)).strip()
form = escolha.title()
pc = random.choice(jokempo)

print('\nVocê escolheu: ''\033[4;32m''{}''\033[m''\n'.format(form))
print('\033[1;36m',' -'*7,'\033[m')
print('\033[1;31m''\n  Jó !!!\n''\033[m')
sleep(1)
print('\033[1;35m''    Ken !!!!!\n''\033[m')
sleep(1)
print('\033[1*9                                                                                                                         --------------- ---------------ojk9 ]~]ml 98in2;34m''     Po !!!!!!!\n''\033[m')
print('\033[1;36m'2qt   nfb2    w  7,' _'*7,'\033[m')
sleep(2)
print('\n\n')
if pc == n1 and form == n1:
    print('\033[1;35m', ' -' * 29, '\033[m')
    print('\033[1;35m''                É, dessa vez vocês empataram!! ''\033[m'
          '\n''\033[1;35m''        A sua escolha e a do computador foram {}!!''\033[m'.format(n1))
    print('\033[1;35m', ' _' * 29, '\033[m')
elif pc == n1 and form == n2:
    print('\033[1;32m', ' -' * 34, '\033[m')
    print('\033[1;32m''             ***PARABÉNS!!!! Você venceu essa rodada!!!!!*** ''\033[m'
          '\n           A sua escolha foi ''\033[1;32m''{}''\033[m'' a do computador foi ''\033[1;31m''{}''\033[m''!!'.format(n2,n1))
    print('\033[1;32m', ' _' * 34, '\033[m')
elif pc == n1 and form == n3:
    print('\033[1;31m',' -'*31,'\033[m')
    print('\033[1;31m''              Poxa!!! Você perdeu essa rodada!!! ''\033[m'
          '\n      A sua escolha foi ''\033[1;31m''{} ''\033[m''a do computador foi ''\033[1;32m' '{}''\033[m''!!'
          '\n''\033[1;31m''                  {} esmaga a {}!!''\033[m'.format(n3,n1,n1,n3))
    print('\033[1;31m', ' _' * 31, '\033[m')
elif pc == n2 and form == n1:
    print('\033[1;31m', ' -' * 30, '\033[m')
    print('\033[1;31m''              Poxa!!! Você perdeu essa rodada!!! ''\033[m'
          '\n      A sua escolha foi ''\033[1;31m''{} ''\033[m''a do computador foi ''\033[1;32m' '{}''\033[m''!!'
          '\n''\033[1;31m''                  {} embrulha a {}!!''\033[m'.format(n1,n2,n2,n1))
    print('\033[1;31m', ' _' * 30, '\033[m')
elif pc == n2 and form == n2:
    print('\033[1;35m', ' -' * 29, '\033[m')
    print('\033[1;35m''                É, dessa vez vocês empataram!! ''\033[m'
          '\n''\033[1;35m''        A sua escolha e a do computador foram {}!!''\033[m'.format(n2))
    print('\033[1;35m', ' _' * 29, '\033[m')
elif pc == n2 and form == n3:
    print('\033[1;32m', ' -' * 35, '\033[m')
    print('\033[1;32m''              ***PARABÉNS!!!! Você venceu essa rodada!!!!!*** ''\033[m'
          '\n           A sua escolha foi ''\033[1;32m''{}''\033[m'' a do computador foi ''\033[1;31m''{}''\033[m''!!'.format(n3,n2))
    print('\033[1;32m', ' _' * 35, '\033[m')
elif pc == n3 and form == n1:
    print('\033[1;32m', ' -' * 36, '\033[m')
    print('\033[1;32m''               ***PARABÉNS!!!! Você venceu essa rodada!!!!!*** ''\033[m'
          '\n           A sua escolha foi ''\033[1;32m''{}''\033[m'' a do computador foi ''\033[1;31m''{}''\033[m''!!'.format(n1, n3))
    print('\033[1;32m', ' _' * 36, '\033[m')
elif pc == n3 and form == n2:
    print('\033[1;31m', ' -' * 31, '\033[m')
    print('\033[1;31m''              Poxa!!! Você perdeu essa rodada!!! ''\033[m'
          '\n      A sua escolha foi ''\033[1;31m''{} ''\033[m''a do computador foi ''\033[1;32m' '{}''\033[m''!!'
          '\n''\033[1;31m''                    {} corta o {}!!''\033[m'.format(n2,n3,n3,n2))
    print('\033[1;31m', ' _' * 31, '\033[m')
elif pc == n3 and form == n3:
    print('\033[1;35m', ' -' * 29, '\033[m')
    print('\033[1;35m''                É, dessa vez vocês empataram!! ''\033[m'
          '\n''\033[1;35m''        A sua escolha e a do computador foram {}!!''\033[m'.format(n3))
    print('\033[1;35m', ' _' * 29, '\033[m')
else:
    print('\033[1;31m', ' -' * 40, '\033[m')
    print('\033[1;31m'"                Você digitou um valor inválido!! Tente novamente!!"'\033[m')
    print('\033[1;31m', ' _' * 40, '\033[m')

