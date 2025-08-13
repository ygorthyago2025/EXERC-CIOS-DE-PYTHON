def media_lista(lista):
    return sum(lista) / len(lista) if lista else 0

numeros = list(map(int, input("Digite números separados por espaço: ").split()))
print("Média:", media_lista(numeros))
