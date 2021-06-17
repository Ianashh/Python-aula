from math import ceil
from math import trunc
valor_do_imóvel = float(input('Qual o valor do imóvel pretendido? R$ '))
valor_do_salário = float(input('Qual a sua renda mensal bruta? R$ '))
período = int(input('Quantos anos vocês quer pagar? '))
parcela = valor_do_imóvel / (período*12)
limite_de_parcela = valor_do_salário * 0.3
parcela_máxima = valor_do_imóvel/limite_de_parcela


if parcela > limite_de_parcela:
    print("\033[1;31m", '-' * 30)
    print('   FINANCIAMENTO RECUSADO!!')
    print(' _' * 15, '\033[m')
else:
    print('\033[1;32m'' -' * 40)
    print('          PARABÉNS!!!! SEU CADASTRO FOI APROVADO POR NOSSO BANCO!!!')
    print(' _' * 40, '\033[m''\n')
    print('Sua parcela de financiamento será de' '\033[1;32m' ' R$ {:.2f}' '\033[m' ' podendo, a sua escolha, chegar '
          '\nao limite de até' '\033[1;32m' ' R$ {:.2f}.' '\033[m'
          '\n\nO prazo escolhido foi de' '\033[1;34m' ' {} anos ' '\033[m' 'para o imóvel no valor de ' '\033[4;32m' 'R$ {:.2f}''\033[m' '.'
          '\n\nCaso opte pela parcela máxima, seu prazo será reduzido para ' '\033[4;35m' '{:.0f} meses''\033[m' ', '
          '\nou ''\033[4;33m''{} anos e {} meses' '\033[m' ' com parcelas de ' '\033[4;32m' 'R$ {:.2f}\n' '\033[m'
          .format(parcela,limite_de_parcela,período,valor_do_imóvel,parcela_máxima,(parcela_máxima/12).__trunc__(),
           (parcela_máxima%12).__ceil__(), limite_de_parcela))


print('\033[1;34m' ' -' * 40, '\033[m')
print ('\033[1;34m''                      O banco Py agradece a preferência!!'
       '\n                              TENHA UM BOM DIA!!!''\033[m')
print('\033[1;33m' ' _' * 40, '\033[m')