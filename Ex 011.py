largura = float(input('Qual a largura da sua parede? '))
altura = float(input('Qual a altura da sua parede? '))
area = largura*altura
print('Sua parede tem a dimenção de {}x{} e sua área é de {:.2f}'.format(largura,altura,area))
print('Para pintar sua parede, serão necessários {:.2F} litros de tinta.'.format(area/2))