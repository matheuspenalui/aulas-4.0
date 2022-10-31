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

  