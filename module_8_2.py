def personal_sum(numbers):
    global i
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчета суммы - {i}')
    return result, incorrect_data


def calculate_average(numbers):
    try:
        total = personal_sum(numbers)
        count = 0
        for i in numbers:
            if isinstance(i, int):
                count += 1
        if total[0] == 0:
            return 0
        average = total[0] / count
        return average

    except ZeroDivisionError:
        return 0

    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
