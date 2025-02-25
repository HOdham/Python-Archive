#nice job overall.
#player object needs to have a hand.  You treated the hand like a seperate object and had to keep track of player and pc hadn seperatly from player and pc.
#putting hand in player object instead of main promotes data encapsulation and simplifies tasks in maind.
#45/50


from random import shuffle
import oomenu as m
import cgbase as b
import player as p
import hand as h
import ascii
import time
import os


def main():                                                                       

    deck = b.Deck()
    deck.shuffle()

    print(ascii.logo)
    
    player_name = input("Enter your name: ").strip()
    if not player_name:
        player_name = "Player"
    player = p.Player(player_name)
    pc = p.Player("PC")
    
    wins = 0
    losses = 0
    ties = 0
    

    play_again = "yes"
    while play_again.lower() == "yes":
        os.system('cls')
        statustracker = f"""
        CURRENT STATS
        WINS: {wins}
        LOSSES: {losses}
        TIES: {ties}
        """
        print(statustracker.strip())
        
        
        player_hand = h.Hand()
        pc_hand = h.Hand()

        print("\nDealing each player 2 cards...\n")
        for _ in range(2):
            card = deck.dealCard()
            player_hand.addCard(card)
            card = deck.dealCard()
            pc_hand.addCard(card)
        print()

        print(f"{player.getName()}'s Hand:")
        for card in player_hand.getCards():
            print(card)
        print("Total value:", player_hand.getValue())
        print()
        
        print(f"{pc.getName()}'s Hand:")
        print(pc_hand.getCards()[0],"\n")

        menu = m.OOMenu(["HIT", "STAY"], "NUMERIC" ,f"{player.getName()}'s Turn: HIT or STAY?")
        menu.displayMenu()
        menu.setUserChoice()
        player.setStatus(menu.getUserChoice())
        print(f"{player.getName()} decides to {player.getStatus()}\n")
        while player.getStatus() == "HIT":
            card = deck.dealCard()
            print(f"{player.getName()} receives: {card}")
            player_hand.addCard(card)
            print("Total value:", player_hand.getValue())
            if player_hand.getValue() > 21:
                print(f"{player.getName()} busts! With a value of {player_hand.getValue()}\n")
                break
            else:
                menu.displayMenu()
                menu.setUserChoice()
                player.setStatus(menu.getUserChoice())
                print(f"{player.getName()} decides to {player.getStatus()}\n")

        print(f"{pc.getName()} decides to {pc.getStatus()}")
        print("Total value:", pc_hand.getValue(),"\n")
        time.sleep(2)
        while pc_hand.getValue() <= 17:
            card = deck.dealCard()
            
            print(f"{pc.getName()} receives: {card}")
            print(f"{pc.getName()} decides to {pc.getStatus()}\n")
            print("Total value:", pc_hand.getValue())
            time.sleep(2)
            pc_hand.addCard(card)
            
            if pc_hand.getValue() > 21:
                print(f"{pc.getName()} busts! With a value of {pc_hand.getValue()}\n")
                break
            if pc_hand.getValue() >= 17:
                pc.setStatus("STAY")
                print("Total value:", pc_hand.getValue())
                print(f"{pc.getName()} decides to {pc.getStatus()}\n")
                break

        if player_hand.getValue() <= 21 and (pc_hand.getValue() > 21 or player_hand.getValue() > pc_hand.getValue()):
            print(f"\n{player.getName()} {ascii.won}\n")
            wins += 1
        elif pc_hand.getValue() <= 21 and (player_hand.getValue() > 21 or pc_hand.getValue() > player_hand.getValue()):
            print(f"\n{pc.getName()} {ascii.won}\n")
            losses += 1
        else:
            print(f"\n{ascii.tie}\n")
            ties += 1

        menu = m.OOMenu(["Yes", "No"],"NUMERIC" ,"Do you want to play again?")
        menu.displayMenu()
        menu.setUserChoice()
        play_again = menu.getUserChoice()

if __name__ == "__main__":
    main()
