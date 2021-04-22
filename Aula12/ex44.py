preço = float(input('Digite o valor de sua compra: '))
op = int(input('Como deseja pagar?\n -À vista [1]\n -À vista no cartão [2]\n -2x No cartão [3]\n -3x Ou mais no cartão[4]\nSua escolha: '))
if op == 1:
    print(f'Sua compra deu {preço-preço*0.1} no total.')
elif op == 2:
    print(f'Sua compra deu {preço-preço*0.05} no total.')
elif op == 3:
    print(f'Sua compra deu duas parcelas de {preço/2} no total.')
elif op == 4:
    print(f'Sua compra de três parcelas de {(preço+(preço*0.20))/3:.2f}')