import random

def generate_question():
    a = random.randint(2, 12)
    b = random.randint(2, 12)
    return a, b, a * b

def ask_question(num):
    a, b, correct_ans = generate_question()
    print(f"Question {num}: {a} x {b} = ?")
    try:
        ans = int(input("Your answer: "))
    except ValueError:
        ans = None
    if ans == correct_ans:
        print("Right!")
        return True
    else:
        print(f"Wrong. The answer is {correct_ans}.")
        return False

import time

start_time = time.time()
# Ask 10 questions here
end_time = time.time()
total_time = end_time - start_time

players = []
for i in range(10):
    name = input(f"Enter player {i+1} name: ")
    start_time = time.time()
    score = 0
    for q in range(1, 11):
        if ask_question(q):
            score += 1
    end_time = time.time()
    total_time = end_time - start_time
    players.append({'name': name, 'score': score, 'time': total_time})
