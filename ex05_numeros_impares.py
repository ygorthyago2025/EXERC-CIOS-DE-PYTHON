def numeros_impares(lista):
    return [n for n in lista if n % 2 != 0]

numeros = list(map(int, input("Digite números separados por espaço: ").split()))
print("Números ímpares:", numeros_impares(numeros))
