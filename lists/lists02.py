arry = []

qtd = int(1)
while qtd <= 10:
    number = float(input(f'Digite o {qtd}° numero: '))
    arry.append(number)
    qtd += 1

for indice in range(0, len(arry)):
    print(f'O {indice + 1}° numero é: {arry[indice]}')
