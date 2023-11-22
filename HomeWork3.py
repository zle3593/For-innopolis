def op(val):
    match val:
        case "save":
            return "сохранить"
        case "load":
            return "загрузить"
        case _:
            return "неизвестная операция"


a = input("Введите операцию на английском: ")
print(op(a))
