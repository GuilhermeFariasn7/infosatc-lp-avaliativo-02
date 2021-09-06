#7- Faça 4 listas: Filmes,jogos,livros e esporte ->>

FILMES = ["O poderoso chefão","Parasitas","Fast and Furious", "O menino do pijama listrado","Tá dando onda"]
#A - adicionar itens a lista:
FILMES.append("frozen")
FILMES.append("Diario de um banana")
print(FILMES)

JOGOS = ["Cs go","LOL","Valorant","GTA V","The last of us"]
#A - adicionar itens a lista:
JOGOS.append("need for speed underground 2")
JOGOS.append("Farcry 5")
print(JOGOS)

LIVROS = ["menina traduzida","Diario de um banana","a culpa é das estrelas","O homem de giz","Gelato"]
#A - adicionar itens a lista:
LIVROS.insert(1,"Frozen")
LIVROS.insert(2,"Galinha pintadinha volume 2")
print(LIVROS)

ESPORTES = ["volei","futebol","basquete","handeibol","surf"]
#A - adicionar itens a lista:
ESPORTES.append("Skate")
ESPORTES.append("Atletismo")
print(ESPORTES)

#B - Juntar todas as lista em uma lista só:
listaGeral = [FILMES,JOGOS,LIVROS,ESPORTES]
print("lista com as lista dentro da lista: ",listaGeral)

#C - Acesse (mostrar) algum item da lista livros:
print("Mostrando da lista livros o livro(menina traduzida)",LIVROS[3])
#D - . Remova um item da lista esporte.

del ESPORTES[3]
print(ESPORTES)

#E - Adicione uma lista chamada “disciplinas”, no item b. (sem criar uma lista separada).
DISCIPLINAS = ["Física","Química"]
listaGeral =  listaGeral + DISCIPLINAS
print(listaGeral)


