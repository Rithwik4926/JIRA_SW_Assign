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
