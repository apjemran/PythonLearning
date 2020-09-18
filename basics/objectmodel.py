'''
Created on 18-Sep-2020

@author: mohd.e.khan
'''

def check_object_ref():
    a = 300
    print(id(a)) #Object Reference of a

    b = a
    print(id(b)) # Should have save object reference
    
    print(a is b)
    
    print(id(a) == id(b))
    
def check_augmented_ref():
    t = 5 # int object 5 is created
    print(id(t))
    
    t+=2 # int object 2 and 7 are create t will refer to 7. 5 & 2 are eligible for garbage collection
    print(id(t))
    
def check_mutable_object():
    r = [3,6,2] # list is mutable
    s = r    
    print(s is r)
    s.append(4)
    print(s)
    print(r)
    
def value_vs_identity_equality():
    r = [2,4,6]
    s = [2,4,6] # both lists are equal (identical) but referring to two different object
    print(r == s) # True as both list have same values
    print(r is s) # False both list referring to different objects
    print(id(r))
    print(id(s))
    
check_object_ref()
check_augmented_ref()
check_mutable_object()
value_vs_identity_equality()
