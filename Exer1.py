#Declaração de variáveis input para inserção de dados
#input da altura da parede
a = float(input("Insira a altura da parede: "))
#input do comprimento da parede
c = float(input("Insira o comprimento da parede: "))
#calculo da área da parede
area = (a*c)
#cálculo da quantia de litros de tinta para pintar a parede
litros = (area/3)
#cálculo da quantia de latas de tinta para pintar a parede
latas = (litros/3.6)
#cálculo do valor das latas de tinta necessárias
valor = (latas*107)
#Resultado da quatia de latas de tinta
print("Precisará de {:.2f} latas de tinta".format(litros)+
#Resultado do valor das latas de tinta
"\nCustará R${:.2f}".format(valor))