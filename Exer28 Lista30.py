#input de tres valores float
x = float(input("Insira um valor: "))
y = float(input("Insira outro valor: "))
z = float(input("Insira outro valor: "))
#Cálculos da soma dos quadrados dos tres valores dos inputs
s = ((x**2)+(y**2)+(z**2))
#Resultado da soma dos quadrados do tres valores dos inputs
print ("A soma do quadrados dos números {}, {} e {} é {:.3f}".format(x, y, z, s))