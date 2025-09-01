import random
import time
import matplotlib.pyplot as plt

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

def award(players):
    players_sorted = sorted(players, key=lambda x: (-x['score'], x['time']))
    prizes = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    print("\nTop 3 Players:")
    for i in range(min(3, len(players_sorted))):
        p = players_sorted[i]
        print(f"{p['name']}: {p['score']} correct answers, {p['time']:.2f} seconds - {prizes[i]}")

def plot_times(players):
    names = [p['name'] for p in players]
    times = [p['time'] for p in players]
    plt.bar(names, times)
    plt.xlabel("Player Name")
    plt.ylabel("Completion Time (seconds)")
    plt.title("Completion Time by Player")
    plt.show()

def main():
    players = []
    num_players = 5
    num_questions = 10

    for i in range(num_players):
        name = input(f"\nEnter name for Player {i+1}: ")
        start_time = time.time()
        score = 0
        for q in range(1, num_questions + 1):
            if ask_question(q):
                score += 1
        end_time = time.time()
        total_time = end_time - start_time
        print(f"{name} finished in {total_time:.2f} seconds with {score} correct answers.\n")
        players.append({'name': name, 'score': score, 'time': total_time})

    award(players)
    plot_times(players)

if __name__ == "__main__":
    main()
