#1 - Quantos números primos são menores que 67

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high: 
        middle = (low + high) // 2
        take_guess = list[middle]

        if take_guess == item: 
            return middle
        
        elif middle > item:
            high = middle - 1

        else: 
            low = middle + 1
    return None


prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

result = binary_search(prime_numbers, 67)

print(f"{result} números primos são menores que 67")