lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']

lista_produtos[1] = 'rímel'  # Substituindo 'batons' por 'rímel'
lista_produtos[4] = 'cremes hidratantes'  # Substituindo 'loções' por 'cremes hidratantes'
lista_produtos.remove('delineadores')  # Removendo 'delineadores'

lista_produtos.append('protetor solar')
lista_produtos.append('máscaras capilares')

print("Lista de produtos atualizada:")
for produto in lista_produtos:
    print(produto)
