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

def calculate_x(a, b):
    return 3 * a + 3 - b + 4 * a

def main():
    a_input = input("Введите значение a: ")
    b_input = input("Введите значение b: ")

    if not is_valid_input(a_input) or not is_valid_input(b_input):
        print("Ошибка: введите корректные числа.")
        return

    a = float(a_input.replace(',', '.'))
    b = float(b_input.replace(',', '.'))

    x = calculate_x(a, b)
    print(f"Результат уравнения x = {x}")

if __name__ == "__main__":
    main()