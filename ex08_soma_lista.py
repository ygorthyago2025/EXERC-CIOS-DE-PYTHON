def soma_lista(lista):
    return sum(lista)

numeros = list(map(int, input("Digite números separados por espaço: ").split()))
print("Soma dos números:", soma_lista(numeros))
