def decimal_to_binary(decimal):
    return bin(decimal).replace("0b", "")


def decimal_to_octal(decimal):
    return oct(decimal).replace("0o", "")


def main():
    try:
        decimal_number = int(input("Введите десятичное число: "))

        binary_result = decimal_to_binary(decimal_number)
        octal_result = decimal_to_octal(decimal_number)

        print(f"\nДесятичное число: {decimal_number}")
        print(f"Двоичное представление: {binary_result}")
        print(f"Восьмеричное представление: {octal_result}")
    except ValueError:
        print("Ошибка: введите корректное десятичное число.")


if __name__ == "__main__":
    main()