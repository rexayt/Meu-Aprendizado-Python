def notas(*num, sit=False):
    dicionário = dict()
    dicionário['Total'] = len(num)
    dicionário['Maior'] = max(num)
    dicionário['Menor'] = min(num)
    dicionário['Média'] = sum(num)/len(num)
    if sit:
        if dicionário['Média'] >= 7:
            dicionário['Situação'] = 'Boa'
        elif dicionário['Média'] >= 5:
            dicionário['Situação'] = 'Médiana'
        elif dicionário['Média'] <= 4:
            dicionário['Situação'] = 'UMA PORCARIA'
    return dicionário

        
resp = notas(3, 3, 5,sit=True)
print(resp)