#!/usr/bin/python3

####
## Tratando Exceções
####

# try:
#     print('Soma de dois valores')
#     numero1 = int(input('Digite um número a ser dividido: '))
#     numero2 = int(input('Digite outro número a ser dividido: '))
#     print(numero1 / numero2)
# except ValueError:
#     print('Insira somente números')

# except ZeroDivisionError as e:
#     print('Não foi possivel fazer a divisão', e)

# except Exception as e:
#         print('Erro na execução do programa', e)
# finally:
#     print('Saindo do script')

#nulo = None

#####
## Lançando Exceções
#####

#try:
opcao = input('Não digite 5: ')
if opcao == '5':
    raise ValueError('Eu falei para você não digitar 5')
#except ValueError as e:
#    print('Deu erro: ',e)
