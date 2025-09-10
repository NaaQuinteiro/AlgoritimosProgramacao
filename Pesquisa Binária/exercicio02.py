#1 - Qual o nome associado ao número 256 e quantas tentativas foram feitas? Quantas tentativas seriam em uma pesquisa sequencial?Qual o nome associado ao número 256 e quantas tentativas foram feitas? Quantas tentativas seriam em uma pesquisa sequencial?

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    contador = 0

    while low <= high: 
        contador += 1
        middle = (low + high) // 2
        take_guess = list[middle][0]

        if take_guess == item: 
            return middle, list[middle][1], contador
        
        elif take_guess > item:
            high = middle - 1

        else: 
            low = middle + 1
    return None


lista = [
    (3, 'Ana'), (10, 'Bruno'), (15, 'Carlos'), (18, 'Daniela'), (19, 'Eduardo'),
    (28, 'Fernanda'), (33, 'Gustavo'), (35, 'Helena'), (43, 'Igor'), (48, 'Juliana'),
    (58, 'Kleber'), (83, 'Larissa'), (84, 'Marcos'), (86, 'Natália'), (97, 'Otávio'),
    (104, 'Patrícia'), (106, 'Rafael'), (115, 'Sabrina'), (120, 'Tiago'), (122, 'Vanessa'),
    (127, 'Amanda'), (143, 'Breno'), (147, 'Camila'), (149, 'Diego'), (151, 'Eliane'),
    (175, 'Fabiano'), (179, 'Gabriela'), (184, 'Henrique'), (187, 'Isabela'), (194, 'João'),
    (199, 'Karen'), (201, 'Leonardo'), (211, 'Mirela'), (213, 'Nicolas'), (232, 'Olívia'),
    (241, 'Pedro'), (244, 'Queila'), (246, 'Rodrigo'), (256, 'Simone'), (258, 'Túlio'),
    (259, 'Ursula'), (261, 'Victor'), (269, 'Wesley'), (273, 'Xênia'), (278, 'Yasmin'),
    (280, 'Zeca'), (288, 'Alana'), (291, 'Caio'), (292, 'Diana'), (294, 'Fábio')
]

print("-----------------PESQUISA BINÁRIA-------------------\n", binary_search(lista, 256))
print("")

print("----------------PESQUISA SEQUENCIAL-----------------")
cont = 0

for i in lista:
    cont += 1;
    if i[0] == 256: 
        print(f"Número: {i[0]}\nNome: {i[1]}\nTentativas: {cont}")

    else:
        continue
