#!/usr/bin/python3

######## 
##Lacos de repetição
##Lacos while
########

#Este laço executa enquanto uma condição for verdadeira

# i = 0
# while( i < 10): # enquanto i for meno que 10
#     print(i) # mostra valor de 1
#     i += 1 # i =i + 1
    #repete

#     #Como fazer controle de um loop while

# i = 0
# while(True):
#     i += 1
#     if i == 3:
#         break
#     if i == 5:
#         continue
#     print('Teoricamente, um  loop infinito')

# Continue retoma do começo a execução de um loop

# i = 100 #número inicial
# while i > 0: # Enquanto 1 < 0
#     i -= 1 # i = i -1
#     if i % 2 == 0:
#         continue
#     print(i)

######
## Laço For
######

#Percorre itens em determinado alcance de valores

# lista = []
# for i in range(1000):
#         lista.append(i)
# print(lista)

# for i in lista:
#     if i % 2 == 0:
#         print(f'\033[31m{i}\033[0m', 'par')
#     if i % 2 == 1:
#         print(f'\033[32m{i}\033[0m', 'impar')

# percorre um dicionário

# dicionario = {'nome':'Daniel', 'sobrenome':'Silva'}
# for i in dicionario:
#     print(dicionario[i])

# for chave, valor in dicionario.items():
#     print(chave)
#     print(valor)

# Enumerando itens de uma lista
# lista = ['item1','item2','item3','item4']

# for i in enumerate(lista):
#     print(i)

# list comprehension

lista = [i for i in range(100)]
print(lista)