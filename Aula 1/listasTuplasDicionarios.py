#!/usr/bin/python3
#import random
# Contagem de lista começar com zero
#lista = ['Arroz','Feijão','Oleo','Sal', 'Açucar', 'Temperos']
#print(lista[0])
#print(lista[4])
#print(lista[0:4])
#print(lista[0:4:2])
#lista3d = [
#    [1,3,4,5],
#    [3,4,5,6],
#    [7,5,7,8]
#]

#print(lista3d[2][2])
#lista.append('carne')
#print(lista)

#lista.insert(0,'Sabão em pó')
#lista.pop(0)
#lista.sort()
#lista.reverse()

#print(lista)
#lista.remove ('Sal')

#lista.insert(7,'Banana')

#print(len(lista))

#print(lista.index('Açucar'))

#print(lista.count('Arroz'))

#print(lista)

#lista[3] = 'Maça'
#print(lista)

################ TUPLAS

# tupla = ('Maça','Banana','Laranja','Abacaxi','Uva')
# print(type(tupla))

# tupla2 = 'valor1', 2, True,2j
# print(type(tupla2))

# print(tupla[3])
# print(tupla[1:4])
# print(tupla[-2])
# print(tupla)

# tupla = (['Indice 1']), 'Nome')
# tupla[0].insert(1,'Indice 2')
# print(tupla)

#############
##### Dicionários
#############
# Criando um dicionário
# apresentacoes = {
#     'Paulista' : 'Salve',
#     'Carioca' : 'VaiFlamengo',
#     'Pirata' : 'Argh',
#     'Minero' : 'Pão de queijo',
#     'Acre ' : 'Barulhos de Dinossauro',
# }

# # Acessando índices de um dicionário
# print(apresentacoes['Paulista'])

# #Criando um dicionario com multi-valores internos
# linguagem_favorita = {
#     'Daniel' : {
#         'linguagem' : 'Python',
#         'Tempo_experiência' : 2
#     },
#     'Olympio' : {
#         'linguagem' : 'R',
#         'linguagem2' : 'VBA',
#         'Tempo_experiencia' : 10
#     },
# }    

# print(linguagem_favorita.get('Daniel'))
# #print(linguagem_favorita.get('Daniel'),['linguagem]'])

# # Acesso a todas chaves
# print(linguagem_favorita.keys())
# # Acesso aos valores
# print(linguagem_favorita.values())
# print(linguagem_favorita.items())

############
####### Números
################

somar = 2 + 2
print(2 + 2)
print(somar)
subtrair = somar - 2
print(subtrair)
multiplicar = subtrair * 3
print(multiplicar)
divisao = multiplicar / 5
print(divisao)

potencia = 2**2
print(potencia, 'Retornando o valor da Potência')
raiz = 2 ** 0.5
print(raiz, 'Retornando o valor da raiz')

letras = 'abcde'
print(letras[0])

letras = 'abcde' + 'opljuk'
#git push
# print(input()'digite um numero: ') + (input('Digite outro numero: '))