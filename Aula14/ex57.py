c = str(input('Digite seu sexo [M/ F]: ')).upper().strip()[0]
while c not in 'MnFf':
    c = str(input('Comando inválido, digite novamente: ')).strip().upper()[0]
print('Seu sexo foi registrado com sucesso')