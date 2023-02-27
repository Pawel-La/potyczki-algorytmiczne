def bit_power(n):
    power = 0
    while n > 0:
        power += 1
        n = n & (n-1)
    return power


def main():
    BIT_POWERS_SUM = int(input())

    bit_powers = []
    strictly_decreasing_sequence = []
    current_bit_power = 0
    i = 1

    while current_bit_power < BIT_POWERS_SUM:
        bit_powers.append(bit_power(i))
        strictly_decreasing_sequence.append(i)
        current_bit_power += bit_powers[-1]
        i += 1

    i = len(bit_powers) - 2
    while current_bit_power > BIT_POWERS_SUM:
        if current_bit_power - bit_powers[i] >= BIT_POWERS_SUM:
            current_bit_power -= bit_powers[i]
            strictly_decreasing_sequence.pop(i)
        i -= 1

    strictly_decreasing_sequence.reverse()
    print(len(strictly_decreasing_sequence))
    print(*strictly_decreasing_sequence)


if __name__ == '__main__':
    main()
