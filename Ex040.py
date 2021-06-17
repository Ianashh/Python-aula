nota1 = float(input('De 0 a 10, qual foi a nota obtida na primeira avaliação? '))
nota2 = float(input('De 0 a 10, qual foi a nota obtida na segunda avaliação? '))
média = (nota1+nota2)/2

if média >= 7:
    print('Sua média foi {:.2f}. PARABÉNS!!! Você está aprovado!!'.format(média))
elif média < 5:
    print(f'Sua média foi {média:.2f}. QUE PENA, VOCÊ ESTÁ REPROVADO POR FALTA DE NOTA.')
else:
    print(f'Sua média foi {média:.2f}. Você está em recuperação.  Procure seu professor para maiores informações.')