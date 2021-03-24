# Pokemon class

from Move_class import *
from moves import *

class Pokemon:
    def __init__(self, name, nature, ability, type1, move1, base_hp, base_atk, base_def, base_spa, 
        base_spd, base_spe, hp_evs = 0, atk_evs = 0, def_evs = 0, spa_evs = 0, spd_evs = 0, 
        spe_evs = 0, hp_ivs = 31, atk_ivs = 31, def_ivs = 31, spa_ivs = 31, spd_ivs = 31, spe_ivs = 31, 
        gender = "Male", level = 100, type2 = None, move2 = None, move3 = None, move4 = None, status_condition = None):
        self.name = name
        self.nature = nature
        self.ability = ability
        self.type1 = type1
        self.gender = gender
        self.level = level
        self.type2 = type2
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4
        self.hp_ivs = hp_ivs
        self.atk_ivs = atk_ivs
        self.def_ivs = def_ivs
        self.spa_ivs = spa_ivs
        self.spd_ivs = spd_ivs
        self.spe_ivs = spe_ivs
        self.hp_evs = hp_evs
        self.atk_evs = atk_evs
        self.def_evs = def_evs
        self.spa_evs = spa_evs
        self.spd_evs = spd_evs
        self.spe_evs = spe_evs
        self.base_hp = base_hp
        self.base_atk = base_atk
        self.base_def = base_def
        self.base_spa = base_spa
        self.base_spd = base_spd
        self.base_spe = base_spe
        self.status_condition = status_condition
        self.hp_stat = 110 + 2 * self.base_hp + self.hp_ivs + self.hp_evs // 4 
        self.atk_stat = 2 * self.base_atk + 5 + self.atk_ivs + self.atk_evs // 4 
        self.def_stat = 2 * self.base_def + 5 + self.def_ivs + self.def_evs // 4
        self.spa_stat = 2 * self.base_spa + 5 + self.spa_ivs + self.spa_evs // 4
        self.spd_stat = 2 * self.base_spd + 5 + self.spd_ivs + self.spd_evs // 4
        self.spe_stat = 2 * self.base_spe + 5 + self.spe_ivs + self.spe_evs // 4
        self.moveset = [self.move1,self.move2,self.move3,self.move4]

# Natures
        if nature == 'lonely':
            self.atk_stat = int(self.atk_stat * 1.1)
            self.def_stat = int(self.def_stat * 0.9)
        elif nature == 'brave':
            self.atk_stat = int(self.atk_stat * 1.1)
            self.spe_stat = int(self.spe_stat * 0.9)
        elif nature == 'adamant':
            self.atk_stat = int(self.atk_stat * 1.1)
            self.spa_stat = int(self.spa_stat * 0.9)
        elif nature == 'naughty':
            self.atk_stat = int(self.atk_stat * 1.1)
            self.spd_stat = int(self.spd_stat * 0.9)
        elif nature == 'bold':
            self.def_stat = int(self.def_stat * 1.1)
            self.atk_stat = int(self.atk_stat * 0.9)
        elif nature == 'relaxed':
            self.def_stat = int(self.def_stat * 1.1)
            self.spe_stat = int(self.spe_stat * 0.9)
        elif nature == 'impish':
            self.def_stat = int(self.def_stat * 1.1)
            self.spa_stat = int(self.spa_stat * 0.9)
        elif nature == 'lax':
            self.def_stat = int(self.def_stat * 1.1)
            self.spd_stat = int(self.spd_stat * 0.9)
        elif nature == 'timid':
            self.spe_stat = int(self.spe_stat * 1.1)
            self.atk_stat = int(self.atk_stat * 0.9)
        elif nature == 'hasty':
            self.spe_stat = int(self.spe_stat * 1.1)
            self.def_stat = int(self.def_stat * 0.9)
        elif nature == 'jolly':
            self.spe_stat = int(self.spe_stat * 1.1)
            self.spa_stat = int(self.spa_stat * 0.9)
        elif nature == 'naive':
            self.spe_stat = int(self.spe_stat * 1.1)
            self.spd_stat = int(self.spd_stat * 0.9)
        elif nature == 'modest':
            self.spa_stat = int(self.spa_stat * 1.1)
            self.atk_stat = int(self.atk_stat * 0.9)
        elif nature == 'mild':
            self.spa_stat = int(self.spa_stat * 1.1)
            self.def_stat = int(self.def_stat * 0.9)
        elif nature == 'quiet':
            self.spa_stat = int(self.spa_stat * 1.1)
            self.spe_stat = int(self.spe_stat * 0.9)
        elif nature == 'rash':
            self.spa_stat = int(self.spa_stat * 1.1)
            self.spd_stat = int(self.spd_stat * 0.9)
        elif nature == 'calm':
            self.spd_stat = int(self.spd_stat * 1.1)
            self.atk_stat = int(self.atk_stat * 0.9)
        elif nature == 'gentle':
            self.spd_stat = int(self.spd_stat * 1.1)
            self.def_stat = int(self.def_stat * 0.9)
        elif nature == 'sassy':
            self.spd_stat = int(self.spd_stat * 1.1)
            self.spe_stat = int(self.spe_stat * 0.9)
        elif nature == 'careful':
            self.spd_stat = int(self.spd_stat * 1.1)
            self.spa_stat = int(self.spa_stat * 0.9)
