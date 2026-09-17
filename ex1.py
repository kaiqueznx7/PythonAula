from unittest import case

opcao = int(input("Digite uma opção de (0 até 3): "))
#A estrutura match-case por padrão compara valores por igualdade
#Em outras linguagens
match opcao:
    case 0:
        print("Opção 0")
    case 1:
        print("Opção 1")
    case 2:
        print("Opção 2")
    case 3:
        print("Opção 3")
    case _:
        print("valor incorreto, digite de 0 até ")