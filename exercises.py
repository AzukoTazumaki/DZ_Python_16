def common_divisor(two_numbers: str) -> str:
    try:
        first_number = int(two_numbers.split(' ')[0])
        second_number = int(two_numbers.split(' ')[1])
        if first_number == 0:
            return str(second_number)
        return common_divisor(f"{' '.join([str(second_number % first_number), str(first_number)])}")
    except ValueError:
        return 'Ошибка. Введите два числа через пробел.'
