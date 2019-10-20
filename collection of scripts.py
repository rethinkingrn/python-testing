import time
import os
import random
from random import seed
from random import randint

welcome = ("welcome to this script, type LIST for a list of programs")
print(welcome)
def main():
    program = input(">>> ")
    time.sleep(0.5)
    if program=="LIST":
        print("CMD - Opens the command prompt in the same window")
        print("NOTEPAD - Opens notepad, nothing special")
        print("LEGEND - Find out whos legend")
        print("EXIT - Closes the script")
        print("IQ - Find someones IQ")
        main()
    if program=="CMD":
        print("Opening CMD")
        time.sleep(1)
        os.system('cmd')
        exit()
    if program=="NOTEPAD":
        print("Opening NOTEPAD")
        os.system('notepad.exe')
        exit()
    if program=="LEGEND":
        time.sleep(.500)
        # user input
        question=input("who is legend? ")
        time.sleep(0.500)
        #basically just don't type henry
        if question=="henry":
            print("bro your iq must be lower than a rock")
        #im always legend
        if question=="matthew":
            print("you have the highest iq out there")
            exit()
        if question=="me":
            print("i can't believe that you thought that yourself is legend")
            exit()
        time.sleep(.500)
        #making the person rethink who he/she typed
        print(question, "is not legend why would you say that")
        time.sleep(1)
        print(question, "is most likely stubborn also so quite a small brain move right there")
        exit()
    if program=="IQ":
        # asking user for a seed
        seednumber = input("What seed do you want it to be?(if you dont know type a random number): ")
        time.sleep(0.500)
        # asking user for a name
        name = input("Whos iq do you want to find? ")
        seed(seednumber) 
        # the randonm nunmber generator stuff
        for _ in range(1):
            # gets a number
            value = random.randint(0, 150)
            # saying what this persons iq is
            print(value, "is that persons iq.")
        time.sleep(1)
        # insulting the person for having a very low iq
        print(name, "has a very low iq")
        time.sleep(1)
        print(welcome)
        main()
    else:
        print("Not a valid program. Type LIST for a list of programs")
        main()

main()