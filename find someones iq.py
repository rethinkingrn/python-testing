import time
import random
from random import seed
from random import randint
print("random website code")
seednumber = input("What seed do you want it to be?(if you dont know type a random number): ")
time.sleep(0.500)
name = input("Whos iq do you want to find? ")
seed(seednumber)
# generate some integers
for _ in range(1):
	value = random.randint(0, 150)
	print(value, "is that persons iq.")
time.sleep(1)
print(name, "has a very low iq")
time.sleep(5)