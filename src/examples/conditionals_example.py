# The conditionals in Python are done with If, elif and else and conditions as booleans. Let's see how:

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
