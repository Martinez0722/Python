# # Dicionario
# meu_dicionario = {'nome':'Gaël','idade':2}
# print(meu_dicionario['nome'])

# minha_lista_dic = [{'nome':'Gaël','idade':2},{'nome':'Raphaël','idade':26},{'nome':'Pavël','idade':29}]
# print(minha_lista_dic[2])

# print(minha_lista_dic[0]['idade'])

# loteria = {'nome':'Sakha', 'numeros':(13,5,16,9,12)}
# print(sum(loteria['numeros']))
# loteria ['nome'] = 'Sissoko'
# print(loteria)

# List Comprehension
# x = [x**2 for x range(5)]
# print(x)

# Classe e Objetos
# Classe é um modelo ou representação de um objeto
# Objeto é uma instância de uma classe
#   class JogadorLoteria:
#     def __init__(self):
#         self.nome = 'Joan'
#          self.numeros  = (1,2,3,4,5)
#         def total (self):
#            return sum(self.numeros)


# jogador_1 = JogadorLoteria()

# jogador_2 = JogadorLoteria()

# jogador_1.total()

#Herança
#     def __init__(self, nome, salario):
#           self.nome = nome
#           self.salario = salario
#       def dados (self):
#           return {'nome': self.nome, 'salario':self.salario}
  

# fabio = Funcionario ('Fabio',7000)

# fabio.dados()


#     class Adm(Funcionario):
#        def __init__(self, nome, salario):
#            super().__init__(nome,salario)
#        def atualizar_dados(self, nome):
#            self.nome = nome
#            return self.dados()
    

#  fernando = Admin('Fernando', 14000)

# fabio.dados()

#  fernando.dados()


#  fernando.atualizar_dados('Fernandinho')

