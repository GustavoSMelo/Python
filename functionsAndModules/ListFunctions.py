def find(list):
    searchName = str(input("Digite o nome que deseja procurar na lista: "))
    resultSearch = 'Nenhum nome encontrado dentro da list'
    for index in range(0, len(list)):
        if(list[index] == searchName):
            resultSearch = f'O nome: {searchName} foi encontrado na {index + 1}° posição da lista'

    input(resultSearch)


def add(list):
    index = int(1)

    while(index <= 10):
        name = str(input('Digite o nome de alguem: '))
        list.append(name)
        index += 1
    print('Lista populada com sucesso !')


def index(list):
    for elements in list:
        print(elements)

