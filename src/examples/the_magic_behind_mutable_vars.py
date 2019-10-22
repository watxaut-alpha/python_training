# As mutable types, they are pointing to the same memory location (they are pointers, like C), so if you have the great
# idea of doing list_1 = list_2, you won't be copying the list, you will be actually copying the pointer location, so if
# you change one, the other also changes. Play the video! ->

# instantiate a list
whoops_list = ["I", "am", "really good", "at Python"]

# play with the devil
i_am_really_bad_at_python_list = whoops_list
i_am_really_bad_at_python_list.append("..OR AM I????")

print(whoops_list)  # will print ["I", "am", "really good", "at Python", "..OR AM I????"]
print(i_am_really_bad_at_python_list)  # will print ["I", "am", "really good", "at Python", "..OR AM I????"]

# And of course, you can check if they are the same object with 'is'. Spoiler, it's True
print(whoops_list is i_am_really_bad_at_python_list)


# WAIT, so if I want to copy a list, how do I do it?
# --> METHOD 1: The Orthographical-Nazi Python guy
import copy

list_copy = copy.deepcopy(whoops_list)
print(list_copy is whoops_list)  # Spoiler, it's False

# --> METHOD 2: The 'I don't have time for this!' guy - don't be this guy
list_copy_2 = whoops_list[:]
print(list_copy_2 is whoops_list)  # Spoiler, it's False


# This, obviously, happens with every MUTABLE variable. So you have to know exactly what you are doing when doing
# this_mutable_var = this_other_mutable_var. Don't say I didn't warn you
