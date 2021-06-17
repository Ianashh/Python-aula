kmh = int(input('Qual a velocidade do carro (Km/h): '))
multa = 7
limite = 80
if kmh > 80:
    print('\nVocê ultrapassou o limite de velocidade da via e será multado.\n')
    print('O valor da sua multa é de R$ {:.2f}\n'.format(multa*(kmh-limite)))
else:
    print('\nVocê está dentro dos limites de velocidade!!\n')

print('Detran-PR')