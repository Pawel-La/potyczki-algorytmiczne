import numpy as np

BIG_NUMBER = 10**9 + 7


def find_first_left(trick):
    return trick.find("L") + 1


def set_up_left_and_right(trick):
    left = np.zeros(len(trick))
    right = np.zeros(len(trick))
    left[1] = 1
    right[1] = 1
    return left, right


def count_fantastic_tricks(trick):
    fantastic_tricks = 0
    first_left = find_first_left(trick)
    left, right = set_up_left_and_right(trick)

    for i in range(first_left, len(trick)):
        if trick[i] == "L":
            left[1:] = left[:-1]
            left[0] = 0
            right += left % BIG_NUMBER
        else:
            right[:-1] = right[1:]
            fantastic_tricks += right[0] % BIG_NUMBER
            fantastic_tricks %= BIG_NUMBER
            left += right % BIG_NUMBER
            right[0] = 0
    return fantastic_tricks


def main():
    def concat_tricks(a, b):
        return TRICKS[a] + TRICKS[b]

    NUMBER_OF_TRICKS = int(input())
    TRICKS = [input() for _ in range(NUMBER_OF_TRICKS)]
    array2d_of_fantastic_tricks = np.zeros(
        shape=(NUMBER_OF_TRICKS, NUMBER_OF_TRICKS),
        dtype=int
    )

    for i in range(NUMBER_OF_TRICKS):
        for j in range(NUMBER_OF_TRICKS):
            concat_trick = concat_tricks(i, j)
            if "L" not in concat_trick:
                continue

            array2d_of_fantastic_tricks[i][j] = \
                count_fantastic_tricks(concat_trick)

    for row in array2d_of_fantastic_tricks:
        print(*row)


if __name__ == '__main__':
    main()
