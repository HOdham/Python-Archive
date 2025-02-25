class DormRoom:
    def __init__(self, color_abbrev, rep):
        self.__color_abbrev = color_abbrev
        self.__rep = rep

    @property #(:
    def color(self):
        return "Blue" if self.__color_abbrev == "B" else "Gold"

    def __str__(self):
        return f"{self.color}{self.__rep}"