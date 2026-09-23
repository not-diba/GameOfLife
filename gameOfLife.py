import random


def main():
    render(random_state(30, 2))


def dead_state(width, height):
    return [[0] * height for _ in range(width)]


def random_state(width, height):
    state = dead_state(width, height)

    for i in range(width):
        for j in range(height):
            random_number = random.random()
            state[i][j] = 0 if random_number >= 0.5 else 1

    return state


def render(board_state):
    for row in board_state:
        for item in row:
            print("o", end="\t") if item == 1 else print("*", end="\t")
        print()


if __name__ == "__main__":
    main()
