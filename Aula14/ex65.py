c=r=ma=me=t=0
s = 'S'
i= int(input('Digite um número: '))
while s not in 'Nn':
    s = str(input('Você deseja continuar?\n[S/N]: ')).upper()
    if s in 'Ss':
        i=int(input('Digite mais um número: '))
        c += 1
        

print(c)