"""
def get_formatted_name ( first_name, last_name, middle_name = ""):
	if middle_name :
		full_name = first_name + " " + middle_name + " " + last_name
	else :
		full_name = first_name + " " + last_name

	return full_name.title()

musician = get_formatted_name("jimi", "handrix")
print(musician)

musician = get_formatted_name("john", "lee", "hooker")
print(musician)



def get_formatted_name ( first_name, middle_name,  last_name):
	full_name = first_name + " " + middle_name + " " + last_name
	return full_name.title()

musician = get_formatted_name("john", "lee", "hooker")

print(musician)



def get_formatted_name ( first_name, last_name):
	full_name = first_name + " " + last_name
	return full_name.title()

musician = get_formatted_name("jimi", "handrix")

print(musician)



def descreva_cidade(nome, pais="brasil"):
	print(f"\nA cidade de {nome.title()} está localizada no país {pais.title()} ")


descreva_cidade("rio de janeiro")
descreva_cidade("sao paulo")
descreva_cidade("joao pessoa")
descreva_cidade("nova iorque", pais="united states")
descreva_cidade("santiago", "chile")



def faca_camisa(tamanho, texto="texto texto texto"):
	print(f"\nTAMANHO DA CAMISA  : {tamanho.upper()}.")
	print(f"MENSAGEM DA CAMISA : {texto.upper()}")


faca_camisa("g")
faca_camisa("m")
faca_camisa(tamanho="p m g", texto="* * * * *")



def faca_camisa(texto, tamanho="G"):
	print(f"\nTAMANHO DA CAMISA  : {tamanho.upper()}.")
	print(f"MENSAGEM DA CAMISA : {texto.title()}")


faca_camisa("eu amo python")
faca_camisa(texto="eu adoro python")
faca_camisa("texto texto texto",tamanho="p")



def faca_camisa(tamanho, texto):
	print(f"\nTAMANHO DA CAMISA  : {tamanho.upper()}.")
	print(f"MENSAGEM DA CAMISA : {texto.title()}")

faca_camisa("G","all men must serve. faceless men most of all")
faca_camisa(tamanho="m",texto="curso intenso de python.")



def descricao_pet(nome_animal, tipo_animal="cachorro"):
	print(f"\nEu tenho um {tipo_animal}.")
	print(f"Meu {tipo_animal} se chama {nome_animal.title()}.")

descricao_pet("jhony")
descricao_pet(nome_animal="fred",tipo_animal="tartaruga")



def descricao_pet(nome_animal, tipo_animal="cachorro"):
	print(f"\nEu tenho um {tipo_animal}.")
	print(f"Meu {tipo_animal} se chama {nome_animal.title()}.")

descricao_pet("jhony")



def descricao_pet(tipo_animal, nome_animal):
	print(f"\nEu tenho um {tipo_animal}.")
	print(f"Meu {tipo_animal} se chama {nome_animal.title()}.")

descricao_pet(tipo_animal="cachorro",nome_animal="jhony")
descricao_pet(nome_animal="cuca",tipo_animal="gato",)



def descricao_pet(tipo_animal, nome_animal):
	print(f"\nEu tenho um {tipo_animal}.")
	print(f"Meu {tipo_animal} se chama {nome_animal.title()}.")

descricao_pet("cachorro","jhony")
descricao_pet("gato","cuca")



def favorite_book(titullo):
	print(f"Um dos meus livros favoritos é : {titullo.title()}.")

favorite_book("curso intensivo de python")



def display_message():
	print(f"Neste capítulo estamos aprendendo sobre funções em Pytthon.")


display_message()


def saudacao(username):
	print(f"Olá {username.title()}. Seja bem vindo ! ")


saudacao("fabio")
"""
