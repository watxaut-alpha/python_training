

# there are 2 type of loops in python: The For loop and the not used one (I'm joking, it's the While loop)

# The For loop:
for i in range(10):  # range creates a list of numbers -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(i)

for s in ["hey", "ho", "let's go"]:
    print(s)

# The for loop iterates over an object and at each iteration the counter ("i" or "s" in this case) will have one value,
# and then the other and then the other until the object has no more items inside


# The While Loop:
# the While loop comes from the devil itself, so watch out. You can end up in an infinite loop easily.
i = 0
while i < 10:  # if you mess with this line -> boom, infinite loop
    print(i)
    i = i + 1  # if you don't include this line -> boom, infinite loop


list_strings = ["hey", "ho", "let's go"]
while i < len(list_strings):
    print(list_strings[i])
    i = i + 1
