from other_functions import str_to_class
from other_functions import typeInput
from other_functions import clear

class Player:
    """
    A class to represent the player (you)

    The __init__ method initializes the player object with player's name and 
    with a default health and stamina value of 100
    """
    # Attribute _name: player's name
    # Invariant: _name is a string

    # Attribute _health: player's health
    # Invariant: _health is an int

    # Attribute _stamina: player's stamina
    # Invariant: _stamina is an int

    # Attribute _healthPotion: # of health potions in player's inventory
    # Invariant: _healthPotions is a string

    # Attribute _staminaPotions: # of stamina potions in player's inventory
    # Invariant: _staminaPotions is a string

    # Attribute _weapons: weapons thst are in player's inventory
    # Invariant: _weapons is a list of weapon objects

    #INITIALIZER
    def __init__(self, name, health = 100, stamina = 100):
        """
        Initializes the player with its attributes

        Parameter name: name of the player
        Precondition: name is a string

        Parameter health: starting health of the player (default 100)
        Precondition: health is an int

        Parameter stamina: starting stamina of the player (default 100)
        Precondition: stamina is an int
        """

        self._name = name
        self._health = health
        self._stamina = stamina
        self._healthPotion = 0
        self._staminaPotion = 0
        self._weapons = []
        # self.coils = {}

    #GETTERS
    def name(self):
        """
        Returns player's current name
        """
        return self._name

    def health(self):
        """
        Returns player's current health
        """
        return self._health

    def stamina(self):
        """
        Returns player's current stamina
        """
        return self._stamina

    def healthPotion(self):
        """
        Returns player's current amount of health potions
        """
        return self._healthPotion

    def staminaPotion(self):
        """
        Returns player's current amount of stamina potions
        """
        return self._staminaPotion

    def weapons(self):
        """
        Returns player's current weapons
        """
        return self._weapons
        
    # def getCoils(self):
    #     return self.coils

    def __str__(self):
        """
        Returns a string representation of player stats
        """
        return(f"\nName: {self._name}\nHealth: {self._health}\nStamina: {self._stamina}\nHealth Potion: {self._healthPotion}\nStamina Potion: {self._staminaPotion}\nWeapons: {self._weapons}")

    #SETTERS
    def newName(self, name):
        """
        Checks if name is blank. 
        If it is not blank, sets a new player name

        Parameter name: new name of the player
        Precondition: name is a string
        """
        while len(name.strip()) < 1:
            clear()
            name = typeInput("Your name cannot be blank so please try again\n\nWhat is your name?").title()
        self._name = name

    def newHealth(self, healthChange):
        """
        Updates player's health by healthChange

        Parameter healthChange: value by which player's health is changed (+ or -)
        Precondition: healthChange is an int
        """
        self._health += healthChange

    def newStamina(self, staminaChange):
        """
        Updates player's stamina by staminaChange

        Parameter staminaChange: value by which player's stamina is changed (+ or -)
        Precondition: staminaChange is an int
        """
        self._stamina += staminaChange

    def newHealthPotion(self, potionChange):
        """
        Updates player's amount of health potions by potionChange

        Parameter potionChange: value by which player's amount of health potions is changed (+ or -)
        Precondition: potionChange is an int
        """
        self._healthPotion += potionChange

    def newStaminaPotion(self, potionChange):
        """
        Updates player's amount of stamina potions by potionChange

        Parameter potionChange: value by which player's amount of stamina potions is changed (+ or -)
        Precondition: potionChange is an int
        """
        self._staminaPotion += potionChange

    def addWeapons(self, weaponClass, weaponName):
        """
        Adds a weapon object to player's weapon inventory

        Calls str_to_class() to convert the weaponClass string (removing spaces)
        to a class call. These weapon classes are located in 'WeaponClass.py'

        Parameter weaponClass: name of the weapon class
        Precondition: weaponClass is a string

        Parameter weaponName: name of the weapon
        Precondition: weaponName is a string
        """
        weaponClass = weaponClass.replace(' ', '')
        self._weapons.append(str_to_class(weaponClass)(weaponName))

    # def addCoil(self, coil):
    #     self.coils.update(coil)
    # def subCoil(self, coil):
    #     self.coils.pop(coil)