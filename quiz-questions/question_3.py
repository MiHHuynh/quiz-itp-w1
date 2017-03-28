"""Intro to Python - Week 1 - Quiz."""


# Question 3
def remove_Es(a_string):
    """Implement the code required to make this function work.

    Write a function `remove_Es` that receives a string and removes all
    the characters `'e'` or `'E'`. Example:

    remove_Es('remoter')  # 'rmotr'
    remove_Es('eEe')      # ''
    remove_Es('abc')      # 'abc'
    """
    # Write your code here
    i = 0
    new_str = []
    for i in len(a_string):
        if a_string[i] != 'e' or a_string[i] != 'E':
            new_str += a_string[i]
    return new_str
