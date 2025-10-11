# importando - modo 1
# import calculo

# importando - modo 2
#from calculo import * # ' * ' quer dizer que você quer TODAS as funcoes
from calculo import dobro, triplo # ' * ' quer dizer que você quer APENAS as funcoes dobro e triplo

print("Olá, Mundo! Agora no VScode!")

print("Programa dos Calculos:")
print("-" * 50)

x = input("Digite o numero e direi o dobro:")

dobro = dobro(x)

print(f"O dobro de '{x}' é: {dobro}")

# fazendo triplo: 

y = input("Digite outro número e agora direi o seu triplo: ")

triplo = triplo(y)

print(f"O triplo de '{y}' é: {triplo}")