
"""
def make_great(lista_de_magicos):
	for count in range(0, len(lista_de_magicos)):
		magico = lista_de_magicos[count]
		lista_de_magicos[count] = "o Grande " + magico
		# Podemos retirar a instrução return e colocar um print : print(lista_de_magicos[count])

	return (lista_de_magicos)

def show_magicians(lista_de_magicos):
	for magico in lista_de_magicos:
		print(magico.title())


magicos = ["david blaine", "teller", "houdini"]

show_magicians(magicos)

grandes_magicos = make_great(magicos)
print()
print(grandes_magicos)


# ABAIXO SEGUE A SOLUÇÃO DO AUTOR PARA ESCREVER A PALAVRA "o Grande" antes do nome do mágico :
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    # Build a new list to hold the great musicians.
    great_magicians = []

    # Make each magician great, and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    # Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians.append(great_magician)

magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)



def show_magicians(lista_de_magicos):
	for magico in lista_de_magicos:
		print(magico.title())


magicos = ["david blaine", "teller", "houdini"]

show_magicians(magicos)



def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print("Printing model : " + current_design)
		completed_models.append(current_design)


def show_completed_models(completed_models):
	print("\nThe following models have been printed : ")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ["iphone case", "robot pedant", "dodecahedron"]
completed_models = []

# Usando [:] na chamada da função, passamos uma cópia da lista "unprinted_designs"
# E assim a lista original é poupada.
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

print(f"Unprinted Designs : {unprinted_designs}")




def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print("Printing model : " + current_design)
		completed_models.append(current_design)


def show_completed_models(completed_models):
	print("\nThe following models have been printed : ")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ["iphone case", "robot pedant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)




# Começa com alguns designs que devem ser impressos
unprinted_designs = ["iphone case", "robot pedant", "dodecahedron"]
completed_models = []

# Simula a impressão de cada design, até que não haja mais nenhum
# Transfere cada design para completed_models após a impressão
while len(unprinted_designs) > 0 : # ou while unprinted_designs :
	current_design = unprinted_designs.pop()
	# Simula a criação de uma impressora 3D a partir do design
	print("Printing Model : " + current_design + ".")
	completed_models.append(current_design)

# Exibe todos os modelos finalizados
print("\nThe following models have been printed : ")
for completed_model in completed_models:
	print(completed_model)



def greet_users(names):
	for name in names :
		msg = "hello, " + name.title() + "!"
		print(msg)

username = ["fabio", "jorge", "pereira"]

greet_users(username)



def make_album(cantor, album, trilhas = ""):

	dicionario_musical = {"nome_cantor": cantor, "nome_album": album}

	if len(trilhas) > 0 :
		dicionario_musical["qtd_trilhas"] = trilhas

	return (dicionario_musical)


#coletanea = {}
print("\nDigite 'quit' para sair a qualquer momento.")

while True :
	cantor = input("\nDigite o nome do artista a ser armazenado : ")
	if cantor == "quit":
		break

	album = input("Digite o nome do album deste artista : ")
	if album == "quit":
		break

	coletanea = make_album(cantor, album)
	print(coletanea)

print("Obrigado por participar.")



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
