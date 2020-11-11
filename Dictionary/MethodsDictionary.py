def store(dictionary):
    login = str(input('Digite seu login: ')).lower()
    password = str(input('Digite sua senha: ')).lower()

    dictionary['login'] = [login]
    dictionary['password'] = [password]
    print('user inserted with success')


def index(dictionary):
    print(dictionary)
