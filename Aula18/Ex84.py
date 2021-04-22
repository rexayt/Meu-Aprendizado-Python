pessoas=[]
pessoas2=[]
leves=[]
pesadas=[] 
maior = menor = cont = 0
o = 'S'
while o in 'Ss':
    nome = str(input('Digite o nome da pessoa: ')).strip()
    while nome == '':
        nome = str(input('Comando inválido\nDigite o nome do indivíduo: '))
    peso = int(input('Digite o peso da pessoa (APENAS NÚMEROS): '))
    pessoas.append(nome)
    pessoas.append(peso)
    pessoas2.append(pessoas[:])
    pessoas.clear()
    o = str(input('Deseja continuar?\n[S/N]: ')).strip().upper()
    while o not in 'SsNn':
        o = str(input('Comando inválido, Digite S ou N: ')).upper().strip()
for c in pessoas2:
    print(c[1])
    if cont == 0:
        maior = c[1]
        menor = c[1]
        leves.append(c[0])
        pesadas.append(c[0])
    else:
        if c[1] > maior:
            maior = c[1]
            if len(pesadas) > 0:
                pesadas.clear()
            pesadas.append(c[0])
        elif c == maior: 
            pesadas.append(c[0])    
        if c[1] < menor:
            menor = c[1]
            if len(leves) > 0:
                leves.clear()
            leves.append(c[0])
        elif c[1] == menor:
            leves.append(c[0])    
    cont += 1
print(f'Os mais leves são: {leves}, pesando {menor} Kilos')
print(f'Os mais pesados são: {pesadas}, pesando {maior} Kilos')
print(pessoas2)