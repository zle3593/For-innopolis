a = 1 # глобальная переменная

def a_func(x): #x - параметр функции
    global a
    y = 15 #y - локальная переменная
    return y + x + a

print(a_func(5))