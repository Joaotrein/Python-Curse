compras = []
lista_enumerada = enumerate(compras)

while True:
     opcao = input("Selecione uma opção\n[i]nserir [a]pagar [l]istar [s]air: ")

     if opcao == "i":
          inserir = input("Digite o que deseja inserir: ")
          try:
               inserir = int(inserir)
               print("Digite apenas letras!")
          except:
               compras.append(inserir)
     elif opcao == "a":
          apagar = int(input("Digite o indicie que deseja apagar: "))
          try:
               compras.pop(apagar)
          except:
               print("Não foi possível apagar, está fora do tamanho da lista")
     elif opcao == "l":
          if len(compras) == 0:
               print("Nada para listar!")
          else:
               for i, valor in lista_enumerada:
                    print(i, valor)
     elif opcao == "s":
          break
     