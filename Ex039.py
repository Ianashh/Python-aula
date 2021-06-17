import datetime
ano_de_nascimento_do_jovem = int(input('Digite seu ano de nascimneto com 4 digitos: '))
idade = datetime.datetime.now().year - ano_de_nascimento_do_jovem
year = datetime.datetime.now().year
if idade < 18:
    print('Você irá se alistar daqui {} anos.'.format(18-idade))
elif idade > 18:
    print('O seu tempo de se alistar foi a {} anos.'.format(idade-18))
else:
    print('Esse é o ano de seu alistamento. Não perca as datas!!')

