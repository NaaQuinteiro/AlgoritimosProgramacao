# frase = "eu estudo no unasp"
# contador = 0

# for i in frase:
#     if i == "e":
#         contador += 1

# print(contador)

# L = [1, 7, 4, 10, 2]
# max = L[0]

# for i in L: 
#     if i > max:
#         max = i

# print(max)

dados = [("joão", 8), ("maria", 7), ("maria", 9), ("joão", 8), ("ricardo", 10), ("joão", 8)]
table = {}

# for nome, valor in dados: 
#     table[nome] = table.get(nome, 0) + valor 
# print(table)

for nome, valor in dados: 
    table[nome] = max(table.get(nome, valor), valor)

print(table)