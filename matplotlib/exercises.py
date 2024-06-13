import matplotlib.pyplot as plt


class Exercises:
    def exercise1(self):
        """Задача: создать график линейной функции
        которая начинается в точке начала координат"""

        figure, axes = plt.subplots()

        # --- figure params ---
        figure.suptitle('Линейная функция')

        # --- axes params ---
        axes.set_xlabel('Расстояние (метр.)')
        axes.set_ylabel('Время (сек.)')
        axes.grid()

        # axes.plot([X], [Y]). Ф-я plot соединяет каждую текущую точку массива со следующей
        axes.plot([0, 150], [0, 50])

        plt.show()

    def exercise2(self):
        """Задача: изобразить простейший график из трех точек"""
        figure, axes = plt.subplots()

        # --- figure params --- #
        figure.suptitle('Простой график')

        # --- axes params --- #
        axes.set_xlabel('ось - х')
        axes.set_ylabel('ось - y')

        axes.plot([1, 2, 3], [2, 4, 1])

        plt.show()

    def exercise3(self):
        """Задача: Написать программу, рисующую линию по точкам из .txt файла"""
        figure, axes = plt.subplots()

        with open('ex#3_data') as file:
            x_cords = []
            y_cords = []

            for line in file.readlines():
                x_cords.append(int(line.split()[0]))
                y_cords.append(int(line.split()[1]))

            # --- figure params --- #
            figure.suptitle('Простой график')

            # --- axes params --- #
            axes.set_xlabel('Ось - х')
            axes.set_ylabel('Ось - y')

            axes.plot(x_cords, y_cords)

        plt.show()


ex = Exercises()
ex.exercise3()
