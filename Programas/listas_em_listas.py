'''

Aqui vemos o conceito de listas dentro de listas


'''

dados = []
dados.append('pedro')
dados.append('25')
pessoas = list()
pessoas.append(dados[:])   # <---   usando esse método, podemos adicionar uma lista, dentro de outra lista
pessoas = [['pedro', 25], ['maria', 24], ['italo', 18]]  # posso adicionar mais elementos nessa lista, desta maneira
for i in pessoas:
    print(f'{i[0]} tem {i[1]} de idade')

print(pessoas)


amigos = []
dados = []

for c in range(0, 3):
    dados.append(str(input("Nome: ")))
    dados.append(str(input("Idade: ")))
    amigos.append(dados[:])
    dados.clear()
print(amigos)