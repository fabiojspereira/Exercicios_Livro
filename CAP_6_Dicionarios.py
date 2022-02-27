"""
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
