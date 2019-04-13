# python_training
A python training for beginners in python and not so beginners in programming

Disclaimer
-----
- Probably after trying out Python, you won't like your previous programming language, so proceed with caution. You are warned.
- All the jokes inside the code are pure fiction, any resemblance to reality is pure luck


Index
-----
* Prerequisites
* IDE
* A brief summary of (nearly) everything I
    * Variables I: immutable variables
    * Conditionals
    * Loops
    * Ex1: The typical programming exercise fo 3s and 5s
    * Variables II: mutable variables
        * The magic behind mutable variables
    * Ex2: Lorem Ipsum
* A brief summary of (nearly) everything II
    * Pure Functions
    * Impure functions
    * Namespace

* Next steps
    * Virtual Environments yay
    * Programming exercises
    * Git

Prerequisites
-----
* Python 3.6 installed [(Python3.6 download page)](https://www.python.org/downloads/release/python-368/)
* PyCharm installed [(Pycharm download page)](https://www.jetbrains.com/pycharm/download/)

IDE
-----
There is a huge variety of IDEs for Python. I personally recommend the community version of Pycharm 
from Jetbrains, it's really good. There are others that I have been told that they are good like:
* Atom
* Visual Studio Code
* Sublime text

A brief summary of (nearly) everything I
-----
###Variables I: immutable variables
There are some types of variables in python that cannot be modified after their creation, they are 
called immutable variables. The list of immutable variables is:

* String
* Int
* Float
* Bool
* Tuple
* Frozenset

```python
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

# Booleans: True or False
condition_a = True
condition_b = 2 < 1

# Tuple:
tuple_numbers = (45, 6j, 7, 8, 9.567, 0, 5, 300_789_431)
```

### Conditionals
The conditionals in Python are done with the keywords 'if', 'elif' and 'else' and conditions as booleans. Let's see how:
```python
# here we have one boolean
some_true_condition = True
if some_true_condition == True:  # if the boolean is True, it will print, if not, it won't do anything
    print("Hey this is True")

if some_true_condition:  # This is the same, but more Pythonic
    print("Hey this still is True")


# In here the condition is something more likely to happen inside the code, when we evaluate if a number is greater
# or less than another
another_condition = 2 < 3
if another_condition:
    print("True indeed")
else:
    print("Nah, it's False")


# with more than one condition and the condition inside the conditional
num = 3
if num < 3:
    print("The number is less than 3")
elif num == 3:
    print("It's equal!")
else:
    print("Nah, it's greater than 3")


# with more than one condition and strings used in conditions. Operators "and", "or" and "not"
s_sentence = "Leon solo"
if "leon" in s_sentence and "solo" in s_sentence:
    print(True)
elif "castilla <3" in s_sentence or "yo duermo abajo y ARRIBA ESPANYA" in s_sentence:
    print("Poner alguna burrada aquí")
elif "fairy" not in s_sentence:  # if this is true, it will print and it won't continue with the other conditions
    print("terrible trampa del fairy")
elif "es Madrid y no Madriz" in s_sentence:
    print("Es que no saben hablar")
else:  # if no case is matched
    print("Los catalanes estamos adoctrinados y tengo un poster de Puigdemont en mi habitacion")
```

### Loops
There are 2 type of loops in python: The For loop and the not used one (I'm joking, it's the While loop).
They are used to loop through iterable objects (like lists, strings, tuples, sets and dictionaries) and/or create 
infinite loops, depending on the case might be useful (for example a bot that is waiting for instructions).

#### For Loop
```python
for i in range(10):  # range creates a list of numbers -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(i)
```
The for loop iterates over an object and at each iteration the counter ("i" in this case) will have one value at a time,
first 0, then 1, then 2... until the object has no more items inside and then python will exit the for loop.

```python
for s in ["hey", "ho", "let's go"]:
    print(s)
print("I'm outside already. Take care of identations in python!")
```

The same in this case, in each iteration, s will be "hey", then s = "ho" and then s = "let's go" and it will exit the
loop and continue with the code.
**NOTE** Python uses indentation to know where For loops, While loops, If conditionals are ended!

#### The While loop - The forgotten one
The While loop comes from the devil itself, so watch out. You can end up in an infinite loop easily.
Although in some cases an infinite loop might come in handy.

Both of the following loops will do the same as in the For loops above:
```python
i = 0
while i < 10:  # if you mess with this line -> boom, infinite loop
    print(i)
    i = i + 1  # if you don't include this line -> boom, infinite loop


list_strings = ["hey", "ho", "let's go"]
while i < len(list_strings):
    print(list_strings[i])
    i = i + 1
```

### Ex1: The typical programming exercise fo 3s and 5s
Now is your time to shine. In this exercise you will to use loop and conditionals.
It is asked:
* Create a loop that goes from 0 to 15.
* If the counter is divisible by 3 print "LOL"
* If the counter is divisible by 5 print "HAH"
* if the counter is divisible by 3 and 5, print "HAHLEL"

### Variables II: mutable variables
Now here is where all the Python fun and mindf*cking comes into play.
There is 3 types of mutable variables: lists, dictionaries and sets.

#### Lists
```python
list_numbers = [12, 33, 44, 55]

# lists of list are also possible! You can create matrix for example
jacobean_matrix = [
    [3, 4, 5],
    [1, 0, 4],
    [0, 3, 1]
]

# to add things to lists (remember, mutable means mutable)
list_numbers.append(66)
print(list_numbers)  # prints '[12, 33, 44, 55, 66]'

# to retrieve an item
print(list_numbers[3])  # prints '55'

# you can also make slices of the list
print(list_numbers[1:3])  # prints [33, 44]. First index inclusive, last exclusive!
```

#### Dictionaries
> I know I am not supposed to give my opinion BUT, probably my favourite variable type - Joan Heredia, 2019 

You can store nearly anything you want inside and retrieve it later with a key.
It's like a table with two columns: the Key and the Value. The only way to get the Value 
is to ask for it with the Key.
```python
# dictionaries are like an UNORDERED list of key:value pairs
d_got_alive = {"juan de las nieves": True, "Tyrion Lannister": True, "Ned Stark": False}

# to retrieve an item, like lists but by the KEY
print(d_got_alive["Ned Stark"])  # prints 'False' :(

# example with for loop
for key in d_got_alive.keys():  # the method .keys() returns a list of the keys in the dictionary. OJU! Might not be ordered!
    s_character = key
    is_alive = d_got_alive[key]
    print("Is {character} alive? {is_alive}".format(character=s_character, is_alive=is_alive))

# to add elements ->
d_got_alive["Tommy Lannister spoiler?"] = False

# if the key already exists, you OVERWRITE the value. Also, the type of the keys and the values might change
d_got_alive["Tyrion Lannister"] = "Maybe, who knows jejejejeje"
```

#### Sets
The bullied variable of Python. Nobody uses sets, but I will explain them anyway. (I am joking, 
but I use them rarely).

```python
# Sets are unordered lists of UNIQUE ITEMS, like dictionaries but without values, only keys.
set_numbers = {5, 3, 6, 7, 7, 7, 7}
print(set_numbers)

# they are useful when you need to know which items are in one set and not in the other
set_numbers_2 = {1, 2, 3, 4, 5}

print(set_numbers_2.intersection(set_numbers))  # the intersection will print another set = {3, 5}
```

#### The MAGIC behind mutable variables
As mutable types, they are pointing to the same memory location (they are pointers, like C), so if you have the great
idea of doing list_1 = list_2, you won't be copying the list, you will be actually copying the pointer location, so if
you change one, the other also changes. Dentro video! ->
```Python
whoops_list = ["I", "am", "really good", "at Python"]
i_am_really_bad_at_python_list = whoops_list
i_am_really_bad_at_python_list.append("OR AM I????")

print(whoops_list)                      # returns '["I", "am", "really good", "at Python", "OR AM I????"]'
print(i_am_really_bad_at_python_list)   # returns '["I", "am", "really good", "at Python", "OR AM I????"]'
print(whoops_list is i_am_really_bad_at_python_list)  # Spoiler, it's True
```
**WAIT**, so if I want to copy a list, how do I do it?
```python
whoops_list = ["I", "am", "really good", "at Python"]

# --> METHOD 1: The Orthographical-N*zi Python guy
import copy
list_copy = copy.deepcopy(whoops_list)
print(list_copy is whoops_list)  # Spoiler, it's False

# --> METHOD 2: The "I don't have time for this!" guy
list_copy_2 = whoops_list[:]
print(list_copy_2 is whoops_list)  # Spoiler, it's False
```

This, obviously, happens with every MUTABLE variable. So you have to know exactly what you are doing when doing
this_mutable_var = this_other_mutable_var. Don't say I didn't warn you. I am 99% sure this will happen at 
some point in your code, but humans do learn by smashing their head into the problems, it's the way we are coded. 

A brief summary of (nearly) everything II
-----
Under construction
### Pure Functions
Under construction
### Impure Functions
Under construction
### Namespace
Under construction

### Next Steps
Gamification with programming quizzes:
https://www.codewars.com/

Mathematic and programming problems:
https://projecteuler.net

ML problem solving competition, big money:
https://www.kaggle.com/
