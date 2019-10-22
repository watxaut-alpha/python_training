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
string_with_simple_quotes = 'I am immutable and I am still a string'
string_text = """
Roses are red,
violets are blue,
this is also a string,
fantastic.
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

if not some_true_condition:  # this will not get printed, as it checks for the condition to be False
    print("I will not get any attention :(")


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
s_sentence = "Lion Alone"
if "Lion" in s_sentence and "Alone" in s_sentence:  # checks BOTH conditions to be true (and they are)
    # will enter here, print "Hey ho!" and skip all other conditions because of the if-elif-else structure
    print("Hey ho!")
elif "not" in s_sentence or "and" in s_sentence:  # checks ONE condition to be true (neither of them are)
    print("<--Input something silly here-->")
elif "lioness" not in s_sentence:  # This is true, but it will not enter here as the first conditional matches
    print("I'm out of test sentences")
else:  # if no case is matched
    print("I am really out of test sentences and this is the else statement")
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
l_objects = ["hey", "ho", "let's go"]
for obj in l_objects:  # will loop through all the objects in the list
    print(obj)
print("I'm outside already. Take care of indentations in python!")
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


# let's create the same loop as in the For loop to iterate through a list of strings but with While
list_strings = ["hey", "ho", "let's go"]
while i < len(list_strings):
    print(list_strings[i])
    i = i + 1

# it's not like for is better than while loop, there will be times where you will be forced to use the while loop
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

# to add things to lists (remember, mutable means mutable like it can change)
list_numbers.append(66)
print(list_numbers)  # prints [12, 33, 44, 55, 66] now

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
d_got_is_alive = {"John Snow": True, "Tyrion Lannister": True, "Ned Stark": True}

# to retrieve an item, like lists but by the KEY
print(d_got_is_alive["Ned Stark"])

# example with for loop
# the method .keys() of a dictionary returns a list of the keys in the dictionary. WATXAUT! It might not be ordered!
for key in d_got_is_alive.keys():
    s_character = key
    is_alive = d_got_is_alive[key]
    print("Is {character} alive? {is_alive}".format(character=s_character, is_alive=is_alive))

# to add elements ->
d_got_is_alive["Tommy Lannister"] = False  # RIP Tommy Lannister (?)

# if the key already exists, you OVERWRITE the value. Also, the type of the keys and the values might change
d_got_is_alive["Tyrion Lannister"] = "Maybe, who knows HUEHUEHUEHUE"
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

### The MAGIC behind mutable variables
As mutable types, they are pointing to the same memory location (they are pointers, like C), so if you have the great
idea of doing list_1 = list_2, you won't be copying the list, you will be actually copying the pointer location, so if
you change one, the other also changes. Dentro video! ->
```python
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

# --> METHOD 1: The Pythonic way
import copy
list_copy = copy.deepcopy(whoops_list)
print(list_copy is whoops_list)  # Spoiler, it's False

# --> METHOD 2: The 'I don't have time for this!' guy - don't be this guy
list_copy_2 = whoops_list[:]
print(list_copy_2 is whoops_list)  # Spoiler, it's False
```

This, obviously, happens with every MUTABLE variable. So you have to know exactly what you are doing when doing
this_mutable_var = this_other_mutable_var. Don't say I didn't warn you. I am 99% sure this will happen at 
some point in your code, but humans do learn by smashing their head into the problems, it's the way we are coded. 

### Ex2: Lorem Ipsum
Hey you should know about lists and dictionaries already!
Given the 3 first paragraphs of Lorem Ipsum as string s_lorem_ipsum:
1. Print how many times the characters "a", "q", "w", "k" appear in s_lorem_ipsum
2. Find the 3 words that appear the most in s_lorem_ipsum

**PRO TIP:** if you do s_lorem_ipsum.split(" "), you will get a list of words, try it out ;)

Coming Soon: A brief summary of (nearly) everything II
-----
Under construction
- Pure Functions
- Impure Functions
- Namespace

### Next Steps
- Gamification with programming quizzes: https://www.codewars.com/

- Mathematic and programming problems: https://projecteuler.net

- ML problem solving competition, big money: https://www.kaggle.com/
