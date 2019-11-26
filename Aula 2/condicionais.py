#!/usr/bin/python3


#####
##Estrutura de condiconal simples
###### 
#nome = input('Digite seu nome: ')

# if nome == 'Daniel':
#     print('Olá, professor')
# print('Seja bem vindo')

#####
##Condicional composta
#####

# if nome == 'Daniel':
#     print(f'Bem vindo professor {nome}')
# else:
#     print(f'Bem vindo aluno {nome}')
# print('Você pode utilizar a plataforma')


## Comparando duas condições

# nome = input('Digite seu nome: ').strip().title()
# sobrenome = input('Digite seu sobrenome: ').strip().title()

# if nome == 'Daniel' and sobrenome == 'Silva': #pode-se utilizar o OR
#      print(f'Bem vindo professor {nome}')
# else:
#      print(f'Bem vindo aluno {nome}')
# print('Você pode utilizar a plataforma')


#####
##Condicionais Encadeadas
#####

# nome = input('Digite seu nome: ').strip().title()
# sobrenome = input('Digite seu sobrenome: ').strip().title()

# if nome == 'Daniel':
#     if sobrenome == 'Silva':
#         print('Olá, professor')
#     else:
#         print('Você é Daniel, mas não é professor')
# else:
#     print(f'Olá aluno {nome}')

#####
##Condicionais aninhadas
#####

#Validaçãp em mais de um fator
#com comportamento diferente

nome = input('Digite seu nome: ').strip().title()
if nome == 'Daniel':
    print(f'Seu nome é muito bonito, {nome}')
elif nome == 'Juliana':
    print(f'Seu nome é bem legal, {nome}')
elif nome == 'Jorge':
    print(f'Seu nome é bem feio, {nome}')
else:
    print(f'Seu nome é bem normal, {nome}')

