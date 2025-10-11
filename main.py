import calculo

print("Olá, Mundo! Agora no VScode!")

print("Programa dos Calculos:")
print("-" * 50)

x = input("Digite o numero e direi o dobro:")

dobro = calculo.dobro(x)

print(f"O dobro de '{x}' é: {dobro}")

# fazendo triplo: 

y = input("Digite outro número e agora direi o seu triplo: ")

triplo = calculo.triplo(y)

print(f"O triplo de '{y}' é: {triplo}")