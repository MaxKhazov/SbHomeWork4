# Задача 8. Хватит ли зарплаты

hours = int(input('Введите отработанные часы: '))
credit = int(input('Введите остаток по кредиту: '))
food = int(input('Введите траты на еду: '))

salary = ((hours * 200) / 8) + hours
expenses = credit + food

print('Вы заработали:', salary, 'рублей')

if salary >= expenses:
    print('Часов хватает - можно отдохнуть!')
else:
    print('Часов недостаточно! Придётся идти работать.')
