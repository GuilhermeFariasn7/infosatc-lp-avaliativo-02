#Escreva um programa para verificar se um elemento x está presente em uma lista.

FRUTAS = []
FRUTAS = ["banana","morango",'laranja','abacate','jecaa']
verificar = input("Digite algo para saber se está na lista: ")
if verificar in FRUTAS:
    print(verificar," está na lista!")
else:
    print(verificar," nao está na lista!")