def remover_duplicatas(lista):
    return list(set(lista))

numeros = list(map(int, input("Digite números separados por espaço: ").split()))
print("Lista sem duplicatas:", remover_duplicatas(numeros))
