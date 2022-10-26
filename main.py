def fac(num):
    if isinstance(num, int):
        if num == 0:
            return 1
        elif num < 0:
            return ('Число должно быть больше 0')
        elif isinstance(num, bool):
            return ('Введён неверный тип данных. Введите число от 0 и выше')
        return fac(num - 1) * num
    else:
        return ('Введён неверный тип данных. Введите число от 0 и выше')

print(fac('True'))