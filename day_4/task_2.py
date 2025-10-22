# random module
import random

# random.randint(a,b)--> to generate the whole number (0 <= X <=1)
# random.random()--> to generate the float number (0.0 <= X <1.0 )
# random.uniform(a,b)--> floating numbers

random_integer=random.randint(1,10)
print(random_integer)

random_number_0_to_1=random.random()
print(random_number_0_to_1)

random_float=random.uniform(1,10)
print(random_float)

