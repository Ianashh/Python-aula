m = float(input('Quantos metros: '))
cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'lilas':'\033[35m',
         'ciano':'\033[36m'}
formatação = {'negrito':'\033[1m',
              'sublinhado':'\033[4m'}
print("A medida de {}{}{} corresponde a: {}\n{:.4} km, \n{:.4f} hm, \n{:.4f} dam, \n{:.4f} dm, \n{:.4f} cm, "
      "\n{:.4f} mm.{} "
      .format(cores['lilas'],m,cores['limpa'],cores['vermelho'], m/1000, m/100, m/10, m*10, m*100, m*1000,cores['limpa']))


