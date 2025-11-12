# import Counter from collections
from collections import Counter
import numpy as np
hps = np.array([35, 39, 45, 44, 55, 115, 40, 50])

names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fiona', 'George', 'Hannah']
primary_types = ['Warrior', 'Mage', 'Rogue', 'Cleric', 'Ranger', 'Paladin', 'Bard', 'Druid']
secondary_types = ['Fire', 'Ice', 'Shadow', 'Light', 'Earth', 'Holy', 'Wind', 'Water']
generations = [1, 1, 2, 2, 3, 3, 4, 4]
pokemon = ['Pikachu', 'Charmander', 'Bulbasaur', 'Squirtle', 'Eevee', 'Jigglypuff', 'Meowth', 'Psyduck']
ash_pokedex = ['Pikachu', 'Bulbasaur', 'Charmander', 'Squirtle', 'Eevee']
misty_pokedex = ['Squirtle', 'Psyduck', 'Staryu', 'Togepi', 'Jigglypuff']
brock_pokedex = ['Onix', 'Geodude', 'Zubat', 'Vulpix', 'Machop']
name = ['Pikachu', 'Charmander', 'Bulbasaur', 'Squirtle', 'Eevee', 'Jigglypuff', 'Meowth', 'Psyduck', 'Pikachu']

# Combine names and primary_types
names_type1 = [*zip(names, primary_types)]

print(*names_type1[:5], sep='\n')

# Combine all three lists together
names_types = [*zip(names, primary_types, secondary_types)]

print(*names_types[:5], sep='\n')

# Combine five items from names and three items from primary_types
differing_lengths = [*zip(names[:5], primary_types[:3])]

print(*differing_lengths, sep='\n')

# Collect the count of primary types
type_count = Counter(primary_types)
print(type_count, '\n')

# Collect the count of generations
gen_count = Counter(generations)
print(gen_count, '\n')

# Use list comprehension to get each Pokémon's starting letter
starting_letters = [name[0] for name in names]

# Collect the count of Pokémon for each starting_letter
starting_letters_count = Counter(starting_letters)
print(starting_letters_count)

# Import combinations from itertools
from itertools import combinations

# Create a combination object with pairs of Pokémon
combos_obj = combinations(pokemon, 2)
print(type(combos_obj), '\n')

# Convert combos_obj to a list by unpacking
combos_2 = list(combos_obj)
print(combos_2, '\n')

# Collect all possible combinations of 4 Pokémon directly into a list
combos_4 = list(combinations(pokemon, 4))
print(combos_4)

# Convert both lists to sets
ash_set = set(ash_pokedex)
misty_set = set(misty_pokedex)

# Find the Pokémon that exist in both sets
both = ash_set.intersection(misty_set)
print(both)

# Find the Pokémon that Ash has and Misty does not have
ash_only = ash_set.difference(misty_set)
print(ash_only)

# Find the Pokémon that are in only one set (not both)
unique_to_set = ash_set.symmetric_difference(misty_set)
print(unique_to_set)

# Convert Brock's Pokédex to a set
brock_pokedex_set = set(brock_pokedex)
print(brock_pokedex_set)

# Check if Psyduck is in Ash's list and Brock's set
print('Psyduck' in ash_pokedex)
print('Psyduck' in brock_pokedex_set)

# Check if Machop is in Ash's list and Brock's set
print('Machop' in ash_pokedex)
print('Machop' in brock_pokedex_set)

def find_unique_items(data):
    uniques = []

    for item in data:
        if item not in uniques:
            uniques.append(item)

    return uniques

# Use find_unique_items() to collect unique Pokémon names
uniq_names_func = find_unique_items(names)
print(len(uniq_names_func))

# Convert the names list to a set to collect unique Pokémon names
uniq_names_set = set(names)
print(len(uniq_names_set))

# Check that both unique collections are equivalent
print(sorted(uniq_names_func) == sorted(uniq_names_set))

# Use the best approach to collect unique primary types and generations
uniq_types = set(primary_types)
uniq_gens = set(generations)
print(uniq_types, uniq_gens, sep='\n')

