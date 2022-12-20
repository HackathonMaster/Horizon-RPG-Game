import time, os, sys
from time import sleep
from Classes.WeaponClass import* #only for str_to_class function


#printing text imitating typing
def typeText(text, typeSpeed = .04):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(typeSpeed)

def typeInput(text, typeSpeed = .04):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(typeSpeed)
  value = input()  
  return value 

#clear terminal
def clear():
  if os.name == 'nt':
    os.system("cls")
  else:
    os.system("clear")
  # print('\033[2J\033[H')

def pCont():
  input(yellow + "\n\nPress enter to continue" + reset)

def str_to_class(str):
  return getattr(sys.modules[__name__], str)

def intro():
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
  clear()
  typeText("You got kidnapped by the Carja tribe and you are now stuck in the Sun Ring")
  sleep(.5)
  typeText("\nYour only way to escape is to fight the machines in the arena until you prove yourself to be a worthy warrior")
  sleep(1)
  typeText("\n\nTo win your freedom back, you must win every machine trial in the arena and please Helis enough to let you go")
  sleep(.5)
  pCont()
  clear()
  typeText("You will have to fight 5 machines, one each round with varrying difficulties")
  sleep(1)
  typeText("\n\nYou will be randomly assigned 3 weapon classes and you will have the choice to pick one weapon from each class")
  sleep(1)
  typeText("\n\nGood Luck and Happy Hunting!!!")
  sleep(.5)
  pCont()
  clear()



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