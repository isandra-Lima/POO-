from pessoa import Pessoa
from contabancaria import Contabancaria

cliente=Pessoa(
    nome= 'Maria luiza',
    cpf= '123.456.789-28',
    email= 'Marialuiza@gmail.com',
    telefone= '81 995478654'
)


conta=Contabancaria(
    agencia= '0456',
    tipo_conta='Corrente',
    numero_conta= '54879-0',
    saldo= 3680.80,
    titular=cliente
)

cliente.exibir_dados_pessoais()
conta.exibir_saldo()
conta.exibir_dados_conta()
