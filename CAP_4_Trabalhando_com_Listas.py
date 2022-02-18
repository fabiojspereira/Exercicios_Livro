lista_pecas = ["ssd","hdd","monitor","vga","cpu","fonte","memória ram"]
print("LISTA COMPLETA : ", lista_pecas)
print("\nOs três primeiros itens de hardware são : ", lista_pecas[0:3])
print("Alguns itens do meio da lista de hardware são : ", lista_pecas[3:6])
print("Os três últimos itens de hardware são : ", lista_pecas[-3:])

hardware_copiado = lista_pecas[:]
lista_pecas.append("mouse e teclado")
hardware_copiado.append("gabinete de alumínio")
print("\nItens diferentes foram adicionados às listas separadamente :")
print("Lista original : ",lista_pecas)
print("Lista copiada  : ",hardware_copiado)

#Utilizando laço FOR
print("\nLISTA ORIGINAL")
for contador in lista_pecas:
	print(contador,end=" ")
print("\n\nLISTA COPIADA")
for contador in hardware_copiado[:]:
	print(contador,end=" ")


"""
jogadores = ["romário","edmundo","mauro galvão","bebeto","ronaldo"]
#print(jogadores[-3:])
print("Aqui vem a lista dos 3 primeiros jogadores da lista :")
for contador in jogadores[:3]:
	print(contador.title())

copia_lista = jogadores[:]
#copia_lista = jogadores #Não serve para copiar listas.
jogadores.append("taffarel")

print("\njogadores :\n",jogadores)
print("\nCópia :\n",copia_lista)


# Abrangência de lista // List comprehensions
cubos = [numero**3 for numero in range(1,11)]
print(cubos)


cubos = []
for numero in range(1,11):
	cubos.append(numero**3)
	x = numero**3
	print("Cubo de",numero,"é :",x)


numeros_multiplos_3 = []
for contador in range(3,31,3):
	numeros_multiplos_3.append(contador)
print(numeros_multiplos_3)


numeros_impares = []
for contador in range(1,21,2):
	numeros_impares.append(contador)
print(numeros_impares)


lista = []
for contador in range(1,1000001):
	lista.append(contador)
	print(contador)
print("Menor valor da lista : ",min(lista))
print("Maior valor da lista : ",max(lista))
print("Soma geral da lista  : ",sum(lista))


for contador in range(1,21):
	print(contador,end=" ")


# Abrangência de lista // List comprehensions
resultado = [ contador**2 for contador in range(1,11)]
print(resultado)


digitos = []
for contador in range(0,10):
	digitos.append(contador)
print("Digitos cadastrados :",digitos)
minimo = min(digitos)
maximo = max(digitos)
print("Menor valor : ",minimo)
print("Maior valor : ",maximo)
print("Soma geral  : ",sum(digitos))


quadrado_perfeito = list()
for contador in range (1,11):
	#numero = contador**2
	quadrado_perfeito.append(contador**2)
print(quadrado_perfeito)


for contador in range(1,5):
	print(contador)
print()
for contador in range(1,6):
	print(contador)
print()
lista = list(range(1,11))
print(lista)


lista_pizzas = ["calabresa","pepperoni","chocolate","quatro queijos"]
for pizza in lista_pizzas:
	print(pizza)
	print("Sabor da pizza colocado na lista : "+pizza,"\n")
print("Estes são meus sabores favoritos !")


lista_magicos = ["Mister M","Mister Z","Harry Houdini"]
for magicos in lista_magicos:
	print(magicos.title()+", foi um excelente mágico !")
	print("Estamos prontos para o seu próximo truque, "+ magicos.title()+" !!!\n")

print("Obrigado a todos pela presença !!")
"""
