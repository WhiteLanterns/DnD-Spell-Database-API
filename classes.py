# Defines the main class, a character, the data of which will be accessed for the sheet
class Character:
    # Sets the default variables for the class
    def __init__(self, pl_name, ch_name, level, ch_class, hp, ac, equppied_armor):
        self.pl_name = pl_name
        self.ch_name = ch_name
        self.level = level
        self.ch_class = ch_class
        self.hp = hp
        self.ac = ac
        self.equipped_armor = equppied_armor

    # Checks to see if player's character is a caster
    def is_caster(casters, ch_class, has_spells=False):
        casters = [] #List of casters
        if ch_class in casters:
            has_spells = True

# Defines a class, the armors in the game
class Armor(Character.ac, Character.equipped_armor):
    def __init__(self, is_equipped, armors, description):
        self.armors = armors
        self.is_equpped = is_equipped
        self.description = description
    
    def equip_armor(armors, is_equipped, ac):
        armors = {}
        if is_equipped == False:
            is_equipped = True
            for keys in armors:
                ac += armors[keys]
            