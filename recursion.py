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
    # l.reverse() is what one would do if they were NOT insane. Insane people
    # write recursive ridiculousness here:

    if len(l) == 1:
        return l
    
    temp = l.pop()

    return [temp] + reverse(l)

# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    if n <= 2: 
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

# Finds the item i in the list l.... RECURSIVELY
def find(listIn, i):
   
    if listIn == []:
        return None

    elif listIn[0] == i:
        return i

    return find(listIn[1:],i)

# Determines if a string is a palindrome
def palindrome(some_string):

    if len(some_string) <=1 :
        return True
    
    firstchar = some_string[0]
    lastchar = some_string[-1]

    if len(some_string) == 2:
        return (some_string[0] == some_string[1])

    short_string = some_string[1:-1]
    return palindrome (short_string)  


# Given the width and height of a sheet of paper, and the number of times to fold it, return the final dimensions of the sheet as a tuple. Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):

    if folds == 0:
        return(width,height)

    return fold_paper(height, width/2.0,folds-1)
 
# Count up
# Print all the numbers from 0 to target
def count_up(target, n):
    print n
    if target <= n:
        return       
    
    count_up(target, n+1)
    return

# extra credit -- solve the Hanoi pyramid proglem

def hanoi(n, source, dest, helper):
    
    print n
    if n > 0:
        hanoi(n-1, source, helper, dest)
        ring = source.pop()
        dest.append(ring)
        hanoi(n-1, helper, dest, source)

    pass


