n = int(input ('Qual número deseja escolher? '))
cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'lilas':'\033[35m',
         'ciano':'\033[36m'}
formatação = {'negrito':'\033[1m',
              'sublinhado':'\033[4m'}

print('O dobro de {}{}{} vale {}{}{}'.format(cores['azul'],n,cores['limpa'],cores['verde'],(n*2),cores['limpa']))
print('O triplo de {}{}{} vale {}{}{}'.format('\033[34m',n,'\033[m','\033[32m',(n*3),'\033[m'))
print('A raiz quadrada de {}{}{} é igual a {}{}{:.2f}{}'.format('\033[34m',n,'\033[m','\033[4m','\033[32m',(n**(1/2)),'\033[m'))

