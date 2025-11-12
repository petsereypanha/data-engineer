import numpy as np

# Create a list of integers (0-50) using list comprehension
nums_list_comp = [num for num in range(51)]
print(nums_list_comp)

# Create a list of integers (0-50) by unpacking range
nums_unpack = [*range(51)]
print(nums_unpack)

# Create a list using the formal name
formal_list = list(range(51))
print(formal_list)

# Create a list using the literal syntax
literal_list = []
print(literal_list)

# Print out the type of formal_list
print(type(formal_list))

# Print out the type of literal_list
print(type(literal_list))

def convert_units(heroes, heights, weights):

    new_hts = [ht * 0.39370  for ht in heights]
    new_wts = [wt * 2.20462  for wt in weights]

    hero_data = {}

    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data

def convert_units_broadcast(heroes, heights, weights):

    # Array broadcasting instead of list comprehension
    new_hts = heights * 0.39370
    new_wts = weights * 2.20462

    hero_data = {}

    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data

def calc_bmi_lists(sample_indices, hts, wts):

    # Gather sample heights and weights as lists
    s_hts = [hts[i] for i in sample_indices]
    s_wts = [wts[i] for i in sample_indices]

    # Convert heights from cm to m and square with list comprehension
    s_hts_m_sqr = [(ht / 100) ** 2 for ht in s_hts]

    # Calculate BMIs as a list with list comprehension
    bmis = [s_wts[i] / s_hts_m_sqr[i] for i in range(len(sample_indices))]

    return bmis

def calc_bmi_arrays(sample_indices, hts, wts):

    # Gather sample heights and weights as arrays
    s_hts = hts[sample_indices]
    s_wts = wts[sample_indices]

    # Convert heights from cm to m and square with broadcasting
    s_hts_m_sqr = (s_hts / 100) ** 2

    # Calculate BMIs as an array using broadcasting
    bmis = s_wts / s_hts_m_sqr

    return bmis

def get_publisher_heroes(heroes, publishers, desired_publisher):

    desired_heroes = []

    for i,pub in enumerate(publishers):
        if pub == desired_publisher:
            desired_heroes.append(heroes[i])

    return desired_heroes
def get_publisher_heroes_np(heroes, publishers, desired_publisher):

    heroes_np = np.array(heroes)
    pubs_np = np.array(publishers)

    desired_heroes = heroes_np[pubs_np == desired_publisher]

    return desired_heroes

# Sample data
heroes = ['Luke Skywalker', 'Darth Vader', 'Leia Organa', 'Han Solo', 'Yoda']
publishers = ['George Lucas', 'George Lucas', 'George Lucas', 'George Lucas', 'George Lucas']
# Use get_publisher_heroes() to gather Star Wars heroes
star_wars_heroes = get_publisher_heroes(heroes, publishers, 'George Lucas')

print(star_wars_heroes)
print(type(star_wars_heroes))

# Use get_publisher_heroes_np() to gather Star Wars heroes
star_wars_heroes_np = get_publisher_heroes_np(heroes, publishers, 'George Lucas')

print(star_wars_heroes_np)
print(type(star_wars_heroes_np))