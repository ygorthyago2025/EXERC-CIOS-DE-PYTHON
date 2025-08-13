def numeros_pares(lista):
    return [n for n in lista if n % 2 == 0]

numeros = list(map(int, input("Digite números separados por espaço: ").split()))
print("Números pares:", numeros_pares(numeros))
