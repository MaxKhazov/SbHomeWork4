# Задача 2. Поступление

subject_1 = int(input('Введите количество баллов по русскому языку: '))
subject_2 = int(input('Введите количество баллов по математике: '))
subject_3 = int(input('Введите количество баллов по информатике: '))

score = subject_1 + subject_2 + subject_3
print('Общее количество баллов:', score)

if score >= 270:
    print('Поздравляем! Вы на бюджете!')
else:
    print('К сожалению, вы не прошли на бюджет.')
