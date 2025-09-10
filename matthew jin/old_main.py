from pokemon.pokemon import Pokemon
import pokemon.electric as electric
from move import Move
from trainer import Trainer
from battle import Battle
import move_data as md
import random
from collections import defaultdict


def get_multiplier(move_type, pokemon_type):
    type_chart = {
        "normal": {
            "fighting": 2,
            "ghost": 0
        },
        "fire": {
            "grass": 0.5,
            "fire": 0.5,
            "water": 2,
            "steel": 0.5,
            "rock": 2,
            "ground": 2,
            "ice": 0.5,
            "bug": 0.5,
            "fairy": 0.5
        },
        "water": {
            "fire": 0.5,
            "water": 0.5,
            "grass": 2,
            "ice": 0.5,
            "steel": 0.5,
            "electric": 2,
        },
        "electric": {
            "electric": 0.5,
            "ground": 2,
            "flying": 0.5,
            "steel": 0.5,
        },
        "grass": {
            "fire": 2,
            "water": 0.5,
            "grass": 0.5,
            "electric": 0.5,
            "ice": 2,
            "poison": 2,
            "ground": 0.5,
            "flying": 2,
            "bug": 2,
        },
        "ice": {
            "fire": 2,
            "ice": 0.5,
            "fighting": 2,
            "steel": 2,
            "rock": 2,
        },
        "fighting": {
            "flying": 2,
            "psychic": 2,
            "bug": 0.5,
            "rock": 0.5,
            "fairy": 2,
        },
        "poison": {
            "ground": 2,
            "psychic": 2,
            "poison": 0.5,
            "fighting": 0.5,
            "grass": 0.5,
            "bug": 0.5,
            "fairy": 0.5,
        },
        "ground": {
            "fire": 0.5,
            "water": 2,
            "electric": 0,
            "grass": 2,
            "ice": 2,
            "poison": 0.5,
            "flying": 0.5,
            "bug": 0.5,
            "rock": 0.5,
            "steel": 0.5,
        },
        "flying": {
            "electric": 2,
            "grass": 0.5,
            "fighting": 0.5,
            "bug": 0.5,
            "rock": 2,
        },
        "psychic": {
            "fighting": 0.5,
            "poison": 0.5,
            "psychic": 0.5,
            "bug": 2,
            "ghost": 2,
            "dark": 2,
        },
        "bug": {
            "fire": 2,
            "grass": 0.5,
            "flying": 2,
            "psychic": 0.5,
            "dark": 0.5,
        },
        "rock": {
            "fire": 0.5,
            "water": 2,
            "grass": 2,
            "ice": 0.5,
            "fighting": 2,
            "flying": 0.5,
            "bug": 0.5
        },
        "ghost": {
            "normal": 0,
            "psychic": 0.5,
            "ghost": 2,
            "dark": 2,
        },
        "dragon": {
            "fire": 0.5,
            "water": 0.5,
            "electric": 0.5,
            "grass": 0.5,
            "ice": 2,
            "dragon": 2,
            "fairy": 2,
        },
        "dark": {
            "fighting": 2,
            "psychic": 0,
            "bug": 2,
            "ghost": 0.5,
            "dark": 0.5,
            "fairy": 2,
        },
        "steel": {
            "fire": 2,
            "ice": 0.5,
            "fighting": 2,
            "ground": 2,
            "flying": 0.5,
            "rock": 0.5,
            "steel": 0.5,
            "fairy": 0.5,
        },
        "fairy": {
            "fighting": 0.5,
            "poison": 2,
            "dragon": 0,
            "dark": 0.5,
            "steel": 2,
        },
    }

    return type_chart.get(pokemon_type.lower()).get(move_type.lower(), 1)


