from random import*
from time import sleep
from Classes.PlayerClass import*
from Classes.WeaponClass import*
from other_functions import*
from Dictionaries.weapons import weaponsList


#logic to prevent player from having more thzan one weapon from a particular weapon class
def weaponRandomization(skip):
    """
    Displays welcome message and picks a random weapon class from the weapons dictionary

    Calls dispWeapons() to display weapons and prompting the player to choose a specific 
    weapon from the weapon class chosen in this function

    Then removes weaponClass from the list weaponsCopy to avoid duplicate 
    weapons from the same class

    Paramater skip: status of whether user wants to see dialogue
    Precondition: skip is a boolean
    """

    if not skip:
        clear()
        typeText(f"\nWelcome {player.name()}, here you will be choosing your 3 weapons of choice", sleep = 1)
        typeText("\n\nChoose carefully because you would not be able to change your loadout until the next round", sleep = .5)
        pCont()
    
    weaponsCopy = weaponsList  
    num = ["first", "second", "third"]
    for i in range (3):
        
        weaponKey = list(weaponsCopy.keys())[randint(0,(len(weaponsList)-1)-i)]
        clear()
        typeText(f"Your {num[i]} weapon class is {weaponKey}\n", sleep = .5)
        dispWeapons(weaponKey)
        weaponsCopy.pop(weaponKey)
        

#UI for weapon choice
def dispWeapons(weaponClass):
    """
    Displays all weapons under 'weaponClass' in the weapon dictionary

    Calls chooseWeapon() to prompt the player to choose a weapon

    Parameter weaponClass: weapon type that acts as an ID to retrieve all weapons under it
    Precondition: weaponClass is a string
    """

    choiceIndex = 0
    for i in (weaponsList[weaponClass].keys()):
        choiceIndex += 1
        print(f"\n{choiceIndex}) {i}")
        for key, value in weaponsList[weaponClass][i].items():
            print(key, ' : ', value)
            # sleep(.015)
        sleep(.4)
    chooseWeapon(weaponClass, choiceIndex)


#logic for choosing weapon
def chooseWeapon(weaponClass, choiceIndex):
    """
    The logic for prompting the player to choose a weapon
    
    After the player makes a choice, the weapon object is added to the 
    player._weapons list attribute

    Parameter weaponClass: weapon type that acts as an ID to retrieve all weapons under it
    Precondition: weaponClass is a string

    Parameter choiceIndex: the number of weapons under weaponClass (aka the max number allowed for the player to select a weapon)
    Precondition:choiceIndex is an int
    """

    while (True):
        input = typeInput("\nTo add a weapon to your loadout, enter its respective index", .015).upper()

        if input == "WEAPONS" or input == "WEAPON":
            clear()
            counter = 0
            for i in (weaponsList[weaponClass].keys()):
                counter += 1
                print(f"\n{counter}) {i}")
                for key, value in weaponsList[weaponClass][i].items():
                    print(key, ' : ', value)
                    # sleep(.015)
                sleep(.5)

        elif input.isdigit() and int(input) >= 1 and int(input) <= choiceIndex:
            weaponName = list(weaponsList[weaponClass].keys())[int(input)-1] # Name of the weapon chosen by player
            player.addWeapons(weaponClass, weaponName) # adds the weapon object to the player's inventory
            break # ends the while loop
        else:
            clear()
            typeText(f"Something doesn\'t look right! Check if you entered a number between 1 and {choiceIndex}", .015)
            typeText("\n\nEnter 'weapons' to view weapon options", .015)


#UI for potion quantity choice
def potions(skip):
    """
    Displays a congratulations message and instructions on how the potion system works

    Contains the logic for setting a random number of potion slots and setting
    the number of health and stamina potions for the player object based on player input

    Paramater skip: status of whether user wants to see dialogue
    Precondition: skip is a boolean
    """

    if not skip:
        clear()
        typeText(f"{player.name()}, congratulations on successfully selecting your weapons, but now it is time for potions!", sleep = .5)
        typeText("\n\nThere are two types of potions: health and stamina", sleep = 1)
        typeText("\n\nHealth is going to denote player health and will deplete if you fail to escape machine attacks", sleep = .5)
        typeText("\nStamina will be used for dodging machine attacks and for using special attacks on weapons", sleep = 1)
        typeText("\n\nHealth potions will increase your health whereas stamina potions are going to increase your stamina\nby a random amount ranging from 40 to 80", sleep = .5)
        pCont()

    clear()
    potionSlots = randint(3,6)
    typeText(f"You are given {potionSlots} potion slots, and you can choose the quantity of each potion you will take to battle", sleep = .5)
    input = typeInput("\n\nHow many health potions would you like? The rest of the slots will be filled up with stamina potions")

    while (True):

        if (input.isdigit() and int(input) <= potionSlots):
            player.newHealthPotion(int(input)) #updates the player object's healthPotion quantity
            player.newStaminaPotion(potionSlots - int(input)) #updates the player object's staminaPotion quantity

            typeText(f"\n{player.healthPotion()} health potion(s) and {player.staminaPotion()} stamina potion(s) have been added to your inventory!", sleep = .5)
            break

        else:
            clear()
            typeText(f"Something doesn\'t look right! Check if you typed in a number between 0 and {potionSlots}", .015)
            input = typeInput("\n\nHow many health potions would you like? The rest of slots will be filled up with stamina potions", .015)



clear()
player = Player("", 100, 100) #name, health, stamina
skip = intro() #status for instructions/story shown or not
player.newName(typeInput("What is your name?").title())
weaponRandomization(skip)
potions(skip)