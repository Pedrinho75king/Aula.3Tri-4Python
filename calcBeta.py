print("-----Calculadora-----")

n1 = float(input("Digite um nùmero: "))
n2 = float(input("Digite um nùmero: "))
operador = input("Informa o operador (+,-,/,*,%): ")
print("\n")

if operador == '+':
    resultado = n1 + n2
    print(f"Resultado: {resultado}")