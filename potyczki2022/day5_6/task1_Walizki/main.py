from math import gcd, lcm
import numpy as np


class Fraction:
    def __init__(self, meter, denominator):
        self.meter = meter
        self.denominator = denominator

    def get_meter(self):
        return self.meter

    def get_denominator(self):
        return self.denominator

    def set_meter(self, meter):
        self.meter = meter

    def set_denominator(self, denominator):
        self.denominator = denominator

    def get_meter_to_add(self):
        return self.meter // gcd(self.meter, self.denominator)

    def get_denominator_to_add(self):
        return self.denominator // gcd(self.meter, self.denominator)


def main():
    NUMBER_OF_PLATFORMS = int(input())

    how_many = np.zeros(NUMBER_OF_PLATFORMS + 1)
    how_many[1] = 1

    rounds = np.zeros(NUMBER_OF_PLATFORMS + 1)
    rounds[1] = 1

    fraction = Fraction(0, 0)
    result = 1

    for i in range(1, NUMBER_OF_PLATFORMS + 1):
        platform_data = input().split()
        number_of_baggage_carousels = int(platform_data[0])
        if not (number_of_baggage_carousels and how_many[i]):
            continue
        if number_of_baggage_carousels >= 2:
            task = rounds[i] * lcm(how_many[i], number_of_baggage_carousels)\
                   // how_many[i]
            result = lcm(result, task)

        fraction.set_meter(how_many[i])
        fraction.set_denominator(rounds[i] * number_of_baggage_carousels)

        meter = fraction.get_meter_to_add()
        denominator = fraction.get_denominator_to_add()

        for j in range(1, number_of_baggage_carousels + 1):
            platform_number = int(platform_data[j])
            if rounds[platform_number] == 0:
                how_many[platform_number] = meter
                rounds[platform_number] = denominator
            else:
                LCM = lcm(denominator, rounds[platform_number])

                how_many[platform_number] *= LCM // rounds[platform_number]
                how_many[platform_number] += ((meter * LCM) // denominator)
                rounds[platform_number] = LCM

                GCD = gcd(how_many[platform_number], rounds[platform_number])
                how_many[platform_number] //= GCD
                rounds[platform_number] //= GCD

    print(result)


if __name__ == '__main__':
    main()
