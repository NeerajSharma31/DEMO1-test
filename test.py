
import pandas as pd
import random
import math
from utility import *
from config import A, B , NAME # OR IF WANT ALL THAN TYPE AT THE END *
from config import *

a = random.randint(1, 10)
print("Random Number: {}".format(a))

def add(a, b, c):
    return a + b + c

result = add(2, 3, 4)

print("Addition is {}".format(result))


print(math.sqrt(a))

print(A,B, NAME, AGE)
