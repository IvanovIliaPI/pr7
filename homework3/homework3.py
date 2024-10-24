def decimal_to_sixth(decimal_number):
    if decimal_number == 0:
        return "0"

    is_negative = decimal_number < 0
    decimal_number = abs(decimal_number)

    sixth_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 6
        sixth_number = str(remainder) + sixth_number
        decimal_number //= 6

    return "-" + sixth_number if is_negative else sixth_number


def is_valid_input(value):
    if value.count('-') > 1 or value.count('.') > 1 or value.count(',') > 1:
        return False
    if value.count('-') == 1 and value[0] != '-':
        return False
    if value.count('.') > 0 and value.count(',') > 0:
        return False
    if value.replace('-', '').replace('.', '').replace(',', '').isdigit() or \
            value.replace('-', '').replace('.', '').replace(',', '').replace(' ', '').isdigit():
        return True
    return False

try:
    decimal_input = input("Введите десятичное число: ")

    if not is_valid_input(decimal_input):
        print("Ошибка: введите корректное число.")
    else:
        decimal_number = int(float(decimal_input.replace(',', '.')))
        result = decimal_to_sixth(decimal_number)
        print(f"Шестеричное представление числа: {result}")
except ValueError:
    print("Ошибка: введите корректное целое число.")