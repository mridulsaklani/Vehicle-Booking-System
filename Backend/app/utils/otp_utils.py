
import math
import random
def generate_otp()->int:
    return math.ceil(100000 + random.random() * 900000)
