a = input("Введите первое число: ")
b = input("Введите второе число: ")

if a.replace('.', '', 1).replace('-', '', 1).isdigit() and b.replace('.', '', 1).replace('-', '', 1).isdigit():
    a = float(a)
    b = float(b)

    if a < b:
        for i in range(int(a) + 1, int(b)):
            print(i)
    else:
        for i in range(int(b) + 1, int(a)):
            print(i)
else:
    print("Ошибка: введите числа")
