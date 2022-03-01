"""
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
"""
