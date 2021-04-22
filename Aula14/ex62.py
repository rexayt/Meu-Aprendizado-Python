p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a PA: '))
f = p
b = 0
c = 1
n = 10
while n != 0:
    b += n
    while c <= b:
        print('{} ->'.format(f), end=' ')
        f += r
        c += 1
    print('Pausa')
    n = int(input('Quantos números você quer contar a mais? '))
print('Cabô, {} termos, foram mostrados.'.format(b))