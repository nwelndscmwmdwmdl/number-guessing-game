import random

def get_difficulty():
    print("\nSelect Difficulty:")
    print("1. Easy (1–50, 10 attempts)")
    print("2. Medium (1–100, 7 attempts)")
    print("3. Hard (1–500, 5 attempts)")

    while True:
        choice = input("Enter choice (1/2/3): ")
        if choice == "1":
            return 50, 10
        elif choice == "2":
            return 100, 7
        elif choice == "3":
            return 500, 5
        else:
            print("Invalid choice. Try again.")

def play_game():
    max_number, max_attempts = get_difficulty()
    secret_number = random.randint(1, max_number)
    attempts = 0

    print(f"\nI'm thinking of a number between 1 and {max_number}")
    print(f"You have {max_attempts} attempts.\n")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                score = (max_attempts - attempts + 1) * 10
                print(f"\n🎉 Correct! You guessed it in {attempts} attempts.")
                print(f"🏆 Your score: {score}")
                return

            print(f"Attempts left: {max_attempts - attempts}\n")

        except ValueError:
            print("Please enter a valid number.")

    print(f"\n💀 Game Over! The number was {secret_number}")

def main():
    print("🎮 Welcome to Number Guessing Game v2")

    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
