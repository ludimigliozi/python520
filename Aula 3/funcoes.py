# #!/usr/bin/python3
# #### Funçoes
# ## blocos de código pré-definidos para execução

# def mostrar_hello_word():
#      print('hello wolrd')

# # mostrar_hello_word()

# def menu(): 
#     print('Escolha a opção')
#     print('1 - Registar produto')
#     print('2 - Consultar saldo do caixa')
#     print('3 - Abrir caixa registradoras')
#     print('4 - Fechamento do mês')
#     return input('Digite a opção desejada: ')

# def registrar_produto():
#         print('produto registrado')

# def consultar_saldo():
#         print('saldo é R$ X')

# def abrir_caixa():
#         print('abrindo')

# def fechamento():
#         print('fechando')

# # Estrutura principal

# while True:
#     print('Caixa Registradora')
#     opcao = menu()
#     if opcao == '1':
#         registrar_produto()
#     elif opcao == '2':
#         consultar_saldo()
#     elif opcao == '3':
#         abrir_caixa()
#     elif opcao == '4': 
#         fechamento()
#     else:
#         break 
#     input()

# Funções anonimas
var = lambda x : x*2
print(var(2))

numeros = list(range(1,100))

# def dobro(x):
#     return x * 2

print(list(map(lambda x : x * 2,numeros)))

