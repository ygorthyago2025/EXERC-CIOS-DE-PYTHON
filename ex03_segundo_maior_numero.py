def segundo_maior(lista):
    return sorted(set(lista))[-2]

numeros = list(map(int, input("Digite números separados por espaço: ").split()))
print("Segundo maior número:", segundo_maior(numeros))
