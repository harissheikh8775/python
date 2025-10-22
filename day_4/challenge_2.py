# Who will pay the bill
# by using the random module
# other method--> random.choice(friends) i.e by using the choice function
import random
friends=["Alice","Bob","Charlie","Haris","David"]

random_name=random.randint(0,len(friends)-1)

print(f"{friends[random_name]} will pay the bill.")
