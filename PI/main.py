import numpy as np
from decimal import *

# **Find PI to the Nth Digit** - 

# Enter a number and have the program generate &pi; 
number = input("Enter number: ")
limits = 1
while(limits):
       while(not number.isdigit()):
              print("Please enter a number.")
              number = input("Enter number: ")
       number1 = int(number)
       if (number1 >= 1 and number1 <= 48):
              limits = 0
       else:
              print("Enter a number between 1-48 (inclusive).")
              number = 'a'
getcontext().prec = number1+1
print(f"The number pi up to {number1} decimal places is: {Decimal(np.pi)/Decimal(1)}.")



