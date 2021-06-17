for c in range(2,1000):
    if c %2 != 0 or c == 2:
       if c %3 != 0 or c == 3:
          if c % 5 != 0 or c == 5:
              if c %7 != 0 or c == 7:
                  if c % 11 != 0 or c == 11:
                    print('O número {} é um número primo.'.format(c))
