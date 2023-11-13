import os
import sys

from random import choice
from random import randint
from random import sample


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


path = resource_path('support')
with open(path, 'r', encoding='utf-8') as f:
    support = f.read().split('\n')


path = resource_path('susses')
with open(path, 'r', encoding='utf-8') as f:
    susses = f.read().split('\n')

path = resource_path('about')
with open(path, 'r', encoding='utf-8') as f:
    cup = f.read()


class Quest:
    def __init__(self, text, ans):
        self.text = text
        self.ans = ans


def task_1(text, var):
    os.system("CLS")

    a = choice([['НЕ', 'not'], ['', '']])
    b = choice([['НЕ', 'not'], ['', '']])

    c = choice([['И', 'and'], ['ИЛИ', 'or']])
    d = sample(2 * ['<', '>', '<=', '>='], 2)

    e = sample(range(10, 20), 2)

    text += f'{a[0]}(x {d[0]} {e[0]}) {c[0]} {b[0]}(x {d[1]} {e[1]})'

    exp = f'{a[1]}(x {d[0]} {e[0]}) {c[1]} {b[1]}(x {d[1]} {e[1]})'

    x = 0

    match var:
        case 2:
            for x in range(101, 0, -1):
                if eval(exp):
                    break

        case 3:
            for x in range(1, 101):
                if eval(exp):
                    break

        case 1:
            x = randint(1, 100)
            text += f'\nпри x = {x}:\n'
            x = eval(exp)

    return Quest(text, x)


def create_var(var):
    q = ''
    match var:
        case 2:
            text = 'Напишите наибольшее целое число x, для которого истинно высказывание:\n'
            q = task_1(text, var)
            while (q.ans == 100) or (q.ans == 1) or (q.ans == 101):
                q = task_1(text, var)
        case 3:
            text = 'Напишите наименьшее целое число x, для которого истинно высказывание:\n'
            q = task_1(text, var)
            while (q.ans == 100) or (q.ans == 1) or (q.ans == 101):
                q = task_1(text, var)
        case 1:
            text = 'Определите истинность высказывания [True/False]:\n'
            q = task_1(text, var)

    return q
