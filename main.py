import random
import os

def guess_game_simulated():
    number_to_guess = random.randint(1, 5)
    max_attempts = 3
    fake_target = "C:/Windows" if os.name == "nt" else "/System"

    print("Guess the number between 1 and 5. You have 3 tries.")
    print(f"⚠️ You are already late! 😉")

    for i in range(max_attempts):
        try:
            guess = int(input(f"Attempt {i + 1}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess == number_to_guess:
            print("✅ You guessed correctly! The system is safe.")
            return
        else:
            print("❌ Wrong guess.")

    print(f"💀 You failed! Pretending to delete {fake_target}...")
    print("Deleting files...")
    for i in range(5):
        print(f"Removing system file {i+1}/5...")
    print("💣 Just kidding! This is a simulation. No files were harmed.")

guess_game_simulated()

