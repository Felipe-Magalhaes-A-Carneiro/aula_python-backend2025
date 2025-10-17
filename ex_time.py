import time

segundos_hoje = time.time()
print(segundos_hoje)

data = time.ctime() #retorna em formato UCT
print(data )

# print("Executando processamento dos dados... Isso pode demorar")
# time.sleep(3) # Trabalha com segundos, fará o terminal 'esperar' o tempo dado no parâmetro 

# print("Executando processamento dos dados... Sim ainda...")
# time.sleep(3)
# print("Executando processamento dos dados... Que situação...")

data_detalhes = time.gmtime()
print(data_detalhes)

