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
