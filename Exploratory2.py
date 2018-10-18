# this function looks at a list of numbers and counts the amount of
#     positive numbers
def positive_count(list_o_numbers):
    test = 0
    # this creates an empty list, later used to count positive numbers
    if type(list_o_numbers) != list:
        raise TypeError("This was NOT correct.")
    for thing in list_o_numbers:
        if type(thing) != int:
            raise TypeError("This is not an int")
        if thing > 0:
            test += 1
    return test

print positive_count([69, 13, 25, -2003])
print positive_count ("what is even going on anymore")
