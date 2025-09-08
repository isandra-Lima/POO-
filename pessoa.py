class Pessoa:
    def __init__(self,nome,cpf,email,telefone):
        self.nome= nome
        self.cpf=cpf
        self.email=email
        self.telefone=telefone

    def exibir_dados_pessoais(self):
        print('====Dados Pessoais====')
        print(f'Nome: {self.nome}')
        print(f'Cpf : {self.cpf}')
        print(f'email: {self.email}')
        print(f'telefone: {self.telefone}')
        
