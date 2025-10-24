from tabulate import tabulate
# DESAFIO - Arquivos - CSV

# Faça um programa que pergunte ao usuário as quatro informações e insira
# cadastro "dados.txt" ao final do cadastro, ele listara todos os contatos cadatrados


# Armazenar dados
nome = input("Digite o seu nome: ").title()
sobrenome = input("Digite o seu sobrenome: ").title()
email = input("Escreva o seu e-mail: ").lower()
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
    
# FASE 03 (Alternativa com tabulate)
lista_tabulate = []

for cadastro in linhas:
    # cria uma list nova
    lista_linha = []
    listadados = cadastro.split(sep = ',')
    for dado in listadados:
        lista_linha.append(dado)
    lista_tabulate.append(lista_linha)

print(tabulate(lista_tabulate, headers = "firstrow", tablefmt = "fancy_grid"))