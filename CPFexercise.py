cpf = "04151660046"  # Removed the replace function to simplify

digitosList = [int(digit) for digit in cpf[:-2]]  

digitos_mult = []
contador = 10
for i in digitosList:
    digitos_mult.append(i * contador)
    contador -= 1

soma = sum(digitos_mult)
y = soma * 10 % 11
y = 0 if y > 9 else y

digitosList.append(y)  

digitos_mult2 = []
contador2 = 11
for k in digitosList:
    digitos_mult2.append(k * contador2)
    contador2 -= 1

soma2 = sum(digitos_mult2)
c = soma2 * 10 % 11
c = 0 if c > 9 else c

if c == int(cpf[-1]) and y == int(cpf[-2]):
    print("CPF válido")
else:
    print("CPF inválido")
