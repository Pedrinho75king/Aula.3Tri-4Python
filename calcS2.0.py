def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

print("-----Calculadora-----")
n1 = float(input("Digite um nùmero: "))
n2 = float(input("Digite um nùmero: "))
operador = input("Informa o operador (+,-,*,/,%): ")
print("\n")

if operador == '+':
    resultado = n1 + n2
    print(f"Resultado: {resultado}")
elif operador == '-':
    resultado = n1 - n2
    print(f"Resultado: {resultado}")
elif operador == '*':
    resultado = n1 * n2
    print(f"Resultado: {resultado}")
elif operador == '/':
    resultado = n1 / n2
    print(f"Resultado: {resultado}")
    if(n2 == 0):
        resultado = "Divisão por zero é impossível"
elif operador == '%':
    resultado = n1 % n2
    print(f"Resultado: {resultado}")