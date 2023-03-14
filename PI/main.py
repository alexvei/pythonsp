import numpy as np
from decimal import *


def get_prompt():
       while True:
              number_string = input("Enter number: ")
              if number_string.isdigit():
                     number = int(number_string)
                     if 1 <= number <= 48:
                            return number
              print("Enter a number between 1-48 (inclusive).")


def pi_calc(number):
       try:
              getcontext().prec = number + 1
              pi = Decimal(np.pi) / Decimal(1)
              return pi
       except InvalidOperation:
              print("Error: requested precision too large.")
              return None


def main():
       number = get_prompt()
       pi = pi_calc(number)
       if pi is not None:
              print(f"The number pi up to {number} decimal places is: {pi}.")


if __name__ == "__main__":
       main()
