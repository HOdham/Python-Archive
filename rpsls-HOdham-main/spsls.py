import random
import os
from hMenu import getMenuCustomLetters
#nice job on this program 35/35

def printTie():
    print("""
 /$$$$$$ /$$   /$$               /$$$$$$        /$$$$$$$$ /$$           /$$
|_  $$_/| $$  | $/              /$$__  $$      |__  $$__/|__/          | $$
  | $$ /$$$$$$|_//$$$$$$$      | $$  \\ $$         | $$    /$$  /$$$$$$ | $$
  | $$|_  $$_/  /$$_____/      | $$$$$$$$         | $$   | $$ /$$__  $$| $$
  | $$  | $$   |  $$$$$$       | $$__  $$         | $$   | $$| $$$$$$$$|__/
  | $$  | $$ /$$\\____  $$      | $$  | $$         | $$   | $$| $$_____/    
 /$$$$$$|  $$$$//$$$$$$$/      | $$  | $$         | $$   | $$|  $$$$$$$ /$$
|______/ \\___/ |_______/       |__/  |__/         |__/   |__/ \\_______/|__/\n""")

def printPc():
    print("""
 /$$$$$$$   /$$$$$$        /$$      /$$                    
| $$__  $$ /$$__  $$      | $$  /$ | $$                    
| $$  \\ $$| $$  \\__/      | $$ /$$$| $$  /$$$$$$  /$$$$$$$ 
| $$$$$$$/| $$            | $$/$$ $$ $$ /$$__  $$| $$__  $$
| $$____/ | $$            | $$$$_  $$$$| $$  \\ $$| $$  \\ $$
| $$      | $$    $$      | $$$/ \\  $$$| $$  | $$| $$  | $$
| $$      |  $$$$$$/      | $$/   \\  $$|  $$$$$$/| $$  | $$
|__/       \\______/       |__/     \\__/ \\______/ |__/  |__/\n""")

def printPlayer():
    print("""
 /$$$$$$$  /$$                                               /$$      /$$                    
| $$__  $$| $$                                              | $$  /$ | $$                    
| $$  \\ $$| $$  /$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$       | $$ /$$$| $$  /$$$$$$  /$$$$$$$ 
| $$$$$$$/| $$ |____  $$| $$  | $$ /$$__  $$ /$$__  $$      | $$/$$ $$ $$ /$$__  $$| $$__  $$
| $$____/ | $$  /$$$$$$$| $$  | $$| $$$$$$$$| $$  \\__/      | $$$$_  $$$$| $$  \\ $$| $$  \\ $$
| $$      | $$ /$$__  $$| $$  | $$| $$_____/| $$            | $$$/ \\  $$$| $$  | $$| $$  | $$
| $$      | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$            | $$/   \\  $$|  $$$$$$/| $$  | $$
|__/      |__/ \\_______/ \\____  $$ \\_______/|__/            |__/     \\__/ \\______/ |__/  |__/
                         /$$  | $$                                                           
                        |  $$$$$$/                                                           
                         \\______/\n""")

def printLogo():
    print("""
 /$$$$$$$  /$$$$$$$   /$$$$$$  /$$        /$$$$$$ 
| $$__  $$| $$__  $$ /$$__  $$| $$       /$$__  $$
| $$  \\ $$| $$  \\ $$| $$  \\__/| $$      | $$  \\__/
| $$$$$$$/| $$$$$$$/|  $$$$$$ | $$      |  $$$$$$ 
| $$__  $$| $$____/  \\____  $$| $$       \\____  $$
| $$  \\ $$| $$       /$$  \\ $$| $$       /$$  \\ $$
| $$  | $$| $$      |  $$$$$$/| $$$$$$$$|  $$$$$$/
|__/  |__/|__/       \\______/ |________/ \\______/\n""")

def randomPcChoice(choices):
    return random.choice(choices)

def whoWins(pcChoice, playerChoice):
    rules = (
        ('ROCK', ('XSCISSORS', 'LIZARD')),
        ('PAPER', ('ROCK', 'SPOCK')),
        ('XSCISSORS', ('PAPER', 'LIZARD')),
        ('LIZARD', ('PAPER', 'SPOCK')),
        ('SPOCK', ('ROCK', 'XSCISSORS'))
    )


    if pcChoice == playerChoice:
        return 'tie'

    for rule in rules:
        if rule[0] == pcChoice and playerChoice in rule[1]:
            return 'pc'
    return 'player'

def playGame():
    player_score = 0
    pc_score = 0
    play_again = 'Y'
    printLogo()
    options = ('ROCK', 'PAPER', 'XSCISSORS', 'LIZARD', 'SPOCK')
    while play_again == 'Y':
    
        pcChoice = randomPcChoice(options)

        playerChoice =  getMenuCustomLetters(options)
        winner = whoWins(pcChoice, playerChoice)

        
        print(f"\nDisplay Choices → Player: {playerChoice} VS PC: {pcChoice}")

        if winner == 'player':
            printPlayer()
            player_score += 1
        elif winner == 'pc':
            printPc()
            pc_score += 1
        elif winner == 'tie':
            printTie()


        print(f"\nRunning Score → Player {player_score} Computer {pc_score}")

        print("Play Again?")
        play_again = getMenuCustomLetters(('Y', 'N') )
        os.system("cls")


if __name__ == "__main__":
    playGame()
