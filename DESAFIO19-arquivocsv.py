# DESAFIO - Arquivos - CSV

# Faça um programa que pergunte ao usuário as quatro informações e insira
# cadastro "dados.txt" ao final do cadastro, ele listara todos os contatos cadatrados


# Armazenar dados
nome = input("Digite o seu nome: ")
sobrenome = input("Digite o seu sobrenome: ")
email = input("Escreva o seu e-mail: ")
cpf = input("Digite o seu CPF: ")

# Trata os dados em uma linha
novo_registro = f"\n{nome},{sobrenome},{email},{cpf}"

# armazena os dados tratados
armazenar_dados = open('dados_cadastros.csv','a')
armazenar_dados.write(novo_registro)

armazenar_dados.close()

# FASE 02
# Fazer a leitura do arquivo pelo terminal:
visualizar_dados = open("dados_cadastros.csv", 'r')
linhas = visualizar_dados.readlines()

print(linhas)

# FASE 03
# Imprimir lista tratada e editada para impressão no terminal
for cadastro in linhas[1:]:
    listadados = cadastro.split(sep = ',')
    string_lista = f"""
    Nome = {listadados[0]}
    Sobrenome = {listadados[1]}
    e-mail = {listadados[2]}
    CPF = {listadados[3]}
"""