from random import randint


def generate_number() -> list[int]:
    rnd_lst: set = set()

    while len(rnd_lst) < 4:
        rnd_lst.add(randint(0, 9))

    return list(rnd_lst)


def input_guess() -> list[int]:
    try:
        guess_input: int = int(input("Enter your guess: "))
        num_lst = [int(x) for x in str(guess_input)]

        return num_lst

    except ValueError:
        raise ValueError("You must enter an integer")


def start_game():
    life: int = 10
    guess_num = generate_number()
    guess = input_guess()

    while guess_num != guess and life > 0:
        life -= 1
        has_num: list[int] = list({x for x in guess if x in guess_num})

        match: list[int] = [x for x in has_num if guess.index(x) == guess_num.index(x)]

        check: list[int] = [x for x in has_num if x not in match]

        if len(match) == 1:
            print(f"{len(match)} number is correct and in the right position")

        elif len(match) > 1:
            print(f"{len(match)} numbers are correct and in the right position")

        if len(check) == 1:
            print(f"{len(check)} number is correct but in the wrong position")

        elif len(check) > 1:
            print(f"{len(check)} numbers are correct but in the wrong position")
        if not match and not has_num:
            print("No number is correct")

        print("\n")
        print("\u2764\uFE0F  " * life)

        guess = input_guess()

    if guess_num == guess:
        print(f"You guessed correctly the number was {guess_num}")
    else:
        print(f"You ran out of life \u2764\uFE0F . The number was {guess_num}")


start_game()
