from datetime import datetime

ano_de_nascimento_do_atleta = int(input('Digite o ano de nascimento do atleta: '))
idade = datetime.now().year - ano_de_nascimento_do_atleta

if idade <= 9:
    print('O atleta de {} anos é classificado como MIRIM.'.format(idade))
elif idade <= 14:
    print('O atleta de {} é classificado como INFANTIL.'.format(idade))
elif idade <= 19:
    print('O atleta de {} é classificado como Junior.'.format(idade))
elif idade <= 20:
    print('O atleta de {} é classificado como SÊNIOR.'.format(idade))
else:
    print('O atleta de {} é classificado como MASTER.'.format(idade))
