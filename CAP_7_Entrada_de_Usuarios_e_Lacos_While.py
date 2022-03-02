lista_sanduiche_pedidos = [
	'pastrami', 'veggie', 'grilled cheese',
	'pastrami', 'turkey', 'roast beef', 'pastrami'
	]

lista_sanduiches_prontos = []

print(f"ESTAMOS SEM SANDUÍCHE DE {'pastrami'.upper()}")

for sanduiche in lista_sanduiche_pedidos:
	if sanduiche == "pastrami":
		lista_sanduiche_pedidos.remove("pastrami")

while lista_sanduiche_pedidos:
	sanduiche = lista_sanduiche_pedidos.pop()
	print(f"Preparei seu sanduíche : \033[1;34m{sanduiche}\033[m")
	lista_sanduiches_prontos.append(sanduiche)

print(f"\nLISTA DE SANDUÍCHES PREPARADOS :\n{lista_sanduiches_prontos}")



lista_sanduiche_pedidos = ["x-burguer trio","egg-burguer","picanha-burguer","big bob","big mac cheddar"]
lista_sanduiches_prontos = []

#for sanduiche in lista_sanduiche_pedidos:
#	print(f"Preparei seu sanduíche : \033[1;34m{sanduiche}\033[m")
#	preparado = sanduiche
#	lista_sanduiches_prontos.append(preparado)

while lista_sanduiche_pedidos:
	sanduiche = lista_sanduiche_pedidos.pop()
	print(f"Preparei seu sanduíche : \033[1;34m{sanduiche}\033[m")
	lista_sanduiches_prontos.append(sanduiche)

print(f"\nLISTA DE SANDUÍCHES PREPARADOS :\n{lista_sanduiches_prontos}")



lista = ["A","B","C","D","E","F","G"]
dic = {}

for x in range(1, len(lista)+1):
	dic[lista[x-1]] = x

print(dic.keys())
print(dic.values())

print()
print(dic)
print()

dic["A"] = "fabio"
dic["A"]

for chave, valor in dic.items():
	print(f"CHAVE : {chave}       VALOR : {valor}")



lista_de_resposta = {}

check_001 = True

while check_001 == True:
	nome = input(f"Qual o seu nome ? ")
	resposta = input(f"Qual sua cor favorita {nome.title()} ? ")

	lista_de_resposta[nome] = resposta

	continua_001 = input("Deseja continuar o cadastro ? [sim / nao]")
	if continua_001 == "nao":
		check_001 = False
	else:
		check_001 = True

print(f"\nRESULTADOS :")

for chave, valor in lista_de_resposta.items():
	print(f"A cor favorita de {chave.title()} é {valor.upper()}.")

print(lista_de_resposta)



usuarios_sem_cadastro = ["priscila","alice","briam","candace","fabio","jhony"]
usuarios_confirmados = []

print(f"LISTA ORIGINAL : {usuarios_sem_cadastro}\n")

while len(usuarios_sem_cadastro) > 0:
	user = usuarios_sem_cadastro[-1]
	usuarios_sem_cadastro.pop()
	print(f"Lista de usuários após a retirada do último usuário {user} : {usuarios_sem_cadastro}")
	print(f"Verificando usuário : {user.title()}.")
	usuarios_confirmados.append(user)

print(f"\nUsuários confirmados :")
for nome in usuarios_confirmados:
	print(nome.title())



usuarios_sem_cadastro = ["alice","briam","candace"]
usuarios_confirmados = []


while usuarios_sem_cadastro:
	usuario_atual = usuarios_sem_cadastro.pop()
	print(f"Verificando usuário : {usuario_atual.title()}.")
	usuarios_confirmados.append(usuario_atual)

print(f"\nUsuários confirmados :")
for nome in usuarios_confirmados:
	print(nome.title())



check_001 = True
while check_001 == True:
	print("Digite a idade do consumidor")
	print("'quit' para sair do programa")
	idade = input("\n: ")

	if idade == "quit":
		check_001 = False

	else:

		idade = int(idade)
		if idade < 3:
			print("Entrada gratuita\n")
			check_001 = True

		elif idade < 13:
			print("Entrada custa : R$10,00.\n")
			check_001 = True

		else:
			print("Entrada custa : R$15,00.\n")
			check_001 = True



mensagem = "Digite a idade do consumidor"
mensagem += "\n'quit' para sair do programa"
mensagem += "\n: "

check_001 = True
while check_001 == True:
	idade = input(mensagem)

	if idade == "quit":
		break

	idade = int(idade)
	if idade < 3:
		print("Entrada gratuita\n")
	elif idade < 13:
		print("Entrada custa : R$10,00.\n")
	else:
		print("Entrada custa : R$15,00.\n")



mensagem = "Digite o ingrediente desejado : "
mensagem += "\n'quit ' para encerrar o programa."
mensagem += "\n: "

check_001 = True
while check_001 == True:
	ingrediente = input(mensagem)
	if ingrediente == "quit":
		break
	else:
		print(f"o ingrediente {ingrediente} será adicionado à sua pizza !\n")



numero = 0
while numero < 10 :
	numero += 1
	if numero % 2 == 0:
		#print("par")
		continue

	print(numero)



prompt = "Digite o nome de uma cidade que você já visitou :"
prompt += "\nDigite 'quit' para sair do programa a qualquer momento."

check_001 = True
while check_001 == True:
	city = input(prompt)
	if city == "quit":
		break
	else:
		print(f"Eu adoraria visitar {city}. ")
		check_001 = True



prompt = "Diga algo e eu irei repetir."
prompt += "\nDigite 'quit' para sair do programa"
prompt += "\n: "

check_001 = True

while check_001 == True:
	mensagem = input(prompt)
	if mensagem == "quit":
		check_001 = False
	else:
		print(mensagem)
		print()
		
		

prompt = "Diga algo e eu irei repetir."
prompt += "\nDigite 'quit' para sair do programa"
prompt += "\n: "

mensagem = ""
while mensagem != "quit":
	mensagem = input(prompt)
	if mensagem != "quit":
		print(f"\n{mensagem}\n")



numero = 1

while numero <= 5:
	print(numero)
	numero += 1
	
print()
print(numero)



qtd_pessoas = int(input("Quantos lugares senhor ? "))
if qtd_pessoas > 8:
	print(f"Como são {qtd_pessoas} pessoas senhor, terá que esperar um pouco.")
else:
	print("Sua mesa está pronta senhor !")


tipo_carro = str(input("Qual carro você deseja alugar ? "))
print(f"Deixe me ver se consigo um {tipo_carro} para você.")



numero = int(input("Digite um número : "))

if numero % 2 == 0:
	print(f"O número {numero} é par")
else:
	print(f"O número {numero} é impar")



idade = input("Qual sua idade : ")
idade = int(idade)
if idade < 100:
	print("novo")
else:
	print("velho")



prompt = "Se você nos disser seu nome, poderemos conversar melhor."
prompt += "\nQual seu nome : "
#print(f"frase :\n{prompt}")
name = input(prompt)
print(f"Olá {name} !")



mensagem = input("diga algo e eu irei repetir : ")
print(mensagem)

name = input("Digite seu nome : ")
print(f"Olá {name} !")
