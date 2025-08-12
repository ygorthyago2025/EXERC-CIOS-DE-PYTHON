def menor_numero(lista):
    return min(lista)

numeros = list(map(int, input("Digite números separados por espaço: ").split()))
print("Menor número:", menor_numero(numeros))
