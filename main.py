#var = ["a", "b", "c", "d", "e", "f", "g", "h"]
#print(var[0])

#print(var.index("a"))

#var2 = "hello"

#print(var2[0])

# thing to consider

# loop
# range
# random

import random
import math

num = 7.2
print(math.ceil(num))

def paint_calc(height, width, cover):
  num_cans = math.ceil( (height * width) / cover)
  print(f"You'll need {num_cans} cans of paint.")

paint_calc(height=4, width=9, cover=5)

#  ------------------------------------
change = 0.2099999999
change = round(change, 2)
print(f"change = ${change}")

#  ------------------------------------
change = 0.3
change = round(change, 2)
change = f"{change:.2f}"
print(f"change = ${change}")
print(change)
print(float(change))
