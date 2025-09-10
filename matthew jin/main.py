from pokemon.pokemon import Pokemon
import pokemon.electric as electric
from move import Move
from trainer import Trainer
from battle import Battle
import move_data
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

    pokemon_weaknesses = type_chart.get(pokemon_type.lower())
    if pokemon_weaknesses is None:
        return 1
    return pokemon_weaknesses.get(move_type.lower(), 1)


electric_names = [
    "Raichu", "Pichu", "Rotom-Wash", "Shinx (Shiny)", "Electabuzz", "Pawmot",
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
normal_names = [    "Meowth", "Ursaluna", "Staravia", "Komala(Shiny)", "Lechonk", "Braviary",
    "Unfezant", "Maushold", "Dundunsparce", "Regigigas", "Persian"
]
fire_names = [
    "Charizard", "Arcinine", "Talonflame", "Moltres", "Salandit(Shiny)",
    "Scovillain", "Magmar", "Slugma", "Coalossal", "Camerupt", "Blaziken",
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
    "Gengar", "Ghastly", "Haunter(Shiny)", "Misdrevus", "Mismagius",
    "Annilape", "Drifblim", "Driffloon", "Greveard", "Houndstone", "Shuppet",
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

pokemon_one: Pokemon = electric.Raichu(78)

pokemon_two: Pokemon = Pokemon(grass_names[grass_index],
                               "grass",
                               70,
                               random.randint(139, 199),
                               speed=60)

electric_moves = [move_data.Thunder, move_data.ThunderBolt, move_data.Discharge, move_data.Nuzzle]
psychic_moves = [move_data.Psychic, move_data.Psyshock, move_data.PsychoCut, move_data.HeartStamp]

pokemon_one.learn(electric_moves[random.randint(0, len(electric_moves) - 1)])
pokemon_two.learn(psychic_moves[random.randint(0, len(psychic_moves) - 1)])

party1: list[Pokemon] = [pokemon_one, pokemon_two]

ash: Trainer = Trainer(party1, "Ash")

pokemon_three: Pokemon = Pokemon(grass_names[grass_index],
                                 "grass",
                                 65,
                                 random.randint(139, 199),
                                 speed=50)
party2: list[Pokemon] = [pokemon_three]

bob: Trainer = Trainer(party2, "Bob")

battle: Battle = Battle(ash, bob)
battle.start()
