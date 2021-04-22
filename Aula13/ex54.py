from datetime import date
from time import sleep
cont = 0
con = 0
for c in range(1, 8):
    v = int(input('Digite a data de nascimento da {} pessoa:\033[1;32m \033[m'.format(c)))
    a = date.today().year - v
    sleep(1)
    if a <= 21:
        cont += 1
    else:
        con += 1
print('Tivemos {} pessoas maiores de idade.'.format(con))
print('Tivemos {} pessoas menores de idade.'.format(cont))
