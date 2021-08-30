p = float(input("Insira o valor do prêmio: "))
cofres = (p*0.07)
v = (p*0.93)
pg = (v*0.46)
sg = (v*0.32)
tg = (v*0.22)
print("Valor total do prêmio: R${:.2f}".format(p)+
"\nValor a ser divido: R${:.2f}: ".format(v)+
"\nPrimeiro ganhador: R${:.2f}:".format(pg)+
"\nSegundo ganhador: R${:.2f}:".format(sg)+
"\nTerceiro ganhador: R${:.2f}:".format(tg))