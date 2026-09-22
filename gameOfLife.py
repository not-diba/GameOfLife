import random


def main():
    random_state(5, 5)


def dead_state(width, height):
    return [[0] * height] * width


def random_state(width, height):
    state = dead_state(width, height)

    for i in range(width):
        for j in range(height):
            random_number = random.random()
            state[i][j] = 0 if random_number >= 0.5 else 1

    print(state)


if __name__ == "__main__":
    main()
