""" Vá a uma loja online de computadores, faça uma lista de itens para montar um pc
gamer. Não se esqueça de colocar um gabinete cooler master e uma placa de
vídeo GeForce RTX 2080Ti.
A. Depois de ir para o carrinho de compras na loja online, você percebeu que
o gabinete cooler master e a placa GeForce RTX 2080Ti passaram do valor
do seu orçamento para montar seu pc gamer. Então REMOVA os dois itens
da sua lista. """
PCGAMER = ["processador i5 9400f","memória: hyperX 8g 33360hz","Placa mãe: asus h310m","Placa de vídeo: Geforce RTX 2080TI","Gabinete: cooler master"]
print("Peças para meu pc Gamer\n",PCGAMER)

PCGAMER.remove("Placa de vídeo: Geforce RTX 2080TI")
PCGAMER.remove("Gabinete: cooler master")


print("Tive que tirar a placa de video e o gabinete por motivos financeiros... então a nova lista é essa:\n",PCGAMER)


