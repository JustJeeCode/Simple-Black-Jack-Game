'''
- The player and dealer each get two cards
- The game asks the player if the player would like to hit or stay
- highest player wins
'''
from random import randint
from Cards import Player
from Cards import Computer
import time

def player_hit_stay():
    # Hit or stay
    hit_or_stay = input("\nDo you chose to \"Hit\" or \"Stay\"? [H/S]\n\n>>> ")

    if hit_or_stay == "H" or hit_or_stay == "h" or hit_or_stay == "hit" or hit_or_stay == "Hit":
        new_card = randint(1, 10)
        Player.cards.append(new_card)

        print("Dealers deck: [x, " + str(Computer.cardTwo) + "]")
        print("Your deck: " + str(Player.cards))
        time.sleep(1)

        card_total = sum(Player.cards)
        if card_total > 21:
            print("You lost! Dealer Won...")
            print("Dealers deck: [x, " + str(Computer.cardTwo) + "]")
            print("Your deck: " + str(Player.cards))
            quit()
        else:
            player_hit_stay()
            time.sleep(1)
    else:
        print("\nYou stayed...")
        print("Dealers deck revealed: " + str(Computer.cards))
        print("Your deck: " + str(Player.cards))
        time.sleep(1)
        computer_hit_stay()

def computer_hit_stay():
    #AI HERE
    sumPlayerCards = sum(Player.cards)
    sumComputerCards = sum(Computer.cards)

    if sumPlayerCards > sumComputerCards:
        new_card = randint(1, 10)
        Computer.cards.append(new_card)

        print("\nDealer Hit!")
        print("Dealers deck: " + str(Computer.cards))
        print("Your deck: " + str(Player.cards))
        time.sleep(1)

        if sumComputerCards > 21:
            print("\nYou win!!! Your deck counted to " + str(sumPlayerCards) + "\nand the dealers deck counted to " + str(sumComputerCards) + ".")
            quit()
        else:
            computer_hit_stay()
    else:
        print("\nDealer Stayed!")

        if sumComputerCards > 21:
            print("\nYou win!!! Your deck counted to " + str(sumPlayerCards) + "\nand the dealers deck counted to " + str(sumComputerCards) + ".")
            quit()

        if sumPlayerCards > sumComputerCards:
            print("\nYou win!!! Your deck counted to " + str(sumPlayerCards) + "\nand the dealers deck counted to " + str(sumComputerCards) + ".")
            quit()
        elif sumPlayerCards == sumComputerCards:
            print("\nYou tied!!! Your deck counted to " + str(sumPlayerCards) + "\nand the dealers deck counted to " + str(sumComputerCards) + ".")
            quit()
        else:
            print("\nYou lost!!! Your deck counted to " + str(sumPlayerCards) + "\nand the dealers deck counted to " + str(sumComputerCards) + ".")
            quit()
        


def main():
    #Computer cards
    Computer.cards = []
    Computer.cardOne = randint(1, 10)
    Computer.cardTwo = randint(1, 10)

    Computer.cards.append(Computer.cardOne)
    Computer.cards.append(Computer.cardTwo)

    print("Dealers deck: [x, " + str(Computer.cardTwo) + "]")

    #Players cards
    Player.cards = []
    Player.cardOne = randint(1, 10)
    Player.cardTwo = randint(1, 10)

    Player.cards.append(Player.cardOne)
    Player.cards.append(Player.cardTwo)

    print("Your deck: " + str(Player.cards))

    gameOn = True
    while gameOn:
        player_hit_stay()


if __name__ == "__main__":
    main()