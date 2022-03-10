lista = ["a","b","c"]
print(lista)
lista.pop()
print(lista)
lista.append("d")
print(lista)
lista.remove(lista[0])
print(lista)
lista.append("e")
lista.append("a")
lista.append("c")
print(sorted(lista))
print(sorted(lista, reverse=True))
print(lista)



localidades = ["Inglaterra","Estados Unidos","Maldivas","Japão","Egito"]
print("\033[1;34mOrdem original das localidades :\n",localidades,"\033[m")

print("\nLista organizada com SORTED() :\n",sorted(localidades))
print("\nLista original exibida :\n",localidades)
print("\nLista organizada com SORTED() e invertida através de parametro :\n",sorted(localidades, reverse=True))
print("\nLista original exibida :\n",localidades)

localidades.reverse()
print("\nLista organizada com função REVERSE() :\n",localidades)

localidades.reverse()
print("\nLista organizada com função REVERSE() novamente, voltando ao normal :\n",localidades)

localidades.sort()
print("\nLista organizada com SORT() :\n",localidades)

localidades.sort(reverse=True)
print("\nista organizada com SORT() em modo REVERSO=TRUE :\n",localidades)



carros = ["bmw","audi","toyota","subaru","volvo","mercedes"]
print("Lista Normal :\n",carros)
print("\nOrdenados via SORTED() :\n",sorted(carros))
print("\nExibindo mais uma vez a lista ORIGINAL sem alteração :\n",carros)
#carros.sort()
#print("\nOrdenados via SORT() :\n",carros)
carros.reverse()
print("\nUsando REVERSE(), inverte as posições sem colocar em ordem alfabética :\n",carros)

carros.sort(reverse=True)
print("\nLista organizada com SORT() em modo REVERSO=TRUE :\n",carros)

carros.sort(reverse=False)
print("\nInversa duas vezes e volta ao original em ordem  :\n",carros)

print("\nLista final após as modificações :\n",carros)

print("\nExibindo o tamanho da lista de carros :",len(carros),"carros(s) cadastrados na lista")



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
print(lista_bicicletas[2].title())
print(lista_bicicletas[-1].title())
print(lista_bicicletas[-3].title())

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
