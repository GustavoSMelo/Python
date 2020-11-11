users = {}
print(users)

users = {'usuarios': ['Gustavo Santos Melo', 'Geovana Macedo Godoy'],
         'emails': ['gustavo@mail.com', 'geovana@mail.com']}
print(users)

users['senhas'] = ['123456', '123']

print(users)

print(users.get('emails'))
