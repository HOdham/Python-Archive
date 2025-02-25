import random

class Die:
    def __init__(self):
        self.__value = None

    def roll(self):
        self.__value = random.randint(1, 6)


#no value function to get value for line 20 in main.
    def value(self):
        return self.__value
