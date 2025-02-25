import oomenu
# Given by the lab write up
def main():
    mainMenu = oomenu.OOMenu(("one", "two", "three", "exit"), "ALPHA")
    subMenu1 = oomenu.OOMenu(("Rocky", "Bullwinkle", "Sherman"), "NUMERIC")
    subMenu2 = oomenu.OOMenu(("Luke", "Leia", "Han"), "NUMERIC")
    subMenu3 = oomenu.OOMenu(("Peter", "Rocket", "Drax", "Groot"), "NUMERIC")

    while mainMenu.getUserChoice() != "exit":
        mainMenu.displayMenu()
        mainMenu.setUserChoice()
        print("You chose", mainMenu.getUserChoice())

        if mainMenu.getUserChoice() == "one":
            subMenu1.displayMenu()
            subMenu1.setUserChoice()
            print("You chose", subMenu1.getUserChoice())

        elif mainMenu.getUserChoice() == "two":
            subMenu2.displayMenu()
            subMenu2.setUserChoice()
            print("You chose", subMenu2.getUserChoice())

        elif mainMenu.getUserChoice() == "three":
            subMenu3.displayMenu()
            subMenu3.setUserChoice()
            print("You chose", subMenu3.getUserChoice())

main()

