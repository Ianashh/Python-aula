salario = float(input('Qual o salário a atribuir? R$ '))
dez = 0.10
quinze = 0.15

if salario > 1250.00:
    print ('\nO aumento salarial será de 10% passando a ser {:.2f}'
           .format (salario + salario * dez))
else:
    print('\nO aumento salarial será de 15% passando a ser {:.2f}'
          .format(salario + salario * quinze))

print ('Att. Emerson Marcelino\nAcessor de RH.')