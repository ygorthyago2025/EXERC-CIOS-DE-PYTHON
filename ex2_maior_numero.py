def maior_numero(lista):
    return max(lista)

numeros = list(map(int, input("Digite números separados por espaço: ").split()))
print("Maior número:", maior_numero(numeros))
