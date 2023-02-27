GO_UP = 1
GO_DOWN = -1
MIN_PITCH = -1_000_001
MAX_PITCH = 1_000_001


def main():
    def how_many_changes_needed(next_move, recent):
        number_of_changes = 0
        for pitch in pitches:
            if recent * next_move >= pitch * next_move:
                number_of_changes += 1
                recent = MAX_PITCH * next_move
            else:
                recent = pitch
            next_move *= -1
        return number_of_changes

    _ = int(input())
    pitches = [int(pitch) for pitch in input().split()]

    print(min(how_many_changes_needed(GO_UP, MIN_PITCH),
              how_many_changes_needed(GO_DOWN, MAX_PITCH)))


if __name__ == '__main__':
    main()
