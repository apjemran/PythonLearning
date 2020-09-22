'''
Created on 22-Sep-2020

@author: mohd.e.khan
'''
tup = ("Test", 1, 2.0)

print(tup)
print(tup[0])
print(tup*3)

tup + ("Test1",3)

print(tup)

tup1 = ("Test", ("Nested","Tuples", 1))

for item in tup1:
    print(item)
    
print(tup1[1][0])

tup2 = ("Single Element Tuple",) # Create single element tuple
print(tup2)

# Tuple unpacking - Destructuring operation that unpacks data structures into names reference

def minmax(items):
    return min(items), max(items)

print(minmax([4,5,14,64,3,67,12]))

minimum, maximum = minmax([4,5,14,64,3,67,12])
print(minimum)
print(maximum)

(a,b,(c,d)) = (1,2,(3,4))

print(a,b,c,d)  # 1 2 3 4

a  = "First"
b = "Second"

a, b = b, a #Swap a and b

print(a,b) # Second First

print("Nested" in tup1) # False
print("Nested" in tup1[1]) # True

