import time
import os
import random
from random import seed
from random import randint

welcome = ("Welcome to this script, type LIST for a list of programs")
kovans = ("Don't forget to use code Kovans in the Fortnite CHAPTER 2 item shop")
print(kovans)
def main():
    time.sleep(2)
    print(welcome)
    program = input(">>> ")
    time.sleep(0.5)
   
    if program=="LIST":
        print("CMD - Opens the command prompt in the same window")
        print("NOTEPAD - Opens notepad, nothing special")
        print("LEGEND - Find out whos legend")
        print("EXIT - Closes the script")
        print("IQ - Find someones IQ")
        print("CALCULATOR - Opens the Windows Calculator")
        main()
    
    if program=="CMD":
        time.sleep(1)
        print("Opening CMD")
        time.sleep(1)
        os.system('cmd.exe')
        main()
   
    if program=='EXIT':
        time.sleep(1)
        print('Exiting now')
        exit()
   
    if program=="NOTEPAD":
        print("Opening NOTEPAD")
        os.system('notepad.exe')
        main()
    
    if program=="CALCULATOR":
        time.sleep(1)
        print("Opening CALCULATOR")
        os.system('calc.exe')
        main()
    
    if program=="LEGEND":
        time.sleep(.500)
        # user input
        print("who is legend? Type NAMES for a list of names.")
    def NAME():
        question=input(">>> ")
        time.sleep(0.500)
        #basically just don't type henry
       
        if question=="NAMES":
            print("ALL must be lower-cased")
            print("You can type any name, these just have a cool responce")
            print("----------------------------------------------------------")
            print("henry")
            print("matthew")
            print("me")
            print("yin")
            print("----------------------------------------------------------")
            NAME()
        if question=="henry":
            print("bro your iq must be lower than a rock")
            main()
        
        #im always legend
        if question=="matthew":
            print("you have the highest iq out there")
            main()
        
        if question=="me":
            print("i can't believe that you thought that yourself is legend")
            time.sleep(2)
            main()
        
        if question=="yin":
            print("Cool you're original")
            main()
        time.sleep(.500)
        
        #making the person rethink who he/she typed
        print(question, "is not legend why would you say that")
        time.sleep(1)
        print(question, "is most likely stubborn also so quite a small brain move right there")
        main()
    NAME()
    if program=="IQ":
        # asking user for a name
        name = input("Whos iq do you want to find? ")
        seednumber = input("What do you think his/her iq is? ")
        time.sleep(0.500)
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