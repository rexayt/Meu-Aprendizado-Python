p=int(input('Digite um número: '))
t = 0
for c in range(1, p + 1,):
    if p % c == 0:
        print('\033[33m', end=' ')
        t += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('O número {}, foi divísivel {} vezes'.format(p, t))
if t == 2:
    print('O número {} é PRIMO'.format(p))
else:
    print('O número {} não é primo.'.format(p))