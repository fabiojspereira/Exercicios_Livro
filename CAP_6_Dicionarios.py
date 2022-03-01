"""
cidades = {
	"rio de janeiro": {"pais": "Brasil", "pop": "6 milhões", "nível de violência": "alto"},
	"joao pessoa": {"pais": "Brasil", "pop": "900 mil", "nível de violência": "baixo"},
	"campina grande": {"pais": "Brasil", "pop": "300 mil", "nível de violência": "médio"}
	}

for cidade, info_cidade in cidades.items():
	pais = info_cidade['pais']
	populacao = info_cidade['pop']
	violencia = info_cidade['nível de violência']

	print(f"\nCidade : {cidade.title()}")
	print(f"País : {pais.title()}")
	print(f"População : {populacao}")
	print(f"Nível de violência : {violencia}")


#for chave, valor in cidades.items():
#	print(f"\nNome da cidade : {chave}")
#	print(f"País : {valor['pais']}")
#	print(f"População : {valor['pop']}")
#	print(f"Nível de violência : {valor['nível de violência']}")



numeros_favoritos = {
	"fabio": [9, 10],
	"priscila":[1, 7, 100, 500],
	"jhony":[12],
	"pereira":[500, 1000, 0]
	}

for chave, valor in numeros_favoritos.items():
	print(f"\nOs numeros favoritos de {chave.title()} são :")
	for numeros in valor:
		print(f"{numeros}")



lugares_favoritos = {
	"fabio": ["egito","joao pessoa", "eua"],
	"priscila": ["argentina", "egito", "europa"],
	"jhony": ["cama", "cambuca de comida", "colo do papai e mamae"]
	}

for pessoa, lugar in lugares_favoritos.items():
	print(f"\n{pessoa.title()}, gosta dos seguintes lugares :")
	for nome_do_lugar in lugar:
		print(f"{nome_do_lugar}")



jhony = {
	"tipo_animal":"cachorro",
	"nome_do_dono":"fabio"
	}

fred = {
	"tipo_animal": "cachorro",
	"nome_do_dono": "maria"
	}

cuca = {
	"tipo_animal": "gato",
	"nome_do_dono": "felipe"
	}

pets = [ jhony, fred, cuca ]

for animal in pets:
	print()
	print(f"{'ESPÉCIE DO ANIMAL':<20}{':':<2}{animal['tipo_animal'].title()}")
	print(f"{'NOME DO DONO':<20}{':':<2}{animal['nome_do_dono'].title()}")



pessoa_001 = {
	"primeiro_nome": "fabio",
	"segundo_nome": "pereira",
	"idade": "41",
	"cidade": "joão pessoa",
	"endereco": "pedro firmino do nascimento 454 - apt 301"
	}

pessoa_002= {
	"primeiro_nome": "priscila",
	"segundo_nome": "lourenco",
	"idade": "37",
	"cidade": "joão pessoa",
	"endereco": "pedro firmino do nascimento 454 - apt 301"
	}

pessoa_003 = {
	"primeiro_nome": "jhony",
	"segundo_nome": "bravo",
	"idade": "12",
	"cidade": "joão pessoa",
	"endereco": "pedro firmino do nascimento 454 - apt 301"
	}

lista_pessoas = [ pessoa_001, pessoa_002, pessoa_003 ]
for pessoa in lista_pessoas:
	print()
	print(f"{'NOME':<15}{':':<2}{pessoa['primeiro_nome'].title()}")
	print(f"{'SOBRENOME':<15}{':':<2}{pessoa['segundo_nome'].title()}")
	print(f"{'IDADE':<15}{':':<2}{pessoa['idade'].title()}")
	print(f"{'CIDADE':<15}{':':<2}{pessoa['cidade'].title()}")
	print(f"{'ENDEREÇO':<15}{':':<2}{pessoa['endereco'].title()}")




usuarios = {
	"0001":{
		"nome":"fabio",
		"sobrenome":"pereira",
		"localidade":"brasil"
		},

	"0002":{
		"nome":"priscila",
		"sobrenome":"lourenco",
		"localidade":"brasil"
		}
	}


for user_name, user_info in usuarios.items():
	print(f"\n{'USUÁRIO':<15}{':':<2}{user_name}")
	print(f"{'NOME COMPLETO':<15}{':':<2}{user_info['nome'].title() + ' ' + user_info['sobrenome'].title()}")
	print(f"{'LOCALIDADE':<15}{':':<2}{user_info['localidade'].title()}")



linguagens_favoritas = {
	"fabio": ["python", "c++", "visual basic"],
	"mario": ["python"],
	"carlos": ["html"],
	"pereira": ["pascal"],
	"jhony": ["pascal"],
	"jorge": ["python", "pascal"],
	"roberto": ["c"],
	"priscila": ["html"],
	"roger": ["ruby"],
	"fred": ["python"]
}

#for chave, valor in linguagens_favoritas.items():
#	print(f"As linguagens favoritas de \033[1;34m{chave.title()}\033[m são :\n {valor}\n")

for chave, valor in linguagens_favoritas.items():
	if len(valor) > 1:
		print(f"As linguagens favoritas de \033[1;34m{chave.title()}\033[m são :")
		for linguagens in valor:
			print(linguagens,end=" ")
			print()
	else:
		print(f"\nA linguagem {linguagens} é a única linguagem favorita de \033[1;34m{chave.title()}\033[m")



pizza = {"massa":"grossa", "ingredientes":["queijo", "tomate", "camarao"]}
print(f"Foi feito o pedido de uma pizza com massa \033[1;34m{pizza['massa']}\033[m e com os seguintes ingredientes :")

for ingredientes in pizza["ingredientes"]:
	print(ingredientes)



alienigenas = list()

for alien in range(30):
	valores = {"cor":"verde", "pontos":5, "velocidade":"lento"}
	alienigenas.append(valores)

for contador in range(5):
	print(f"{contador+1} - {alienigenas[contador]}")
print(f"Total de alienígenas criados : {len(alienigenas)}\n")

for contador in range(0, 3, 1):
	alienigenas[contador] = {"cor":"amarelo", "pontos":10, "velocidade":"normal"}

for contador in range(5):
	print(f"{contador+1} - {alienigenas[contador]}")
print(f"Total de alienígenas criados : {len(alienigenas)}\n")

print("NOVAS INSTRUÇÕES")
for alien in alienigenas[5:10]:
	if alien["cor"] == "verde":
		alien["cor"] = "branco"
		alien["pontos"] = 50
		alien["velocidade"] = "ultra"

for contador in range(15):
	print(f"{contador+1} - {alienigenas[contador]}")
print(f"Total de alienígenas criados : {len(alienigenas)}\n")



alien_0 = {"cor":"verde", "ponto":"5"}
alien_1 = {"cor":"amarelo", "ponto":"10"}
alien_2 = {"cor":"vermelho", "ponto":"15"}

alienigenas = [alien_0,alien_1,alien_2]

for x in alienigenas:
	print(x)



linguagens_favoritas = {
	"fabio": "python",
	"mario": "python",
	"carlos": "html",
	"pereira": "pascal",
	"jhony": "pascal",
	"jorge": "python",
	"roberto": "c",
	"priscila": "html",
	"roger": "ruby",
	"fred": "python"
}

lista = list()
lista_002 = ["fabio","pereira"]
print(lista)
lista.append(linguagens_favoritas.copy())  # forma de alimentar uma LISTA com dicionários.
lista.append(linguagens_favoritas.copy())  # forma de alimentar uma LISTA com dicionários.
lista.append(linguagens_favoritas.copy())  # forma de alimentar uma LISTA com dicionários.

print(lista)
print(len(lista))
print(lista_002)
print(len(lista_002))



lista_pessoas = [
	"fabio","mario","jorge","souza","carlos",
	"pereira","priscila","lourenco","flavio",
	"fabio","fred","silva"]

linguagens_favoritas = {
	"fabio": "python",
	"mario": "python",
	"carlos": "html",
	"pereira": "pascal",
	"jhony": "pascal",
	"jorge": "python",
	"roberto": "c",
	"priscila": "html",
	"roger": "ruby",
	"fred": "python"
}

for pessoa in lista_pessoas:
	if pessoa in linguagens_favoritas:
		print(f"Muito obrigado por já ter respondido a pesquisa {pessoa.title()}.")
		print(f"Linguagem favorita de {pessoa.title()} : {(linguagens_favoritas[pessoa].title())}.\n")
	else:
		print(f"\033[1;31m{pessoa.title()}\033[m, você precisa fazer parte desta pesquisa !\n")



glossario = {"print": "comando usado para facilitar a forma de debugar códigos",
			 "if": "comando usado para resolver situações de condições",
			 "for": "comando utilizado para percorrer um conjunto de instruções",
			 "break": "comando utilizado para encerrar laços e outras condições",
			 "while": "comando utilizado para construção de laços", "elif": "sub comando da instrução if."}

for chave, valor in glossario.items():
	print(f"COMANDO : {chave.title()}\nSignificado : {valor.title()}")

print()
for chave in glossario.keys():
	print(f"Comandos citados neste glossário : {chave}")



linguagens_favoritas = {
	"fabio": "python",
	"mario": "python",
	"carlos": "html",
	"pereira": "pascal",
	"jhony": "pascal",
	"jorge": "python",
	"roberto": "c",
	"priscila": "html",
	"roger": "ruby",
	"fred": "python"
}

print("Existem linguagens repetidas mas vamos mostrar sem repetição")

for valor in set(linguagens_favoritas.values()):
	print(valor.title())



linguagens_favoritas = {
	"fabio": "python",
	"mario": "c",
	"carlos": "html",
	"pereira": "ruby",
	"jhony": "pascal"
	}

print(f"Dicionário : {linguagens_favoritas}\n")

for chave in (linguagens_favoritas.keys()):
	print(f"CHAVES DO DICIONÁRIO : {chave}")
print()
for valor in linguagens_favoritas.values():
	print(f"VALORES DO DICIONÁRIO : {valor}")



linguagens_favoritas = {
	"fabio": "python",
	"mario": "c",
	"carlos": "html",
	}

amigos = ["mario", "carlos", "fabio"]

# Aqui ele usa a variável key para armazenar a string que está dentro da lista de amigos.
for key in linguagens_favoritas.keys():
	print((key.title()))
	if key in amigos:
		print(f"Olá {key.title()}, notei que sua linguagem favorita é {(linguagens_favoritas[key]).title()}\n")

# Aqui é a forma direta de chamar o valor de dentro do dicionário
for key, value in linguagens_favoritas.items():
	print((key.title()))
	if key in amigos:
		print(f"Olá {key.title()}, notei que sua linguagem favorita é {value.title()}\n")



user_0 = {
	"primeiro_nome":"fabio",
	"segundo_nome":"pereira",
	"idade":"41",
	"cidade":"joão pessoa",
	"endereco": "pedro firmino do nascimento 454 - apt 301"
	}

#for key, value in user_0.items():
#	print(f"\nCHAVE : {key.title()}")
#	print(f"VALOR : {value.title()}")

# Produz o mesmo resultado
for key in user_0:
	print(key)
print()
for key in user_0.keys():
	print(key)



dic_002 = {"fabio":"9", "priscila":"7", "jhony":"1", "pereira":"500"}
print(dic_002)
print(f"Numero favorito do fabio é : {dic_002['fabio']}")
print(f"Numero favorito do priscila é : {dic_002['priscila']}")
print(f"Numero favorito do jhony é : {dic_002['jhony']}")
print(f"Numero favorito do pereira é : {dic_002['pereira']}")



linguagens_favoritas = {"fabio": "python",
						"mario": "c",
						"carlos": "html",
						}

print(f"A linguagem favorita do Fabio é {linguagens_favoritas['fabio'].title()}")



alien_0 = {"x_pos" : 0 , "y_pos" : 25 , "velocidade" : "media"}
print(f"Posicão X original : {alien_0['x_pos']}")

alien_0["pontos"] = 5
#alien_0["velocidade"] = "alta"

# Move o alien para a direita
# Determina a distância que o alienígena deve se deslocar de acordo com sua velocidade atual

if alien_0["velocidade"] == "baixa":
	x_incremento = 1
elif alien_0["velocidade"] == "media":
	x_incremento = 2
else:
	x_incremento = 3

# A nova posição é a posição antiga somada ao incremento
alien_0["x_pos"] = alien_0["x_pos"] + x_incremento

print(f"A nova posição X do alienígena é {alien_0['x_pos']}")

print(alien_0)
del alien_0["pontos"]
print(alien_0)



alien_0 = {"cor": "verde", "pontos": 5}
print(alien_0["cor"])
print(alien_0["pontos"])

pontuacao = alien_0["pontos"]
print(f"Você ganhou {str(pontuacao)} pontos ")

alien_0["posicao x"] = 0
alien_0["posicao y"] = 25
#alien_0 = {"peso":"100 kg"} # Desta forma você recria o dicionario
print(alien_0)

alien_0 = {}
alien_0["cor"] = "verde"
alien_0["pontos"] = 5
print(alien_0)

print("Agora o alien mudou de cor !!")
alien_0["cor"] = "branco"
print(alien_0)
"""
