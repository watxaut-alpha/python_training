# Now here is where all the Python fun and mindf*cking comes into play
# There is 3.5 types of mutable variables: lists, dictionaries and sets. Class instances are also mutable, but
# everything in python is a class so..


# ------------> LISTS
# ----------------------------
list_numbers = [12, 33, 44, 55]

# lists of list are also possible! You can create matrix for example
jacobean_matrix = [
    [3, 4, 5],
    [1, 0, 4],
    [0, 3, 1]
]

# to add things to lists (remember, mutable means mutable)
list_numbers.append(66)
print(list_numbers)

# to retrieve an item
print(list_numbers[3])  # prints '55'

# you can also make slices of the list
print(list_numbers[1:3])  # prints [33, 44]. First index inclusive, last exclusive!


# ---------> DICTIONARIES, probably my favourite variable in python
# ----------------------------
# dictionaries are like an UNORDERED list of key:value pairs
d_got_alive = {"juan de las nieves": True, "Tyrion Lannister": True, "Ned Stark": False}

# to retrieve an item, like lists but by the KEY
print(d_got_alive["Ned Stark"])

# example with for loop
for key in d_got_alive.keys():  # the method .keys() returns a list of the keys in the dictionary. OJU! Might not be ordered!
    s_character = key
    is_alive = d_got_alive[key]
    print("Is {character} alive? {is_alive}".format(character=s_character, is_alive=is_alive))

# to add elements ->
d_got_alive["Tommy Lannister spoiler?"] = False

# if the key already exists, you OVERWRITE the value. Also, the type of the keys and the values might change
d_got_alive["Tyrion Lannister"] = "Maybe, who knows jejejejeje"


# -----> Sets, the bullied variable of Python
# ----------------------------
# nobody uses sets, but I will explain them anyway.
# Sets are unordered lists of UNIQUE ITEMS, like dictionaries but without values, only keys.
set_numbers = {5, 3, 6, 7, 7, 7, 7}
print(set_numbers)

# they are useful when you need to know which items are in one set and not in the other
set_numbers_2 = {1, 2, 3, 4, 5}

print(set_numbers_2.intersection(set_numbers))  # the intersection will print another set = {3, 5}
