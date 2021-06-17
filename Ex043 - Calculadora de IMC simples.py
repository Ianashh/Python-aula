print('\033[1;32m'' _' * 40, '\033[m')
print('\033[1;32m''      Olá, bem vindo(a) a cauculadora de IMC (Índice de Massa Corporal)!!!''\033[m')
print('\033[1;32m'' _' * 40, '\033[m','\n')
peso = float(input('Por favor. qual o seu peso atual em quilogramas (Kg)? '))
altura = float(input('E agora, digite sua altura em metros (m)? '))
imc = peso/(altura*altura)

print('\033[4;35m''\nSeu IMC é de {:.2f}''\033[m'.format(imc))

if   imc < 18.5:
       print('\nSegundo o IMC, você se encontra ' '\033[1;31m' 'abaixo' '\033[m' ' do peso.\n')
elif imc < 25:
       print('\nSegundo o IMC, você se encontra ' '\033[1;32m' 'no peso ideal.\n' '\033[m')
elif imc < 30:
       print('\nSegundo o IMC, você se encontra ' '\033[1;33m' 'em sobrepeso.\n' '\033[m')
else:
       print('\nSegundo o IMC, você se encontra ' '\033[1;31m' 'em obesidade mórbida.\n' '\033[m')

print('\033[1;34m' ' -' * 40)
print('                           Procure seu médico. '
      '\n          Esse cáuculo não substitui um acompanhamento profissional.')
print(' _' * 40, '\033[m')