s = 0

while True:
    x = input("Введите число:")

    if x == "stop" or x == "end":
        break

    if x.replace('.', '', 1).replace('-', '', 1).isdigit():
        s += float(x)
    else:
        print("Ошибка: введите число")

print(s)
