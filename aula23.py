#Operadores in e not in
# Strings são interáveis
# 0 1 2 3 4 5
# O t á v i o
#-1 -2 -3 -4 -5
nome = 'Otávio'
print(nome[2])
print(nome[-2])
print('á' in nome)
print('vio' in nome)
print(10 * '----')
print('teste' not in nome)
print('zero' not in nome)
print(10 * '----')
nome2 = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')
if encontrar in nome:
    print(f'{encontrar} não está em {nome2}')
else :
    print(f'{encontrar} não está em {nome2}')