#Declaração de variáveis input para inserção de dados
#input do valor total do prêmio
p = float(input("Insira o valor total do prêmio: "))
#desconto dos cofres estaduais
cofres = (p*0.07)
#valor a ser dividido após o desconto dos cofres
v = (p*0.93)
#prêmio primeiro ganhador
pg = (v*0.46)
#prêmio segundo ganhador
sg = (v*0.32)
#prêmio terceiro ganhador
tg = (v*0.22)
#Resultado do valor total do prêmio
print("Valor total do prêmio: R${:.2f}".format(p)+
#Resultado do valor descontado para os cofres
"\nValor descontado para os cofres".format(cofres)+
#Resutado do valor a ser dividido para os ganhadores
"\nValor a ser divido: R${:.2f}: ".format(v)+
#Valor recebido pelo primeiro ganhador
"\nPrimeiro ganhador: R${:.2f}:".format(pg)+
#Valor recebido pelo segundo ganhador
"\nSegundo ganhador: R${:.2f}:".format(sg)+
#Valor recebido pelo terceiro ganhador
"\nTerceiro ganhador: R${:.2f}:".format(tg))