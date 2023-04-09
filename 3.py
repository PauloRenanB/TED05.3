''' Armazene os nomes de alguns de seus amigos em uma lista chamada amigos. Exiba o nome de cada
pessoa acessando cada elemento da lista um de cada vez.
'''

amigos = []

qnt_amigos = int(input('Quantos amigos você tem? '))

c = 1
while c <= qnt_amigos:
    amigos.append(input('Qual nome dos seus amigos? '))
    c += 1
print(f'Sao seus amigos: {amigos}')