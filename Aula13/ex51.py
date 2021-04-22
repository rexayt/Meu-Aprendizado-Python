n = int(input('Digite um número: '))
r = int(input('Digite quantos números serão pulados: '))
for c in range(n, n + (10-1) * r, r):
    print(c, end=' -> ')
print('cabo')