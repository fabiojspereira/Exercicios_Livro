nome = "Fabio"
print("Olá " + nome + ", você gostaria de aprender um pouco sobre Python hoje ?")

nome = "fabio jorge de souza pereira"
print(nome.title())
print(nome.lower())
print(nome.upper())

citacao = 'Albert Einstein certa vez disse : " Uma pessoa que nunca cometeu um erro jamais tentou nada novo. "'
print(citacao)

famous_person = "albert einstein"
mesage = ("\n"+famous_person.title() + ' certa vez disse : " Uma pessoa que nunca cometeu um erro jamais tentou nada novo. "')
print(mesage)

pre = "Olá"
nome = "   fabio            "
pos = "Tchau"
print(pre,nome,pos)
print(nome.rstrip(),pos)
print(pre,nome.lstrip())
print(pre,nome.strip(),pos)

numero = 9
print("Meu número favorito é :",numero)
print("Meu número favorito é : "+ str(numero))

BLOCO = "XXX"

nome = "Fabio"
print(nome.rstrip()+BLOCO,"\n")
print(BLOCO,nome.lstrip(),BLOCO,"\n")
print(BLOCO,nome.strip(),BLOCO,"\n")

texto1 = "FABIO      "
texto2 = "    PEREIRA"
print(texto1 + texto2,"\n")

texto1 = texto1.rstrip()
texto2 = texto2.lstrip()
print(texto1+texto2,"\n")

name = "fabio jorge de souza pereira"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "fabio\n"
last_name = "pereira\n"
full_name = first_name + last_name
message = ("Olá\n" + full_name.title())
print(message)
