'''
Created on 18-Sep-2020

@author: mohd.e.khan
'''
from _ast import arg

global_var = 'this is global var'

def check_varscopes(arg):
    global_var = arg
    return global_var

print(check_varscopes(5))
print(global_var)

def check_varscopes_global(arg):
    global global_var #Use global key word to use global var rather than creating a local var of same name
    global_var = arg
    return global_var

print(check_varscopes_global(5))
print(global_var)
