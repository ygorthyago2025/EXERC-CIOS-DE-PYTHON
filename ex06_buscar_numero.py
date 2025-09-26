def buscar_numero(numero, lista):
    return numero in lista

# Lista fixa
numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42,
           999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2]

alvo = int(input("Digite o número para buscar: "))
print("Encontrado?", buscar_numero(alvo, numeros))
