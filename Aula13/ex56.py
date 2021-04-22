si = 0
sim = 0
nm = ''
mi = 0
muié = 0
for c in range(1, 4+1):
    n=str(input('Digite seu nome: '))
    i=int(input('Digite sua idade:'))
    s=str(input('Digite seu sexo [M/F]: '))
    sim += i
    if c == 1 and s in 'Mm':
        si = i
        nm = n
    if s in 'Mm' and i > si:
        si = i
        nm = n
    if i < 20 and s in 'Ff':
        muié += 1
mi = sim / 4
print('A média de idade do grupo é {} anos.'.format(mi))
print('O homem mais velho é o {}, e tem {} anos.'.format(nm, si))
if muié >= 2:
    print('Tem {} mulheres com menos de 20 anos'.format(muié))
else:
    print('Tem {} mulher com menos de 20 anos.'.format(muié))
