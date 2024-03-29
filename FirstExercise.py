nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

if nome and idade:
     print(f'Seu nome é ${nome}')
     print(f"Seu nome invertido é {nome[::-1]}")
     if ' ' in nome:
          print("Seu nome contém espaço")
     else:
          print("Seu nome não contem espaços")
     print(f"Seu nome contém {len(nome)}")
     print(f"A primeira letra do seu nome é {nome[0:1]}")
     print(f"A ultima letra do seu nome é {nome[-1]}")
else:
     print("Desculpe, você deixou campos vazios")     