gen1_gen2_name_lengths_loop = []
poke_names = ['Pikachu', 'Charmander', 'Bulbasaur', 'Squirtle', 'Eevee', 'Jigglypuff', 'Meowth', 'Psyduck']
poke_gens = [1, 1, 1, 1, 1, 2, 1, 1]

for name,gen in zip(poke_names, poke_gens):
    if gen < 3:
        name_length = len(name)
        poke_tuple = (name, name_length)
        gen1_gen2_name_lengths_loop.append(poke_tuple)

# Collect Pokémon that belong to generation 1 or generation 2
gen1_gen2_pokemon = [name for name,gen in zip(poke_names, poke_gens) if gen < 3]

# Create a map object that stores the name lengths
name_lengths_map = map(len, gen1_gen2_pokemon)

# Combine gen1_gen2_pokemon and name_lengths_map into a list
gen1_gen2_name_lengths = [*zip(gen1_gen2_pokemon, name_lengths_map)]

print(gen1_gen2_name_lengths_loop[:5])
print(gen1_gen2_name_lengths[:5])

poke_list = []
stats = np.array([[35, 55, 40, 50, 50, 90],
                  [39, 52, 43, 60, 50, 65],
                  [45, 49, 49, 65, 65, 45],
                  [44, 48, 65, 50, 64, 43],
                  [55, 55, 50, 45, 65, 55],
                  [115, 45, 20, 45, 25, 20],
                  [40, 45, 35, 40, 40, 90],
                  [50, 52, 48, 65, 50, 55]])

for pokemon,row in zip(names, stats):
    total_stats = np.sum(row)
    avg_stats = np.mean(row)
    poke_list.append((pokemon, total_stats, avg_stats))

# Create a total stats array
total_stats_np = np.sum(stats, axis=1)

# Create an average stats array
avg_stats_np = np.mean(stats, axis=1)

# Combine names, total_stats_np, and avg_stats_np into a list
poke_list_np = [*zip(names, total_stats_np, avg_stats_np)]

print(poke_list_np == poke_list, '\n')
print(poke_list_np[:3])
print(poke_list[:3], '\n')
top_3 = sorted(poke_list_np, key=lambda x: x[1], reverse=True)[:3]
print('3 strongest Pokémon:\n{}'.format(top_3))

# Collect the count of each generation
gen_counts = Counter(generations)

# Improve for loop by moving one calculation above the loop
total_count = sum(gen_counts.values())

for gen,count in gen_counts.items():
    gen_percent = round(count / total_count * 100, 2)
    print('generation {}: count = {:3} percentage = {}'
          .format(gen, count, gen_percent))
pokemon_types = ['Fire', 'Water', 'Grass', 'Electric', 'Psychic', 'Rock', 'Ground', 'Flying']
# Collect all possible pairs using combinations()
possible_pairs = [*combinations(pokemon_types, 2)]

# Create an empty list called enumerated_tuples
enumerated_tuples = []

for i, pair in enumerate(possible_pairs, 1):
    enumerated_pair_tuple = (i,) + pair
    enumerated_tuples.append(enumerated_pair_tuple)

# Convert all tuples in enumerated_tuples to a list
enumerated_pairs = [*map(list, enumerated_tuples)]
print(enumerated_pairs)

poke_zscores = []

for name,hp in zip(names, hps):
    hp_avg = hps.mean()
    hp_std = hps.std()
    z_score = (hp - hp_avg)/hp_std
    poke_zscores.append((name, hp, z_score))
highest_hp_pokemon = []

for name,hp,zscore in poke_zscores:
    if zscore > 2:
        highest_hp_pokemon.append((name, hp, zscore))

# Calculate the total HP average and total HP standard deviation
hp_avg = np.mean(hps)
hp_std = np.std(hps)

# Use NumPy to eliminate the previous for loop
z_scores = (hps - hp_avg) / hp_std

# Combine names, hps, and z_scores
poke_zscores2 = [*zip(names, hps, z_scores)]
print(*poke_zscores2[:3], sep='\n')

# Use list comprehension with the same logic as the highest_hp_pokemon code block
highest_hp_pokemon2 = [(name, hp, zscore) for name, hp, zscore in poke_zscores2 if zscore > 2]
print(*highest_hp_pokemon2, sep='\n')