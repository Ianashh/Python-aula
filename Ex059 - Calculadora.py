from time import sleep
# Passo 1: criar variáveis

n1 = float(input('Digite o 1º valor: '))
n2 = float(input('Digite o 2º valor: '))
escolha = ''

# Passo 2: Rodar "while" até pedir pra sair do programa


while escolha != 9:
      escolha = int(input('\033[1;34m''MENU\n''\033[m'
                          '\033[1;33m''[1]''\033[m''\033[1;34m''SOMAR''\033[m''\n'
                          '\033[1;33m''[2]''\033[m''\033[1;34m''SUBTRAIR''\033[m''\n'
                          '\033[1;33m''[3]''\033[m''\033[1;34m''MULTIPLICAR''\033[m''\n'
                          '\033[1;33m''[4]''\033[m''\033[1;34m''DIVIDIR''\033[m''\n'
                          '\033[1;33m''[5]''\033[m''\033[1;34m''MAIOR VALOR''\033[m''\n'
                          '\033[1;33m''[6]''\033[m''\033[1;34m''MENOR VALOR''\033[m''\n'
                          '\033[1;33m''[7]''\033[m''\033[1;34m''EXPONENCIAL''\033[m''\n'
                          '\033[1;33m''[8]''\033[m''\033[1;34m''NOVOS NÚMEROS''\033[m''\n'
                          '\033[1;33m''[9]''\033[m''\033[1;34m''SAIR DO PROGRAMA''\033[m''\n'
                          f'\nNúmeros escolhidos {n1} e {n2}\n'
                          '\033[1;33m''\nDIGITE UMA OPÇÃO: ''\033[m'))
      if escolha == 1:
          print('\033[32m' f'\nA soma de {n1} mais {n2} é igual a {n1+n2}''\033[m')
      elif escolha == 2:
          print('\033[32m' f'\nA subtração de {n1} menos {n2} é igual a {n1 - n2}''\033[m')
      elif escolha == 3:
          print('\033[32m' f'\nA multiplicação de {n1} vezes {n2} é igual a {n1 * n2}''\033[m')
      elif escolha == 4:
          print('\033[32m' f'\nA divisão de {n1} por {n2} é igual a {n1 / n2}''\033[m')
      elif escolha == 5:
          print('\033[32m' f'\nO maior número entre {n1} e {n2} é {max(n1,n2)}''\033[m')
      elif escolha == 6:
          print('\033[32m' f'\nO menor número entre {n1} e {n2} é {min(n1,n2)}''\033[m')
      elif escolha == 7:
          print('\033[32m' f'\nO número {n1} elevado a {n2} é igual a {pow(n1,n2)}''\033[m')
      elif escolha == 8:
          print('\033[32m' f'\nDigite 2 novos números!!''\033[m')
          n1 = float(input('Digite o 1º valor: '))
          n2 = float(input('Digite o 2º valor: '))
      elif escolha == 9:
          print('\033[31m' f'\nO programa está se encerrando!!')
          sleep(1)
          print('....5')
          sleep(1)
          print('...4')
          sleep(1)
          print('..3')
          sleep(1)
          print('.2')
          sleep(1)
          print('1')
          sleep(2)
          print('PROGRAMA FINALIZADO! ATÉ BREVE!!''\033[m')
          break
      else:
          print(f'\nA opção "{escolha}" não é uma opção válida!!')
          escolha = int(input('\033[1;34m''MENU\n''\033[m'
                              '\033[1;33m''[1]''\033[m''\033[1;34m''SOMAR''\033[m''\n'
                              '\033[1;33m''[2]''\033[m''\033[1;34m''MULTIPLICAR''\033[m''\n'
                              '\033[1;33m''[3]''\033[m''\033[1;34m''MAIOR VALOR''\033[m''\n'
                              '\033[1;33m''[4]''\033[m''\033[1;34m''NOVOS NÚMEROS''\033[m''\n'
                              '\033[1;33m''[5]''\033[m''\033[1;34m''SAIR DO PROGRAMA''\033[m''\n'))