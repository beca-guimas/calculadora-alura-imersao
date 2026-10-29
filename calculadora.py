# ==========================================
# CALCULADORA SIMPLES EM PYTHON
# As quatro operações matemáticas básicas
# ==========================================

# 1. FUNÇÕES PARA AS OPERAÇÕES
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: não é possível dividir por zero!"
    return a / b

# 2. MENU E ENTRADA DE DADOS
print("=== CALCULADORA SIMPLES ===")
print("1. Adição (+)")
print("2. Subtração (-)")
print("3. Multiplicação (*)")
print("4. Divisão (/)")

opcao = input("Escolha uma operação (1, 2, 3 ou 4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# 3. PROCESSAMENTO E RESULTADO
if opcao == '1':
    resultado = somar(num1, num2)
    print(f"Resultado: {num1} + {num2} = {resultado}")

elif opcao == '2':
    resultado = subtrair(num1, num2)
    print(f"Resultado: {num1} - {num2} = {resultado}")

elif opcao == '3':
    resultado = multiplicar(num1, num2)
    print(f"Resultado: {num1} * {num2} = {resultado}")

elif opcao == '4':
    resultado = dividir(num1, num2)
    print(f"Resultado: {num1} / {num2} = {resultado}")

else:
    print("Opção inválida! Escolha um número de 1 a 4.")
