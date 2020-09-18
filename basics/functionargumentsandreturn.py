'''
Created on 18-Sep-2020

@author: mohd.e.khan
'''
import time

def pass_argument(ls):
    print(ls)
    fls = ls
    print("After assigning a new list to fls")
    fls=["Modifying", "It", "Inside", "Function"]
    print("Argument:", ls)
    print(fls)
    
    
ls = ["A", "List", "To", "Pass"]  
pass_argument(ls)
print(ls)
    
def default_arg(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)
    
default_arg("Mohd Emran Khan") 
default_arg("Mohd Emran Khan", "*")
default_arg("Mohd Emran Khan", border="#")
default_arg(message="Mohd Emran Khan", border="#")
default_arg(border="#", message="Mohd Emran Khan")
#default_arg(border="#","Mohd Emran Khan") SyntaxError: positional argument follows keyword argument 

time.ctime()
def default_value_evaluation(arg=time.ctime()):
    print(arg)
    
default_value_evaluation();
print(time.perf_counter_ns())
default_value_evaluation()
   
    
def pass_arg(menu=[]):
    menu.append("Butter")
    return menu


print(pass_arg()) # ['Butter']
print(pass_arg(["Bread"])) # ['Bread', 'Butter']
print(pass_arg()) # ['Butter', 'Butter']
print(pass_arg()) # ['Butter', 'Butter', 'Butter']

def pass_arg_enhanced(menu=None):
    if menu is None:
        menu = []
    menu.append("Butter")
    return menu

print(pass_arg_enhanced()) # ['Butter']
print(pass_arg_enhanced(["Bread"])) # ['Bread', 'Butter']
print(pass_arg_enhanced()) # ['Butter']
print(pass_arg_enhanced()) # ['Butter']