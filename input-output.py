from random import randint, seed


def guess_number_game():
    seed()
    input("Pick a number from 1 to 10 and press Enter when ready")
    low = 1
    high = 10
    while True:
        number = randint(low, high)
        answer = input(f"Is it {number}? (yes/no)\n")
        if answer.lower() == "yes":
            print("Hurra!")
            return
        else:
            answer = input(f"Is it lower than {number}? (yes/no)\n")
            if answer.lower() == "yes":
                high = max(number-1, low)
            else:
                low = min(number+1, high)
            print(f"Okay, then it should be between {low} and {high}")

guess_number_game()
