lista_carros = ["audi","bmw","subaru","toyota"]

carro = "subaru"
print(f"O carro escolhido é : '{carro}'")

print("\nO carro é == 'subaru'? Eu acho que é verdade")
print(carro == "subaru" )
print("\nO carro é == 'audi'? Eu acho que é falso")
print(carro == "audi" )
print("\nO carro está escrito em maiusculo ?")
print(carro == carro.upper())
print("\nO carro está escrito em minusculo ?")
print(carro == carro.lower())
print("\nO carro está escrito desta forma : 'Subaru' ?")
print(carro == carro.title())
print("\nO carro está escrito desta forma : 'subaru' ou 'SUBARO' ?")
print((carro == carro.lower()) or carro == carro.upper())
print("\nO carro 'Audi' está na lista de carros ?")
print("audi" in lista_carros)
print("\nO carro 'volvo' não está na lista de carros ?")
print("volvo" not in lista_carros)


lista_de_ingredientes = ["tomate","mussarela","oregano","milho"]
pedido_cliente = ["tomate","nutela","bacon","oregano","mussarela","milho","camarao"]

falha = list()


print(f"LISTA DE INGREDIENTES DISPONÍVEIS NA PIZZARIA : {lista_de_ingredientes}")
print(f"INGREDIENTES SOLICITADOS PELO CLIENTE : {pedido_cliente}")
print()
for ingrediente_cliente in pedido_cliente:
	if ingrediente_cliente in lista_de_ingredientes:
		print(f"ingrediente {ingrediente_cliente} está disponível na pizzaria.")
	else:
		print(f"Ingrediente {ingrediente_cliente} não está disponível no momento.")
		falha.append(ingrediente_cliente)

print(f"\nIngredientes que faltaram na pizza do cliente : {falha}")


idade_0 = 22
idade_1 = 18
resultado = ( idade_0 >= 21 ) or ( idade_1 >= 21)
print(resultado)

idade_0 = 18
resultado = ( idade_0 >= 21 ) or ( idade_1 >= 21)
print(resultado)


idade_0 = 22
idade_1 = 18

resultado = idade_0 >= 21 and idade_1 >= 21
print(resultado)

idade_0 = 22
idade_1 = 22

resultado = idade_0 >= 21 and idade_1 >= 21
print(resultado)


lista_carros = ["audi","bmw","subaru","toyota"]

for carro in lista_carros:
	if carro == "bmw":
		print(carro.upper())
	else:
		print(carro.title())

car = "bmw"
car == "bmw"
print(car == "bmw")
