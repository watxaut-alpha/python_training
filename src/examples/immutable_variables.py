

# Examples of immutable variables in Python
# ----> Numbers
integer_num = 4
float_num = 4.5
complex_num = 4j


# ----> Strings
string_sentence = "Hey I am immutable"
string_text = """
Las rosas son rojas,
las violetas son azules,
este poema no rima,
puta vida.
"""

print(type(string_sentence) == type(string_text))  # Spoiler, this prints "True"


# Booleans: True or False
condition_a = True
condition_b = 2 < 1
print(condition_a is True)
print(condition_a is False)
print(not True is False and True is not False)


# ----> Weird things
# this type is called tuple and it's immutable also. It's like a list, but it cannot be changed
tuple_numbers = (45, 6j, 7, 8, 9.567, 0, 5, 300_789_431)

try:
    # spoiler: this fails because tuples are not mutable. You cannot change tuples, although
    # you CAN redefine the variable
    tuple_numbers.append(45)
except:
    print("I SAID TUPLES ARE IMMUTABLE!!")




