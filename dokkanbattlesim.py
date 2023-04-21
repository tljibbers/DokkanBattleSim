import random
import sys
from summonPool import summonPool

global dragonStone
global token
dragonStone = 50
token = 1
yourBox = []

def welcome():
    print("------------------------------------------------------------------------------------------------------------------")
    print("Welcome to the Dokkan Battle Simulator!")
    print("Here you can simulate the hit mobile game Dragon Ball Z Dokkan Battle!")
    print("The main feature in this simulator is the Summoning System, which uses dragon stones to summon.")
    print("To be able to summon, you have to have tokens.")
    print("By playing the mini games and winning, you will be able to get tokens and try to summon your favorite characters.")
    print("To start with, you will get 50 stones and 1 token!")
    print("Try your best, and have fun!")
    print("------------------------------------------------------------------------------------------------------------------")
    print(" ")

def menu():
    print("0 - Exit")
    print("1 - Summon")
    print("2 - Get Dragon Stones")
    print("3 - All Characters in Summon Pool")
    print("4 - Your Characters")
    print("5 - Play for Tokens")
    print("6 - Save")
    print("7 - Delete File")

def characterList(summonPool):
    print(" ")
    print("----------------------------")
    for i in summonPool:
        print(i)
    print("----------------------------")
    print(" ")


def yourBoxList(yourBox):
    print(" ")
    print("----------------------------")
    for i in yourBox:
        print(i)
    print("----------------------------")
    print(" ")

def getDragonStones(dragonStone, token):
    extraStone = 0
    extraStone = random.randint(1, 7)
    dragonStone = dragonStone + extraStone
    subToken = 1

    if token != 0:
        if extraStone == 1:
            print("Gohan is chopping wood...")
            print("Gohan was not able to chop up much wood. You got " + str(extraStone) + " dragonstones.")
            
        elif extraStone == 2:
            print("Gohan is chopping wood...")
            print("Gohan was not able to chop up much wood. You got " + str(extraStone) + " dragonstones.")
            
        elif extraStone == 3:
            print("Gohan is chopping wood...")
            print("Gohan was able to get a bit of wood! You got " + str(extraStone) + " dragonstones!")
            
        elif extraStone == 4:
            print("Gohan is chopping wood...")
            print("Gohan was able to get a bit of wood! You got " + str(extraStone) + " dragonstones!")
            
        elif extraStone == 5:
            print("Gohan is chopping wood...")
            print("Gohan got a lot of wood chopped! You got " + str(extraStone) + " dragonstones!")
            
        elif extraStone == 6:
            print("Gohan is chopping wood...")
            print("Gohan got a lot of wood chopped! You got " + str(extraStone) + " dragonstones!")
            
        elif extraStone == 7:
            print("Gohan is chopping wood...")
            print("Gohan got all of the wood chopped! You got " + str(extraStone) + " dragonstones!")
            
    else:
        print("You don't have enough tokens. Get a token to get some dragon stones.")

    token = token - subToken
    return dragonStone, token
    
def getToken(token):
    addToken = 0
    

def summon(summonPool, dragonStone, yourBox):
    print("Do you want to do a Multi-Summon of ten characters, or a Single-Summon of one?")
    print("1 - Single = 5 Stones")
    print("2 - Multi = 50 Stones")
    pick = int(input())
    
    if pick == 1:
        print("Okay, doing a Single-Summon!")
        print(" ")
        dragonStone = dragonStone - 5
        randomCard = random.choice(summonPool)
        print("----------------------------")
        print("You got " + randomCard + "!")
        print("----------------------------")
        yourBox.append(randomCard)
        print(" ")
        return dragonStone
    elif pick == 2:
        print("Okay, doing a Multi-Summon")
        print(" ")
        dragonStone = dragonStone - 50
        print("----------------------------")
        for i in range(9):
            randomCard = random.choice(summonPool)
            print("You got " + randomCard + "!")
            yourBox.append(randomCard)
        print("----------------------------")
        print(" ")
        return dragonStone
    else:
        print("This number is not valid.")


def menuFunction(summonPool, dragonStone, token, yourBox):
    print(" ")
    print("You currently have " + str(dragonStone) + " dragonstones.")
    print("You currently have " + str(token) + " tokens.")
    print(" ")
    pick = int(input("Pick an Option: "))
    if pick == 0:
        print("Exiting the simulator.")
        sys.exit()
    if pick == 1:
        if dragonStone < 5:
            print("You do not have enough dragonstones. Please play for tokens and roll for more.")
            menu()
            menuFunction(summonPool, dragonStone, token, yourBox)
        else:
            print("Going to the summon area!")
            dragonStone = summon(summonPool, dragonStone, yourBox)
            menu()
            menuFunction(summonPool, dragonStone, token, yourBox)
    if pick == 2:
        if token < 1:
            print("You do not have enough tokens to roll for dragonstones. Please play some of the mini-games to gain more.")
            menu()
            menuFunction(summonPool, dragonStone, token, yourBox)
        else:
            print("Let's get some dragon stones!")
            dragonStone, token = getDragonStones(dragonStone, token)
            menu()
            menuFunction(summonPool, dragonStone, token, yourBox)
    if pick == 3:
        print("Let's check the characters!")
        characterList(summonPool)
        menu()
        menuFunction(summonPool, dragonStone, token, yourBox)
    if pick == 4:
        print("Let's check your box!")
        yourBoxList(yourBox)
        menu()
        menuFunction(summonPool, dragonStone, token, yourBox)
    else:
        print("Invalid option. Pick another option.")
        menu()
        menuFunction(summonPool, dragonStone, token, yourBox)



welcome()
menu()
menuFunction(summonPool, dragonStone, token, yourBox)

