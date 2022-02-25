lista_usuarios = ["fabio","jhony","Priscila","AdMiN","PEREIRA","santos","Antonio","frEd"]
lista_novos_usuarios = ["fred","tadeu","PEREIRA","chico","rodrigo","priscila","Antonio","ana","aDmin","FABIO"]

print(f"lista de usuários cadastrados :\n{lista_usuarios}")

# ESTE TRECHO DO CÓDIGO FORMATA TODO O CONTEÚDO DA LISTA DE USUÁRIOS PARA lower
contador = 0
for usuario in lista_usuarios:
	lista_usuarios[contador] = usuario.lower()
	contador = contador + 1

print(f"\nlista de usuários cadastrados formatada : \n{lista_usuarios}\n")

# FORMA DE VERIFICAÇÃO : palavra - PALAVRA - Palavra
for usuario in lista_novos_usuarios:
	if (usuario.lower() in lista_usuarios) or (usuario.upper() in lista_usuarios) or (usuario.title() in lista_usuarios):
		print(f"O nome de usuário \033[1;31m{usuario}\033[m já está em uso !!! Forneça um nome diferente !!!")
	else:
		print(f"O nome de usuário {usuario} está disponível.")


"""
lista_numeros = [1,2,3,4,5,6,7,8,9,]

for n in lista_numeros:
	if n == 1:
		#print(f"{n} termina em ST")
		print(f"{n}st")

	elif n == 2:
		#print(f"{n} termina em ND")
		print(f"{n}nd")

	elif n == 3:
		#print(f"{n} termina em RD")
		print(f"{n}rd")

	else:
		#print(f"{n} termina em TH")
		print(f"{n}th")



lista_usuarios = ["fabio","jhony","Priscila","AdMiN","PEREIRA","santos","Antonio"]
print(f"lista de usuários cadastrados :\n{lista_usuarios}")

contador = 0
for usuario in lista_usuarios:
	lista_usuarios[contador] = usuario.lower()
	contador = contador + 1

print(f"\nlista de usuários cadastrados formatada : \n{lista_usuarios}")


lista_novos_usuarios = ["fred","tadeu","PEREIRA","chico","rodrigo","Antonio","ana","aDmin","FABIO"]
print()
for usuario in lista_novos_usuarios:
	if (usuario.lower() in lista_usuarios) or (usuario.upper() in lista_usuarios) or (usuario.title() in lista_usuarios):
		print(f"O nome de usuário {usuario} já está em uso !!! Forneça um nome diferente !!!")
	else:
		print(f"O nome de usuário {usuario} está disponível.")



lista_usuarios = ["fabio","jhony","priscila","admin","pereira","santos"]
#lista_usuarios = []


if lista_usuarios:
	for usuario in lista_usuarios:
		if usuario == "admin":
			print(f"\nSeja bem vindo administrador !\n{usuario.title()} deseja ver o relatório de status ?\n")
		else:
			print(f"Seja bem vindo {usuario.title()} ao sistema python 1.0 ! ")
else:
	print("Não existem usuários no sistema !")



lista_de_ingredientes_pizzaria = ["tomate","nutela","bacon","oregano","mussarela","camarão","azeitona",
								  "milho","calabresa","ervilha","frango","catupiry","atum"]

lista_de_ingredientes_cliente = ["calabresa","mussarela","batata frita","milho","brigadeiro"]

for ingrediente in lista_de_ingredientes_cliente:
	if ingrediente in lista_de_ingredientes_pizzaria:
		print(f"Ingrediente {ingrediente} adicionado com sucesso.")
	else:
		print(f"{ingrediente}. Ingrediente indisponível em nossa pizzaria.")



lista = list()

#lista.append("A")

if lista :
	print("Tem item")
else:
	print("Não tem nenhum item !")



lista_de_ingredientes_solicitados = ["tomate","nutela","bacon","oregano","mussarela","camarao","azeitona","milho","calabresa"]
for ingredientes in lista_de_ingredientes_solicitados:
	print(f"{ingredientes} foi adicionado a sua pizza !")

frutas_favoritas = ["maçã","banana","uva","laranja"]

if "laranja" in frutas_favoritas:
	print("Laranja está na lista de favoritas !")

if "maçã" in frutas_favoritas:
	print("Maçã está na lista de favoritas !")

if "tangerina" in frutas_favoritas:
	print("Tangerina está na lista de favoritas !")



alien_color = "red"

if alien_color == "green":
	print("Você acertou um alienigena da cor verde ! 5 pontos. ")

elif alien_color == "yellow":
	print("Você acertou um alienigena da cor amarelo ! 10 pontos. ")

else:
	print("Você acertou um alienigena da cor vermelha ! 15 pontos. ")



idade = int(input("BEM VINDO AO PARQUE PYTHON. DIGITE SUA IDADE : "))

if idade < 4:
	entrada = 0
	#print("Sua entrada custa : R$0,00")
elif idade >= 4 and idade <= 18:
	entrada = 5
	#print("Sua entrada custa : R$5,00")

elif idade < 65:
	entrada = 10

elif idade >= 65:
	entrada = 5

#else:
	#entrada = 5
	#print("Sua entrada custa : R$10,00")

print(f"Sua entrada no parque custara {entrada} reais")



usuarios_banidos = ["vitor","mauro","freitas"]
usuario = "fabio"

if usuario not in usuarios_banidos:
	print(f"{usuario.title()},você pode fazer postagens normalmente !")



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
"""
