'''
Created on 17-Sep-2020

@author: mohd.e.khan
'''
import math

def square(x):
    return x*x

n = square(10)

print(n)

def testsqrt(n):
    print(math.sqrt(n))
    
testsqrt(25)

def even_odd(n):
    if n%2 == 0:
        print("even")
        return
    else:
        print("odd")
        
ed = even_odd(13)
print(ed)

def nth_root(radicant, n):
    return radicant ** (1/n)

def ordinal_suffix(value):
    s = str(value)
    if s.endswith('11'):
        return 'th'
    elif s.endswith('12'):
        return 'th'
    elif s.endswith('13'):
        return 'th'
    elif s.endswith('1'):
        return 'st'
    elif s.endswith('2'):
        return 'nd'
    elif s.endswith('3'):
        return 'rd'
    return 'th'

def ordinal(value):
    return str(value) + ordinal_suffix(value)

def display_nth_root(radicant, value):
    root = nth_root(radicant, value)
    message = "The " + ordinal(value) + " root of " + str(radicant) + " is " + str(root)
    print(message)

display_nth_root(25, 2)
display_nth_root(125, 3)