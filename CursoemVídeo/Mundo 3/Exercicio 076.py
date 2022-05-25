print('===' * 15)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('===' * 15)
listagem = 'Lápis', 1.75,\
           'Borracha', 2.00,\
           'Caderno', 15.90,\
           'Estojo', 25.00,\
        'Trasnferidor', 4.20,\
           'Compasso', 9.99,\
           'Mochila', 120.32,\
           'Canetas', 22.30,\
           'Livro', 34.90
for c in range(0, len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<30}', end='')
    else:
        print(f'R$ {listagem[c]:>7.2f}')