electric_names = [
    "Raichu", "Pichu", "Rotom-Wash", "Shinx (Shiny)", "Electrabuzz", "Pawmot",
    "Pikachu", "Ampharos", "Luxray", "Magnemite", "Galvantula", "Miriadon"
]
psychic_names = [
    "Azelf", "Mespirit", "Uxie", "Espeon (Shiny)", "Alakazam", "Mewtwo",
    "Calyrex (Ice Rider)", "Malamar", "Gallade", "Metagross", "Wobbuffet",
    "Slowking"
]
grass_names = [
    "Leafeon", "Sceptile", "Meowscarada", "Celelbi", "Torterra",
    "Snivy(Shiny)", "Seedot", "Vileplume", "Gogoat", "Dhelmise", "Arbolivia",
    "Jumpluff"
]
normal_names = [
    "Meowth", "Ursaluna", "Staravia", "Komala(Shiny)", "Lechonk", "Braviary",
    "Unfezant", "Maushold", "Dundunsparce", "Regigigas", "Persian"
]
fire_names = [
    "Charizard", "Arcinine", "Talonflame", "Moltres", "Salandit(Shiny)",
    "Scovillan", "Magmar", "Slugma", "Coalossal", "Camerupt", "Blaziken",
    "Centiskorch"
]
water_names = [
    "Buizel(Shiny)", "Psyduck", "Malamar", "Starmie", "Lapras", "Quaquaval",
    "Gyarados", "Greninja", "Ducklett", "Dewgong", "Veluza", "Palkia"
]
ice_names = [
    "Cetitan", "Weavile", "Beartic", "Frosmoth", "Froslass(Shiny)",
    "Abombasnow", "Articuno", "Delibird", "Baxcalibur", "Snover", "Snom",
    "Cetoddle"
]
fighting_names = [
    "Machamp", "Hitmonchan", "Hawlucha", "Lucario", "Mienshao", "Mankey",
    "Sawk(Shiny)", "Passmissian", "Zamazenta", "Breloom", "Poliwrath", "Throh"
]
poison_names = [
    "Arbok", "Toxtricty", "Grafrafri", "Weezing", "Victreebell(Shiny)",
    "Skuntank", "Revaroom", "Drapoin", "Draglage", "Galarian Slowbro",
    "Pechraunt", "Toxapex"
]
ground_names = [
    "Hippowadon", "Donphan", "Sandaconda", "Gliscor(Shiny)", "Groudon",
    "Dugtrio", "Golem", "Whiscash", "Mudsdale", "Krookodile", "Garchomp",
    "Diggersby"
]
flying_names = [
    "Pidgeot", "Ho-Oh", "Swoobat(Shiny)", "Oricorio(Pom-Pom Style)",
    "Pelliper", "Tropius", "Sawana", "Staraptor", "Noivern", "Skamory",
    "Noctowl", "Vullaby"
]
bug_names = [
    "Venomoth(Shiny)", "Vivion", "Masqurin", "Volcarona", "Spidops",
    "Cutiefly", "Kriketot", "Frosmoth", "Scatterbug", "Larvesta", "Tarontula",
    "Kriketune"
]
rock_names = [
    "Geodude", "Graveler", "Onix", "Rockruff", "Lycanroc(Dusk Form)", "Klawf",
    "Terrakion", "Nosepass", "Probopass", "Cranidos(Shiny)", "Ramprados",
    "Binacle"
]
ghost_names = [
    "Gengar", "Ghastly", "Haunter(Shiny)", "Misdrevaus", "Misagius",
    "Annilape", "Drifblim", "Drifbloon", "Greveard", "Houndstone", "Shuppet",
    "Banette"
]
dragon_names = [
    "Dratini", "Dragonair", "Dragonite", "Bagon(Shiny)", "Shelgon",
    "Salamence", "Dreepy", "Draloark", "Dragapult", "Axew", "Fraxure",
    "Haxorus"
]
dark_names = [
    "Mandibuzz", "Umbreon(Shiny)", "Caravana", "Sharpedo", "Sableye",
    "Murkrow", "Honchkrow", "Tyranitar", "Houndour", "Houndoom", "Nuzleaf",
    "Shrifty"
]
steel_names = [
    "Steelix(Shiny)", "Hondedge", "Doublade", "Aegislash", "Ferroseed",
    "Ferrothorn", "Zacian", "Cufant", "Copperajah", "Orthworm", "Beldum",
    "Metang"
]
fairy_names = [
    "Rimonbee", "Whimsicott", "Azumarill", "Daschbun", "Iggilybuff",
    "Jiggilypuff", "Wiggilytuff(Shiny)", "Fidough", "Impidimp", "Morgrem",
    "Grimmsnarl", "Mr. Mime"
]
electric_index = random.randint(0, len(electric_names) - 1)
psychic_index = random.randint(0, len(psychic_names) - 1)
grass_index = random.randint(0, len(grass_names) - 1)
'''
pokemon_one = Pokemon(electric_names[electric_index], "electric", 61,
                      random.randint(139, 199))
'''
pokemon_one = electric.Raichu(78)

pokemon_two = Pokemon(grass_names[grass_index],
                      "grass",
                      70,
                      random.randint(139, 199),
                      speed=60)

