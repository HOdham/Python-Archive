#alpha and numeric functions are reversed, dont forget to fix this as we discusses.


class OOMenu:
    def __init__(self, choices, menu_type="NUMERIC",banner = None): # set default type to numeric
        self.__type = menu_type
        self.__menu = {}
        self.__userChoice = None # init the usechoice
        self.__banner = banner
        if self.__type == "ALPHA":
            self.setAlpha(choices)
        else:
            self.setNumeric(choices)

    def setNumeric(self, choices):
        index = 1 # start the index at 1
        for choice in choices:
            self.__menu[str(index)] = choice #add the choices and their values to the dict
            index += 1 # keep indexing up

    def setAlpha(self, choices):
        for index in range(len(choices)): # same thing just converting to ASCII 
            self.__menu[chr(97 + index)] = choices[index] 

    def displayMenu(self):
        print(self.__banner)
        for key, value in self.__menu.items():# displays the menu
            print(key, "-", value)
        print()

    def getUserChoice(self):
        return self.__userChoice # returns the selection

    def setUserChoice(self):
        choice = input("Enter your choice: ").lower() # validation checking
        while choice not in self.__menu:
            print("Invalid choice. Please select an option from the menu.")
            choice = input("Enter your choice: ").lower()
        self.__userChoice = self.__menu[choice]

