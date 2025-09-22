class Restaurante:
    def __init__(self, nome, avaliacoes):
        self.nome = nome
        self.avaliacoes = avaliacoes

    def calcular_media(self):
        if not self.avaliacoes:
            return 0  # Evita divisão por zero
        return sum(self.avaliacoes) / len(self.avaliacoes)

    def verificar_avaliacao(self):
        media = self.calcular_media()
        return "Bem avaliado" if media >= 7.0 else "Mal avaliado"


# Lista de restaurantes com notas
restaurantes = [
    Restaurante("Pizza da Vila", [8, 9, 7, 6, 10]),
    Restaurante("Sushi Top", [6, 5, 4, 7]),
    Restaurante("Churrascaria Gaúcha", [9, 8, 10, 10])
]

# Contadores para o desafio extra
bem_avaliados = 0
mal_avaliados = 0
restaurante_com_maior_media = restaurantes[0]
maior_media = restaurantes[0].calcular_media()

# Exibe as informações dos restaurantes
for r in restaurantes:
    media = r.calcular_media()
    situacao = r.verificar_avaliacao()

    print(f"Restaurante: {r.nome}")
    print(f"Média das avaliações: {media:.2f}")
    print(f"Situação: {situacao}\n")

    # Contagem de bem/mal avaliados
    if situacao == "Bem avaliado":
        bem_avaliados += 1
    else:
        mal_avaliados += 1

    # Verifica se é o restaurante com maior média
    if media > maior_media:
        maior_media = media
        restaurante_com_maior_media = r

# Resultado final do desafio extra
print("Resumo Final:")
print(f"Restaurantes bem avaliados: {bem_avaliados}")
print(f"Restaurantes mal avaliados: {mal_avaliados}")
print(f"Restaurante com a maior média: {restaurante_com_maior_media.nome} ({maior_media:.2f})")
