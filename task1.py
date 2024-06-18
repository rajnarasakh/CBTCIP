def get_feedback(code, guess):
    """Provides feedback in terms of correct digits in correct place and correct digits in wrong place."""
    correct_place = sum(c == g for c, g in zip(code, guess))
    correct_digits = sum(min(code.count(x), guess.count(x)) for x in set(guess))
    return correct_place, correct_digits - correct_place

def mastermind_game():
    """Main game function for the two-player Mastermind game."""
    print("Welcome to the two-player Mastermind game!")
    
    # Player 1 sets the code
    while True:
        code1 = input("Player 1, set a 4-digit code (digits between 1-6): ")
        if len(code1) == 4 and all(d in '123456' for d in code1):
            code1 = list(map(int, code1))
            break
        else:
            print("Invalid input. Please enter a 4-digit code with digits between 1 and 6.")
    
    attempts_p2 = 0
    while True:
        attempts_p2 += 1
        guess = input("Player 2, make your guess: ")
        if len(guess) == 4 and all(d in '123456' for d in guess):
            guess = list(map(int, guess))
            correct_place, wrong_place = get_feedback(code1, guess)
            print(f"Feedback: {correct_place} correct place, {wrong_place} correct digit(s) in the wrong place.")
            if correct_place == 4:
                print(f"Player 2 guessed the code {code1} in {attempts_p2} attempts!")
                break
        else:
            print("Invalid input. Please enter a 4-digit number with digits between 1 and 6.")
    
    # Player 2 sets the code
    while True:
        code2 = input("Player 2, set a 4-digit code (digits between 1-6): ")
        if len(code2) == 4 and all(d in '123456' for d in code2):
            code2 = list(map(int, code2))
            break
        else:
            print("Invalid input. Please enter a 4-digit code with digits between 1 and 6.")
    
    attempts_p1 = 0
    while True:
        attempts_p1 += 1
        guess = input("Player 1, make your guess: ")
        if len(guess) == 4 and all(d in '123456' for d in guess):
            guess = list(map(int, guess))
            correct_place, wrong_place = get_feedback(code2, guess)
            print(f"Feedback: {correct_place} correct place, {wrong_place} correct digit(s) in the wrong place.")
            if correct_place == 4:
                print(f"Player 1 guessed the code {code2} in {attempts_p1} attempts!")
                break
        else:
            print("Invalid input. Please enter a 4-digit number with digits between 1 and 6.")
    
    # Determine the winner
    if attempts_p1 < attempts_p2:
        print("Player 1 wins and is crowned Mastermind!")
    elif attempts_p1 > attempts_p2:
        print("Player 2 wins and is crowned Mastermind!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    mastermind_game()
