import random
b = range(1000)
número = random.choice(b)
alfab = str(número)
print(b)
print(número)
print(alfab)
print(type(alfab))
#caraca nunca sofri tanto hahaha mas fazer por módulos vale a pena. baby steps count.py
if número >= 1000:
    print('O número é {}.\nEsse número é classificado em:'
          '\nMilhar {}\nCentena {}\nDezena {}\nUnidade {}'
          .format(alfab, alfab[0], alfab[1], alfab[2], alfab[3]))
elif número == range(1000):
    print('O número é{}. Esse número é classificado em:'
          '\nMilhar {} \nCentena {}\nDezena {}\nUnidade {}'
          .format(alfab, alfab[0], alfab[1], alfab[2], alfab[3]))
elif número == range(100):
    print('O número é{}. Esse número é classificado em:'
          '\nMilhar 0 \nCentena {}\nDezena {}\nUnidade {}'
    .format(alfab, alfab[0], alfab[1], alfab[2], alfab[3]))
else:

    print('desisto')

    print('\033[1;32m'' -' * 40)
    print('          PARABÉNS!!!! SEU CADASTRO FOI APROVADO POR NOSSO BANCO!!!')
    print(' _' * 40, '\033[m')