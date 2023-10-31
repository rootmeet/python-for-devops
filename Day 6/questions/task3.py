#!/usr/bin/python

# logical operators

x = -15
y = False
print("Result x and y:", (x & y) )
print("Result x or y:", (x | y) )
print("Result not x:", (not x) )
print("Result not y:", (not y) )


a = 10
b = 10
c = -10
  
if a > 0 and b > 0:  
    print("The numbers are greater than 0")  
  
if a > 0 and b > 0 and c > 0:  
    print("The numbers are greater than 0")  
else:  
    print("Atleast one number is not greater than 0") 


a = 37
  
if not a:  
    print("Boolean value of a is True")  
  
if not (a%3 == 0 or a%5 == 0):  
    print("10 is not divisible by either 3 or 5")  
else:  
    print("10 is divisible by either 3 or 5")