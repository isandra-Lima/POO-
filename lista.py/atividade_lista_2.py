#6-questão
numero=[25,10,15,30,5]
print(f'O Comprimento da lista: {len(numero)}')

#7-questão
print(f'A Soma dos elementos da lista: {sum(numero)}')

#8-questão
print(f'A Lista ordenada: {sorted(numero)}')

#9-questão
print(f'Lista invertida: {list(reversed(numero))}')

#10-questão
frutas1=['banana','maçã','laranja']
frutas2=['uva','abacaxi','melancia']
frutas=frutas1+frutas2
print(f'A nova lista de frutas: {frutas}')

#11-questão 
numeros=[1,2,3,4,5,6,7,8,9,10]
novo_numero= int(input('Digite um número para adicionar na lista: '))
if novo_numero in numeros:
    print('Número já existe na lista.')
else:
    numeros.append(novo_numero)
    print(f'Número adicionado. Nova lista: {numeros}')
