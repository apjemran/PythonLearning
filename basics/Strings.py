'''
Created on 22-Sep-2020

@author: mohd.e.khan
'''

import math

str1 = "First Hand"
str1.join(" Joined") 

print(str1)

str2 = ";".join(["List","Separated","By","Semicolon"]) #List;Separated;By;Semicolon

print(str2)

str3 = "Unforgetable";

print(str3.partition("forget"))

departure, separator, arrival = "London:Delhi".partition(":")
print(departure)
print(separator)
print(arrival)

strformat = "The age of {0} is {1}".format("Emran","35")

print(strformat)

value = f"One plus 3 is {1+3}"
print(value)

value = 4 * 20;

print(f"the value is {value}")

print(f"value of pi is: {math.pi}")

print(f"Math constants: pi={math.pi:.3f}") # Upto three decimal points