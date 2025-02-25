#there is a lot of good here but it does not run. I corrected a few errors see my comments.
#I think they stem from you try ing to access class variables directly and not using a getter function. 
# Ifeel like you tried to changed this but did so hurridly and did not get everything.
#also there is a cannot compare objects wtih < operator.  Unless you code that out you can not compare objects directly, You have to compare some specific object value.

#slow down when coding. Im glad you like this, but you seem to be rushing through which leads to these types of errors.
#35/50

#I have no idea what happend but i ran the code from the previous push (the one I think you graded and it ran with no found issues)


import oomenu
import yahtzee
import dice

def roll_dice(dice,keep_dice=None):
    if keep_dice is None:
        for die in dice:
            die.roll()
    else:
        for i in range(5):
            if i not in keep_dice:
               dice[i].roll()

def print_dice(dice):
    print("╔══════╦═══╦═══╦═══╦═══╦═══╗")
    print("║ Dice ║ 1 ║ 2 ║ 3 ║ 4 ║ 5 ║")
    print("╚══════╩═══╩═══╩═══╩═══╩═══╝")
    dice_values = []
    for die in dice:
        dice_values.append(str(die.value())) # cannot access self.__value in a class this way you need a getter function. I added one to get your pgm torun.
    print("╔══════╦═══╦═══╦═══╦═══╦═══╗")
    print(f"║ Face ║ {dice_values[0]} ║ {dice_values[1]} ║ {dice_values[2]} ║ {dice_values[3]} ║ {dice_values[4]} ║")
    print("╚══════╩═══╩═══╩═══╩═══╩═══╝")
    

def main():
    dice_list = []
    for _ in range(5):
        dice_list.append(dice.Die())
        
    yahtzee_game = yahtzee.Yahtzee()
    
    print("Initial Roll:")
    roll_dice(dice_list)
    print_dice(dice_list)

    
    print("\nUpper Half:")
    yahtzee_game.score_upper(dice_list)
    
    print("\nLower Half:")
    yahtzee_game.score_lower(dice_list)
    

    
    for _ in range(2):
        keep_dice = input("\nEnter die number(s) to keep (separated by a space), or press enter to keep none: ").split()
        if keep_dice:
            keep_indices = []
            for die in keep_dice:
                if die.isnumeric():
                    keep_indices.append(int(die) - 1)
            roll_dice(dice_list, keep_indices) 
            print_dice(dice_list)
    
            print("\nUpper Half:")
            yahtzee_game.score_upper(dice_list)
    
            print("\nLower Half:")
            yahtzee_game.score_lower(dice_list)
        else:
            break 
        
    print("Select the category to score in")
    
    choices = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "Three of a Kind", "Four of a Kind", 
               "Full House", "Small Straight", "Large Straight", "Chance", "Yahtzee"]
    menu = oomenu.OOMenu(choices,"NUMERIC")
    menu.displayMenu()
    menu.setUserChoice()
    category = menu.getUserChoice()

    value = input(f"Enter the score you wish to keep for {category}: ")
    while not value.isnumeric():
        value = input(f"Invalid Please Enter a number {category}: ")
        
    value = int(value)

    yahtzee_game.set_score(category, value)
    yahtzee_game.print_scorecard()
    
    
    

if __name__ == "__main__":
        main()
