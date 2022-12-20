from other_functions import*
# #player class where the player is stored as an object with attributes health, stamina, and name

class Player:
    
    #constructor
    def __init__(self, name, health = 100, stamina = 100, healthPotion = 0, staminaPotion = 0):
        self._name = name
        self._health = health
        self._stamina = stamina
        self._healthPotion = healthPotion
        self._staminaPotion = staminaPotion
        self._weapons = []
        # self.coils = {}

    #getters
    def name(self):
        return self._name

    def health(self):
        return self._health

    def stamina(self):
        return self._stamina

    def healthPotion(self):
        return self._healthPotion

    def staminaPotion(self):
        return self._staminaPotion

    def weapons(self):
        return self._weapons
    # def getCoils(self):
    #     return self.coils

    def __str__(self):
        return(f"\nName: {self._name}\nHealth: {self._health}\nStamina: {self._stamina}\nHealth Potion: {self._healthPotion}\nStamina Potion: {self._staminaPotion}\nWeapons: {self._weapons}")

    #setters for updating player stats and items/inventory
    def newName(self, name):
        self._name = name

    def newHealth(self, healthChange):
        self._health += healthChange

    def newStamina(self, staminaChange):
        self._stamina += staminaChange

    def newHealthPotion(self, potionChange):
        self._healthPotion += potionChange

    def newStaminaPotion(self, potionChange):
        self._staminaPotion += potionChange

    def addWeapons(self, weaponClass, weaponName):
        weaponClass = weaponClass.replace(' ', '')
        self._weapons.append(str_to_class(weaponClass)(weaponName))

    # def addCoil(self, coil):
    #     self.coils.update(coil)
    # def subCoil(self, coil):
    #     self.coils.pop(coil)
