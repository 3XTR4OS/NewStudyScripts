# -*- coding: utf8 -*-
import pprint
from sys import stdin
import colleges_Info


def infinity_input(sight):
    messages = []
    for i in stdin:
        messages.append(i.strip().split(sight))

    return messages


def classic_input():
    pass


def write_info():
    with open('info.txt', 'w') as file:
        file.writelines([f'{profession}: {temperament}, \n' for profession, temperament in infinity_input()])

# ---------------------------------------------------
# for i in sorted(infinity_input('.'), key=lambda x: x[1]):
#     print(f'{i[0]}.{i[1]} ({i[-1]})')
# -----------------------
# lst = []
# for i in infinity_input('–'):
#     lst.append([i[0][2::].strip(), i[-1].strip()])
#
# pprint.pprint(lst)
# --------------------------
# for i in infinity_input():
#     print(i)
# for num, val in enumerate(subjects):
#     print(f"{num}: {val}")
# -------------------------------------------
# pprint.pprint(colleges_Info.COLLEGES['Хабаровский технический колледж'])
# --------------------------------------------------------
# for key, val in colleges_Info.COLLEGES['Хабаровский технический колледж'].items():
#     print(f'"{key}": "{val.lower()}",')
# ---------------------------------------------------
# lst = [['Экономика и бухгалтерский учет', 'Флегматик'],
#        ['Финансы', 'Меланхолик'],
#        ['Компьютерные системы и комплексы', 'Холерик'],
#        ['Право и организация социального обеспечения', 'Сангвиник'],
#        ['Строительство и эксплуатация городских путей сообщения', 'Холерик'],
#        ['Строительство и эксплуатация зданий и сооружений', 'Сангвиник'],
#        ['Техническая эксплуатация подъемно-транспортных, строительных, дорожных '
#         'машин и оборудования',
#         'Холерик'],
#        ['Техническое обслуживание и ремонт автомобильного транспорта', 'Меланхолик'],
#        ['Технология деревообработки', 'Флегматик'],
#        ['Информационные системы и программирование', 'Флегматик'],
#        ['Обеспечение информационной безопасности автоматизированных систем',
#         'Меланхолик']]
#
# for i in lst:
#     print(f'"{i[0]}": "{i[-1]}",')
