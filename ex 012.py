preço = float(input('Qual o preço do produto? RS '))
desc = 0.95
print('\033[m''O produto que custava' '\033[34;40m' 'R$ {}' '\033[m'' na promoção, '
      'com desconto de 5%, vai custar ''\033[4;32m''R$ {:.2f}.''\033[m'.format(preço,preço*desc))
