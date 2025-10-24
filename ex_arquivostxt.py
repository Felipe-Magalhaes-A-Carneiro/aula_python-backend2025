# >>> EXEMPLO 01 - Lendo um arquivoe colocando as linhas em uma

conteudo_arquivo = open("exemplo_codificacao"
".txt", "r")
linhas = conteudo_arquivo.readlines()

print(linhas)

# >>> EXEMPLO 02 - Abrindo um arquivo em modo escrita(w) e escrevendo

arquivo_escrever = open("testew.txt", "w")

string = "Olá \n sou um texto\n com 3 linhas."

arquivo_escrever.write(string)

# # fechar o programa - Importante para não prejudicar a memória
arquivo_escrever.close()

# EXEMPLO 03 - Abrindo arquivo em modo append(a) oara continuar escrevendo

arquivo_append = open("testew.txt", "a")

nova_string = "\nOlá, sou um novo texto\n utilizando append"

arquivo_append.write(nova_string)