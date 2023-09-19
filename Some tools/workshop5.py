import random


def guess_random_number(tries, start, stop):
    target = random.randint(start, stop)

    while tries != 0:
        print("Tries remaining:", tries)
        guess = int(input("Enter your guess: "))

        if guess == target:
            print("Congratulations! You guessed the number.")
            return

        if guess < target:
            print("Guess higher!")
        else:
            print("Guess lower!")

        tries -= 1

    print("Sorry, you ran out of tries. The number was", target)


def guess_random_num_linear(tries, start, stop):
    target = random.randint(start, stop)

    for guess in range(start, stop+1):
        print("Guessing:", guess)
        if guess == target:
            print("Congratulations! You guessed the number.")
            return
        tries -= 1
        if tries == 0:
            break

    print("Sorry, you ran out of tries. The number was", target)


def guess_random_num_binary(tries, start, stop):
    target = random.randint(start, stop)
    low, high = start, stop

    while low <= high and tries > 0:
        mid = (low + high) // 2
        print("Guessing:", mid)
        if mid == target:
            print("Congratulations! You guessed the number.")
            return
        elif mid < target:
            low = mid + 1
        else:
            high = mid - 1
        tries -= 1

    print("Sorry, you ran out of tries. The number was", target)


# Test driver code
# guess_random_number(5, 0, 10)
# guess_random_num_linear(5, 0, 10)
guess_random_num_binary(5, 0, 10)
