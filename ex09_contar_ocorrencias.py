def contar_ocorrencias(lista, valor):
    return lista.count(valor)

numeros = list(map(int, input("Digite números separados por espaço: ").split()))
alvo = int(input("Digite o número para contar: "))
print(f"O número {alvo} aparece {contar_ocorrencias(numeros, alvo)} vezes.")
