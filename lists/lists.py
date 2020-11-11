numbers = []

while True:
    typedNumber = int(input('digite um numero para colocar no array '))
    numbers.append(typedNumber)

    again = str(input('Deseja continuar [S/n] ou [s/n] ?'))
    while again != 'S' and again != 's' and again != 'n' and again != 'N':
        again = str(input('Deseja continuar [S/n] ou [s/n] ?'))

    if again == 's' or again == 'S':
        continue
    else:
        break

for elements in numbers:
    print(elements)
