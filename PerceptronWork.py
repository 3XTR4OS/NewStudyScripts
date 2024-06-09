class NeuronWorkPrototype:
    def __init__(self, connections: list[tuple[int, float]]):
        self.__perceptron_sum: int = 0
        self.__connections = connections

    def reaction(self):
        for connection in self.__connections:
            self.__perceptron_sum += connection[0] * connection[1]

        return self.__perceptron_sum

    def activate_function(self):
        return 0 if self.__perceptron_sum <= 1 else 1

    def take(self):
        print(self.__connections)
        print(self.activate_function())


n = NeuronWorkPrototype([(1, 0.3), (0, 0.2), (1, 0.5), (1, 2.1)])
n.reaction()
n.take()
