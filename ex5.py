
idade = int(input("Digite sua idade: "))

match idade:
    case x if x > 18:
        print("maior que 18")
    case x if x < 18:
        print("menor que 18")
    case _:
        print("Valor invalido")