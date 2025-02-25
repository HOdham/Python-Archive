class Hand:
    def __init__(self):
        self.__cards = []
        self.__value = 0

    def addCard(self, card):
        self.__cards.append(card)
        self.__calculateValue()

    def __calculateValue(self):
        self.__value = 0
        for card in self.__cards:
            if card.getRank() in {"J", "Q", "K"}:
                self.__value += 10
            elif card.getRank() == "A":
                if self.__value + 11 <= 21:
                    self.__value += 11  
                else:
                   self.__value += 1
            else:
                self.__value += card.getRank()

    def getValue(self):
        return self.__value

    def getCards(self):
        return self.__cards