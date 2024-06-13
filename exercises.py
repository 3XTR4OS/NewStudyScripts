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


ex = Exercises()
ex.exercise1()
