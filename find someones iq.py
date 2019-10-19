import time
import random
from random import seed
from random import randint
# useless
print("random website code")
# asking user for a seed
seednumber = input("What seed do you want it to be?(if you dont know type a random number): ")
time.sleep(0.500)
# asking user for a name
name = input("Whos iq do you want to find? ")
seed(seednumber)
# the randonm nunmber generator stuff
for _ in range(1):
	# gets a number
	value = random.randint(0, 150)
	# saying what this persons iq is
	print(value, "is that persons iq.")
time.sleep(1)
# insulting the person for having a very low iq
print(name, "has a very low iq")
time.sleep(5)