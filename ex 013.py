salario = float(input('\033[1;35m''Qual o salário do funcionário? R$ ''\033[m'))
au5 = 1.05
au10 = 1.10
au15 = 1.15
au20 = 1.20
au25 = 1.25
au30 = 1.30
au35 = 1.35
au40 = 1.40
print('\033[1;31m''_'*45)
print('\033[m''\033[4m'
      '\nUm funcionário que ganha R$ {:.2f}, ao '
      '\nauferir aumento salarial, passará a receber '
      '\nconfome as seguintes porcentagens:\n'
      '\033[m''\033[1;32m''\n R$ {:.2f} para 5%\n R$ {:.2f} para 10%\n '
      'R$ {:.2f} para 15%\n R$ {:.2f} para 20%\n R$ {:.2f} para 25%\n '
      'R$ {:.2f} para 30%\n R$ {:.2f} para 35%\n R$ {:.2f} para 40%''\033[m'
      .format(salario,salario*au5,salario*au10,salario*au15,salario*au20,
      salario*au25,salario*au30,salario*au35,salario*au40))
print('\033[1;31m''_'*45)
