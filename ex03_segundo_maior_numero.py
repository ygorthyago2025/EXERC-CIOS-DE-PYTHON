def segundo_maior(lista):
    return sorted(set(lista))[-2]

# Lista fixa
numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42,
           999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2]

print("Segundo maior número:", segundo_maior(numeros))
