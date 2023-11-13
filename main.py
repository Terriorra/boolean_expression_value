from function import create_var
from random import choice
from function import support
from function import susses
from function import cup

name = input('Приветствую. Как к тебе обращаться? ')
print('Здесь три раздела, для прохождения необходимо ответить 10 раз подряд правильно.')
print('Для тройки можно пройти только один раздел. Для четверки - два, для пятёрки - три.')
input('Для продолжения нажмите enter...')

grade = 2
n = 10

for var in range(1, 4):
    right = 0
    while right < n:
        a = create_var(var)
        print(f'Осталось решить {n - right}.')
        print(f'Раздел: {var}.')
        print(f'Текущая оценка {grade}.')
        print(20 * '=' + '\n')
        print(a.text)
        ant = input('Введите ответ: ').strip()
        print()
        if ant == str(a.ans):
            print(f"Верно, {name}!")
            print(choice(susses))
            right += 1
        else:
            print(f'Не верно, {name}. Верный ответ {a.ans}.')
            print(choice(support))
            right = 0

        input('\nДля продолжения нажмите enter...')

    print("Раздел завершен.")
    grade += 1
    print(f'Текущая оценка {grade}.')
    input('Для продолжения нажмите enter...')


print('Программа завершена.')
print(cup)
input('Для продолжения нажмите enter...')
