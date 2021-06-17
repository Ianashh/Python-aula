din = float(input("Quanta grana vc tem ai? R$ "))
b = din/3.27
cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'lilas':'\033[35m',
         'ciano':'\033[36m'}
formatação = {'negrito':'\033[1m',
              'sublinhado':'\033[4m'}

print('Blz, da pra comprar uns {}{}US$ {:.2f}{}'.format(formatação['sublinhado'],cores['verde'],b,cores['limpa']))


