class Robot:
    def __init__(self, name, variety):
        self.name = name
        self.variety = variety
        print("Robot")

    def get_info(self):
        return "{} is a {} robot".format(self.name, self.variety)


class ServiceRobot(Robot):
    def __init__(self, name):
        super().__init__(name, "service")
        self.name = name


chappi = ServiceRobot("Chappi")
print(chappi.get_info())

class Instrument:
    def __init__(self, size):
        self.size = size

class Stringed(Instrument):
    def __init__(self, n_strings):
        self.n_strings = n_strings

class Violin(Stringed):
    def __init__(self, cost):
        super().__init__(4)
        super(Stringed, self).__init__(50)
        self.cost = cost

my_violin = Violin(680)
print("size:", my_violin.size, 
      "\nstrings:", my_violin.n_strings, 
      "\ncost:", my_violin.cost)