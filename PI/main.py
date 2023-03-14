import numpy as np
from decimal import *


# Prompt and checking.
def get_prompt():
       while True:
              number_string = input("Enter number: ")
              if number_string.isdigit():
                     number = int(number_string)
                     if 1 <= number <= 48:
                            return number
              print("Enter a number between 1-48 (inclusive).")



# Get the decimal places prompted.
def pi_calc(number):
       try:
              getcontext().prec = number + 1
              pi = Decimal(np.pi) / Decimal(1) # If I don't divide by 1, decimal module doesn't give me appropriate decimal places.
              return pi
       except InvalidOperation:    # Using try-except, a bit overkill here, but good practice.
              print("Error: requested precision too large.")  
              return None

# Entire script runs on a simple main function.
def main():
       number = get_prompt()
       pi = pi_calc(number)
       if pi is not None:
              print(f"The number pi up to {number} decimal places is: {pi}.")


# Ensures standalone script.
if __name__ == "__main__":
       main()
