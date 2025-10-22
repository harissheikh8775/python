# Who will pay the bill
# by using the random module

import random
friends=["Alice","Bob","Charlie","Haris","David"]

random_name=random.randint(0,len(friends)-1)

print(f"{friends[random_name]} will pay the bill.")
