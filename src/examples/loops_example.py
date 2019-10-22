# there are 2 type of loops in python: The For loop and the not used one (I'm joking, it's the While loop)

# ## The For Loop ##
for i in range(10):  # range creates a list of numbers -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(i)

l_objects = ["hey", "ho", "let's go"]
for obj in l_objects:  # will loop through all the objects in the list
    print(obj)

# The for loop iterates over an object and at each iteration the counter ("i" or "obj" in this case) will
# have one value each iteration, and then the other, and then the other.. until the last of the objects. Then it will
# continue with the execution of the script


# ## The While Loop ##
# the While loop comes from the devil itself, so watch out. You can end up in an infinite loop easily.
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
