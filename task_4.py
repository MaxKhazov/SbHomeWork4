#Задача 4. Калькулятор скидки

from turtle import pos


pos_1 = int(input('Введите стоимость первого товара: '))
pos_2 = int(input('Введите стоимость второго товара: '))
pos_3 = int(input('Введите стоимость трертьего товара: '))

check = pos_1 + pos_2 + pos_3

if check > 10000:
    check = check - (check * 10 / 100)

print("Итоговая сумма:", check)