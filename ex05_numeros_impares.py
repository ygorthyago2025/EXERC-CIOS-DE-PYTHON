def numeros_impares(lista):
    return [n for n in lista if n % 2 != 0]

# Lista fixa
numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42,
           999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2]

print("Números ímpares:", numeros_impares(numeros))

