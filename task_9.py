# Задача 9. Плохой циферблат

odo = int(input('Введите пробег: '))
today = int(input('Введите сегодняшнее число: '))

dig1 = odo // 100
dig2 = odo % 100 // 10
dig3 = odo % 10

dig_sum = dig1 + dig2 + dig3

if dig_sum > today:
    print('Сброс.')
    print('Пробег: 0')
else:
    print('Сегодня не сломался.')
    print('Пробег:', odo)
