from time import sleep
n = int(input('Digite um número: '))
for c in range(1, 10+1):
    print('{} x {} = {}'.format(n, c, n*c))
    sleep(1)