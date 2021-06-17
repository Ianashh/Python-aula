a = float(input('\033[1;35m''Qual a quantidade de Kms percorridos: Km: '))
b = float(input('\033[1;35m''Qual a quantidade de dias alugados: Dias: '))
aa = a*0.15
bb = b*60
print('\033[1;31m''_'*45)

print('O valor total a pagar é de: ''\033[4;32m''R$ {:.2f}''\033[m'.format(aa+bb))


print('\033[1;31m''_'*45)