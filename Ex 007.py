n1 = float(input('Qual a primeira nota do aluno? '))
n2 = float(input('Qual a segunda nota do aluno? '))

formatação = {'negrito':'\033[1m',
              'sublinhado':'\033[4m'}

print('A média entre {:.2f} e {:.2f} é igual a {}{:.2f}'.format(n1,n2,formatação['sublinhado'],((n1+n2)/2)))
