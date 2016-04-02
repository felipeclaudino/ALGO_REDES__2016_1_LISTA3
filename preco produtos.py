#CENTRO UNIVIVERSITARIO - UNIPE
#REDES DE COMPUTADORES - PROFEº JEFFERSON BAROBSA
#ALGORITIMOS E PROGRAMAÇÃO
#FELIPE CLAUDINO DA SILVA - 1510010081
# CÓDIGO EM PYTHON

#preco_produtos
precos = [float(input("digite o preco do primeiro produto: ")),
		  float(input("digite o preco do segundo produto: ")),
		  float(input("digite o preco do terceiro produto: ")),
		  float(input("digite o preco do quarto produto: ")),
		  float(input("digite o preco do quinto produto: "))]


ate_49 = 0
ate_80 = 0
maior_80 = 0

for valor in precos:
	if valor < 50:
		ate_49 = ate_49 + 1
	if valor >= 50 and valor <= 80:
		ate_80 = ate_80 + 1
	if valor > 80:
		maior_80 = maior_80 + 1

print ("%d produtos abaixo de 50,00" % ate_49)
print ("%d produtos entre 50,00 & 80,00" % ate_80)
print ("%d produtos acima de 80,00" % maior_80)


