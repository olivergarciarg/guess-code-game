import random

# GET GUESS


def get_guess():
    return list(input("What is your guess"))

# GENERATE RANDOM NUMBER


def generate_code():
    digits = [str(num) for num in range(10)]
    # shuffle the digits and grab the first 3
    random.shuffle(digits)
    return digits[:3]

# GENERATE CLUES


def generate_clues(code, user_guess):
    if user_guess == code:
        return "CODE CRACKED"
    clues = []
    for ind, num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("close")
    if not clues:
        return ["Nope"]
    else:
        return clues

# RUN GAME LOGIC


print("Welcome to code braker")

secret_code = generate_code()
print(secret_code)

clue_report = []

while clue_report != "CODE CRACKED":
    guess = get_guess()
    clue_report = generate_clues(secret_code, guess)
    print("here is the result of your guess")
    for clue in clue_report:
        print(clue)

