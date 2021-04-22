lista = []
pares = []
ímpares = []
c = 'S'
while True:
    while c == 'S':
        num = int(input('Digite um número: '))
        lista.append(num)
        if num % 2 == 0:
            pares.append(num)
        else:
            ímpares.append(num)
        c = str(input('Você deseja continuar? [S/N]: ')).upper()
    break   
print(lista)
print(pares)
print(ímpares)