from function import create_var

grade = 2

right = 0
n = 10
while right < n:
    a = create_var(3)
    print(a.text)
    ant = input('Введите ответ [True/False]: ').strip()
    if ant == str(a.ans):
        print("Верно!")
        right += 1
    else:
        print(f'Не верно. Верный ответ {a.ans}.')
        right = 0

    print(f'Осталось решить {n - right}.')
    print(f'Текущая оценка {grade}.')
    input('Для продолжения нажмите enter...')

print("Раздел завершен.")
grade += 1
print(f'Текущая оценка {grade}.')
input('Для продолжения нажмите enter...')

right = 0
while right < n:
    a = create_var(1)
    print(a.text)
    ant = input('Введите ответ: ').strip()
    if ant == str(a.ans):
        print("Верно!")
        right += 1
    else:
        print(f'Не верно. Верный ответ {a.ans}.')
        right = 0

    print(f'Осталось решить {n - right}.')
    print(f'Текущая оценка {grade}.')
    input('Для продолжения нажмите enter...')

print("Раздел завершен.")
grade += 1
print(f'Текущая оценка {grade}.')
input('Для продолжения нажмите enter...')

right = 0
while right < n:
    a = create_var(2)
    print(a.text)
    ant = input('Введите ответ: ').strip()
    if ant == str(a.ans):
        print("Верно!")
        right += 1
    else:
        print(f'Не верно. Верный ответ {a.ans}.')
        right = 0

    print(f'Осталось решить {n - right}.')
    print(f'Текущая оценка {grade}.')
    input('Для продолжения нажмите enter...')

print("Раздел завершен.")
grade += 1
print(f'Текущая оценка {grade}.')
print('Программа завершена.')
input('Для продолжения нажмите enter...')
