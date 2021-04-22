f=str(input('Digite uma frase: ')).strip().upper()
p = f.split()
j = ''.join(p)
i = ''
for c in range(len(j)-1, -1, -1):
    i += j[c]
if i == j:
    print('A frase é um palíndromo')
else:
    print('¯\_(ツ)_/¯')