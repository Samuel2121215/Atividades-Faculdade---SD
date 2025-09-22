# Lista de compras com 5 produtos (cada um é um dicionário)
compras = [
    {"nome": "Arroz", "quantidade": 7, "preco": 30.00},
    {"nome": "Feijão", "quantidade": 10, "preco": 8.00},
    {"nome": "Leite", "quantidade": 2, "preco": 5.00},
    {"nome": "Pão", "quantidade": 10, "preco": 0.50},
    {"nome": "Café", "quantidade": 15, "preco": 12.00}
]

# Inicializa variáveis para o total e os produtos especiais
total_gasto = 0
produto_mais_caro = compras[0]
produto_maior_quantidade = compras[0]

# Mostra os itens e faz os cálculos
for item in compras:
    nome = item["nome"]
    quantidade = item["quantidade"]
    preco = item["preco"]

    print(f"Produto: {nome} | Quantidade: {quantidade} | Preço: R$ {preco:.2f}")

    total_gasto += quantidade * preco

    # Verifica se o produto atual é mais caro que o armazenado
    if preco > produto_mais_caro["preco"]:
        produto_mais_caro = item

    # Verifica se a quantidade atual é maior que a armazenada
    if quantidade > produto_maior_quantidade["quantidade"]:
        produto_maior_quantidade = item

# Exibe o resumo da compra
print("\nResumo da Compra:")
print(f"Total de itens diferentes: {len(compras)}")
print(f"Total gasto: R$ {total_gasto:.2f}")
print(f"Produto mais caro: {produto_mais_caro['nome']} (R$ {produto_mais_caro['preco']:.2f})")
print(f"Produto com maior quantidade: {produto_maior_quantidade['nome']} ({produto_maior_quantidade['quantidade']} unidades)")
