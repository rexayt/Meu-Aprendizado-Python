n = c = 0
while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break
    for c in range(1, 10+1):
        print(f'  {n} X {c} = {n*c}'))
print('Fim')