electric_moves = [md.Thunder, md.ThunderBolt, md.Discharge, md.Nuzzle]
psychic_moves = [md.Psychic, md.Psyshock, md.PsychoCut, md.HeartStamp]

pokemon_one.learn(electric_moves[random.randint(0, len(electric_moves) - 1)])
pokemon_two.learn(psychic_moves[random.randint(0, len(psychic_moves) - 1)])

party1 = [pokemon_one, pokemon_two]

#=========================
pokemon_three = Pokemon(grass_names[grass_index],
                        "grass",
                        65,
                        random.randint(139, 199),
                        speed=50)
party2 = [pokemon_three]
ash = Trainer(party1, "Ash")
bob = Trainer(party2, "Bob")

battle = Battle(ash, bob)

# # Using print, and ash/bob variables, print out the things below

# # Pikachu
# print(ash.party[0].name)

# # ash's first pokemon's type
# print(ash.party[0].type)
# # 154 (Pikachu's HP)
# print(ash.party[0].HP)
# # Volt Tackle
# print(ash.party[0].moves[0].name)

# # 120 (Volt tackle's Damage)

# # Meowstic

# # Psychic (Meowstic's Type)

# # 167 (Meowstic's HP)

# # Psyshock
# print(bob.party[0].moves[0].name)

# # 80 (Psyshock's Damage)
# print(bob.party[0].moves[0].damage)

# print(f"{pokemon_two.name}'s Moves:")

# # Psyshock , Damage: 80 , Accuracy : 100 , Type: Psychic

battle.pokemon2 = bob.party[0]

#print the pokemon send out by bob using variables
#should say "<trainer name> sent out <pokemon name>"

print(f"{battle.trainer2.name} sent out {battle.pokemon2.name}")

while (True):

    if (battle.pokemon2 and battle.pokemon2.HP <= 0):
        # find which pokemon to bring out
        other_pokemon = [poke for poke in battle.trainer2.party if poke.HP > 0]
        if len(other_pokemon) == 0:
            print("You won!")
            quit()
        else:
            # select a random pokemon from the other pokemon
            r = random.randint(0, len(other_pokemon) - 1)
            battle.pokemon2 = other_pokemon[r]
            print(f"{battle.trainer2.name} sent out {battle.pokemon2.name}")
    #intro
    print("Your Pokemon are:")
    for slot, pokemon in enumerate(ash.party):
        print(f"{slot+1}. {pokemon.name}")

    while battle.pokemon1 is None:
        # pick pokemon to send out
        print("")
        user_input = int(input("Choose which Pokemon to send out: "))
        print("")
        valid = user_input > 0 and user_input <= len(ash.party)
        if user_input > len(ash.party):
            print("Try Again")
            continue

        battle.pokemon1 = ash.party[user_input - 1]

    # puts out pokemon

    print(f'{battle.pokemon1.name}  VS  {battle.pokemon2.name}')

    # <pokemon1's name> VS <pokemon2's name>

    for slot, move in enumerate(battle.pokemon1.moves):
        print(
            f"{slot + 1}. {move.name} , Damage: {move.damage} , Accuracy: {move.accuracy} , Type: {move.type}"
        )

    while True:
        move_choice = int(input("Select a move: "))
        print("")
        valid = move_choice > 0 and move_choice <= len(ash.party)
        if move_choice > len(ash.party):
            print("Try Again")
            continue
        else:
            break

    move = battle.pokemon1.moves[move_choice - 1]
    print("You selected", move.name)

    victim = battle.pokemon2
    attacker = battle.pokemon1
    print("")

    STAB = 1

    if move.type == attacker.type:
        STAB = 1.5

    multiplier = get_multiplier(move.type, victim.type)
    move_damage = move.damage * STAB * multiplier

    print(move.type)
    print(victim.type)
    print(multiplier * STAB)

    #if multiplier == 0
    # print out "it doesn't affect {victim.name}"
    #if multiplier < 1
    # "it's not very effective"
    #if multiplier >= 2
    # it's super effective
    if multiplier == 0:
        print(f"It dosent affect {victim.name}...")
    elif multiplier < 1:
        print("It's not very effective...")
    elif multiplier >= 2:
        print("It's super effective!")
    victim.HP -= move_damage
    if victim.HP < 0:
        victim.HP = 0

    #If the victim pokemon has less than or equal to 0 HP, print "<pokemon name> fainted!"
    print(
        f"{victim.name} took {move_damage} damage. {victim.name} now has {victim.HP} HP left."
    )

    if victim.HP <= 0:
        print(f"{victim.name} fainted!")
    print("")
