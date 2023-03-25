# Operação de uma conta bancária
class OperacaoBancaria:
    def __init__(self, titular, data_operacao, valor_operacao, saldo):
        self.titular        = titular
        self.data_operacao  = data_operacao
        self.valor_operacao = valor_operacao
        self.saldo          = saldo

    def operacao_credito(self):
        self.valor_operacao += 20

    def operacao_debito(self):
        self.valor_operacao -=5

movimentacao_valor = OperacaoBancaria(titular="Laura", data_operacao="22/03/2023", valor_operacao=200, saldo=200)
movimentacao_valor.operacao_debito()         
print(f"Titular {movimentacao_valor.titular} - data operacao {movimentacao_valor.data_operacao}  saldo {movimentacao_valor.valor_operacao}")
movimentacao_valor.operacao_credito()
print(f"Titular {movimentacao_valor.titular} - data operacao {movimentacao_valor.data_operacao} saldo {movimentacao_valor.valor_operacao}")

print("#")
print("############################")
print("#")
