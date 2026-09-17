dia = (input("Digite um dia da semana (1 até 7): ")).lower()

#funçaõ lower: transformar texto em minusculo

match dia:
    case "segunda"| "terça" | "quarta" | "quinta" | "sexta":
        print("Dia útil")
    case "sábado" | "domingo":
        print("Final de semana")