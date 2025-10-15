import random
from art import logo

def play_game():
    print(logo)
    print("Welcome to a guess number!")
    print("Im thinking of a number between 1 and 100.")


    # Компьютер загадывает число
    secret_number = random.randint(1, 100)

    # Игрок выбирает уровень сложности
    while True:
        level = input("Print a difficulty. Type 'easy' or 'hard': ").strip().lower()
        if level == 'easy':
            attempts = 10
            print("You have 10 attempts  to guess the number.")
            break
        elif level == 'hard':
            attempts = 5
            print("You have 5 attempts  to guess the number.")
            break

        else:
            print("Please type 'easy' or 'hard'")

    # Игровой цикл

    while attempts > 0:
        print(f"\nYou have {attempts} attempts_remaining.")
        guess = input("Make a guess: ")
        if not guess.isdigit():
            print("Enter a digit number")
            continue
        guess = int(guess)

        if guess < secret_number:
            print("Too low.")
        elif guess > secret_number:
            print("Too high.")
        else:
            print(f"Correct! The number was {secret_number}. You win!")
            break

        attempts -= 1

        if attempts == 0:
            print(f"You have run out of attempts! The number was{secret_number}.")
            break
        else:
            print("Please guess again!")

    #  Спрашиваем, хочет ли игрок сыграть снова
    play_again = input("\nDo you want to play again? Type 'y' or 'n': ").lower()
    if play_again == 'y':
        print("\n" * 20)
        play_game()  # 🔁 запускаем заново
    else:
        print("Thanks for playing! Goodbye 👋")

play_game()