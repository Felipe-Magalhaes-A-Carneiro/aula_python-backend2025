# No menu tera opcoes como abaixo:
# Digite a opção desejada:
# 1- Calcular o dobro
# 2- Calcular o triplo
# 3- Calcular o quadrado
# 4- Finalizar

# Implemente tambem a nova funcao quadrado na biblioteca calculo

# Mude o programa principal pra mostrar o menu em loop, e excute a 
# função escolhida pelo usuario até que ele escolha 4 e finalize o programa

# importando - modo 1
import calculo

# importando - modo 2
#from calculo import * # ' * ' quer dizer que você quer TODAS as funcoes
#from calculo import dobro, triplo, quadruplo# ' * ' quer dizer que você quer APENAS as funcoes dobro e triplo

print("""\n === PROGRAMA DE CALCULO ===\n""")

inicializar = input("Digite 'y' para começar ou 'n' para sair.")

def menu():
    while True:
        print("""Escolha uma das opções abaixo:
                1- Calcular o dobro
                2- Calcular o triplo
                3- Calcular o quadrado
                4- Finalizar
            """)
        
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            print("1- Calcular o dobro\n")
            numero = int(input("Digite o número que deseja ser dobrado: "))

            dobro = calculo.dobro(numero)
            print(f"""O dobro de {numero} é: {dobro}\n""")
        
        elif opcao == "2":
            print("2- Calcular o triplo\n")
            numero = int(input("Digite o número que deseja ter o seu triplo: "))
            
            triplo = calculo.triplo(numero)
            print(f"""O triplo de {numero} é: {triplo}\n""")
        
        elif opcao == "3":
            print("3- Calcular o quadrado\n")
            numero = int(input("Digite o número que deseja ter o seu quadruplo "))

            quadruplo = calculo.quadruplo(numero)
            print(f"""O quadruplo de {numero} é: {quadruplo}\n""")

        elif opcao == "4":
            print("\n4- Finalizar. Finalizando... Obrigado. Volte sempre!")
            break

        else:
            print("\nDigite um dos comandos disponíveis")

if inicializar == "y":
    menu()
