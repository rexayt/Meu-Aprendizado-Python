p = int(input('Digite o primeiro número: '))
r= int(input('Digite a razão da PA: '))
c= 1
f = p
while c <= 10:
    print('{}'.format(f), end='')
    print(' ->' if c < 10 else '-> Fim', end=' ')
    f += r
    c += 1
    