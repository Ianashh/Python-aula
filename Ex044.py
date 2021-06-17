
preço = float(input('Qual o valor do produto? R$ '))
parcela = (int(input('Deseja parcelar o valor de R$ {:.2f} em quantas vezes? '.format(preço))))
à_vista = preço * 0.90
cartão= preço * 0.95
parc2 = preço / 2
parcx = (preço * 1.2) / parcela

if parcela == 0:
    print('O valor a pagar é R$ {:.2f}'.format(à_vista))
elif parcela == 1:
    print('O valor a pagar no cartão é R$ {:.2f}'.format(cartão))
elif parcela == 2:
    print('O valor a pagar em até 2x é R$ {:.2f}'.format(preço/2))
else:
    print('O valor a pagar é de {}x de R$ {:.2f}'.format(parcela,parcx))