

# The conditionals in Python are done with If, elif and else and conditions as booleans. Let's see how:

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



