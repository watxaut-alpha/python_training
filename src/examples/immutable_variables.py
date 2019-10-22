# Examples of immutable variables in Python
# ----> Numbers
integer_num = 4
float_num = 4.5
complex_num = 4j


# ----> Strings
string_sentence = "Hey I am immutable"
string_with_simple_quotes = 'I am immutable and I am still a string'
string_text = """
Roses are red,
violets are blue,
this is also a string,
fantastic.
"""

print(type(string_sentence) == type(string_text) == type(string_with_simple_quotes))  # Spoiler, this prints "True"


# Booleans: True or False
condition_a = True
condition_b = 2 < 1
print(condition_a is True)
print(condition_a is False)
print(not True is False and True is not False)  # ((!True == False) and (True == !False)) = True


# ----> Weird things
# this type is called tuple and it's immutable also. It's like a list, but it cannot be changed once is declared
tuple_numbers = (45, 6j, 7, 8, 9.567, 0, 5, 300_789_431)

try:
    # spoiler: this fails because tuples are not mutable and raises AttributeError -> will execute the print statement
    tuple_numbers.append(45)
except AttributeError:
    print("I SAID TUPLES ARE IMMUTABLE!!")

# You CANNOT change tuples, although you CAN redefine the variable again of course.

# The trailing comma is necessary for python to know that the (45) is considered a tuple,
# not an integer with parenthesis
tuple_numbers = tuple_numbers + (45,)
