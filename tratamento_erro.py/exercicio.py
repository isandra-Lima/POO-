while True:
    nome = input("Digite seu nome: ")

    if not nome:
        print("Nome inválido: não pode estar vazio.")
        continue

    if any(c.isdigit() for c in nome):
        print("Nome inválido: não pode conter números.")
        continue

    break

while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 0:
            print("Idade não pode ser negativa.")
        else:
            break
    except ValueError:
        print("Erro: Digite um número inteiro para a idade.")

print(f"\nNome: {nome} - Idade: {idade}")

