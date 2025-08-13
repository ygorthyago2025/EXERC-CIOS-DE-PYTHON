def percorrer_lista(lista):
    for elemento in lista:
        print(elemento)

# Entrada do usuário
numeros = list(map(int, input("Digite números separados por espaço: ").split()))
percorrer_lista(numeros)
