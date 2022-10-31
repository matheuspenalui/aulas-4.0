documento = int(input('''digite o tipo de documento:
1- para RG
2- para titulo de eleitor
'''))
if documento == 1:
   rg = int(input("digite seu rg: "))
   if rg == 12345678:
       print("nome do eleitot: João Carmo")
       print("pode votar")
   else:
       print("eleitor não encontrado")
elif documento == 2:
   titulo = int(input("digite seu titulo: "))
   if titulo == 11122233344:
       print("nome do eleitot: João Carmo")
       print("pode votar")
   else:
       print("eleitor não encontrado")
candidato1 = ("Paulo Freire")
candidato2 = ("Jean Piaget")
voto = int(input("digite o numero de seu canditato: "))
if voto == 10:
    print(candidato1)
elif voto == 20:
    print(candidato2)
else:
    print("candidato não encontrado")