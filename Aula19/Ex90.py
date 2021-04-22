dicionário = {'Nome': '', 'Média': 0, 'Situação': ''}
dicionário['Nome'] = str(input('Digite o Nome do aluno: '))
dicionário['Média'] = float(input('Digite a Média do aluno: '))
if dicionário['Média'] >= 5 and dicionário['Média'] <= 7:
    dicionário['Situação'] = 'Recuperação'
elif dicionário['Média'] >= 7:
    dicionário['Situação'] = 'Aprovado'
else:
    dicionário['Situação'] = 'Reprovado'
print('-='*30)
for k, v in dicionário.items():
    print(f'  - {k} é igual a {v}')
