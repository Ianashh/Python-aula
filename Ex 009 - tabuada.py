n = int(input('Digite um numero para ver sua tabuada: '))
cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'lilas':'\033[35m',
         'ciano':'\033[36m'}
formatação = {'negrito':'\033[1m',
              'sublinhado':'\033[4m'}
print('_' *15)
print('{}{}{} x 01 = {} \n{} x 02 = {} \n{} x 03 = {} \n{} x 04 = {} \n{} x 05 = {} \n{} x 06 = {} \n{} x 07 = {} \n{} x 08 = {} \n{} x 09 = {} \n{} x 10 = {}{}'
    .format(formatação['sublinhado'],cores['verde'],n, n*1,n, n*2,n, n*3,n, n*4,n, n*5,n, n*6,n, n*7,n, n*8,n, n*9,n, n*10,cores['limpa']))
print('_' *15)