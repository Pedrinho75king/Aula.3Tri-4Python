print("-----Calculadora-----")
n1 = float(input("Digite um nùmero: "))
n2 = float(input("Digite um nùmero: "))
print("\n")

resultado = n1 + n2
print("A soma é:", resultado)

resultado = n1 - n2
print("A subtração é:", resultado)

resultado = n1 * n2
print("A multiplicação é:", resultado)

if (n2 == 0):
    print("Não é possível dividir por zero")
else:
    resultado = n1 / n2
    print("A divisão é:", resultado)

resultado = n1 % n2
print("O resto é:", resultado)