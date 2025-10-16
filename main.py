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
import interface

# importando - modo 2
#from calculo import * # ' * ' quer dizer que você quer TODAS as funcoes
#from calculo import dobro, triplo, quadrado # ' * ' quer dizer que você quer APENAS as funcoes dobro e triplo
#from interface import mostra_menu

print("""
      >>> BEM-VINDO À CALCULADORA SENAI <<<
          === PROGRAMA DE CÁLCULO ===
      """)

inicializar = input("Digite 'y' para começar ou 'n' para sair. ")

def menu():
    while True:
        interface.mostra_menu()
        
        opcao = input("\nDigite a opção desejada: ")

        if opcao == "1":
            print("\n1- Calcular o dobro\n")
            numero = int(input("Digite o número que deseja ser dobrado: "))

            dobro = calculo.dobro(numero)
            print(f"""\nO dobro de {numero} é: {dobro}\n""")
        
        elif opcao == "2":
            print("\n2- Calcular o triplo\n")
            numero = int(input("Digite o número que deseja ter o seu triplo: "))
            
            triplo = calculo.triplo(numero)
            print(f"""\nO triplo de {numero} é: {triplo}\n""")
        
        elif opcao == "3":
            print("\n3- Calcular o quadrado\n")
            numero = int(input("Digite o número que deseja ter o seu quadrado: "))

            quadrado = calculo.quadrado(numero)
            print(f"""\nO quadruplo de {numero} é: {quadrado}\n""")

        elif opcao == "4":
            print("\n4- Calcular a raiz quadrada\n")
            numero = int(input("Digite o número que deseja ter a sua raiz quadrada: "))

            raiz_quadrada = calculo.raiz_sqrt(numero)
            print(f"""\nA raiz quadrada de {numero} é: {raiz_quadrada}\n""")

        elif opcao not in [1, 2, 3]:
            print("\n5- Finalizar. Finalizando... Obrigado. Volte sempre!\n")
            break

        else:
            print("\nDigite um dos comandos disponíveis\n")
            continue # pula para o proximo loop do while

if inicializar == "y":
    menu()
