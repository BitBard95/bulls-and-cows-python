import random

def generate_secret():
    digits = list("0123456789")
    random.shuffle(digits)
    return ''.join(digits[:4])

def calculate_bulls_and_cows(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    return bulls, cows

def is_valid_guess(guess):
    return guess.isdigit() and len(guess) == 4 and len(set(guess)) == 4

def main():
    secret = generate_secret()
    attempts = 0

    print("🎯 Welcome to Bulls and Cows!")
    print("Try to guess the 4-digit secret number with unique digits. \n")

    while True:
        guess = input("Enter your guess: ").strip()

        if not is_valid_guess(guess):
            print("Invalid input. Please enter a 4-digit number with unique digits.")
            continue

        attempts += 1
        bulls, cows = calculate_bulls_and_cows(secret, guess)
        print(f"Bulls: {bulls}, Cows: {cows}")

        if bulls == 4:
            print(f"\n🎉 Congratulations! You guessed the number {secret} in {attempts} attempts.")
            break

if __name__ == "__main__":
    main()