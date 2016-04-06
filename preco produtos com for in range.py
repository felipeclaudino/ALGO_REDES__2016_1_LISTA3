#CENTRO UNIVIVERSITARIO - UNIPE
#REDES DE COMPUTADORES - PROFEº JEFFERSON BAROBSA
#ALGORITIMOS E PROGRAMAÇÃO
#FELIPE CLAUDINO DA SILVA - 1510010081
# CÓDIGO EM PYTHON

#preco_produtos

precos = list()
for i in range (0, 5):
	precos.append (float(input("digite o preço do produto n. %d: " % (i+1))))



ate_49 = 0
ate_80 = 0
maior_80 = 0
media = ((precos[0]) + (precos[1]) + (precos[2]) + (precos[3]) + (precos[4])) / 5 

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
print (" media dos produtos foi R$%.2f" % float(media))


