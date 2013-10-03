# Multiply all the elements in a list

def multiply_list(l):
    if l == []:
        return 1
    return l[0] * multiply_list(l[1:])

# factorial(0) will run forever.
def factorial(l):
    if l == 0:
        return 0
    elif l == 1:
        return 1
    return l * factorial(l-1)

# Count the number of elements in the list l
def count_list(l):
    if l == []:
        return 0
    return 1 + count_list(l[1:])

# Sum all of the elements in a list
def sum_list(l):
    if l == []:
        return 0
    return l[0] + sum_list(l[1:])

# Reverse a list without slicing or loops
def reverse(l):
    if l == []:
        return []
    return [l.pop()] + reverse(l)

# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    if n <= 0:
        return 0
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    if l == []:
        return False
    elif i == l[0]:
        return True
    return find(l[1:], i)

# Determines if a string is a palindrome
def palindrome(some_string):
    if len(some_string) == 1 or len(some_string) == 0:
        return True
    if some_string[0] == some_string[-1]:
        palindrome(some_string[1:-1])
        return True
    else:
        return False

# Given the width and height of a sheet of paper, and the number of times to fold it, return the final dimensions of the sheet as a tuple. Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    if folds == 0:
        return (width, height)
    if height > width:
        return fold_paper(width, height/2.0, folds-1)
    elif width >= height:
        return fold_paper(width/2.0, height, folds-1)

# Count up
# Print all the numbers from 0 to target
def count_up(target, n):
    if n == target:
        print n
        return
    print n
    count_up(target,n+1)