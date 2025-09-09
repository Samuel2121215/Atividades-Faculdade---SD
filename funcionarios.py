# Classe Funcionario
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def verificar_faixa(self):
        if self.salario >= 3000:
            return "Acima da média"
        else:
            return "Abaixo da média"



# Lista de funcionários (instâncias da classe)
funcionarios = [
    Funcionario("Samuel", 2500),
    Funcionario("Luca", 3200),
    Funcionario("Araujo", 3000)
]

#extra

acima_media = 0
abaixo_media = 0

# Exibição dos dados
print("📋 Lista de Funcionários:\n")
for f in funcionarios:
    situacao = f.verificar_faixa()
    print(f"Nome: {f.nome}")
    print(f"Salário: R$ {f.salario:.2f}")
    print(f"Situação: {situacao}")
    print("-" * 30)

    if situacao == "Acima da média":
        acima_media += 1
    else:
        abaixo_media += 1

# Resultados do desafio extra
print("\n Resumo:")
print(f"Funcionários acima da média: {acima_media}")
print(f"Funcionários abaixo da média: {abaixo_media}")
