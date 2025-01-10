import collections

# Tuplas em Python

# Uma tupla é uma coleção ordenada e imutável de itens. Em Python, tuplas são definidas usando parênteses ().

# Criando uma tupla
tupla1 = (1, 2, 3, 4, 5)
tupla2 = ("a", "b", "c")
tupla3 = (1, "a", True, 3.14)

# Acessando elementos de uma tupla
print(tupla1[0])  # Saída: 1
print(tupla2[1])  # Saída: b

# Tuplas são imutáveis, o que significa que não podemos alterar seus elementos após a criação
# tupla1[0] = 10  # Isso causará um erro

# Podemos concatenar tuplas
tupla4 = tupla1 + tupla2
print(tupla4)  # Saída: (1, 2, 3, 4, 5, 'a', 'b', 'c')

# Podemos repetir tuplas
tupla5 = tupla2 * 3
print(tupla5)  # Saída: ('a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c')

# Podemos verificar a existência de um item na tupla
print(3 in tupla1)  # Saída: True
print("d" in tupla2)  # Saída: False

# Podemos obter o comprimento de uma tupla
print(len(tupla1))  # Saída: 5

# Podemos desempacotar tuplas
a, b, c = tupla2
print(a)  # Saída: a
print(b)  # Saída: b
print(c)  # Saída: c

# Métodos de tuplas
# count() - retorna o número de vezes que um valor aparece na tupla
print(tupla1.count(3))  # Saída: 1

# index() - retorna o índice do primeiro valor correspondente
print(tupla1.index(4))  # Saída: 3

# Tuplas aninhadas
tupla6 = (tupla1, tupla2)
print(tupla6)  # Saída: ((1, 2, 3, 4, 5), ('a', 'b', 'c'))

# Convertendo outras coleções para tuplas
lista = [1, 2, 3]
tupla7 = tuple(lista)
print(tupla7)  # Saída: (1, 2, 3)

# Módulos úteis para trabalhar com tuplas

# namedtuple - permite criar tuplas com campos nomeados
Pessoa = collections.namedtuple('Pessoa', 'nome idade')
pessoa1 = Pessoa(nome="João", idade=30)
print(pessoa1.nome)  # Saída: João
print(pessoa1.idade)  # Saída: 30

# zip - combina várias listas em uma lista de tuplas
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
tuplas_zip = list(zip(lista1, lista2))
print(tuplas_zip)  # Saída: [(1, 'a'), (2, 'b'), (3, 'c')]