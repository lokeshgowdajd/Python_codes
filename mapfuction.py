"""The map() function in Python is a powerful tool for transforming data efficiently and concisely. 
It allows you to apply a specified function to each item in an iterable (such as a list, tuple, or dictionary) and
returns a new iterable (a map object) containing the results."""

#using lambda function
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))  # Output: [2, 4, 6, 8]


# Define a function to double a number
def double(n):
    return n * 2

numbers = (1, 2, 3, 4)
result = map(double, numbers)
print(list(result))  # Output: [2, 4, 6, 8]
