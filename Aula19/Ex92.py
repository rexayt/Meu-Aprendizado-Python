from datetime import datetime
pessoa={}
pessoa['Nome']=str(input('Digite o nome da pessoa: '))
nas =int(input('Digite a data de nascimento da pessoa: '))
pessoa['Idade']=datetime.now().year - nas
pessoa['ctps'] = int(input('Digite o número da carteira de trabalho (0 se não tiver): '))
if pessoa['ctps'] != 0:
    pessoa['Ano de contratação']=int(input('Digite o ano de contratação: '))
    pessoa['Salário']=float(input('Digite o salário: '))
    pessoa['Aposentadoria'] = pessoa['Idade'] + ((pessoa['Ano de contratação']+35)-datetime.now().year)
print('-='*30)
for k, v in pessoa.items():
    print(f' - {k} tem o valor {v}')