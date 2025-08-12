def buscar_numero(numero, lista):
    return numero in lista

numeros = list(map(int, input("Digite números separados por espaço: ").split()))
alvo = int(input("Digite o número para buscar: "))
print("Encontrado?", buscar_numero(alvo, numeros))
