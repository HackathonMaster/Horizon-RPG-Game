from Dictionaries.weapons import weaponsList

class Weapon(object):
    """
    A class to represent all weapons
    """
    # Attribute _name: weapon's name
    # Invariant: _name is a string

    # Attribute _damage: weapon's damage
    # Invariant: _damage is an int

    # Attribute _criticalHeat: weapon's critical hit chance (converted from percent to decimal)
    # Invariant: _criticalHit is a float

    #INITIALIZER
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

    #GETTERS
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

    #OTHER FUNCTIONS
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
    """
    A class to represent all spears
    """
    # Attribute _pwrDamage: spear's power attack damage
    # Invariant: _pwrDamage in an int

    # Attribute _staminaCost: spear's power attack stamina cost
    # Invariant: _staminaCost is an int

    #INITIALIZER
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
    """
    A class to represent all hunter bows
    """
    # Attribute _maxStack: max # of arrows allowed for stacking
    # Invariant: _maxStack is an int

    # Attribute _staminaCost: bow's stamina cost for each arrow stacked
    # Invariant: _staminaCost is an int
    
    #INITIALIZER
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
    """
    A class to represent all blastslings
    """

    #INITIALIZER
    def __init__(self, name):
        """
        Initializes the blastsling with its respective attributes retrieving them 
        directly from the weapons dictionary

        Super class is only called to intialize the name, damage, and critical 
        hit chance attributes

        Parameter name: name of the spear and acts as an ID to retrieve other attributes
        Precondition: name is a string
        """
        super().__init__(name, 'Blastslings')


class ShredderGauntlets(Weapon):
    """
    A class to represent all shredder gauntlets
    """
    # Attribute _shotsExplos: number of shots required before explosion
    # Invariant: _shotsExplos is an int

    # Attribute _explosDamage: shredder gauntlet's explosion shot damage 
    # Invariant: _explosDamage is a float

    #INITIALIZER
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
        self._explosDamage = self._damage * weaponsList['Shredder Gauntlets'][name]['Explosion Damage Multiplier']


class SpikeThrowers(Weapon):
    """
    A class to represent all spike throwers
    """
    # Attribute _pwrDamage: spike thrower's explosive attack damage
    # Invariant: _pwrDamage in an int

    # Attribute _staminaCost: spike thrower's explosive spike stamina cost
    # Invariant: _staminaCost is an int

    #INITIALIZER
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