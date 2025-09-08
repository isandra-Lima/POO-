
class Contabancaria():
    def __init__(self,agencia,tipo_conta,numero_conta,saldo,titular):
        self.agencia=agencia
        self.tipo_conta=tipo_conta
        self.numero_conta=numero_conta
        self.saldo=saldo
        self.titular= titular

    def exibir_saldo(self):
        print(f"seu saldo atual: R${self.saldo:.2f}")

    def exibir_dados_conta(self):
        print( '=====Dados da conta====')
        print(f'Agência: {self.agencia}')
        print(f'Tipo de conta : {self.tipo_conta}')
        print(f'Numero de conta: {self.numero_conta}')

