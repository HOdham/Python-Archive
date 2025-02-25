import time
#I feel like you have a firm grasp on this, but also that you are rushing to get it done and missing out on important concepts covered in class.  Like how to make variable private and when to do so.
#

class Card:
    #make variables private with __
    def __init__(self, suit, rank):
        self.__suit = suit
        self.__rank = rank

    def __str__(self):
        self.__symbols = {"clubs": "\u2663", "hearts": "\u2661", "spades": "\u2660", "diamonds": "\u2662"} # create a dictonary with the suit's going w thier symbols
        if self.__rank in {"J", "Q", "K", "A"}: # checks if the card is a str
            return self.__symbols[self.suit] + self.rank # asigns the rank and suit vars to their respected values
        else:
            return self.__symbols[self.suit] + str(self.rank) # because the rest of the cards are numbers casts them into a string and returns

    def __repr__(self):
        return f"{self.__rank} of {self.__suit}" 
    
    def getRank(self):
        return self.__rank
    
    def getSuit(self):
        return self.__suit


class Deck:
    def __init__(self):
        self.__cards = []
        self.__suits = ["clubs", "hearts", "spades", "diamonds"] # suits in a list
        self.__ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"] # all the cards
        for suit in self.__suits: # loop through every suit to asign all of its cards
            for rank in self.__ranks: # now sort out the ranks
                self.__cards.append(Card(suit, rank)) # append it to the cards lsit this list will hols diffrent instances of the card class(I belive they will hold diffrent memory addresses)

    def __str__(self):
        deck_str = ""
        for card in self.__cards:
            deck_str += str(card) + "\n"
        return deck_str #returns the self.cards string adds a newline after every card and its suit.

    def __repr__(self):
        return str(self.__cards) # returns the list in a single line.

    def printDeck(self):
        print(self)# by printing self the __str__ method is called internally

    def shuffle(self):
        import random
        random.shuffle(self.__cards) #this is the python version of table.Random() it takes a list and chooses an item at a random index (:

    def dealCard(self):
        return self.__cards.pop() # gone over in class pops the first item in the list

def main():  # DO NOT MODIFY MAIN
#you may comment sectios out until you are working on them.


#This line of code creates an ordered deck:
    deck1 = Deck()

#This portion of code prints out the deck in the order that it was created
    print("<--- Deck printed in order it was completed --->")
    deck1.printDeck()
    print()
    time.sleep(2)

#This protion of the code shuffles the deck and prints it out
    print("<--- Deck printed after shuffled --->")
    deck1.shuffle()
    deck1.printDeck()
    time.sleep(2)
    print()

#This porton of code deals and prints 3 cards.
    print("<--- Deal and print3 cards --->")
    for x in range(3):
        card = deck1.dealCard()
        print(card, end =  "\t")
    print("\n")

#This portion of code prints the Deck. Notice that the 3 cards that were dealt are no longer in the deck
    print("<--- Deck with 3 cards removed --->")
    deck1.printDeck()


main()
