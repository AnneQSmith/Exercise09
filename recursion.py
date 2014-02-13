# Multiply all the elements in a list
def multiply_list(l):
    total = 1 # Set total to 1
    if l == []: # Set the base case, if our list is empty
        return 1 # return 1
    else: #if our list is not empty
      total = l.pop() * multiply_list(l) # total is equal to last number in list * multiply_list(l)
    return total

# Return the factorial of n
def factorial(n):
    total = 1
    if n == 1:
        return 1
    else:
        total = factorial(n-1) * n
    return total

# Count the number of elements in the list l
def count_list(l):
    total = 0
    if l == []:
        return 0
    else:
        l.pop()
        total = count_list(l) + 1 
    return total

# Sum all of the elements in a list
def sum_list(l):
    total = 0
    if l == []:
        return 0
    else:
        total = l.pop() + sum_list(l)
        
    return total


# Reverse a list without slicing or loops
def reverse(l):
    return []

# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    pass

# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    return None

# Determines if a string is a palindrome
def palindrome(some_string):
    return False

# Given the width and height of a sheet of paper, and the number of times to fold it, return the final dimensions of the sheet as a tuple. Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    return (0, 0)

# Count up
# Print all the numbers from 0 to target
def count_up(target, n):
    return

## Tests

print multiply_list(range(1,6))