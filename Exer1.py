a = float(input("Insira a altura da parede: "))
c = float(input("Insira o comprimento da parede: "))
area = (a*c)
litros = (area/3)
latas = (litros/3.6)
valor = (latas*107)
print("Precisará de {:.2f} latas de tinta".format(litros)+
"\nCustará R${:.2f}".format(valor))