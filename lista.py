import random

# Listas são coleções ordenadas de elementos, mutaveis em python, e podem conter elementos de diferentes tipos.
# Elas são definidas por valores separados por vírgula, dentro de colchetes.   

# Criando uma lista
minha_lista = [1, 2, 3, 4, 5]
print("Lista original:", minha_lista)

# Adicionando elementos à lista
minha_lista.append(6)
print("Após adicionar 6:", minha_lista)

# Inserindo elementos em uma posição específica
minha_lista.insert(2, 2.5)
print("Após inserir 2.5 na posição 2:", minha_lista)

# Removendo elementos da lista
minha_lista.remove(2.5)
print("Após remover 2.5:", minha_lista)

# Removendo o último elemento da lista
ultimo_elemento = minha_lista.pop()
print("Após remover o último elemento:", minha_lista)
print("Elemento removido:", ultimo_elemento)

# Acessando elementos da lista
print("Primeiro elemento:", minha_lista[0])
print("Último elemento:", minha_lista[-1])

# Fatiando a lista
print("Elementos do índice 1 ao 3:", minha_lista[1:4])

# Comprimento da lista
print("Comprimento da lista:", len(minha_lista))

# Iterando sobre a lista
print("Iterando sobre a lista:")
for elemento in minha_lista:
    print(elemento)

# Usando list comprehension
quadrados = [x**2 for x in minha_lista]
print("Quadrados dos elementos da lista:", quadrados)

# Usando o módulo random para embaralhar a lista
random.shuffle(minha_lista)
print("Lista embaralhada:", minha_lista)

# Ordenando a lista
minha_lista.sort()
print("Lista ordenada:", minha_lista)

# Revertendo a lista
minha_lista.reverse()
print("Lista revertida:", minha_lista)

# Verificando se um elemento está na lista
print("3 está na lista?", 3 in minha_lista)
print("10 está na lista?", 10 in minha_lista)

# Contando ocorrências de um elemento
minha_lista.append(3)
print("Lista após adicionar 3 novamente:", minha_lista)
print("Número de ocorrências de 3:", minha_lista.count(3))

# Encontrando o índice de um elemento
print("Índice do primeiro 3:", minha_lista.index(3))

# Copiando a lista
copia_lista = minha_lista.copy()
print("Cópia da lista:", copia_lista)

# Limpando a lista
minha_lista.clear()
print("Lista após limpar:", minha_lista)