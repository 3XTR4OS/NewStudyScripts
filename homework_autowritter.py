# -*- coding: utf-8 -*-

import pyperclip
import sys
import HOMEWORK_CONFIG


def make_cool_periods():
    TEACHERS_DICT = HOMEWORK_CONFIG.TEACHERS

    messages = [x for x in [x.strip() for x in sys.stdin] if x != '']
    lessons_temp = [i for i in range(0, len(messages) + 1, 5)]
    lessons_slice = [(lessons_temp[i], lessons_temp[i + 1]) for i in range(len(lessons_temp) - 1)]
    periods = [messages[m_slice[0]:m_slice[-1]] for m_slice in lessons_slice]
    result = ''

    for period in periods:
        result += f'🧿{period[1]} [Пара №{period[0]}]🧿\n'
        result += f'🧑‍🏫Преподаватель: {TEACHERS_DICT[period[2]]} 🧑‍🏫\n'
        result += f'⏳Время: {period[3]}⏳ \n'
        result += f'🚪Кабинет: {period[4]}🚪 \n'
        result += f'🔻Домашка: \n'
        result += '\n'

    with open('дз.txt', 'w', encoding='UTF-8') as text_file:
        text_file.writelines(result)
    pyperclip.copy(result)

    print('УСПЕШНО ВЫПОЛНЕНО.\nРЕЗУЛЬТАТ СКОПИРОВАН В БУФЕР ОБМЕНА')


make_cool_periods()
