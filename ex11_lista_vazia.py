def lista_vazia(lista):
    return len(lista) == 0

itens = input("Digite elementos separados por espaço (ou pressione Enter para lista vazia): ").split()
print("A lista está vazia?", lista_vazia(itens))
