import json
import os

os.chdir("day_two")


with open("pokemon.json") as pokemon_file:
    pokemon_list = json.load(pokemon_file)["results"]

# print(pokemon[0])

normal_type_pokemon = [
    pokemon for pokemon in pokemon_list if "Normal" in pokemon["type"]
]

with open("pokemon.json", "w") as pokemon_file:
    json.dump(normal_type_pokemon, pokemon_file)
