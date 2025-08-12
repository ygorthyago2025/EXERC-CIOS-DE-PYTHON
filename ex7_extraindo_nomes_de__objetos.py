# Definindo uma classe para exemplo
class Objeto:
    def __init__(self, nome):
        self.nome = nome

def extrair_nomes(lista_objetos):
    """Retorna uma lista com os nomes de cada objeto."""
    return [obj.nome for obj in lista_objetos]

# Criando lista de objetos
objetos = [
    Objeto("Cadeira"),
    Objeto("Mesa"),
    Objeto("Computador"),
    Objeto("Caneta")
]

# Testando a função
nomes = extrair_nomes(objetos)
print(nomes)  
