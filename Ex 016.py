import math

n = float(input('\033[32m''Digite um número: ''\033[m'))

print('\033[35m''_'*45)

print('\033[4;34m''O número ''\033[m''{:.2f}''\033[4;34m'' tem a parte inteira ''\033[m' '{:.2f}''\033[m'.format(n, math.trunc(n)))

print('\033[35m''_'*45)