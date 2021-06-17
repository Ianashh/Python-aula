distancia = float(input('Qual a distância, em quilometros, total da viagem? '))
passagem1 = 0.50*distancia
passagem2 = 0.45*distancia

if distancia <= 200:
    print ('\nSeu custo com passagem será de R$ {:.2f}.\n'.format(passagem1))
else:
    print('\nSeu custo com passagem será de R$ {:.2f}.\n'.format(passagem2))

print('Escolha sempre com segurança e economia.\nEscolha a Decorolar.com')
