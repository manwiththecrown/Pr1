num1 = float(input("Введите число 1: "))
num2 = float(input("Введите число 2: "))
while True:
    simbol = input("Выберите действие ( +, -, *, /, **, % ): ")
    if simbol == "+":
        num1 = num1 + num2
        print("Сумма равна:", num1)
        num2 = float(input("Введите число: "))
    elif simbol == "-":
        num1 = num1 - num2
        print("Разность равна:", num1)
        num2 = float(input("Введите число: "))
    elif simbol == "*":
        num1 = num1 * num2
        print("Произведение равно:", num1)
        num2 = float(input("Введите число: "))
    elif simbol == "/":
        if num2 != 0:
            num1 = num1 / num2
            print("Частное равно ", num1)
        else:
            print("Число не может равняться 0 ")
        num2 = float(input("Введите число: "))
    elif simbol == "**":
        num1 = num1 ** num2
        print("Степень равна:", num1)
        num2 = float(input("Введите число: "))
    elif simbol == "%":
        if num2 != 0:
            num1 = num1 % num2
            print("Остаток от деления равен:", num1)
        else:
            print("Число не может равняться 0 ")
        num2 = float(input("Введите число: "))
    else:
      print("Выберите корректное действие...")
      
      
