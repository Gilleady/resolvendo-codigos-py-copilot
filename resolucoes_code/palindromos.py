# Solicita ao usuário que insira uma palavra
palavra = input("Digite uma palavra: ")

# Verifica se a palavra é um palíndromo
if palavra == palavra[::-1]:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")