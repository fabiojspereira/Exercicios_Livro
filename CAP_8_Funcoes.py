"""
def make_album(cantor, album, trilhas = ""):
	dicionario_musical = {"nome_cantor": cantor, "nome_album": album}

	if len(trilhas) > 0 :
		dicionario_musical["qtd_trilhas"] = trilhas

	return (dicionario_musical)


exibir_album = make_album("michael jackson", "bad")
print(exibir_album)
exibir_album = make_album("queen", "a kind of magic", "9")
print(exibir_album)



def make_album(cantor, album, trilhas = 0):
	if trilhas > 0 :
		dicionario_musical = {"nome_cantor" : cantor, "nome_album" : album, "qtd_trilhas" : trilhas}
	else :
		dicionario_musical = {"nome_cantor" : cantor, "nome_album" : album}

	return (dicionario_musical)


exibir_album = make_album("michael jackson", "bad")
print(exibir_album)

exibir_album = make_album("queen", "a kind of magic", 9)
print(exibir_album)



def city_country(cidade, pais):
	print(cidade.title() + ", " + pais.title())

city_country("joão pessoa", "brasil")
city_country("rio de janeiro", "brasil")



def get_formatted_name(first_name, last_name):
	full_name = first_name + " " + last_name
	return full_name.title()

while True :
	print("\nPor favor diga seu nome : ")
	print("Digite 'quit' para sair a qualquer momento...")
	f_name = input("Primeiro Nome : ")
	if f_name == "quit":
		break

	l_name = input("Último nome : ")
	if l_name == "quit":
		break

	formatted_name = get_formatted_name(f_name, l_name)
	print("\nOlá, " + formatted_name + "!")



def get_formatted_name(first_name, last_name):
	full_name = first_name + " " + last_name
	return full_name.title()

while True :
	print("\nPor favor diga seu nome : ")
	f_name = input("Primeiro Nome : ")
	l_name = input("Último nome : ")

	formatted_name = get_formatted_name(f_name, l_name)
	print("\nOlá, " + formatted_name + "!")


def build_person(first_name, last_name, age=""):
	person = {"first":first_name, "last":last_name}
	if age:
		person["age"] = age
	return person

musician = build_person("jimi", "hendrix", age = 42 )
print(musician)
print()
musician = build_person("jimi", "hendrix")
print(musician)
print()
musician = build_person("jimi", "hendrix", 42)
print(musician)



def build_person(first_name, last_name):
	person = {"first":first_name, "last":last_name}
	return person


dicionario = dict()
lista = list()

for contador in range(1,4):
	print(f"Execução {contador}")
	dicionario = build_person("fabio" + str(contador), "pereira" + str(contador))
	lista.append(dicionario)

print()
print(f"Dicionário {lista}")

count = 1
for contador in lista :
	print(f"ITEM {count} da lista : {contador}")
	count+=1



def build_person(first_name, last_name):
	person = {"first":first_name, "last":last_name}
	return person

musician = build_person("jimi", "hendrix")

print(musician)
print(musician.items())
print(musician.keys())
print(musician.values())
print()
print(musician["first"].title())
print(musician["last"].title())




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
