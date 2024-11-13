# Solicita ao usuário que insira um número
numero = int(input("Digite um número: "))

# Verifica se o número é ímpar ou par
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")