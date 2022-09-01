# # # # # Variáveis
# # # # from socket import SOMAXCONN


# # # # a = 10 # Int
# # # # b = 'String' #Str
# # # # c = 10.22 # float
# # # # d = True # Boolean
# # # # variavel_com_nome_grande = 'variável'

# # # # # Operadores Aritméticos
# # # # 3 + 2 #Soma
# # # # 4 - 3 #Subtração
# # # # 10/2 # Divisão
# # # # 10*3 # Multiplicação
# # # # 10%3 # Resto da divisão
# # # # 3 ** 2 # Potenciação

# # # # # Comparação
# # # # b = 5-3
# # # # b =2
# # # # b == 2 # Igual
# # # # b != 3 # Diferente
# # # # b > 3 # Maior
# # # # b < 1 # Menor
# # # # b >= 3 # Maior ou igual
# # # # b <= 1 # Menor ou igual

# # # # # Operadores lógicos and or not
# # # # # A e B

# # # # # Função ou metodo 
# # # # def meu_metodo():
# # # #     print ('Ola')
# # # #     print("Mundo")

# # # # meu_metodo()

# # # # def soma_dois_valores(x,y):
# # # #     soma = x + y
# # # #     return soma

# # # # soma_dois_valores(5,3)

# # # # Lista
# # # notas = [3,5,6,4,8]
# # # print(notas)

# # # #Adicionar um novo valor a lista
# # # notas.append(10)
# # # notas.append(8)
# # # notas.append(10)
# # # notas.append(10)
# # # notas.append(5)
# # # print(notas)

# # # #Verificar o comprimento da lista
# # # len(notas)
# # # print(len(notas))

# # # #Somar elementos de uma lista entre si
# # # sum(notas)
# # # print(sum(notas))

# # # #Acessar índices específicos de uma lista
# # # notas[0]
# # # print (notas[0])

# # # #Acessar o ultimo índice de uma lista
# # # notas[-1]
# # # print (notas[-1])

# # #TUPLAS ou TUPLES - Os elementos são como listas com a diferença que os elementos são colocados entre parenteses e a tupla não pode ter seus elementos alterados

# # tupla = (3,4,5)
# # print(tupla)

# # #Novos valores podem ser adicionados a uma tupla
# # tupla+=(4,)

# # A tupla será substituída por uma nova com o valor inserido
# # print(tupla)

# #Sets São como listas com a diferença que seus elementos são armazenados em chaves {},e não podem haver elementos repetidos, os elementos repetidos serão exibidos no console apenas uma vez, a ordem do set não é garantida e não possui índice

# set_nota ={1,2,3,4,5,7,20}
# print(set_nota) 

# set_notas = {1,2,2,3,3,5,6,4}
# print(set_notas)

# #Adicionar um elemento a um set

# set_nota.add(10)
# print(set_nota)

# Condicionais if else
# pessoas_conhecidas = ['John', 'Mary','Stacy','Fabian']
# pessoa = input('Entre com o nome de uma pessoa:')

# # if pessoa in pessoas_conhecidas:
# #     print('Você conhece essa pessoa')
# # else:
# #     print('Você não conhece essa pessoa')
# # 
# if pessoa in pessoas_conhecidas:
#     print('Você conhece '+str(pessoa))
# else:
#     print('Você não conhece '+str(pessoa))

#Loops
# minha_variavel ='Salut'
# for caracter in minha_variavel:
#     print(caracter)

# Criação automática de Listas
# range(0,10)
# lista = list(range(11))
# print(lista)

# #Criação automática Set
# range(0,10)
# set7 = set(range(11))
# print(set7)

# #Criação automática de Listas
# range(0,10)
# lista = list(range(1,12,2))
# print(lista)

# #Loop for
# numeros_pares = list(range(0,11,2))
# print(numeros_pares)
# for numero in numeros_pares:
#     print(numero**2)
    
# Loop while
# x = 0
# while x<=100:
#     print(x,x**3)
#     x += 2 #incrementação

# usuario_quiser = True

# while usuario_quiser:
#     usuario_input = input("Quer continuar? (S/N)")
#     if usuario_input == 'N':
#         usuario_quiser = False
