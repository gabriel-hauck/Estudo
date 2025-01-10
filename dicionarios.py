from collections import defaultdict
from collections import OrderedDict
from collections import Counter
import json

# Introdução aos Dicionários em Python

# Criando um dicionário
meu_dicionario = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}

# Acessando valores
print(meu_dicionario["nome"])  # Saída: João
print(meu_dicionario.get("idade"))  # Saída: 25

# Adicionando novos pares chave-valor
meu_dicionario["profissão"] = "Engenheiro"
print(meu_dicionario)

# Atualizando valores
meu_dicionario["idade"] = 26
print(meu_dicionario)

# Removendo pares chave-valor
del meu_dicionario["cidade"]
print(meu_dicionario)

# Iterando sobre um dicionário
for chave, valor in meu_dicionario.items():
    print(f"{chave}: {valor}")

# Métodos úteis de dicionários
print(meu_dicionario.keys())  # Retorna todas as chaves
print(meu_dicionario.values())  # Retorna todos os valores
print(meu_dicionario.items())  # Retorna todos os pares chave-valor

# Verificando a existência de uma chave
if "nome" in meu_dicionario:
    print("A chave 'nome' existe no dicionário")

# Limpando o dicionário
meu_dicionario.clear()
print(meu_dicionario)  # Saída: {}

# Módulos úteis para trabalhar com dicionários

# collections: defaultdict

dicionario_default = defaultdict(int)
dicionario_default["chave1"] += 1
print(dicionario_default)  # Saída: defaultdict(<class 'int'>, {'chave1': 1})

# collections: OrderedDict

dicionario_ordenado = OrderedDict()
dicionario_ordenado["chave1"] = "valor1"
dicionario_ordenado["chave2"] = "valor2"
print(dicionario_ordenado)  # Saída: OrderedDict([('chave1', 'valor1'), ('chave2', 'valor2')])

# collections: Counter

lista = [1, 2, 2, 3, 3, 3]
contador = Counter(lista)
print(contador)  # Saída: Counter({3: 3, 2: 2, 1: 1})

# json: Trabalhando com dicionários e JSON

dicionario_json = {
    "nome": "Maria",
    "idade": 30,
    "cidade": "Rio de Janeiro"
}

# Convertendo dicionário para JSON
dicionario_json_str = json.dumps(dicionario_json)
print(dicionario_json_str)

# Convertendo JSON para dicionário
dicionario_convertido = json.loads(dicionario_json_str)
print(dicionario_convertido)