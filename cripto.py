from auxiliar import cipher
from getpass import getpass

passwords = {'wallet': 'Lqod36fQA9oA0g3'}

print('Que pass estas buscando?')
keyword = input()

if keyword in passwords.keys():
    print('Cual es la llave?')
    print(cipher(passwords[keyword],getpass()))
else:
    print('No tenes guardada esa pass')

