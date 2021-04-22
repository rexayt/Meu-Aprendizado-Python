p = str(input('Digite uma expressão matemática: '))
lista = []
for c in p:
    if c == '(':
        lista.append('(')
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            pilha.append(')')
            break
