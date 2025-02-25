#this does all validation
def getUserInput(choices, menuItems):
    userChoice = input(f"Enter your choice: ").upper()

    while (len(userChoice) != 1 or userChoice not in choices) and (len(userChoice) == 0 or userChoice not in choices):
        print("Invalid choice. Please enter a single letter from the available choices.")
        userChoice = input("Enter your choice: ").upper()

    if len(userChoice) > 0 and userChoice[0].upper() in choices:
        index = choices.find(userChoice[0].upper())
        return menuItems[index].upper()
    else:
        return menuItems[choices.find(userChoice)].upper()

def printWithNumber(menuItems):
    index = 1
    for item in menuItems:
        print(f"{index}. {item}")
        index += 1

def setNumbers(menuItems):
    numbersStr = ''
    index = 1
    for x in menuItems:
        numbersStr += str(index)
        index += 1
    return numbersStr

def printWithCapitalLetters(menuItems):
    index = 65
    for item in menuItems:
        print(f"{chr(index)}. {item}")
        index += 1

def setCapLetters(menuItems):
    lettersStr = ''
    index = 65
    for x in menuItems:
        lettersStr += chr(index)
        index += 1
    return lettersStr


def printCustomLetters(menuItems):
    for item in menuItems:
        letter = item[0].upper()
        print(f"{letter}. {item}")

def setCustomLetters(menuItems):
    lettersStr = ''
    for item in menuItems:
        lettersStr += item[0].upper()
    return lettersStr

def getMenuNumber(menuItems):
    printWithNumber(menuItems)
    numbers = setNumbers(menuItems)
    return getUserInput(numbers, menuItems)


def getMenuCapLetters(menuItems):
    printWithCapitalLetters(menuItems)
    letters = setCapLetters(menuItems)
    user_choice = getUserInput(letters, menuItems)
    return user_choice

def getMenuCustomLetters(menuItems):
    printCustomLetters(menuItems)
    letters = setCustomLetters(menuItems)
    return getUserInput(letters, menuItems)