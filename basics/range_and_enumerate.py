'''
Created on 22-Sep-2020

@author: mohd.e.khan
'''
range1 = range(10)

for i in range(10):
    print(i)
    
for i in range(5,10):
    print(i)

print("*" * 10)
for i in range(0,100,10):   
    print(i)

lst = list(range(10,20))
print(lst)

# Enumerate to get index 
t = [1,2,4,5,7,3]
for i in enumerate(t):
    print(i)