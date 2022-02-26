"""
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
