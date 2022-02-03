
lista_convidados = ["Jhony","Nilza","Fabiola"]
print("Seja bem vindo ao jantar " + lista_convidados[0] + ".")
print("Seja bem vinda ao jantar " + lista_convidados[1] + ".")
print("Seja bem vinda ao jantar " + lista_convidados[2] + ".")

print("Convidado " + lista_convidados[2] + " não poderá comparecer ao jantar !" )

# lista_convidados[2] = "Priscila"
# lista_convidados.pop()
# lista_convidados.append("Priscila")

del lista_convidados[2]
lista_convidados.insert(2,"Priscila")

print("\nLISTA DE CONVIDADOS CONFIRMADOS")
print(lista_convidados)

print("\nSeja bem vindo ao jantar " + lista_convidados[0] + ".")
print("Seja bem vinda ao jantar " + lista_convidados[1] + ".")
print("Seja bem vinda ao jantar " + lista_convidados[2] + ".")

print("\nFoi encontrada uma mesa maior para o jantar !")
lista_convidados.insert(3,"Fabio")
lista_convidados.insert(4,"Maria")
lista_convidados.insert(5,"Solange")

print("Seja bem vindo ao jantar " + lista_convidados[0] + ".")
print("Seja bem vindo ao jantar " + lista_convidados[1] + ".")
print("Seja bem vindo ao jantar " + lista_convidados[2] + ".")
print("Seja bem vindo ao jantar " + lista_convidados[3] + ".")
print("Seja bem vindo ao jantar " + lista_convidados[4] + ".")
print("Seja bem vindo ao jantar " + lista_convidados[5] + ".")

print("\nTivemos um problema com a mesa, infelizmente. \nApenas dois lugares disponíveis...")
retirado = lista_convidados.pop()
print("Infelizmente seu nome foi retirado da lista de convidados " + retirado + ".")
retirado = lista_convidados.pop()
print("Infelizmente seu nome foi retirado da lista de convidados " + retirado + ".")
retirado = lista_convidados.pop()
print("Infelizmente seu nome foi retirado da lista de convidados " + retirado + ".")
retirado = lista_convidados.pop()
print("Infelizmente seu nome foi retirado da lista de convidados " + retirado + ".")

print("\nLISTA DE CONVIDADOS PRESENTES")
print(lista_convidados[0])
print(lista_convidados[1])

del lista_convidados[0:2]
print("\nLISTA DE CONVIDADOS")
print(lista_convidados)



"""
lista_bicicletas = ["trek","trek","trek","cannondale","trek","redline","specialized","trek"]
print(lista_bicicletas)
soma = 0
print(len(lista_bicicletas))
print("*"*50)

for count in range ( 0, len(lista_bicicletas)):
	if "trek" in lista_bicicletas:
		print(lista_bicicletas)
		lista_bicicletas.remove("trek")
		print("Uma palavra 'trek' foi localizada e apagada !")
		print(lista_bicicletas,"\n")
		soma = soma + 1

print("FINALIZADO")
print(soma)
print(lista_bicicletas)

print(lista_bicicletas[0].title())
print(lista_bicicletas[3].title())
print(lista_bicicletas[-1].title())
print(lista_bicicletas[-4].title())

txt = ("Minha primeira bicicleta foi uma " + lista_bicicletas[0].title() + ".")
print (txt)

nomes = ["fabio","jorge","souza","pereira"]
print("\nBom dia "+nomes[0])
print("Bom dia "+nomes[1])
print("Boa noite "+nomes[2])
print("Boa tarde "+nomes[3])

lista_bicicletas[2] = "caloi"
print(lista_bicicletas)

lista_bicicletas.append("GTS")
lista_bicicletas.append("OGGY")

print(lista_bicicletas)

lista_bicicletas.insert(5, "ITEM INSERT")
print(lista_bicicletas)

del lista_bicicletas[5]
print(lista_bicicletas)

poped_item = lista_bicicletas.pop()
print(lista_bicicletas)
print("Ultimo item que foi apagado :",poped_item)

lista_bicicletas.remove("caloi")
print(lista_bicicletas)
"""
