#CENTRO UNIVIVERSITARIO - UNIPE
#REDES DE COMPUTADORES - PROFEº JEFFERSON BAROBSA
#ALGORITIMOS E PROGRAMAÇÃO
#FELIPE CLAUDINO DA SILVA - 1510010081
# CÓDIGO EM PYTHON

#nota do cinema

avaliacao = [int(input("1º opnião digite de  1 a 3: ")),
			int(input("2º opnião digite de  1 a 3: ")),
			int(input("3º opnião digite de  1 a 3: ")),
			int(input("4º opnião digite de  1 a 3: ")),
			int(input("5º opnião digite de  1 a 3: ")),]

otimo = 0 
bom = 0
regular = 0 
numero_invalido = 0

for opniao in avaliacao:
	if opniao == 3:
		otimo = otimo +1
	if opniao == 2:
		bom = bom +1
	if opniao == 1:
		regular = regular +1
	if opniao > 3:
		numero_invalido = numero_invalido + 1

print ("%d avaliação otima" % otimo)
print ("%d avaliação bom" % bom)
print ("%d avaliação regular" % regular)
print ("%d avaliação com numeros invalidos" % numero_invalido)