from random import randint
from time import sleep
verde = '\033[1;32m'
azul = '\033[1;34m'
amarelo = '\033[1;33m'
vermelho = '\033[1;31m'
purpura = '\033[1;35m'
fmt0 = '\033[m'
pc = 0
cont = 0
print(verde,"="*34)
print('          PAR OU ÍMPAR!!')
print('',"="*34,fmt0)
sleep(2)
print('\033[1;34m''\n     Faaala querido usuário!!!'
      '\n           Tudo bom??''\033[m')
sleep(2)
print('\n''\033[1;33m''****** Negócio é o seguinte, *****'
      '\n***** vejamos quantas vezes ******'
      '\n**** seguidas consegue ganhar ****'
      '\n********** de mim no *************'
      '\n******** PAR ou ÍMPAR!!! *********\n''\033[m')
sleep(5)

while True:
    print(azul,'~'*33)
    jogador = int(input('         FAÇA SUA JOGADA: '))
    print('','~' * 33,fmt0)
    pc = randint(0, 5)
#    if jogador != isinstance(jogador):
    #        while jogador != isinstance(jogador):
    #        print(vermelho, '=' * 25)
    #        print('    Opção inválida!!')
    #        print('=' * 25, fmt0)
    #        sleep(2)
    #        print(azul, '\n      Escolha um número!!', fmt0)
    #        sleep(2)

    print(purpura,f'\nBeleza!! Você escolheu o número {jogador}.',fmt0)
    jogada = input('\033[1;35m''   E ai? Par ou Ímpar [P/I]: ''\033[m').strip().title()

    sleep(2)
    if jogada[0] == 'P':
        print(amarelo, '\n    BELEZA ESTOU ESCOLHENDO!!\n', fmt0)
        sleep(3)
        if (jogador + pc) %2 == 0:
            cont += 1
            print(verde,f'          PARABÉNS !!! '
                        f'\n     A minha escolha foi {pc}.'
                        f'\n       Nossa soma deu {jogador + pc}. '
                        f'\n    Você venceu essa rodada!!!'
                        f'\n         {cont} x 0 pra você!!\n',fmt0)
        elif (jogador + pc) %2 == 1:
            if cont == 1:
                print(vermelho, f'      Haha!!! Essa eu ganhei!! '
                                f'\n        Escolhi o número {pc}.'
                                f'\n', fmt0, verde,
                      f'Você conseguiu vencer {cont} rodada.', fmt0)
                break
            elif cont == 0:
                print(vermelho, f'      Haha!!! Essa eu ganhei!! '
                                f'\n        Escolhi o número {pc}.'
                                f'\n', fmt0, verde,
                      f'Você conseguiu vencer {cont} rodadas. =/ '
                      f'\n     Mais sorte na próxima vez!!!', fmt0)
                break
            else:
                print(vermelho, f'      Haha!!! Essa eu ganhei!! '
                                f'\n        Escolhi o número {pc}.'
                                f'\n', fmt0, verde,
                      f'Você conseguiu vencer {cont} rodadas.', fmt0)
                break

    elif jogada[0] == 'I':
        print(amarelo, '\n    BELEZA ESTOU ESCOLHENDO!!\n', fmt0)
        sleep(3)
        if (jogador + pc) %2 == 1:
            cont += 1
            print(verde, f'          PARABÉNS !!! '
                         f'\n     A minha escolha foi {pc}.'
                         f'\n       Nossa soma deu {jogador + pc}. '
                         f'\n    Você venceu essa rodada!!!'
                         f'\n         {cont} x 0 pra você!!\n', fmt0)
        elif (jogador + pc) %2 == 0:
            if cont == 1:
                print(vermelho,f'      Haha!!! Essa eu ganhei!! '
                               f'\n          Escolhi o número {pc}.'
                               f'\n',fmt0,verde,f'Você conseguiu vencer {cont} rodada.\n',fmt0)
                break
            elif cont == 0:
                print(vermelho, f'      Haha!!! Essa eu ganhei!! '
                                f'\n          Escolhi o número {pc}.'
                                f'\n', fmt0, verde,
                      f'Você conseguiu vencer {cont} rodadas. =/ '
                      f'\n     Mais sorte na próxima vez!!!', fmt0)
                break
            else:
                print(vermelho, f'      Haha!!! Essa eu ganhei!! '
                                f'\n          Escolhi o número {pc}.'
                                f'\n', fmt0, verde,
                      f'Você conseguiu vencer {cont} rodadas.', fmt0)
                break

    else:
        print(vermelho,'='*34)
        print('           Opção inválida!!')
        print('','=' * 34,fmt0)
        sleep(2)
        print(azul,'\n         Escolha um número!!\n',fmt0)
        sleep(2)