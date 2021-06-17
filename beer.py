from math import ceil
beer = (int(input('Quantas beers pretende comprar? ')))
preçobeer= float(input('Qual o valor unitário das beers? R$ '))
desconto = float(input('Informe o valor do cupom de desconto: R$ '))
frete = float(input('Informe o valor do frete: R$ '))
beertotal = beer*preçobeer
vl = beertotal-desconto
if frete == 0:
      print('\nO valor de {} beers é de R$ {:.2f}.\n'
      '\nO valor com desconto é de R$ {:.2f}.\n'
      '\nSaindo cada beer no valor líquido de R$ {:.2f}\n'
      '\nPara chegar a R$ 100.00, seu pedido deve conter {} beers(Desconsiderando o frete). '
      .format(beer,beertotal,beertotal-desconto,vl/beer,ceil(100/preçobeer)))
else:
      print('\nO valor de {} beers é de R$ {:.2f}.\n'
            '\nO valor com desconto é de R$ {:.2f}.\n'
            '\nSaindo cada beer no valor líquido de R$ {:.2f}\n'
            '\nPara chegar a R$ 100.00, seu pedido deve conter {} beers(Desconsiderando o frete).\n'
            '\nValor unitário líquido com frete sai por {:.2f}. Valor total com frete: {:.2f}'
            .format(beer, beertotal, beertotal - desconto, vl / beer, ceil(100 / preçobeer),(frete+vl)/beer,frete+vl))