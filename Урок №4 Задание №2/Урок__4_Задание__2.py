def main():
    # Запрашиваем у пользователя пятизначное целое число
    try:
        number = int(input("Введите пятизначное целое число: "))
    except ValueError:
        print("Ошибка: введено не целое число.")
        return

    # Проверяем, что число действительно пятизначное
    if number < 10000 or number > 99999:
        print("Ошибка: число должно быть пятизначным.")
        return

    # Извлекаем цифры
    ten_thousands = number // 10000 % 10  # Десятки тысяч
    thousands = number // 1000 % 10        # Тысячи
    hundreds = number // 100 % 10           # Сотни
    tens = number // 10 % 10                 # Десятки
    units = number % 10                       # Единицы

    # Выполняем вычисления
    difference = ten_thousands - thousands
    if difference == 0:
        print("Ошибка: деление на ноль.")
        return

    result = (tens ** units) * hundreds / difference

    # Выводим результат
    print(f"Результат: {result}")

if __name__ == "__main__":
    main()