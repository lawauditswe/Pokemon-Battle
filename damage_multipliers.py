# Random - damage roll from 85% to 100%

import random
from random import randint
from moves import *
from Move_class import *

#Damage rolls
def random_number():
    rand = (100 - random.randint(0,15))/100
    return rand

# STAB
def stab(attacking_Pokemon,move): 
    if move.typing == attacking_Pokemon.type1 or move.typing == attacking_Pokemon.type2:
        return 6144/4096
    return 1

# Type effectiveness - use dictionaries? a dictionary w/in dictionary
def effectiveness(move,target_Pokemon):
    typing = [target_Pokemon.type1]
    if target_Pokemon.type2 != None:
        typing.append(target_Pokemon.type2)

    effectiveness = 1

    for types in typing:
        if move.typing == 'normal':
            if types == 'ghost':
                effectiveness *= 0
            elif types == 'rock' or types == 'steel':
                effectiveness *= 0.5
        elif move.typing == 'fighting':
            if types == 'ghost':
                effectiveness *= 0
            elif types == 'flying' or types == 'poison' or types == 'bug' or types == 'psychic' or types == 'fairy':
                effectiveness *= 0.5
            elif types == 'normal' or types == 'rock' or types == 'steel' or types == 'ice' or types == 'dark':
                effectiveness *= 2
        elif move.typing == 'flying':
            if types == 'rock' or types == 'steel' or types == 'electric':
                effectiveness *= 0.5
            if types == 'fighting' or types == 'bug' or types == 'grass':
                effectiveness *= 2
        elif move.typing == 'poison':
            if types == 'steel':
                effectiveness *= 0
            elif types == 'poison' or types == 'ground' or types == 'rock' or types == 'ghost':
                effectiveness *= 0.5
            elif types == 'grass' or types == 'fairy':
                effectiveness *= 2
        elif move.typing == 'ground':
            if types == 'flying':
                effectiveness *= 0
            elif types == 'bug' or types == 'grass':
                effectiveness *= 0.5
            elif types == 'poison' or types == 'rock' or types == 'steel' or types == 'fire' or types == 'electric':
                effectiveness *= 2
        elif move.typing == 'rock':
            if types == 'fighting' or types == 'ground' or types == 'steel':
                effectiveness *= 0.5
            elif types == 'flying' or types == 'bug' or types == 'fire' or types == 'ice':
                effectiveness *= 2
        elif move.typing == 'bug':
            if types == 'fighting' or types == 'flying' or types == 'poison' or types == 'ghost' or types == 'steel' or types == 'fire' or types == 'fairy':
                effectiveness *= 0.5
            elif types == 'grass' or types == 'psychic' or types == 'dark':
                effectiveness *= 2
        elif move.typing == 'water':
            if types == 'water' or types == 'grass' or types == 'dragon':
                effectiveness *= 0.5
            elif types == 'ground' or types == 'rock' or types == 'fire':
                effectiveness *= 2
        elif move.typing == 'ghost':
            if types == 'normal':
                effectiveness *= 0
            elif types == 'dark':
                effectiveness *= 0.5
            elif types == 'ghost' or types == 'psychic':
                effectiveness *= 2
        elif move.typing == 'steel':
            if types == 'steel' or types == 'fire' or types == 'water' or types == 'electric':
                effectiveness *= 0.5
            elif types == 'rock' or types == 'ice' or types == 'fairy':
                effectiveness *= 2
        elif move.typing == 'fire':
            if types == 'rock' or types == 'fire' or types == 'water' or types == 'dragon':
                effectiveness *= 0.5
            elif types == 'bug' or types == 'steel' or types == 'grass' or types == 'ice':
                effectiveness *= 2
        elif move.typing == 'grass':
            if types == 'flying' or types == 'poison' or types == 'bug' or types == 'steel' or types == 'fire' or types == 'grass' or types == 'dragon':
                effectiveness *= 0.5
            elif types == 'ground' or types == 'rock' or types == 'water':
                effectiveness *= 2
        elif move.typing == 'electric':
            if types == 'ground':
                effectiveness *= 0
            elif types == 'grass' or types == 'electric' or types == 'dragon':
                effectiveness *= 0.5
            elif types == 'flying' or types == 'water':
                effectiveness *= 2
        elif move.typing == 'psychic':
            if types == 'dark':
                effectiveness *= 0
            elif types == 'steel' or types == 'psychic':
                effectiveness *= 0.5
            elif types == 'fighting' or types == 'poison':
                effectiveness *= 2
        elif move.typing == 'ice':
            if types == 'steel' or types == 'fire' or types == 'water' or types == 'ice':
                effectiveness *= 0.5
            elif types == 'flying' or types == 'ground' or types == 'grass' or types == 'dragon':
                effectiveness *= 2
        elif move.typing == 'dragon':
            if types == 'fairy':
                effectiveness *= 0
            elif types == 'steel':
                effectiveness *= 0.5
            elif types == 'dragon':
                effectiveness *= 2
        elif move.typing == 'dark':
            if types == 'fighting' or types == 'dark' or types == 'fairy':
                effectiveness *= 0.5
            elif types == 'ghost' or types == 'psychic':
                effectiveness *= 2
        elif move.typing == 'fairy':
            if types == 'poison' or types == 'steel' or types == 'fire':
                effectiveness *= 0.5
            elif types == 'fighting' or types == 'dragon' or types == 'dark':
                effectiveness *= 2
    return effectiveness