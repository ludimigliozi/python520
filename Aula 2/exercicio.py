#!/usr/bin/python3


#####
## Exercício condicional composta
#####

# Criar uma variável idade onde recebe uma
# idade via linha de comando, validar se essa
# pessoa pode beber, caso possa, atribuir
# ao valor de uma variável embriagado valor true, senão false

# idade = input('Você é maior de 18 anos? ')

# if idade == 'sim':
#     print('você está bebado')
# else:
#     print('Você esta sóbrio')

# idade = int(input('Digite sua idade: '))

# if idade >= 18:
#     embriagado = True 
# else:  
#     embriagado = False

# print(embriagado)



#Criar condicional para que se a pessoa estiver embriagada,
#mostrar uma mensagem que ela não pode dirigir

# idade = input('Você possui CNH ').strip()

# if idade == 'sim':
#     print('você pode dirigir')
# else:
#     print('Você não pode dirigir')



# bebida = input('Você bebeu alguma bebida com alcool? ').strip()

# if bebida == 'sim':
#     print('você não pode dirigir')
# else:
#     print('Você pode dirigir')

# idade = input('Digite sua idade ').strip()
# habilitacao = input('Você possui habilitação ').strip().lower()

# #Criar validação se a pessoa bebebu para atribuir a variavel embriagado como True ou Flasse

# if idade >= 18:
#     embriagado = True
# else:
#     embriagado = False

# if habilitacao == 'sim':
#     habilitação = True
# else:
#     habilitacao = False


# if habilitacao == 'sim' and not embriagado:
#     print('Você pode dirigir')
# else:
#     print('VocÊ não pode dirigir')


# idade = input('Digite sua idade ').strip()
# habilitacao = input('Você possui habilitação ').strip().lower()

#Criar validação se a pessoa bebebu para atribuir a variavel embriagado como True ou Flasse


#!/usr/bin/python3

#####
## Exercicio condicional composta
#####

# Criar uma variavel idade onde recebe uma
# idade via linha de comando, validar se essa
# pessoa pode beber ou não, caso possa, atribuir
# ao valor de uma variável embriagado o valor true, senão false

# idade = int(input('Digite sua idade: '))

# # Criar Validação se a pessoa bebeu para atribuir a variável 
# # embriagado como True ou false

# if idade >= 18:
#     # If's validam se variável tem conteúdo
#     habilitacao = input('Você possui Habilitação: [y para sim e n para não] ').strip().lower()
#     if habilitacao == 'y':
#         habilitacao = True
#         bebeu = input('Você bebeu? digite algo para sim, enter para não ').strip()
#         if bebeu:
#             embriagado = True
#         else:
#             embriagado = False
#     else:
#         habilitacao = False
# else:
#     embriagado = False

# # Criar uma validação para que se a pessoa tiver carteira de
# # motorista, ela possa dirigir. Porém
# # Criar condicional para que se a pessoa estiver embriagada,
# # mostrar uma mensagem que ela não pode dirigir


#!/usr/bin/python3

#####
## Exercicio condicional composta
#####

# Criar uma variavel idade onde recebe uma
# idade via linha de comando, validar se essa
# pessoa pode beber ou não, caso possa, atribuir
# ao valor de uma variável embriagado o valor true, senão false

idade = int(input('Digite sua idade: '))

# Criar Validação se a pessoa bebeu para atribuir a variável 
# embriagado como True ou false

if idade >= 18:
    # If's validam se variável tem conteúdo
    habilitacao = input('Você possui Habilitação: [y para sim e n para não] ').strip().lower()
    if habilitacao == 'y':
        habilitacao = True
        bebeu = input('Você bebeu? digite algo para sim, enter para não ').strip()
        if bebeu:
            embriagado = True
        else:
            embriagado = False
    else:
        habilitacao = False
else:
    embriagado = False


# Criar uma validação para que se a pessoa tiver carteira de
# motorista, ela possa dirigir. Porém
# Criar condicional para que se a pessoa estiver embriagada,
# mostrar uma mensagem que ela não pode dirigir

#elif idade < 0:
#    print('Você é invalida')

if 'embriagado' in globals())
    if habilitacao and not embriagado:
    print('Você pode dirigir')
else:
    print('Você não pode dirigir')
