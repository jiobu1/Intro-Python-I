"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
https://www.programiz.com/python-programming/list-comprehension
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [x for x in range(1,6)]
# just 6 does not work because it starts from 0 rather than 1

print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [x**3 for x in range(10)]

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [name.upper() for name in a]

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = [int(n) for n in x if int(n) % 2 == 0]

print(y)

"""
Answers:
[1, 2, 3, 4, 5]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
['FOO', 'BAR', 'BAZ']
Input: 14,9,12,13,7 returns [14, 12]
"""