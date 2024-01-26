#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is {int(math.fmod(number, 10))} and ", end="")
if number % 10 > 5:
    print("is greater than 5")
elif number % 10 == 0:
    print("is 0")
else:
    print("is less than 6 and not 0")
