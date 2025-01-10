# conjuntosdedados.py

# Conjuntos em Python são coleções não ordenadas de elementos únicos.
# Eles são úteis para armazenar elementos distintos e realizar operações de conjunto como união, interseção e diferença.

# Criando conjuntos
conjunto_vazio = set()
conjunto_com_elementos = {1, 2, 3, 4, 5}

# Adicionando elementos
conjunto_com_elementos.add(6)

# Removendo elementos
conjunto_com_elementos.remove(3)  # Lança um erro se o elemento não existir
conjunto_com_elementos.discard(4)  # Não lança erro se o elemento não existir

# Verificando a existência de um elemento
existe = 2 in conjunto_com_elementos  # Retorna True
nao_existe = 10 in conjunto_com_elementos  # Retorna False

# Operações de conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

# União
uniao = conjunto_a | conjunto_b  # {1, 2, 3, 4, 5}

# Interseção
intersecao = conjunto_a & conjunto_b  # {3}

# Diferença
diferenca = conjunto_a - conjunto_b  # {1, 2}

# Diferença simétrica
diferenca_simetrica = conjunto_a ^ conjunto_b  # {1, 2, 4, 5}

# Subconjunto e Superconjunto
conjunto_c = {1, 2}
eh_subconjunto = conjunto_c <= conjunto_a  # True
eh_superconjunto = conjunto_a >= conjunto_c  # True

# Conjuntos imutáveis (frozenset)
conjunto_imutavel = frozenset([1, 2, 3])

# Métodos adicionais
tamanho = len(conjunto_com_elementos)  # Tamanho do conjunto
conjunto_com_elementos.clear()  # Remove todos os elementos

# Exemplo prático: Remover duplicatas de uma lista
lista_com_duplicatas = [1, 2, 2, 3, 4, 4, 5]
lista_sem_duplicatas = list(set(lista_com_duplicatas))  # [1, 2, 3, 4, 5]

# Exemplo prático: Encontrar elementos comuns entre duas listas
lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
elementos_comuns = list(set(lista1) & set(lista2))  # [3, 4]

# Exemplo prático: Verificar se todos os elementos de uma lista são únicos
lista = [1, 2, 3, 4, 5]
todos_unicos = len(lista) == len(set(lista))  # True

print("Conjuntos em Python são poderosos e úteis para várias operações!")