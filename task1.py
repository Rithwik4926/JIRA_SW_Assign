import random

def generate_question():
    a = random.randint(2, 12)
    b = random.randint(2, 12)
    return a, b, a * b
