#1-questão
numero=[10,20,30,40,50]
print(numero)

#2-questão
print('Primeiro elemento:', numero[0])
print('Último elemento:', numero[-1])
print('Elementos do meio:', numero[1:4])

#3-questão
numero[2]=35
print('Lista após a modificação:', numero)

#4-questão
novo_numero=int(input('Digite um novo número para adicionar à lista: '))
numero.append(novo_numero)
print('Lista após adicionar o novo número:', numero)

#5-questão
numero.remove(novo_numero)
print('Lista após remover o novo número:', numero)