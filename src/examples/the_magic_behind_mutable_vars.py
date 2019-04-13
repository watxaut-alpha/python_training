

# As mutable types, they are pointing to the same memory location (they are pointers, like C), so if you have the great
# idea of doing list_1 = list_2, you won't be copying the list, you will be actually copying the pointer location, so if
# you change one, the other also changes. Dentro video! ->
whoops_list = ["I", "am", "really good", "at Python"]
i_am_really_bad_at_python_list = whoops_list
i_am_really_bad_at_python_list.append("OR AM I????")

print(whoops_list)
print(i_am_really_bad_at_python_list)
print(whoops_list is i_am_really_bad_at_python_list)  # Spoiler, it's True


# WAIT, so if I want to copy a list, how do I do it?
# --> METHOD 1: The Orthographical-N*zi Python guy
import copy
list_copy = copy.deepcopy(whoops_list)
print(list_copy is whoops_list)  # Spoiler, it's False

# --> METHOD 2: The "I don't have time for this!" guy
list_copy_2 = whoops_list[:]
print(list_copy_2 is whoops_list)  # Spoiler, it's False


# This, obviously, happens with every MUTABLE variable. So you have to know exactly what you are doing when doing
# this_mutable_var = this_other_mutable_var. Don't say I didn't warn you
