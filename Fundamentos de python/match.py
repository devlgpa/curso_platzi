
dia = input("Ingrese un día de la semana: ").lower()

match dia:
    case "lunes":
        print("Hoy es Lunes")
    case "martes":
        print("Hoy es Martes")
    case "miércoles":
        print("Hoy es Miércoles")
    case "jueves":
        print("Hoy es Jueves")
    case "viernes":
        print("Hoy es Viernes")
    case _:
        print("No coincide con ninguna de las anteriores opciones")