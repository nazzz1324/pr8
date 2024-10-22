s = 0
n = 1
while True:
    x = input(f"Введите число {n}-ое:")

    if x == "stop" or x == "end":
        break

    if x.replace('.', '', 1).replace('-', '', 1).isdigit():
        s += float(x)
        n += 1
    else:
        print("Ошибка: введите число")

print(s)
