
import oomenu as m
class Player:
    def __init__(self, name):
        self.__name = name
        self.__status = "HIT"

    def getName(self):
        return self.__name

    def getStatus(self):
        return self.__status

    def setStatus(self, status):
        self.__status = status
