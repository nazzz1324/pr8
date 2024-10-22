while True:
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")

    if a.lstrip('-').isdigit() and b.lstrip('-').isdigit():
        print("Сумма:", int(a) + int(b))
    else:
        print("Ошибка: введите целые числа")
