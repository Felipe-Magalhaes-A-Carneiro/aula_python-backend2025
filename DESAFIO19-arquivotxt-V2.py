# DESAFIO - 

# Faça um programa que pergunte ao usuário as quatro informações e insira
# cadastro "dados.txt"

# ao final do cadastro, ele listara todos os contatos cadatrados


# Armazenar dados
escolha = input("Começar?")

while True:
    armazenar_dados = open('dados.txt','a')

    nome = input("Digite o seu nome: ")
    sobrenome = input("Digite o seu sobrenome: ")
    email = input("Escreva o seu e-mail: ")
    cpf = input("Digite o seu CPF: ")

    armazenar_dados.write(f"\n{nome},")
    armazenar_dados.write(f"{sobrenome},")
    armazenar_dados.write(f"{email},")
    armazenar_dados.write(f"{cpf}")

    escolha = input("Continuar?")
    if escolha == "":
        break

# Fazer a leitura do arquivo pelo terminal:
visualizar_dados = open("dados.txt", 'r')
linhas = visualizar_dados.readlines()

print(linhas)

