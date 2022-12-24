import time, os, sys
from time import sleep
from Classes.WeaponClass import* #only used in str_to_class function
from keyPress import KBHit #used to skip typing effect


def instructions():
    """
    Prompts the user if they want to see instructions and story.

    Returns False if user WANTS to see instructions/story
    Returns True if user does NOT want to see instructions/story
    """
    skip = ""
    while skip.upper() != 'Y' and skip.upper() != 'N':
        clear()
        skip = typeInput("Would you like to see the instructions and the story? [Y/N]")
    typeText("\nYou can skip any line of text anytime by pressing [enter] or [return] on your keyboard")
    pCont()

    if skip.upper() == 'Y':
        return False
    return True


def intro():
    """
    Greets player and introduces basic game mechanics
    """
    print("*******************************")
    sleep(.5)
    print("*******************************")
    sleep(.5)
    print("Welcome to the Horizon RPG Game")
    sleep(.5)
    print("*******************************")
    sleep(.5)
    print("*******************************")
    sleep(2.5)
    
    skip = instructions()

    if not skip:
        clear()
        typeText("You got kidnapped by the Carja tribe and you are now stuck in the Sun Ring", sleep = .5)
        typeText("\nYour only way to escape is to fight the machines in the arena until you prove yourself to be a worthy warrior", sleep = 1)
        typeText("\n\nTo win your freedom back, you must win every machine trial in the arena and please Helis enough to let you go", sleep = .5)
        pCont()
        typeText("You will have to fight 5 machines, one each round with varrying difficulties", sleep = 1)
        typeText("\n\nYou will be randomly assigned 3 weapon classes and you will have the choice to pick one weapon from each class", sleep = 1)
        typeText("\n\nGood Luck and Happy Hunting!!!", sleep = .5)
        pCont()

    return skip


def typeText(text, typeSpeed = .03, sleep = 0):
    """
    Prints text (imitating typing)

    Checks for keyboard hits and if the 'enter' (Windows) or 'return' (Mac) key is hit,
    the typing effect is skipped for the rest of the text

    Restores original terminal settings at completion

    Paramater text: text that needs to be printed
    Precondition: text is a string

    Paramater typeSpeed: pause duration (in seconds) between characters
    Precondition: typeSpeed is a float or an int

    Paramater sleep: pause duration (in seconds) AFTER finishing printing text
    Precondition: sleep is a float or an int
    """
    keyboard = KBHit()

    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()

        if keyboard.keyboardHit(): 
            c = keyboard.getChar()
            if ord(c) == 10: #ASCII code of 'enter' or 'return' key
                typeSpeed = 0
            sleep = 0

        time.sleep(typeSpeed)
    time.sleep(sleep)
    
    keyboard.set_normal_term() #Restore original terminal settings


def typeInput(text, typeSpeed = .03):
    """
    Prints text (imitating typing) with an input prompt

    Checks for keyboard hits and if the 'enter' (Windows) or 'return' (Mac) key is hit,
    the typing effect is skipped for the rest of the text

    Paramater text: text that needs to be printed
    Precondition: text is a string

    Paramater typeSpeed: pause duration (in seconds) between characters
    Precondition: typeSpeed is a float or an int
    """
    keyboard = KBHit()

    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()

        if keyboard.keyboardHit(): 
            c = keyboard.getChar()
            if ord(c) == 10: #ASCII code for the 'enter' or 'return' key
                typeSpeed = 0

        time.sleep(typeSpeed)

    keyboard.set_normal_term() #Restore original terminal settings to display user inputs
    
    value = input("\n>> " )  
    return value 


def clear():
    """
    Wipes the terminal with no previous history
    """
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")


def pCont():
    """
    Prompts player to press 'enter' to continue and clears the screen
    """
    input(yellow + "\n\nPress [enter] to continue" + reset)
    clear()


def str_to_class(str):
    """
    Used to convert str to a class type

    Paramater str: to convert to class type
    Precondition: str is a string
    """
    return getattr(sys.modules[__name__], str)


#colors
Red = "\033[0;31m"
Green = "\033[0;32m"
Orange = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m" 
black = "\033[0;30m"
red = "\033[0;91m"
green = "\033[0;92m"
yellow = "\033[0;93m"
blue = "\033[0;94m"
magenta = "\033[0;95m"
cyan = "\033[0;96m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"
cyan_back = "\033[0;46m"
purple_back = "\033[0;45m"
white_back = "\033[0;47m"
blue_back = "\033[0;44m"
orange_back = "\033[0;43m"
green_back = "\033[0;42m"
pink_back = "\033[0;41m"
grey_back = "\033[0;40m"
grey = '\033[38;4;236m'
bold = "\033[1m"
underline = "\033[4m"
italic = "\033[3m"
darken = "\033[2m"
invisible='\033[08m'
reverse='\033[07m'
reset='\033[0m'
grey = "\x1b[90m"