class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 1000.0  # saldo começa em 0

    def exibir_saldo(self):
        print(f"Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}")


# --- Teste com input ---
nome = input("Digite o nome do titular da conta: ")
conta = ContaBancaria(nome)
conta.exibir_saldo()
