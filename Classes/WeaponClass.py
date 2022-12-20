from Dictionaries.weapons import weaponsList

class Weapon(object):

    #initializer
    def __init__(self, name, type):
        """
        Initializes the weapon with common attributes across all weapons,
        retrieving them directly from the weapons dictionary (only name, damage, and critical hit)

        Parameter name: name of the weapon and acts as an ID to retrieve other attributes
        Precondition: name is a string

        Parameter type: weapon type that acts as an ID to retrieve attributes from the dictionary
        Precondition: type is a string
        """
        assert name in weaponsList[type], 'INCORRECT weapon name or weapon class'

        self._name = name
        self._damage = weaponsList[type][name]['Damage']
        self._criticalHit = int(weaponsList[type][name]['Critical Hit Chance'][:-1])/100

        # self.coilSlots = coilSlots
        # self.coils = {}

    #getters
    def name(self):
        """
        Returns the name of any weapon
        """
        return self._name

    def damage(self):
        """
        Returns the damage of any weapon
        """
        return self._damage

    #other functions
    def __str__(self):
        """
        Returns a string representation of any weapon
        """

        dictCopy = self.__dict__
        string = ''

        for i in dictCopy.keys():
            string += f'{i} : {dictCopy[i]}\n'

        return string


class Spears(Weapon):

    #initializer
    def __init__(self, name):
        """
        Initializes the spear with its respective attributes retrieving them 
        directly from the weapons dictionary

        Super class is called only to intialize the name, damage, and critical 
        hit chance attributes

        Parameter name: name of the spear and acts as an ID to retrieve other attributes
        Precondition: name is a string
        """
        super().__init__(name, 'Spears')
        self._pwrDamage = weaponsList['Spears'][name]['Power Attack Damage']
        self._staminaCost = weaponsList['Spears'][name]['Power Attack Stamina Cost']


class HunterBows(Weapon):
    
    #initializer
    def __init__(self, name):
        """
        Initializes the hunter bow with its respective attributes retrieving them 
        directly from the weapons dictionary

        Super class is called only to intialize the name, damage, and critical 
        hit chance attributes

        Parameter name: name of the spear and acts as an ID to retrieve other attributes
        Precondition: name is a string
        """
        super().__init__(name, 'Hunter Bows')
        self._maxStack = weaponsList['Hunter Bows'][name]['Max Arrow Stack']
        self._staminaCost = weaponsList['Hunter Bows'][name]['Stacking Stamina Cost']


class Blastslings(Weapon):
    
    #initializer
    def __init__(self, name):
        """
        Initializes the blastsling with its respective attributes retrieving them 
        directly from the weapons dictionary

        Super class is called only to intialize the name, damage, and critical 
        hit chance attributes

        Parameter name: name of the spear and acts as an ID to retrieve other attributes
        Precondition: name is a string
        """
        super().__init__(name, 'Blastslings')


class ShredderGauntlets(Weapon):

    #initializer
    def __init__(self, name):
        """
        Initializes the shredder gauntlet with its respective attributes retrieving them 
        directly from the weapons dictionary

        Super class is called only to intialize the name, damage, and critical 
        hit chance attributes

        Parameter name: name of the spear and acts as an ID to retrieve other attributes
        Precondition: name is a string
        """
        
        super().__init__(name, 'Shredder Gauntlets')
        self._shotsExplos = weaponsList['Shredder Gauntlets'][name]['Shots Before Explosion']
        self._explosDmgMultipler = weaponsList['Shredder Gauntlets'][name]['Explosion Damage Multiplier']
        self._staminaCost = weaponsList['Shredder Gauntlets'][name]['Explosion Stamina Cost']


class SpikeThrowers(Weapon):

    #initializer
    def __init__(self, name):
        """
        Initializes the spike thrower with its respective attributes retrieving them 
        directly from the weapons dictionary

        Super class is called only to intialize the name, damage, and critical 
        hit chance attributes

        Parameter name: name of the spear and acts as an ID to retrieve other attributes
        Precondition: name is a string
        """
        
        super().__init__(name, 'Spike Throwers')
        self._pwrDamage = weaponsList['Spike Throwers'][name]['Explosive Spike Damage']
        self._staminaCost = weaponsList['Spike Throwers'][name]['Explosive Spike Stamina Cost']