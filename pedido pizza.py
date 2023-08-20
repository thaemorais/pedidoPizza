ingr_cliente = []
cont = 's'

while cont.lower() == 's':
    ing = input('Digite o ingrediente que deseja colocar na sua pizza: ')
    ingr_cliente.append(ing)
    cont = input('Deseja acrescentar mais um? s ou n? ')

ingr_estoque = ['tomate', 'pimentao', 'katchup', 'catupiry', 'frango']

print('')
for ingr in ingr_cliente:
    if ingr in ingr_estoque:
        print('Foi adicionado ' + ingr + ' a sua pizza.')
    else:
        print('Sinto muito, não temos ' + ingr + ' em nosso estoque.')

print('\nSua pizza está pronta.\n')