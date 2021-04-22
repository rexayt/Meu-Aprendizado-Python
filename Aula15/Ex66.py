s=n=c=0
while True:
    n = int(input('Digite um número: [Digite 999 para parar.] '))
    if n == 999:
        break
    s += n
    c += 1
if c == 1:
    print(f'Você digitou o número {n}')
elif c == 0:
    print('Você não digitou número além de 999')
else:
    print(f'Você digitou {c} Números e a soma dele é {s}')