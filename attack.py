from Pokemon_class import *
from damage_multipliers import *
from accuracy import *
from critical_hit import *
from damage_multipliers import *
from accuracy import *
from pokemon import *

def attack(attacking_Pokemon,target_Pokemon,move):
    level = attacking_Pokemon.level
    power = move.power
    if move.category == 'physical':
        A = attacking_Pokemon.atk_stat
        D = target_Pokemon.def_stat
    elif move.category == 'special':
        A = attacking_Pokemon.spa_stat
        D = target_Pokemon.spd_stat

    damage = int(int(int(2. * level / 5. + 2.) * power * A / D) / 50.) + 2. # base damage
    crit_damage = int(damage * critical_hit())
    if crit_damage != damage:
        print('A critical hit!\n')
    damage = int(crit_damage * random_number()) # random factor modifier i.e. the 'roll' # in damage_multipliers.py
    damage = int(damage * stab(attacking_Pokemon,move)) # STAB, in damage_multipliers.py

    if damage == 0:
        damage = 1

    damage = int(damage * effectiveness(move,target_Pokemon)) # type effectiveness, in damage_multipliers.py

    return damage